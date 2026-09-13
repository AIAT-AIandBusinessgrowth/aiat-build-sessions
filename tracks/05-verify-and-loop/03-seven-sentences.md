# Seven sentences for working with any agent

| | |
|---|---|
| **Prerequisites** | [The verification ladder](01-verification-ladder.md) · [Five failure patterns](02-five-failure-patterns.md) |
| **Time** | ~15 min |
| **Outcome** | You can plan a small change, check what the agent produces and leave enough information to continue later. |
| **Last verified** | 2026-09-13 |

## Why this matters

Choose a small change, such as adding a CSV export. Use the prompt below to ask for a plan before the agent edits anything. Then check one completed step yourself.

This gives you a way to see what changed and what still needs work. You can use it in a chat assistant, a browser builder, a command-line agent or an editor. A prompt guides the agent; you still need to check whether it followed the request.

## Do it

### 1. The seven sentences (3 min)

1. **Agree on the task before building.** Check the proposed change while it is still a plan.
2. **Check each completed stage.** Run a test, click through the result or inspect the changed file before continuing.
3. **Write down unfinished work.** Give each item a date or an event that tells you when to return to it.
4. **Save the current state outside the chat.** A short file or note lets a fresh session continue without the full conversation. Back it up too.
5. **Remove unnecessary work before adding more.** Check that each feature or step is needed by the request. Preserve the checks that protect required behaviour.
6. **Keep useful lessons in project instructions.** Add a specific rule when a mistake repeats; review old rules when they stop helping.
7. **Check before saying "done".** Say what you actually tested and what remains untested.

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

Start with three of the sentences, for example 1, 2 and 7. Allow about ten minutes for this first attempt. Try the others when they fit your next task.

In pairs, one person chooses a sentence and the other shows it in their tool. Swap afterwards. Alone, try it yourself; keep a note only if it helps you continue later.

| # | Show it like this |
|---|---|
| 1 | Ask the agent for its five-point plan on a small change. Correct anything that does not match your request before building. |
| 2 | Let it do one stage only. Check that stage before you say "continue". |
| 3 | Write one unfinished item as a task with a "due again when" line. |
| 4 | Ask the agent to write the current state into a file or note. Close the chat. Open a new one, paste the state, continue. |
| 5 | Ask: "What in this can we remove without losing what the spec asks for?" Remove something only if it is unnecessary; it is fine to keep the result as it is. |
| 6 | If a mistake has repeated, add one specific instruction that addresses it. Otherwise, leave the file as it is. |
| 7 | Ask the agent: "Show me the check you ran." If there is none, run one before anyone says done. |

## Done when

- [ ] You tried three of the sentences in your own tool and can explain what each helped you check.
- [ ] You can choose a useful sentence for a different task.
- [ ] You used the loop prompt on one real piece of work.
- [ ] Any unfinished work is saved as a task with a date or an event that tells you when to return to it. If nothing remains, say so.

## Data note

Sentence 4 means your state lives in files and notes. Those files follow the same rule as everything else: made-up data only, no real names or records, not even in a "quick note". See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[One work cycle](04-one-work-cycle.md): put the seven sentences together and run one full cycle on your own project.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
