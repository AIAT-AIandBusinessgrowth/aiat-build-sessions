#!/usr/bin/env python3
"""
extract-schema.py: print the structure of a CSV file, never its values.

For every column it prints the column name, an inferred type, the number
of empty cells, the number of distinct values and a short hint. It never
prints a cell value, not even a minimum or a maximum: one extreme value
(the biggest order, the oldest customer) can point to a single person.

Usage:
    python3 extract-schema.py FILE.csv
    python3 extract-schema.py FILE.csv --json

Example:
    python3 extract-schema.py customers.csv

Uses only the Python 3 standard library. It reads the file on your own
computer and sends nothing anywhere.

Before you share the output, read the column names yourself. They are
printed as they are, and a header such as "Notes on Kim" is personal data.
Save spreadsheet files (.xlsx, .ods) as CSV in your spreadsheet app first.
Do not use an online converter: that is an upload.
"""

import argparse
import csv
import json
import re
import sys

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
    """Read all rows. Detects comma, semicolon or tab as separator."""
    with open(path, newline="", encoding="utf-8-sig") as handle:
        sample = handle.read(8192)
        handle.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel
        return list(csv.reader(handle, dialect))


def main():
    parser = argparse.ArgumentParser(
        description="Print the structure of a CSV file, never its values."
    )
    parser.add_argument("csv_file", help="path to a UTF-8 CSV file")
    parser.add_argument("--json", action="store_true", help="print JSON instead of a table")
    args = parser.parse_args()

    try:
        rows = read_rows(args.csv_file)
    except (OSError, UnicodeDecodeError, csv.Error) as error:
        # Only the kind of error: some error messages quote file content.
        sys.exit(f"Could not read the file ({type(error).__name__}). Is it a UTF-8 CSV file?")

    if not rows:
        sys.exit("The file is empty.")

    header, data = rows[0], rows[1:]
    width = max([len(header)] + [len(row) for row in data])
    names = [
        (header[i].strip() if i < len(header) else "") or f"column_{i + 1}"
        for i in range(width)
    ]
    columns = [
        profile(names[i], [row[i] if i < len(row) else "" for row in data])
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
