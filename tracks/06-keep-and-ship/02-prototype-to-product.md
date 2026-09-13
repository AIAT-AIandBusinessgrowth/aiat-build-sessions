# From prototype to product

| | |
|---|---|
| **Prerequisites** | [Keep your work safe](01-keep-your-work-safe.md), [Spec interview](../03-plan-first/01-spec-interview.md), or a three-line mini-spec (what, for whom, done when) |
| **Time** | ~20 min |
| **Outcome** | You can explain who your tool helps, write usable starting instructions and prepare to check it with someone else. |
| **Last verified** | 2026-09-13 |

## Why this matters

Choose one person who could use your prototype, the first working version of your tool. Write what they should be able to do with it. Use their role in course files, such as "office assistant".

Someone else may lack your setup or know less about the app. You will write starting instructions, define what this version does and give users a way to report problems.

## Do it

### 1. Write the one sentence (5 min)

Fill in:

> For **who**, **name** does **what**, instead of **what happens today**.

You can write it yourself or use this interview prompt in Claude Code, Codex or a browser app builder:

```text
Ask me five questions about the tool I built: who uses it, what they do today,
what the tool changes, what it does not do, and what "working" means for them.
Ask one question at a time. Then give me three versions of this sentence:
"For <who>, <name> does <what>, instead of <what happens today>."
```

Pick a version that clearly says who uses the tool and what it helps them do.

### 2. Name your users (3 min)

Choose at least one person other than you who has this problem. A role and task, such as "office assistant booking rooms every Monday", is more useful for design than "everyone in the team".

Keep the list where it belongs: names and contact details go into your private notes. In the repository, describe users by role, for example "office assistant, plans rooms every Monday".

### 3. Cut the scope (5 min)

Write two short lists and a date:

- **In:** the few things this version needs to do. Three to five is a useful starting range for this exercise.
- **Out:** related things you will leave for another version, if any.
- **Stop date:** when you review the version and decide what is ready or still open. The date does not make unfinished work complete.

An **MVP** is the smallest version with which users can try the intended job. Use the [MVP template](../../templates/MVP.md), adapting its example counts to your task. Prompt: "Read my sentence and draft MVP.md with In, Out, and a stop date. Suggest anything we could leave out while keeping the intended job possible. Explain why; do not remove requirements just to shorten the list."

### 4. Write the README (3 min)

A **README** is the file that explains how to use the project. Start with four questions; about twenty lines is a useful exercise target:

1. What does it do, in one sentence?
2. Who is it for?
3. How do I start or open it?
4. What can it not do yet?

Prompt: "Write a README from MVP.md. Twenty lines, plain words, no marketing. Include how to start it from a clean machine." Then read it and delete everything that is not true yet. The fuller handover version follows in the next unit, based on the [product README template](../../templates/README-product.md).

### 5. Set a feedback path (2 min)

Decide on exactly one place where a user reports a problem or an idea: an issue tracker, a simple form, or a shared document. Write into the README:

- where to report,
- what to include ("what you tried, what happened, what you expected"),
- who reads it, and how often.

Choose a place you can check regularly. Do not promise a response time you cannot keep.

### 6. Find what breaks when someone else uses it (2 min plus homework)

Things that work for you often fail for the second person:

| What breaks | Why | What to do |
|---|---|---|
| "Works on my machine" | Hidden setup: installed tools, settings, file paths only you have | Start it once from a clean folder or a fresh account, following only the README |
| Your login is built in | The app uses your account or your API key | Give users their own login. Keep any app API key on the server, with a spend cap; do not send it to users or put it in browser code (see [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md) and [Secrets and keys](../../diy/07-secrets-and-keys.md)) |
| Blank screen on error | Nobody wrote an error message | Show a sentence that says what went wrong and what to try |
| Unexpected input | Empty fields, very long text, special characters, two people at once | Try each one yourself before users do |
| Costs | Every use spends your credits | Set a cap before you share the link |
| Real data shows up | A user types in real customer details | Say "fake data only" on the first screen, see [rule one](../00-orientation/01-rule-one-no-real-data.md) |

Two ways to find your own list:

- Ask the agent: "Try following only the README. Report steps that fail or are unclear, with what you tried. Say what you could not run. If you find no problems, say so."
- Watch a willing colleague use it without helping. Note where they stop or ask a question. Decide whether the instructions, the app or its setup needs a change. An agent's review does not replace this user observation.

## Done when

- [ ] Your opening sentence says who the tool helps and what it does.
- [ ] You named at least one user who is not you (names in private notes, roles in the repository).
- [ ] MVP.md says what this version includes, what it leaves out and when you will review it.
- [ ] The README answers the four questions.
- [ ] The README says where to report problems and who reads the reports.
- [ ] You checked the starting instructions and recorded any problems or checks you could not complete. Fix the most serious confirmed problems before inviting users.

## Data note

Ask testers to use fictional data and keep real names, customers and messages out of screenshots. Before giving feedback to an agent, rewrite the problem with invented details; removing names alone may leave other personal data. The model service receives what you share with it.

## Next

[Handover and first users](03-handover-and-first-users.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
