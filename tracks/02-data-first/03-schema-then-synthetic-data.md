# Schema first, then synthetic data

| | |
|---|---|
| **Prerequisites** | [Exercise: find the personal data](02-exercise-find-the-personal-data.md) |
| **Time** | ~25 min |
| **Outcome** | After this unit you can turn a spreadsheet into a schema without any values, give that schema to an agent, and build with synthetic rows that look like your data. |
| **Last verified** | 2026-09-13 |

## Why this matters

The exercise showed that cleaning a real file is slow and unreliable. So change the order instead of trying harder:

1. Take only the structure: column names and types.
2. Leave every value on your computer.
3. Let the agent invent rows that fit the structure.

The structure is all the agent needs to build ([Does the AI need this?](01-does-the-ai-need-this.md)). Invented rows can go into any tool.

## Do it

### Step 1: Get a local CSV file (3 min)

Practise with `customers.csv` from the [exercise folder](../../exercises/find-the-personal-data/README.md). Later, use a spreadsheet from your own work in exactly the same way.

If your file is a spreadsheet (`.xlsx`, `.ods`), save it as CSV in the spreadsheet app on your computer: "Save as" or "Download as", then CSV. Do not use an online converter: that is an upload.

### Step 2: Extract the schema (5 min)

Pick one way.

**With the script** (needs Python 3 on your computer). It runs locally and sends nothing:

```bash
python3 exercises/find-the-personal-data/extract-schema.py exercises/find-the-personal-data/customers.csv
```

The output for the exercise file starts like this:

```text
Rows (without header): 20
Columns: 12

column         type  empty  distinct  hint
customer_id    text      0        20  every value differs: may identify a row
company        text      0        20  every value differs: may identify a row
email          text      1        19  every value differs: may identify a row
town           text      0         4
date_of_birth  date      8        12  every value differs: may identify a row
notes          text      0        20  every value differs: may identify a row; free text: check by hand
```

It prints column names, types, counts and hints. It never prints a cell value, not even the smallest or largest one, because the biggest order or the oldest customer can point to one person. Add `--json` if you prefer JSON.

**By hand** (no install):

1. Open the file on your computer and copy **only the header row** into a new document.
2. Next to each column name, write its type in plain words: text, whole number, decimal number, date, yes/no.
3. For columns with a small fixed set of values, you may list the values if they say nothing about a person, for example `status: open, paid, overdue`.
4. Copy no data row.

**Check the column names themselves.** A header such as "Kim's clients" or "Notes on Dr Sample" is personal data. Rename it.

**Drop what you do not need.** Ask the one question per column. If your app does not need `date_of_birth` or `last_login_ip`, delete them from the schema now.

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
- Pick three unusual values from your real file and search for them in the generated data, on your computer. They must not appear.
- If the agent wrote code that generates the data with a library such as Faker, check that the e-mail domain is set to `example.com` in the code. Default settings of such libraries can produce addresses at real mail providers, and those can belong to real people.

### Step 5: Build with it (7 min)

- **Browser lane:** paste the synthetic CSV into the chat with "Use this as the sample data in my app", or upload the generated file. It is invented, so that is allowed.
- **CLI lane:** save it as `sample-data.csv` in your `playground` folder, ask the agent to load it, and commit.

Open the preview and check that the app behaves with the edge cases.

### And the real data?

Not in these tracks. If a tool should one day work with real data, your organisation decides where it may run: which approved tool, which contract, often only on a computer inside the organisation. Because you built and tested with synthetic data, that switch is a decision, not a rebuild.

## Done when

- [ ] I have a schema with column names and types, and no values.
- [ ] I checked the column names for personal data and removed columns my app does not need.
- [ ] I generated synthetic rows from the schema and checked the e-mail domain.
- [ ] My first build, or a new one, runs with the synthetic data.

## Data note

Share the schema and the synthetic rows, never the source file. Keep real source files out of any folder where you start a CLI agent, and out of project folders that sync to the cloud.

## Next

[If something went wrong](04-if-something-went-wrong.md)
