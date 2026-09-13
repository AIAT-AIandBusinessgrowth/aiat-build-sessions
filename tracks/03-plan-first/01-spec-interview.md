# Spec interview: let the agent ask the questions

| | |
|---|---|
| **Prerequisites** | [Your first build](../01-first-build/01-your-first-build.md) · [Schema first, then synthetic data](../02-data-first/03-schema-then-synthetic-data.md) |
| **Time** | ~30 min |
| **Outcome** | After this unit you can turn a vague idea into a one-page spec with IN and OUT lists, fake data, a "done when" line and three first tasks, before anything gets built. |
| **Last verified** | 2026-09-13 |

## Why this matters

Most first builds start with a wish list typed into a prompt box. The tool builds something at once. Then you spend the next hour negotiating with the result.

Flip it. The agent asks, you answer. Good questions force decisions you did not know you had to make: who is this for, what is it not, how will you know it works. The written answer is a spec: a short file that you, a colleague or a fresh chat can pick up next week.

This is often the moment an idea turns into a plan. And the most useful part of the spec is the OUT list. A spec that says what will not be built is worth more than ten feature lists.

Anthropic recommends the same pattern for larger features in its Claude Code guide: let the agent interview you, write the result to a spec file, then start a fresh session to build it ([Claude Code best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). Nothing about it is specific to one tool. It works in any chat assistant, browser builder or CLI agent.

## Do it

### 1. Pick one idea (2 min)

Take one real task from your own work or life. Small is fine: a form, a calculator, a checklist, a tiny dashboard. No idea at hand? Pick one from the [idea list in the product sprint](02-product-sprint.md#idea-list).

### 2. Stop the tool from building (1 min)

- **Chat assistant** (Claude, ChatGPT, Gemini and similar): nothing to do. It only writes text.
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

Answer in short sentences. "I don't know yet" is a valid answer. It goes into open questions, not into the bin.

### 4. Read the spec like a critic (5 min)

Check each point. If one fails, tell the agent which line is wrong and ask it to rewrite only that line.

- The top sentence has this shape: "For *who*, *name* does *what*, instead of *what happens today*."
- OUT has at least three items, and at least one of them hurts a little.
- The data section lists fields and types only. No real values.
- "Done when" describes something you can see or click, not a feeling.
- Open questions are honest. An empty list usually means the agent guessed.

### 5. Save it and cut three tasks (5 min)

Save the spec outside the chat window. A chat is gone when the tab closes. A file survives the week.

- Put it where your project lives: a `SPEC.md` file, a note, or the project instructions or knowledge area of your builder.
- Start from the [spec template](../../templates/SPEC.md) if you prefer filling in blanks.
- Write the three tasks where you will see them again: in the tool, in a note, or in an issue tracker such as GitHub Issues.

### 6. Optional: start task one today

Open a fresh chat or session. Paste the spec. Ask for task one only, and ask the agent to tell you how it checked the result. Starting fresh keeps the interview chatter out of the build.

### What a good spec looks like

| Section | What goes in |
|---|---|
| One sentence | For whom, what, instead of what. Nothing more. |
| Problem | What is annoying today, in two or three sentences. |
| Users | The first real person or group who will use it. |
| IN | The three things it must do. |
| OUT | What you deliberately do not build. The more important list. |
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
