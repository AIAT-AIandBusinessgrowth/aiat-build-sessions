# One work cycle: from plan to something finished

| | |
|---|---|
| **Prerequisites** | [Spec interview](../03-plan-first/01-spec-interview.md), or the mini-spec in step 0 below · [Seven sentences](03-seven-sentences.md) |
| **Time** | ~40 min |
| **Outcome** | After this unit you can run one full work cycle on your own project: check the state, agree the scope, build in steps with a check after each, and finish clean with a dated list of what is open. |
| **Last verified** | 2026-09-13 |

## Why this matters

Planning is the part before. This is the part after: how a plan turns into something built, without ending the day unsure what is actually finished.

Without a cycle, work with agents tends to drift. The agent keeps building until nobody remembers what belonged to the task. An hour of unchecked changes is too much to read, so nobody reads it. Open ends stay in the chat and are gone next week.

A cycle has four steps. It costs a few minutes of structure and saves the hour of confusion.

## Do it

You need your spec from the [spec interview](../03-plan-first/01-spec-interview.md) and one of its tasks.

**Step 0, only if you skipped track 03: write a mini-spec (5 min).** Three lines are enough:

```text
What: <one sentence, e.g. "a page that shows which rooms are free this week">
For whom: <a role, e.g. "office assistants who book rooms">
Done when: <a check you can do, e.g. "with the sample data I can see the free rooms for Friday">
```

Pick one small task from it. Keep a cycle log open next to your tool:

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

### Step 1: Check the state before you start (~5 min)

Let the agent look at the project and tell you in five points what it would do. You see at once whether it understood what this is about.

```text
Look at the current project and my spec. Do not change anything yet.
Tell me in five points: what exists now, and what you would do next for this task.
```

- **Browser builder:** it looks at the current app. Use a chat or planning option if the tool has one, so it does not start editing.
- **Chat assistant:** paste the spec and your last state note first.
- **CLI agent:** use a planning or read-only mode if it has one. In Claude Code, press `Shift+Tab` until plan mode is on ([best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). In Codex, type `/plan` or press `Shift+Tab` ([Codex manual](https://learn.chatgpt.com/docs/codex-manual.md), checked 2026-09-13).

If one of the five points is wrong, correct it now. This takes two minutes and saves an hour.

### Step 2: Agree the scope (~5 min)

Write two sentences into the log: what is IN today, and what is explicitly OUT. Tell the agent both.

```text
Scope for today:
IN: [one sentence]
OUT: [one sentence]
If something outside this scope seems necessary, stop and ask me.
```

Without this boundary, the agent keeps building until nobody knows what was part of the task.

### Step 3: Build in stages, check after each (~25 min)

Split the task into two or three stages. After each stage:

1. The agent shows what it changed.
2. The agent runs its check and shows the evidence.
3. You look at the evidence yourself: click through, read the output, try one edge case. See [the verification ladder](01-verification-ladder.md).
4. You write the stage, check and result into the log.
5. Only then: "Continue with the next stage."

```text
Do stage 1 only: [describe it].
Then show me what you changed and how you checked it. Stop and wait for me.
```

If a stage fails twice, do not keep correcting. Write down what you learned, start a fresh chat or session with the spec and your log, and try again. See [five failure patterns](02-five-failure-patterns.md).

### Step 4: Finish clean (~5 min)

At the end, everything open gets written down. What is not written down is gone next week.

```text
We are finishing for today. List:
1. What is done, and how each item was checked.
2. What is open. For each open item: one sentence what it is,
   and one line how we will know it is due again (a date or a trigger).
Write this as a short state note I can paste into a fresh chat next time.
```

Then:

- Copy "done" and "open" into your log.
- Put the open items where you will see them again: in the tool, a note, or an issue tracker such as GitHub Issues. Each one gets a date or a trigger, never just "later".
- Save the state note next to your spec.
- Make sure your work exists somewhere other than this one tab or laptop. More on that in the next unit.

### Run it on your own thing

Do one full cycle now, on a real task from your spec. It does not matter how small the task is. What matters is that all four steps happen, in order, and the log is filled in.

## Done when

- [ ] The agent gave you a five-point state, and you corrected anything wrong before building.
- [ ] The log has one IN sentence and one OUT sentence for today.
- [ ] Every stage in the log has a check and a result you looked at yourself.
- [ ] The log lists what is done (with how it was checked) and what is open.
- [ ] Every open item has a date or a trigger and lives outside the chat.
- [ ] A state note exists that lets you or a fresh chat continue next time.

## Data note

The cycle log, the state note and the open-items list are files that others may see later. Keep them free of real names, customer details and credentials. If a check needs data, use the invented sample data from your spec. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md): make sure what you just finished exists twice.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
