# Exercise: find the personal data

Inspect an invented customer file yourself, without AI, then compare your findings with the solution. You will practise spotting personal information that a quick glance can miss.

| | |
|---|---|
| **Prerequisites** | [Does the AI need this?](01-does-the-ai-need-this.md) |
| **Time** | ~30 min |
| **Outcome** | Identify personal information in a file and explain why you would keep the source file out of an AI tool. |
| **Last verified** | 2026-09-13 |

## Why this matters

Names are easy to spot. Personal data also hides in free-text notes, ID numbers, file names, and in combinations of columns that look harmless on their own.

Comparing your own list with the solution shows what you missed. The exercise does not give you a pass to upload a real file after a quick check.

## Do it

### 1. Open the file without any AI tool (5 min)

Go to [exercises/find-the-personal-data](../../exercises/find-the-personal-data/README.md) and read the rules and the short description of the columns.

Open `customers.csv` in a way that involves no AI:

- **Browser lane:** read it on GitHub (the file page shows it as a table), or download it with the "Download raw file" button and open it in a spreadsheet app on your computer.
- **CLI lane:** open it in a text editor or spreadsheet app. Do not start your coding agent in the exercise folder: it would read the file into its context.

**Do not upload or paste the file into any AI tool**, including to ask it to find personal data. The file is invented, but this exercise is for you to practise. With a real file, the AI would receive the personal data before it could identify it for you.

### 2. Search (15 min)

Make a list with four columns: `customer_id`, column, what you found, why it is personal data.

Where to look:

- whole columns that are personal data in every row that describes a person
- the `notes` column
- file names
- ID numbers and codes that connect to other systems
- combinations of columns that are harmless alone

Working in a pair? Search alone for ten minutes, then merge your lists.

### 3. Compare (5 min)

Open [solution-short.md](../../exercises/find-the-personal-data/solution-short.md) first and tick off what you found. Then read [solution.md](../../exercises/find-the-personal-data/solution.md) for the reason and the fix for each trap.

Write down how many items you found out of the total. Use the count to find gaps in your search, not to judge whether real data is safe to upload.

### 4. Reflect (5 min)

Answer three questions on paper:

1. Which trap did I miss, and why did I miss it?
2. How long would this take on a real file with 2,000 rows and five tabs?
3. What would I have to do before every single prompt, every time, to be safe with a real file?

For this course, you do not need to make a real file safe to upload. Keep it out of the tool. In the next unit, you will describe the columns and ask the agent to invent rows.

## Done when

- [ ] I searched the file without uploading or pasting it into any AI tool.
- [ ] I have a written list with row, column and reason.
- [ ] I compared my list with the solution and know my count.
- [ ] I can name one trap I missed and say why.

## Data note

Every value in `customers.csv` is fictional: addresses on reserved example domains ([RFC 2606](https://www.rfc-editor.org/rfc/rfc2606)), IP addresses from documentation ranges ([RFC 5737](https://www.rfc-editor.org/rfc/rfc5737)), phone numbers with the invalid country code `+00`, ID numbers marked `FAKE`, and bank account numbers starting with the invalid country code `XX`. If a name matches a real person, that is chance.

## Next

[Schema first, then synthetic data](03-schema-then-synthetic-data.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
