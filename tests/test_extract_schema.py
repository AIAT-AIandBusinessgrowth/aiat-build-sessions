"""Regression tests for safe, useful CSV output and actionable failures."""

import csv
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "exercises/find-the-personal-data/extract-schema.py"
SPEC = importlib.util.spec_from_file_location("extract_schema", SCRIPT)
schema = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(schema)


class ExtractSchemaChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "DO_NOT_PRINT_THIS_FILENAME.csv"

    def run_csv(self, content, *args):
        if isinstance(content, str):
            content = content.encode("utf-8")
        self.path.write_bytes(content)
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.path), *args],
            capture_output=True, text=True, check=False,
        )

    def assert_safe_failure(self, content, *args):
        result = self.run_csv(content, *args)
        self.assertNotEqual(0, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertNotIn(str(self.path), result.stderr)
        self.assertNotIn(self.path.name, result.stderr)
        self.assertNotIn("PRIVATE_SENTINEL", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        return result

    def test_default_hides_first_row_even_when_header_is_missing(self):
        for options in [(), ("--json",)]:
            with self.subTest(options=options):
                result = self.run_csv("PRIVATE_SENTINEL,OTHER_SENTINEL\nROW_SENTINEL,VALUE_SENTINEL\n", *options)
                self.assertEqual(0, result.returncode, result.stderr)
                for marker in ("PRIVATE_SENTINEL", "OTHER_SENTINEL", "ROW_SENTINEL", "VALUE_SENTINEL"):
                    self.assertNotIn(marker, result.stdout + result.stderr)
                self.assertIn("column_1", result.stdout)

    def test_names_require_explicit_opt_in_in_table_and_json(self):
        for options in [(), ("--json",)]:
            with self.subTest(options=options):
                result = self.run_csv("safe_field,other_field\nPRIVATE_SENTINEL,SECOND_SENTINEL\n", "--include-column-names", *options)
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertIn("safe_field", result.stdout)
                self.assertNotIn("PRIVATE_SENTINEL", result.stdout + result.stderr)
                self.assertNotIn("SECOND_SENTINEL", result.stdout + result.stderr)

    def test_delimiters_bom_unicode_quoted_separators_and_newlines(self):
        for delimiter in [",", ";", "\t"]:
            for bom in [False, True]:
                with self.subTest(delimiter=repr(delimiter), bom=bom):
                    output = io.StringIO(newline="")
                    writer = csv.writer(output, delimiter=delimiter)
                    writer.writerows([
                        ["größenklasse", "notes", "active"],
                        ["12", "PRIVATE_SENTINEL, semi; tab\t\nnext line", "yes"],
                        ["24", "", "no"],
                    ])
                    content = ("\ufeff" if bom else "") + output.getvalue()
                    result = self.run_csv(content, "--json", "--include-column-names")
                    self.assertEqual(0, result.returncode, result.stderr)
                    data = json.loads(result.stdout)
                    self.assertEqual(2, data["rows"])
                    self.assertEqual(["integer", "text", "yes/no"], [c["type"] for c in data["columns"]])
                    self.assertEqual("größenklasse", data["columns"][0]["column"])
                    self.assertEqual(1, data["columns"][1]["empty"])
                    self.assertNotIn("PRIVATE_SENTINEL", result.stdout + result.stderr)

    def test_empty_files_blank_headers_and_control_characters_fail_safely(self):
        for content in ["", "\n", "\ufeff", "\nfield\nPRIVATE_SENTINEL\n", " ,\nPRIVATE_SENTINEL,x\n", "field,\nPRIVATE_SENTINEL,x\n", "field\x1b,other\nPRIVATE_SENTINEL,x\n"]:
            with self.subTest(content=repr(content[:30])):
                self.assert_safe_failure(content)

    def test_duplicate_headers_after_whitespace_trimming_fail(self):
        self.assert_safe_failure("field, field \nPRIVATE_SENTINEL,x\n", "--json")

    def test_ragged_rows_fail_for_every_delimiter(self):
        for delimiter in [",", ";", "\t"]:
            for row in ["PRIVATE_SENTINEL", delimiter.join(["PRIVATE_SENTINEL", "x", "y"])]:
                with self.subTest(delimiter=repr(delimiter), row=row):
                    self.assert_safe_failure(f"first{delimiter}second\n{row}\n", "--json")

    def test_malformed_quotes_fail_without_echoing_the_row(self):
        for row in ['"PRIVATE_SENTINEL,x\n', '"PRIVATE_SENTINEL"unexpected,x\n']:
            self.assert_safe_failure("first,second\n" + row, "--json")

    def test_invalid_utf8_and_oversized_field_fail_without_values(self):
        self.assert_safe_failure(b"field\nPRIVATE_SENTINEL\xff\n", "--json")
        self.assert_safe_failure("field\nPRIVATE_SENTINEL" + "x" * 150000 + "\n")

    def test_missing_file_error_does_not_echo_the_path(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.path)], capture_output=True, text=True)
        self.assertNotEqual(0, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertNotIn(self.path.name, result.stderr)
        self.assertNotIn(str(self.path), result.stderr)

    def test_header_only_csv_is_a_valid_empty_dataset(self):
        result = self.run_csv("first,second\n", "--json")
        self.assertEqual(0, result.returncode, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(0, data["rows"])
        self.assertEqual(["empty", "empty"], [column["type"] for column in data["columns"]])

    def test_type_inference_whitespace_and_hints_do_not_expose_values(self):
        self.assertEqual("date", schema.cell_type("2026-09-13"))
        self.assertEqual("decimal", schema.cell_type("1,25"))
        self.assertEqual("text", schema.cell_type("00123"))
        self.assertEqual("yes/no", schema.cell_type("TRUE"))
        result = schema.profile("column_1", [" ", " 1 ", "2.5", "PRIVATE_SENTINEL"])
        self.assertEqual("mixed (decimal, integer, text)", result["type"])
        self.assertEqual(1, result["empty"])
        self.assertEqual(3, result["distinct"])
        self.assertNotIn("PRIVATE_SENTINEL", json.dumps(result))
        long = schema.profile("column_1", ["PRIVATE_SENTINEL " + "long words " * 10])
        self.assertIn("free text: check by hand", long["hint"])

    def test_repository_fixture_has_no_cell_values_in_output(self):
        fixture = ROOT / "exercises/find-the-personal-data/customers.csv"
        result = subprocess.run([sys.executable, str(SCRIPT), str(fixture), "--json"], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        data = json.loads(result.stdout)
        with fixture.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        self.assertEqual(len(rows) - 1, data["rows"])
        self.assertEqual(len(rows[0]), len(data["columns"]))
        for row in rows:
            for value in row:
                if len(value) > 5:
                    self.assertNotIn(value, result.stdout)


if __name__ == "__main__":
    unittest.main()
