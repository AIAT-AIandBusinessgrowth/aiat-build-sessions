# Parallel agents

| | |
|---|---|
| **Prerequisites** | [Loop engineering](02-loop-engineering.md), [The verification ladder](../05-verify-and-loop/01-verification-ladder.md) |
| **Time** | ~25 min |
| **Outcome** | After this unit you can decide when parallel agents help, give each one its own working copy and file scope, use subagents for side tasks, and review results before they are merged. |
| **Last verified** | 2026-09-13 |

## Why this matters

Two agents can do twice the work. They can also overwrite each other's files, double your review load and double your bill. Parallel work multiplies output, not trust.

It pays off when tasks are truly independent and your checks are good enough that you review results, not every keystroke. See [The adoption ladder](../04-the-map/03-adoption-ladder.md) for where this step sits.

## Do it

### 1. Decide whether parallel helps (3 min)

| Parallel helps | Parallel hurts |
|---|---|
| Independent features in different files | Two tasks that touch the same files |
| Research on different questions | The plan is still unclear |
| The same change across many files, after it worked on two or three | Task B needs the result of task A |
| You have time to review every result | You cannot review more than one stream |

If in doubt, run one agent and a second one only for review.

### 2. Give each agent its own working copy (5 min)

A **worktree** is a second folder of the same Git repository, on its own branch. Agents in different worktrees cannot overwrite each other's files. They share history, so merging later is normal Git work.

Commit your work first. Then:

```bash
git worktree add -b feature/export ../room-planner-export   # new branch in a new folder
git worktree list                                          # show all worktrees
git worktree remove ../room-planner-export                 # clean up; the branch stays
```

These are standard Git commands ([source](https://git-scm.com/docs/git-worktree), checked 2026-09-13). Start one agent session in each folder.

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - `claude --worktree <name>` (or `-w <name>`) creates a worktree and starts Claude in it. By default it is created under `.claude/worktrees/<name>`. ([source](https://code.claude.com/docs/en/worktrees))

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - The Codex app can run tasks in a dedicated Git worktree. ([source](https://learn.chatgpt.com/docs/environments/git-worktrees))

In a browser app builder there are no worktrees. The closest pattern is to duplicate the project, try the change in the copy, and carry over what works.

### 3. Split the file scope before you start (5 min)

Worktrees prevent collisions while agents work. Conflicts come back at merge time if two agents changed the same file. Prevent that on paper first:

| Agent | Task | May change | Must not touch |
|---|---|---|---|
| A | CSV export | `src/export/`, `tests/export/` | everything else |
| B | Booking form validation | `src/booking/form.*`, `tests/booking/` | everything else |

If two tasks need the same file, run them one after the other.

Put the scope into each agent's brief:

```text
Task: add CSV export of bookings.
You may change only files in src/export/ and tests/export/.
If you need to change any other file, stop and tell me which one and why.
Done when: tests in tests/export/ pass and you show the output.
```

### 4. Use subagents for side tasks (5 min)

A **subagent** is a helper inside one session. It runs in its own context window and returns only a summary. Use it for work that would flood your main conversation: searching a large codebase, reading long logs, or reviewing a diff with fresh eyes.

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - Each subagent runs in its own context window. ([source](https://code.claude.com/docs/en/sub-agents))
> - `/subtask` hands a side task to a subagent that reports back into this conversation. `/fork` copies the conversation into a new background session. `/branch` branches the current conversation to try a different direction. ([source](https://code.claude.com/docs/en/commands))

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - Ask Codex to use subagents for independent work ([subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)). `/agent` inspects and switches between agent threads while they run; the main thread collects their results. `/fork` creates a new chat and keeps the original transcript. ([source](https://learn.chatgpt.com/docs/codex-manual.md))

### 5. Review before merge (5 min)

Every result goes through the same gate, one at a time:

1. **Read the diff.** Does it stay inside its file scope?
2. **Run the checks** in that worktree and look at the output.
3. **Fresh reviewer:** a new session or subagent that sees only the diff and the "done when" line. Tell it: "Only report issues that affect correctness or the stated requirements." A reviewer asked to find problems will always find some; this keeps it from inventing work.
4. **Merge one result**, then run the checks again on the combined state before merging the next.

### 6. Watch the costs (2 min)

Each agent uses its own context, so usage grows with every agent you add.

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - The docs state that agent teams use about 7 times more tokens than standard sessions when teammates run in plan mode, because each teammate has its own context window. `/usage` shows usage. ([source](https://code.claude.com/docs/en/costs))

Start with two agents. Check usage after the first round before adding a third. Set a spend cap first, see [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md).

### Exercise (included in the time above)

Take a small change that splits into two independent parts. Write the scope table, create two worktrees, run one agent in each, review both results with a fresh reviewer, and merge one after the other.

## Done when

- [ ] You can name one task where parallel helps and one where it hurts.
- [ ] Two agents worked in two separate worktrees.
- [ ] Each agent had a written file scope, and neither left it.
- [ ] Each result was reviewed (diff, checks, fresh reviewer) before merge.
- [ ] Checks ran again after each merge.
- [ ] You checked usage after the parallel run.

## Data note

More agents means more copies of your code and data in more places: worktrees on disk, context sent to the vendor, logs. Keep fake data only. A worktree is a fresh checkout, so files your `.gitignore` excludes, such as `.env`, are not in it unless you copy them. Claude Code copies them only when you list them in `.worktreeinclude` ([source](https://code.claude.com/docs/en/worktrees), checked 2026-09-13). Do not spread keys into every worktree. Use one key with a spend cap instead, see [Secrets and keys](../../diy/07-secrets-and-keys.md).

## Next

[Agents in operation](04-agents-in-operation.md)
