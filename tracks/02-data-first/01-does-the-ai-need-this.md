# Does the AI need this?

| | |
|---|---|
| **Prerequisites** | [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md), [Share and export](../01-first-build/02-share-and-export.md) |
| **Time** | ~15 min |
| **Outcome** | After this unit you can ask one question before every paste or upload, explain data minimisation, and tell anonymous data from pseudonymous data. |
| **Last verified** | 2026-09-13 |

## Why this matters

Rule one says what to keep out. This unit gives you the question that decides it case by case, and that still works later when you use tools your organisation has approved.

Data that never reaches a tool cannot leak from it, cannot train a model and never has to be reported.

## Do it

### 1. Learn the one question (2 min)

> **Does the AI really need this piece of data to do the task?**

Ask it for every column, every field and every sentence you paste. Most of the time the answer is no. To build something, the AI needs the **structure** of your data, not the **values**.

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

Anonymisation is hard to do well and hard to prove. When you build with AI, you rarely need it. The easier path is to not use real data at all and invent rows from the structure. That is the unit after the exercise.

### 4. Apply it to your first build (4 min)

List every field your app from [Your first build](../01-first-build/01-your-first-build.md) has. For each field, write: does the AI need real values to build this? Yes or no, and why.

Expect "no" everywhere.

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
