# Spec interview: let the agent ask the questions

Let the AI ask you about your idea before it starts building. Together, write a one-page plan, called a spec, so the next session knows what to build and how you will check it.

| | |
|---|---|
| **Prerequisites** | [Your first build](../01-first-build/01-your-first-build.md) · [Schema first, then synthetic data](../02-data-first/03-schema-then-synthetic-data.md) |
| **Time** | ~30 min |
| **Outcome** | A saved one-page spec with IN, OUT, invented data, a way to check the result and three first tasks. |
| **Last verified** | 2026-09-13 |

## Why this matters

If you start with a vague request, the agent has to fill in the gaps. An interview lets you decide who the app is for, what it should do and what to leave out. Saving those decisions means you can use them again without repeating the conversation.

Anthropic recommends an interview, a spec file and a fresh build session for larger features ([Claude Code best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). You can use the same approach in a chat assistant, browser builder or CLI agent.

## Do it

### 1. Pick one idea (2 min)

Take one real task from your own work or life. Small is fine: a form, a calculator, a checklist, a tiny dashboard. No idea at hand? Pick one from the [idea list in the product sprint](02-product-sprint.md#idea-list).

### 2. Stop the tool from building (1 min)

- **Chat assistant** (Claude, ChatGPT, Gemini and similar): ask for a written plan. Keep actions and file changes off during the interview.
- **Browser app builder** (Lovable, Bolt, v0, Replit and similar): many start building on the first message. Use the tool's chat or planning option if it has one. Or run the interview in a chat assistant and paste the finished spec into the builder afterwards.
- **CLI agent** (Claude Code, Codex and similar): switch to a planning or read-only mode. In Claude Code, press `Shift+Tab` until the status bar shows plan mode ([Claude Code best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). If your agent has no such mode, keep the line "Do not change any files" in the prompt.

### 3. Paste the interview prompt (15 min)

Copy this into a new chat or session:

```text
I want to turn my idea into a short spec. Do not build anything yet.

Interview me: one question at a time, at most eight questions.
Wait for my answer before you ask the next one.

Ask about:
- the problem, and what annoys people about it today
- who it is for, and who will use it first
- what is explicitly NOT part of it
- what data it needs (we only ever use made-up data)
- how we will know in two weeks that it works

Then write a one-page SPEC.md with these sections:
one sentence at the top, problem, users, IN, OUT, data (fake),
done when, open questions.

Finally, suggest three first tasks. Each task must be small enough
for one afternoon and have its own "done when" line.
```

Answer in short sentences. If you do not know something yet, put it in open questions.

### 4. Read the spec like a critic (5 min)

Check each point. If one fails, tell the agent which line is wrong and ask it to rewrite only that line.

- The top sentence has this shape: "For *who*, *name* does *what*, instead of *what happens today*."
- OUT has at least three items, including something useful that you are deliberately leaving for later.
- The data section lists fields and types only. No real values.
- "Done when" describes a result you can check yourself.
- Open questions include anything still undecided. Check that the agent has not silently guessed an answer.

### 5. Save it and cut three tasks (5 min)

Save the spec where you can find and reuse it without searching through the chat.

- Put it where your project lives: a `SPEC.md` file, a note, or the project instructions or knowledge area of your builder.
- Start from the [spec template](../../templates/SPEC.md) if you prefer filling in blanks.
- Write the three tasks where you will see them again: in the tool, in a note, or in an issue tracker such as GitHub Issues.

### 6. Optional: start task one today

Open a fresh chat or session and paste the spec. Ask for task one only, including how the agent checked the result. The new session starts from your decisions instead of the whole interview.

### What a good spec looks like

| Section | What goes in |
|---|---|
| One sentence | For whom, what, instead of what. Nothing more. |
| Problem | What is annoying today, in two or three sentences. |
| Users | The first real person or group who will use it. |
| IN | The three things it must do. |
| OUT | What you deliberately do not build in this version. |
| Data (fake) | Field names, types, value ranges. Sample rows are invented. |
| Done when | What you can observe when it works. |
| Open questions | What you do not know yet, written down honestly. |

A short made-up example:

> For people who book shared meeting rooms, Room Board shows which rooms are free in the next two hours, instead of walking the floor to check.
>
> IN: list of rooms, free or busy for the next two hours, filter by room size.
> OUT: booking rooms, calendar sync, logins.
> Done when: with the 12 fake rooms in the sample file, the page shows the correct free rooms for any time I type in.

## Done when

- [ ] A spec exists outside the chat window (a file, a note, or project instructions).
- [ ] It has a one-sentence top line, problem, users, IN, OUT with at least three items, data (fake), done when, and open questions.
- [ ] Three tasks exist where you will find them again, each with its own "done when" line.
- [ ] Nothing was built during the interview. If you built task one, you did it in a fresh chat or session.

## Data note

The interview asks about data. Describe its shape only: field names, types and value ranges. Never paste real names, e-mail addresses or customer records as "examples", not even one row. If the agent needs sample rows, it invents them, with addresses such as `sam.sample@example.com`. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md) and [Schema first, then synthetic data](../02-data-first/03-schema-then-synthetic-data.md).

## Next

[Product sprint](02-product-sprint.md): do the same as a team of three or four, and add sample data, a picture, a name and a 60-second pitch.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
