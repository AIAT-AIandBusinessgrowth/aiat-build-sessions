#!/usr/bin/env python3
"""
extract-schema.py: print CSV types and counts, without row values.

Columns have neutral names by default. Only --include-column-names prints
the first record as column names, after you have checked it yourself.
The first record must be a header; no program can reliably decide that
for you. Counts are not an anonymisation or permission-to-share guarantee.

Usage:
    python3 extract-schema.py FILE.csv
    python3 extract-schema.py FILE.csv --json
    python3 extract-schema.py FILE.csv --include-column-names

Example:
    python3 extract-schema.py customers.csv

Uses only the Python 3 standard library. It reads the file on your own
computer and sends nothing anywhere.

Before opting in to column names, check the header in your local editor.
A header such as "Notes on Kim" is personal data. Rename it first.
Save spreadsheet files (.xlsx, .ods) as CSV in your spreadsheet app first.
Do not use an online converter: that is an upload.
"""

import argparse
import csv
import json
import re
import sys


class SchemaError(ValueError):
    """A fixed, shareable error message without input values or file paths."""

# Checked in this order. The first pattern that matches names the type.
PATTERNS = [
    ("date", re.compile(r"^\d{4}-\d{2}-\d{2}$|^\d{1,2}[./]\d{1,2}[./]\d{4}$")),
    ("integer", re.compile(r"^[+-]?(0|[1-9]\d*)$")),
    ("decimal", re.compile(r"^[+-]?\d+[.,]\d+$")),
    ("yes/no", re.compile(r"^(true|false|yes|no)$", re.IGNORECASE)),
]
FREE_TEXT_AVG_LENGTH = 30


def cell_type(value):
    """Return the type name of one non-empty cell. Never returns the value."""
    for name, pattern in PATTERNS:
        if pattern.match(value):
            return name
    return "text"


def profile(name, cells):
    """Describe one column by its structure only."""
    filled = [cell.strip() for cell in cells if cell.strip()]
    types = sorted({cell_type(cell) for cell in filled})
    if not types:
        kind = "empty"
    elif len(types) == 1:
        kind = types[0]
    else:
        kind = "mixed (" + ", ".join(types) + ")"

    distinct = len(set(filled))
    hints = []
    if len(filled) > 1 and distinct == len(filled):
        hints.append("every value differs: may identify a row")
    # Long values with spaces are sentences; long values without spaces are codes or hashes.
    with_spaces = sum(1 for cell in filled if " " in cell)
    if (
        filled
        and sum(len(cell) for cell in filled) / len(filled) >= FREE_TEXT_AVG_LENGTH
        and with_spaces >= len(filled) / 2
    ):
        hints.append("free text: check by hand")

    return {
        "column": name,
        "type": kind,
        "empty": len(cells) - len(filled),
        "distinct": distinct,
        "hint": "; ".join(hints),
    }


def read_rows(path):
    """Read a strict, rectangular CSV with a nonempty, unique header."""
    with open(path, newline="", encoding="utf-8-sig") as handle:
        # Infer from the header only: malformed data rows must not change the
        # delimiter and turn a broken multi-column file into one text column.
        header_line = handle.readline()
        handle.seek(0)
        try:
            delimiter = csv.Sniffer().sniff(header_line, delimiters=",;\t").delimiter
        except csv.Error:
            delimiter = ","
        rows = list(csv.reader(handle, delimiter=delimiter, strict=True))

    if not rows or not rows[0] or not any(cell.strip() for cell in rows[0]):
        raise SchemaError("The file needs a nonempty header row.")
    names = [cell.strip() for cell in rows[0]]
    if any(not name for name in names):
        raise SchemaError("Every column needs a header. Check the first row locally.")
    if len(set(names)) != len(names):
        raise SchemaError("Column headers must be unique. Check the first row locally.")
    if any(not name.isprintable() for name in names):
        raise SchemaError("Column headers must be printable text on one line.")
    if any(len(row) != len(names) for row in rows[1:]):
        raise SchemaError("Rows have different widths. Check the CSV export locally.")
    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Print CSV types and counts with neutral column names.",
        epilog="The first row must be a header. Review output locally before sharing.",
    )
    parser.add_argument("csv_file", help="path to a UTF-8 CSV file")
    parser.add_argument("--json", action="store_true", help="print JSON instead of a table")
    parser.add_argument(
        "--include-column-names",
        action="store_true",
        help="print the first row as names ONLY after you have checked it locally",
    )
    args = parser.parse_args()

    try:
        rows = read_rows(args.csv_file)
    except SchemaError as error:
        sys.exit(str(error))
    except (OSError, UnicodeDecodeError, csv.Error) as error:
        # Only the kind of error: some error messages quote file content.
        sys.exit(f"Could not read the file ({type(error).__name__}). Is it a UTF-8 CSV file?")

    header, data = rows[0], rows[1:]
    width = len(header)
    names = [
        header[i].strip() if args.include_column_names else f"column_{i + 1}"
        for i in range(width)
    ]
    columns = [
        profile(names[i], [row[i] for row in data])
        for i in range(width)
    ]

    if args.json:
        print(json.dumps({"rows": len(data), "columns": columns}, indent=2, ensure_ascii=False))
        return

    print(f"Rows (without header): {len(data)}")
    print(f"Columns: {width}")
    print()
    w_name = max([len("column")] + [len(c["column"]) for c in columns])
    w_type = max([len("type")] + [len(c["type"]) for c in columns])
    print(f"{'column':<{w_name}}  {'type':<{w_type}}  {'empty':>5}  {'distinct':>8}  hint")
    for c in columns:
        print(
            f"{c['column']:<{w_name}}  {c['type']:<{w_type}}  "
            f"{c['empty']:>5}  {c['distinct']:>8}  {c['hint']}"
        )


if __name__ == "__main__":
    main()
