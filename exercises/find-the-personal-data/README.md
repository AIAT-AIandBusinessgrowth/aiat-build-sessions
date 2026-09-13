# Exercise: find the personal data

A customer list from a fictional wholesale supplier for small businesses in four towns. Someone deleted the "contact name" column and said: *"It's anonymised now, we can use it with the AI."*

Find everything in the file that is still personal data.

| | |
|---|---|
| **Time** | ~30 min: 5 open, 15 search, 5 compare, 5 reflect |
| **You need** | A spreadsheet app or a text editor, and paper or a notes file |
| **Unit** | [Exercise: find the personal data](../../tracks/02-data-first/02-exercise-find-the-personal-data.md) |

## Rules

1. **Do not upload or paste the file into any AI tool.** Not to find the traps, not to summarise it, not to "just check". With a real file, that upload would already be the leak. Practise the habit here, where nothing can go wrong.
2. Work on your own computer, or read the file on GitHub.
3. **CLI lane:** solve this one without a coding agent. An agent running anywhere in the course folder can read `customers.csv`; the folder is not a barrier and nothing in this repository stops it. You only learn from the exercise by finding the traps yourself.
4. Do not open the solution files until you have finished your list.

## About the file

`customers.csv` has 20 rows and 12 columns. What the columns mean:

| Column | Meaning |
|---|---|
| `customer_id` | The number printed on the customer's loyalty card. The same number is the login for the supplier's online order app. |
| `company` | Name of the customer's business |
| `email` | Contact e-mail address |
| `phone` | Contact phone number |
| `street`, `town` | Delivery address |
| `date_of_birth` | Filled in for customers who signed up for the loyalty card in person |
| `job_title` | What the contact person does |
| `email_sha256` | Added "for privacy": a SHA-256 hash of the e-mail address |
| `last_login_ip` | IP address of the last login to the order app |
| `photo_file` | File name of the attachment stored with the customer |
| `notes` | Free text typed by the sales team |

## Task

Write a list with four columns:

| customer_id | column | what I found | why it is personal data |
|---|---|---|---|

- If a whole column is personal data, write it once and mark it as a column.
- Some rows have no single-cell findings. Being able to say "this cell is not personal data" is part of the skill.
- At the end, count your findings.

Stuck? Look in four places: whole columns, the notes, the file names, and columns that are harmless alone but not together.

## Solution

- [solution-short.md](solution-short.md): one page, to tick off your list
- [solution.md](solution.md): every trap with the reason and what to do instead

## Files

| File | What it is |
|---|---|
| `customers.csv` | The exercise file |
| `solution-short.md` | One-page solution |
| `solution.md` | Full solution |
| `extract-schema.py` | Prints types and counts with neutral column names. Used after this exercise in [Schema first, then synthetic data](../../tracks/02-data-first/03-schema-then-synthetic-data.md). |

## Run the schema script after the exercise

Finish your own findings first. This script describes structure; it does not find the traps for you. Run it yourself in a terminal: no agent is needed for this step, and one started at the repository root can read the exercise file.

Open a terminal in the downloaded or cloned `aiat-build-sessions` folder, the folder containing the main `README.md`. With Python installed, run:

```bash
python3 exercises/find-the-personal-data/extract-schema.py exercises/find-the-personal-data/customers.csv
```

On Windows, use `py -3` in place of `python3` if that is how Python starts on your computer. If neither works, use the [manual method](../../tracks/02-data-first/03-schema-then-synthetic-data.md#step-2-extract-the-schema-5-min).

The default output uses `column_1`, `column_2` and so on. Add `--json` for machine-readable output. To include the original column names, first open the CSV in your local editor and check that its first row contains only safe field names. Then run:

```bash
python3 exercises/find-the-personal-data/extract-schema.py exercises/find-the-personal-data/customers.csv --include-column-names --json
```

The first row must be a header. The script cannot reliably detect a missing header; with that option, a first row of customer data would be printed as names. A name in a header is still personal data. Rename unsafe headers before opting in.

The script accepts UTF-8 CSV, including a byte-order mark, with comma, semicolon or tab separators. It rejects malformed quoted fields, unequal row widths, empty or duplicate headers and empty files. Error messages omit file paths and values. Types are guesses about the format, not validation of dates or business rules.

It runs locally with Python's standard library and sends nothing over the network. Learners run the script themselves after completing the human-only exercise. Maintainers may use an agent to test the script against this fictional fixture and synthetic test cases; that exception is for maintaining the course, not solving the learner's task. Never put a real source file in an agent's workspace or ask an agent to inspect it. Counts and inferred types can still reveal information: review them locally before sharing. This output is neither an anonymisation guarantee nor permission to upload organisational data; a data processing agreement alone does not grant that permission either.

## All data is fictional

Every person, company, town and number in this folder is invented:

- e-mail addresses use reserved example domains ([RFC 2606](https://www.rfc-editor.org/rfc/rfc2606))
- IP addresses come from documentation ranges ([RFC 5737](https://www.rfc-editor.org/rfc/rfc5737))
- phone numbers use the invalid country code `+00`
- ID numbers are marked `FAKE`, and bank account numbers start with the invalid country code `XX`

If a name matches a real person, that is chance.
