# Schema first, then synthetic data

List the spreadsheet's columns and the kind of value each one holds. This is a schema. Use it to generate invented (synthetic) rows for your app, without sending the source file.

| | |
|---|---|
| **Prerequisites** | [Exercise: find the personal data](02-exercise-find-the-personal-data.md) |
| **Time** | ~25 min |
| **Outcome** | A list of columns and types, plus checked invented rows that your app can use. |
| **Last verified** | 2026-09-13 |

## Why this matters

To build and test the app without uploading the original records:

1. Take only the structure: column names and types.
2. Leave every value on your computer.
3. Let the agent invent rows that fit the structure.

The agent can work from this structure and your app's rules ([Does the AI need this?](01-does-the-ai-need-this.md)). You may use the invented rows in your course tools.

## Do it

### Step 1: Get a local CSV file (3 min)

Practise locally with `customers.csv` from the [exercise folder](../../exercises/find-the-personal-data/README.md), after your human-only attempt. Do not let an agent read that file for you. Real work files need your organisation's approved process and stay outside this course and agent-visible folders.

If your file is a spreadsheet (`.xlsx`, `.ods`), save it as CSV in the spreadsheet app on your computer: "Save as" or "Download as", then CSV. Do not use an online converter: that is an upload.

### Step 2: Extract the schema (5 min)

Choose the script if you have Python 3, or follow the manual steps below.

**With the script** (needs Python 3 on your computer). Open a terminal at the top of the downloaded course folder. Run the script yourself; it runs locally and sends nothing:

```bash
python3 exercises/find-the-personal-data/extract-schema.py exercises/find-the-personal-data/customers.csv
```

The script uses neutral names such as `column_1` and `column_2`. It adds estimated types, counts and hints, but prints no original header or cell values. If the file has no header, this also keeps its first data row out of the output. Check the header yourself; the script cannot reliably recognise it.

To include original column names, first inspect the header locally and remove names or sensitive details. Only then opt in:

```bash
python3 exercises/find-the-personal-data/extract-schema.py exercises/find-the-personal-data/customers.csv --include-column-names
```

Add `--json` for JSON output. Invalid quoting, inconsistent row widths or duplicate headers stop with an error. Keep the file local if this happens; do not upload it to a converter. Share only the generic column names and types the agent needs. Counts and distinct-value statistics do not prove anonymisation. Rename neutral columns by hand to describe your intended app.

**By hand** (no install):

1. Open the file on your computer and copy **only the header row** into a new document.
2. Next to each column name, write its type in plain words: text, whole number, decimal number, date, yes/no.
3. For columns with a small fixed set of values, you may list the values if they say nothing about a person, for example `status: open, paid, overdue`.
4. Copy no data row.

**Check the column names themselves.** A header such as "Kim's clients" or "Notes on Dr Sample" is personal data. Rename it.

**Remove columns the app does not need.** For example, leave `date_of_birth` and `last_login_ip` out if they serve no purpose in your app.

### Step 3: Give the schema to the agent (5 min)

Paste this into your builder or your CLI agent:

```text
Here is the structure of a spreadsheet. It contains no real values.

<paste the schema>

Generate 30 rows of synthetic data that fit this structure, as CSV.
Rules:
- Every person and company is obviously fictional.
- Every e-mail address ends in @example.com.
- Phone numbers are clearly invalid, for example +00 555 0101.
- IP addresses come from 192.0.2.0/24 or 198.51.100.0/24.
- ID numbers and bank account numbers use a visibly fake format, starting with FAKE or XX.
- Free-text notes contain business facts only: never health, religion, union membership, politics or family.
- Include a few edge cases: an empty cell, a very long company name, a date in the future.
```

The IP ranges are reserved for documentation ([RFC 5737](https://www.rfc-editor.org/rfc/rfc5737)), and `example.com` is reserved for examples ([RFC 2606](https://www.rfc-editor.org/rfc/rfc2606)).

### Step 4: Check the synthetic data (5 min)

- Search for `@`. Every e-mail address must end in `example.com`.
- Read the names and towns. Anything that sounds like a real person, company or place: ask the agent to replace it.
- Check that every generated row follows the stated invented-data rules. Do not open a real file in the agent workspace to compare it.
- If the agent wrote code that generates the data with a library such as Faker, check that the e-mail domain is set to `example.com` in the code. Default settings of such libraries can produce addresses at real mail providers, and those can belong to real people.

### Step 5: Build with it (7 min)

- **Browser lane:** paste the synthetic CSV into the chat with "Use this as the sample data in my app", or upload the generated file. It is invented, so that is allowed.
- **CLI lane:** save it as `sample-data.csv` in your `playground` folder, ask the agent to load it, and commit.

Open the preview and try the empty cell, long company name and future date. Check whether the app handles each as you intended.

### And the real data?

Real data stays outside these tracks. Your organisation decides which tool, contract and place to run it are approved. An app working with invented rows may still need changes before it can handle real data, including security and operational checks.

## Done when

- [ ] I have a schema with column names and types, and no values.
- [ ] I checked the column names for personal data and removed columns my app does not need.
- [ ] I generated synthetic rows from the schema and checked the e-mail domain.
- [ ] My first build, or a new one, runs with the synthetic data.

## Data note

Share the schema and the synthetic rows, never the source file. Keep real source files out of any folder where you start a CLI agent, and out of project folders that sync to the cloud.

## Next

[If something went wrong](04-if-something-went-wrong.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
