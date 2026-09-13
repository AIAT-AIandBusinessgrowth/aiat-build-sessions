# Seven sentences for working with any agent

| | |
|---|---|
| **Prerequisites** | [The verification ladder](01-verification-ladder.md) · [Five failure patterns](02-five-failure-patterns.md) |
| **Time** | ~15 min |
| **Outcome** | After this unit you can name seven working rules for agent work, show them in your own tool, and use a loop prompt that makes any agent follow them. |
| **Last verified** | 2026-09-13 |

## Why this matters

Some tools enforce a good way of working: plan first, check each step, write down what is open. Most do not. The habits are good either way. These seven sentences work the same in a chat assistant, a browser builder, a CLI agent or an editor.

One warning up front. Reading these sentences changes nothing. Everyone agrees with them. The only way they stick is to show each one in your own tool, once, with your own work. That is what the exercise below is for.

## Do it

### 1. The seven sentences (3 min)

1. **Understand, then agree, then build.** The order is the whole trick. If you build first, you negotiate with the result afterwards.
2. **Every stage ends with a check.** A test, a click-through, a read of what changed. After each stage, not only at the end, where everything arrives at once.
3. **Unfinished work becomes a task, never a vague "later".** Write it down, with one line that says how you will know it is due again.
4. **The state lives in files, not in the chat history.** A chat is gone when the window closes. A file survives a crash and a week.
5. **Simplify first, then lock it in.** Remove what is not needed before you write tests or checklists. Otherwise you lock in exactly what you wanted to get rid of.
6. **What you learned becomes a rule.** A mistake that hurt once gets written into your project instructions. Otherwise it happens again in a month, to you or someone else.
7. **Say "done" only after the check has run.** Not when it looks done. That goes for you and for the agent.

If you only keep one, keep number three. Everything you want to show in a few weeks has to exist as a written task first.

### 2. The loop prompt (2 min)

Paste this at the start of a piece of work, in any agent. A copy lives in the [loop prompt template](../../templates/loop-prompt.md).

```text
Before you change anything: read the project and tell me in five points
what you would do. We agree on the scope first. Only THEN do you build.

Build in small stages. After each stage: show me what you changed
and run the checks (tests, build, or a click-through of the preview).
Do not claim anything you have not actually run or checked.

At the end: list everything that is unfinished. Turn each item into a task
with one line that says how we will know it is due again.
Put the list where I can find it next week (a file, a note, or an issue tracker).
```

In a browser builder, "read the project" means: look at the current app and its instructions. In a chat assistant, paste your spec or state note first.

### 3. Show them, don't just read them (10 min)

Ten minutes are enough for three sentences, not seven. Pick three now, for example 1, 2 and 7. Show the other four during your next work sessions, and write down when.

Work in pairs if you can: one person reads a sentence out loud, the other shows it live in their own tool. Swap after each sentence. Alone, do the same and take a screenshot or a one-line note for each.

| # | Show it like this |
|---|---|
| 1 | Ask the agent for its five-point plan on a small change. Change one point before you let it build. |
| 2 | Let it do one stage only. Check that stage before you say "continue". |
| 3 | Write one unfinished item as a task with a "due again when" line. |
| 4 | Ask the agent to write the current state into a file or note. Close the chat. Open a new one, paste the state, continue. |
| 5 | Ask: "What in this can we remove without losing what the spec asks for?" Remove one thing. |
| 6 | Add one line to your project instructions, based on a mistake from this week. |
| 7 | Ask the agent: "Show me the check you ran." If there is none, run one before anyone says done. |

## Done when

- [ ] You can say the seven sentences from memory, in your own words.
- [ ] You showed three sentences in your own tool today, with a note or screenshot as proof.
- [ ] You wrote down when you will show the other four in your next work sessions.
- [ ] You used the loop prompt on one real piece of work.
- [ ] At least one unfinished item exists as a written task with a "due again when" line.

## Data note

Sentence 4 means your state lives in files and notes. Those files follow the same rule as everything else: made-up data only, no real names or records, not even in a "quick note". See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[One work cycle](04-one-work-cycle.md): put the seven sentences together and run one full cycle on your own project.
