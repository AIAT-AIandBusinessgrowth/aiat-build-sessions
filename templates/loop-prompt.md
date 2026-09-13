# Loop prompt

Choose one small change and paste the first prompt into your tool. It asks for a plan, checked steps and a note you can use next time. You still need to inspect the result. These prompts accompany [Seven sentences](../tracks/05-verify-and-loop/03-seven-sentences.md) and [One work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md).

## 1. The loop prompt

Paste this at the start of a piece of work.

```text
Before you change anything: read the project and tell me in five points
what you would do. We agree on the scope first. Only THEN do you build.

Build in small stages. After each stage: show me what you changed
and run the checks (tests, build, or a click-through of the preview).
Do not claim anything you have not actually run or checked.

At the end: list everything that is unfinished. Turn each item into a task
with one line that says how we will know it is due again.
Put the list where I can find it next week (a file, a note, or an issue tracker).
Do not commit, push, deploy, publish or send messages unless I explicitly
authorised that action for this task. Existing authorisation within the
agreed scope remains valid; ask only if it is missing or the scope changes.
```

- **Browser builder:** "read the project" means look at the current app and its instructions.
- **Chat assistant:** paste your spec or your last state note first.

## 2. One work cycle, step by step

Use these when you want to run the four steps one at a time. A short note of the task, checks and open work is enough.

<details>
<summary>Optional log for a longer work session</summary>

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

**Step 1: check the state.** Use a planning or read-only mode if your tool has one.

```text
Look at the current project and my spec. Do not change anything yet.
Tell me in five points: what exists now, and what you would do next for this task.
```

**Step 2: agree the scope.**

```text
Scope for today:
IN: [one sentence]
OUT: [one sentence]
If something outside this scope seems necessary, stop and ask me.
```

**Step 3: one stage at a time.** Look at the evidence yourself before you continue. If a stage fails twice, start a fresh chat or session with the spec and your log.

```text
Do stage 1 only: [describe it].
Then show me what you changed and how you checked it. Stop and wait for me.
```

**Step 4: finish clean.**

```text
We are finishing for today. List:
1. What is done, and how each item was checked.
2. What is open. For each open item: one sentence what it is,
   and one line how we will know it is due again (a date or a trigger).
Write this as a short state note I can paste into a fresh chat next time.
```

Then put the open items where you will see them again, save the state note next to your spec, and make sure your work exists in a second place.

## 3. Compact loop for CLI agents

For Claude Code, Codex and similar agents that can work with files. From [Loop engineering](../tracks/08-advanced/02-loop-engineering.md). Adapt the paths and decide whether you authorise commits before using it. The separate note files are optional; one project note can hold the same information.

```text
Work in this loop until the plan is done or you are blocked.
1. Research: read what you need. Do not edit yet. Write findings to notes/findings.md.
2. Plan: write notes/plan.md with steps, files and a "done when" line per step.
   Stop and wait for my approval.
3. Build: do one step. Run its check and review the diff.
   If I authorised commits, stage only this task's reviewed files and commit
   with a clear message. Otherwise leave the changes for my review.
4. Verify: show me the command you ran and its output. Do not say "should work".
5. Close: update notes/plan.md (done / open). Add a useful lesson to learnings/
   if there is one. Do not invent a lesson or push without my permission.
Stop after 5 steps or when a check fails twice in a row, and tell me why.
Do not deploy, publish or send messages unless I explicitly authorised that
action for this task. Keep completed checks separate from untested claims.
```

In a browser app builder, run the loop by hand: one change per message, check the preview, save a version before the next change.

## Data note

The cycle log, the state note and the task list are files that others may see later. Keep them free of real names, customer details and keys. See [Rule one: no real data](../tracks/00-orientation/01-rule-one-no-real-data.md).
