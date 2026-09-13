# Exercise: find the personal data

| | |
|---|---|
| **Prerequisites** | [Does the AI need this?](01-does-the-ai-need-this.md) |
| **Time** | ~30 min |
| **Outcome** | After this unit you can find personal data hidden in an ordinary-looking customer file, and explain why the safest upload is no upload. |
| **Last verified** | 2026-09-13 |

## Why this matters

Names are easy to spot. Personal data also hides in free-text notes, ID numbers, file names, and in combinations of columns that look harmless on their own.

Most people find about half of it on the first try. That is the point of the exercise. If a careful person with thirty minutes finds half, a quick look before an upload finds less.

## Do it

### 1. Open the file without any AI tool (5 min)

Go to [exercises/find-the-personal-data](../../exercises/find-the-personal-data/README.md) and read the rules and the short description of the columns.

Open `customers.csv` in a way that involves no AI:

- **Browser lane:** read it on GitHub (the file page shows it as a table), or download it with the "Download raw file" button and open it in a spreadsheet app on your computer.
- **CLI lane:** open it in a text editor or spreadsheet app. Do not start your coding agent in the exercise folder: it would read the file into its context.

**Do not upload or paste the file into any AI tool**, not even to "help find" things. The data is invented, so nothing bad would happen. You are practising the habit: with a real file, asking an AI to find the personal data is already the leak.

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

Write down your count: found out of total.

### 4. Reflect (5 min)

Answer three questions on paper:

1. Which trap did I miss, and why did I miss it?
2. How long would this take on a real file with 2,000 rows and five tabs?
3. What would I have to do before every single prompt, every time, to be safe with a real file?

The honest answer to question 3 is the lesson: you would not do it reliably. So the fix is not "clean the file better". The fix is to not upload the file at all, take only its structure, and invent the rows. That is the next unit.

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
