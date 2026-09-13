# Exercise: find the personal data

A customer list from a fictional wholesale supplier for small businesses in three towns. Someone deleted the "contact name" column and said: *"It's anonymised now, we can use it with the AI."*

Find everything in the file that is still personal data.

| | |
|---|---|
| **Time** | ~30 min: 5 open, 15 search, 5 compare, 5 reflect |
| **You need** | A spreadsheet app or a text editor, and paper or a notes file |
| **Unit** | [Exercise: find the personal data](../../tracks/02-data-first/02-exercise-find-the-personal-data.md) |

## Rules

1. **Do not upload or paste the file into any AI tool.** Not to find the traps, not to summarise it, not to "just check". With a real file, that upload would already be the leak. Practise the habit here, where nothing can go wrong.
2. Work on your own computer, or read the file on GitHub.
3. **CLI lane:** do not start a coding agent in this folder. It would read the file.
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
| `extract-schema.py` | Prints column names and types of a CSV file, never the values. Used in [Schema first, then synthetic data](../../tracks/02-data-first/03-schema-then-synthetic-data.md). |

## All data is fictional

Every person, company, town and number in this folder is invented:

- e-mail addresses use reserved example domains ([RFC 2606](https://www.rfc-editor.org/rfc/rfc2606))
- IP addresses come from documentation ranges ([RFC 5737](https://www.rfc-editor.org/rfc/rfc5737))
- phone numbers use the invalid country code `+00`
- ID numbers are marked `FAKE`, and bank account numbers start with the invalid country code `XX`

If a name matches a real person, that is chance.
