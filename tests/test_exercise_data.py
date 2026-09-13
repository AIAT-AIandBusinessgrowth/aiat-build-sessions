"""Keep the fictional exercise safe and its answer keys consistent."""

import csv
import hashlib
import ipaddress
from pathlib import Path
import re
import unittest


EXERCISE = Path(__file__).resolve().parents[1] / "exercises/find-the-personal-data"


class ExerciseDataChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (EXERCISE / "customers.csv").open(encoding="utf-8", newline="") as handle:
            cls.rows = list(csv.DictReader(handle))

    def test_dataset_is_rectangular_and_customer_ids_are_unique(self):
        self.assertTrue(self.rows)
        self.assertTrue(all(None not in row and None not in row.values() for row in self.rows))
        self.assertEqual(len(self.rows), len({row["customer_id"] for row in self.rows}))

    def test_contact_details_use_reserved_or_invalid_ranges(self):
        networks = [ipaddress.ip_network(value) for value in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")]
        for row in self.rows:
            with self.subTest(row=row["customer_id"]):
                if row["email"]:
                    domain = row["email"].rsplit("@", 1)[-1]
                    self.assertTrue(domain in {"example.com", "example.net", "example.org"} or domain.endswith(".example"))
                    self.assertEqual(hashlib.sha256(row["email"].encode()).hexdigest(), row["email_sha256"])
                self.assertTrue(row["phone"].startswith("+00 "))
                self.assertTrue(any(ipaddress.ip_address(row["last_login_ip"]) in network for network in networks))

    def test_answer_keys_reference_existing_rows_and_agree(self):
        keys = []
        for filename in ["solution.md", "solution-short.md"]:
            text = (EXERCISE / filename).read_text(encoding="utf-8")
            findings = re.findall(r"^\| (B\d+) \| (CARD-\d+) \|", text, re.M)
            self.assertTrue(findings)
            self.assertEqual(len(findings), len(dict(findings)))
            self.assertTrue({row for _, row in findings} <= {row["customer_id"] for row in self.rows})
            self.assertEqual([f"B{index}" for index in range(1, len(findings) + 1)], [key for key, _ in findings])
            keys.append(findings)
        self.assertEqual(keys[0], keys[1])


if __name__ == "__main__":
    unittest.main()
