# Does the AI need this?

Check the fields in your app before sending anything to an AI tool. You will learn to describe the data you need without sharing the real records behind it.

| | |
|---|---|
| **Prerequisites** | [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md), [Share and export](../01-first-build/02-share-and-export.md) |
| **Time** | ~15 min |
| **Outcome** | Decide what the AI needs and explain why removing a name may still leave personal data. |
| **Last verified** | 2026-09-13 |

## Why this matters

An app builder usually needs column names, types and rules to work with. It can invent the example rows. This reduces what you send to the tool, including later when you use a tool your organisation has approved.

## Do it

### 1. Learn the one question (2 min)

> **Does the AI really need this piece of data to do the task?**

Ask this for every column, field and sentence you plan to paste. For these builds, give the AI the **structure** of the data and use invented **values**.

This is called data minimisation. The GDPR makes it a principle: personal data must be "adequate, relevant and limited to what is necessary" for the purpose ([GDPR Article 5(1)(c)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)).

### 2. See it in examples (4 min)

| Task | What the AI needs | What it does not need |
|---|---|---|
| Build a room booking app | room names, time slots, rules such as "at most two hours" | who booked which room |
| Turn bullet points into a weekly status text | the bullet points, tone, length | client names: write `[CLIENT]` |
| Travel cost calculator | distance, rate, rounding rule | which colleague travelled where |
| Dashboard for a customer list | column names and types | a single real row |
| Improve a reply to a complaint | what the problem is, your draft | the sender's name, address and contract number |
| Fix a broken spreadsheet formula | the formula and three invented rows that show the error | the real sheet |

### 3. Anonymous is not the same as pseudonymous (5 min)

| | Anonymous | Pseudonymous |
|---|---|---|
| **What happened** | Nobody can identify the people any more, with the means that are reasonably likely to be used | Identifying details were replaced, but a way back exists somewhere |
| **Examples** | "31 bookings in March, 12 of them on Mondays", counted over a large group | "Customer C-0042", initials, a hashed e-mail address, "the new colleague in accounting" |
| **Still personal data?** | No | **Yes** ([GDPR Recital 26](https://eur-lex.europa.eu/eli/reg/2016/679/oj)) |

Three traps:

- **Deleting the name is not anonymisation.** Date of birth, postcode and gender together often point to exactly one person.
- **Hashing an e-mail address is pseudonymisation.** The same address always gives the same hash. Anyone with a list of addresses can compute the hashes and compare.
- **Small groups give people away.** "The only person in team B on leave in May" is one person.

Removing names does not prove that nobody can be identified. For this course, leave the real data out and invent rows from the structure. You will do that after the next exercise.

### 4. Apply it to your first build (4 min)

List every field your app from [Your first build](../01-first-build/01-your-first-build.md) has. For each field, write: does the AI need real values to build this? Yes or no, and why.

For this practice app, replace real values with invented examples. If you think a field needs real data, revisit what the app must do before uploading anything.

**CLI lane:** the same question applies to files. Before you start an agent in a folder, check what else is in that folder. The agent can read it.

## Done when

- [ ] I can say the one question from memory.
- [ ] I checked every field of my first build and wrote yes or no with a reason.
- [ ] I can explain in one sentence why a hashed e-mail address is still personal data.

## Data note

The question covers more than tables: screenshots with names in the corner, pasted e-mail threads with signatures, file names, and spreadsheet tabs you never looked at. Check before you paste.

> **Not legal advice.** GDPR terms are used as the reference. Your organisation's data protection contact has the final word.

## Next

[Exercise: find the personal data](02-exercise-find-the-personal-data.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
