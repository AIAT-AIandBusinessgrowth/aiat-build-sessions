# One work cycle: from plan to something finished

| | |
|---|---|
| **Prerequisites** | [Spec interview](../03-plan-first/01-spec-interview.md), or the mini-spec in step 0 below · [Seven sentences](03-seven-sentences.md) |
| **Time** | ~40 min |
| **Outcome** | You can finish one small change, check that it works and save what someone needs to continue next time. |
| **Last verified** | 2026-09-13 |

## Why this matters

Pick one small task from your plan, such as showing only the free rooms for Friday. Ask the agent what already exists before it changes anything.

You will agree on the task, build it in small steps, check the result and save what remains open. This makes it easier to see whether today's task is finished and where to start next time.

## Do it

You need your spec from the [spec interview](../03-plan-first/01-spec-interview.md) and one of its tasks.

**Step 0, only if you skipped track 03: write a mini-spec (5 min).** Three lines are enough:

```text
What: <one sentence, e.g. "a page that shows which rooms are free this week">
For whom: <a role, e.g. "office assistants who book rooms">
Done when: <a check you can do, e.g. "with the sample data I can see the free rooms for Friday">
```

Keep a short note of the task, what you checked and what remains open. You can use your existing project notes.

<details>
<summary>Optional layout for a longer work session</summary>

```text
Cycle log
Date:
Project:
Task:

1. State (five points from the agent):
2. Scope today IN (one sentence):
   Scope today OUT (one sentence):
3. Stages and checks:
   Stage 1:            Check:            Result:
   Stage 2:            Check:            Result:
   Stage 3:            Check:            Result:
4. Done (checked):
   Open (each with a date or a trigger):
```

</details>

### Step 1: Check the state before you start (~5 min)

Let the agent look at the project and tell you in five points what exists and what it would do. Compare those points with your request and the current app.

```text
Look at the current project and my spec. Do not change anything yet.
Tell me in five points: what exists now, and what you would do next for this task.
```

- **Browser builder:** it looks at the current app. Use a chat or planning option if the tool has one, so it does not start editing.
- **Chat assistant:** paste the spec and your last state note first.
- **CLI agent:** use a planning or read-only mode if it has one. In Claude Code, press `Shift+Tab` until plan mode is on ([best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). In Codex, type `/plan` or press `Shift+Tab` ([Codex manual](https://learn.chatgpt.com/docs/codex-manual.md), checked 2026-09-13).

If a point is wrong or claims something you have not checked, resolve that before building.

### Step 2: Agree the scope (~5 min)

Tell the agent what to change today and what to leave alone. This is the task's **scope**. Two sentences are enough:

```text
Scope for today:
IN: [one sentence]
OUT: [one sentence]
If something outside this scope seems necessary, stop and ask me.
```

Keep these sentences with your task note so you can compare the result with the request.

### Step 3: Build in stages, check after each (~25 min)

Split the task into two or three stages. After each stage:

1. The agent shows what it changed.
2. The agent runs its check and shows the output. If it cannot run the check, it says so.
3. You inspect the result: click through, read the output, try an unusual input. See [the verification ladder](01-verification-ladder.md).
4. Note what the check showed if you will need it later.
5. Only then: "Continue with the next stage."

```text
Do stage 1 only: [describe it].
Then show me what you changed and how you checked it. Stop and wait for me.
```

If a stage fails twice, do not keep correcting. Write down what you learned, start a fresh chat or session with the spec and your log, and try again. See [five failure patterns](02-five-failure-patterns.md).

### Step 4: Finish clean (~5 min)

Save what is complete and what remains open so you can resume without rereading the whole conversation.

```text
We are finishing for today. List:
1. What is done, and how each item was checked.
2. What is open. For each open item: one sentence what it is,
   and one line how we will know it is due again (a date or a trigger).
Write this as a short state note I can paste into a fresh chat next time.
```

Then:

- Check the proposed "done" and "open" lists against what you saw.
- Put the open items where you will see them again: in the tool, a note, or an issue tracker such as GitHub Issues. Each one gets a date or a trigger, never just "later".
- Save the state note next to your spec.
- Make sure your work exists somewhere other than this one tab or laptop. More on that in the next unit.

### Run it on your own thing

Try these four steps on one task from your spec. Use the finished result yourself. Then check whether the saved note gives a fresh session enough information to continue.

## Done when

- [ ] The agent gave you a five-point state, and you corrected anything wrong before building.
- [ ] You can say what belonged to today's task and what was left out.
- [ ] You looked at the result of each stage's check yourself.
- [ ] Your note says what is done, how it was checked and what is open.
- [ ] Every open item has a date or a trigger and lives outside the chat.
- [ ] A state note exists that lets you or a fresh chat continue next time.

## Data note

The cycle log, the state note and the open-items list are files that others may see later. Keep them free of real names, customer details and credentials. If a check needs data, use the invented sample data from your spec. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Choose test values](05-choosing-test-values.md): pick the few numbers that show whether your check really worked.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
