# Parallel agents

| | |
|---|---|
| **Prerequisites** | [Loop engineering](02-loop-engineering.md), [The verification ladder](../05-verify-and-loop/01-verification-ladder.md) |
| **Time** | ~25 min |
| **Outcome** | You can split two independent tasks between agents, keep their files separate and check the combined result. |
| **Last verified** | 2026-09-13 |

## Why this matters

Pick two small changes and write the files each one needs. If they need the same file or one depends on the other's result, do them in order. Otherwise, try one agent on each task.

Working in parallel can save time on independent tasks. It also creates two results to review and uses more of your account allowance. You will separate the work, review it and check that both changes work together. See [The adoption ladder](../04-the-map/03-adoption-ladder.md) for where this fits in the course.

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

A **worktree** is a second folder of the same Git repository, on its own branch. Each has separate checked-out files, reducing accidental overwrites. This does not restrict where an agent can write; scope and permissions still matter. Worktrees share history, so merging later is normal Git work.

From your own project's main folder, check `git status` and commit the files you have reviewed. Then create the separate folder:

```bash
git worktree add -b feature/export ../room-planner-export   # new branch in a new folder
git worktree list                                          # show all worktrees
```

These are standard Git commands ([source](https://git-scm.com/docs/git-worktree), checked 2026-09-13). Check `git worktree list` first if resuming: reuse your existing branch/folder or pick unused names. Do not remove an active worktree to make the command succeed.

Start one agent session in each folder. Worktrees separate working files; shared services, ports, Git history and external accounts still need coordination. Never stop a process just because it occupies the port you wanted.

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - `claude --worktree <name>` (or `-w <name>`) creates a worktree and starts Claude in it. By default it is created under `.claude/worktrees/<name>`. ([source](https://code.claude.com/docs/en/worktrees))

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - The Codex app can run tasks in a dedicated Git worktree. ([source](https://learn.chatgpt.com/docs/environments/git-worktrees))

If your browser app builder does not offer Git worktrees, use a project copy for an experiment. Review and carry over the change yourself; a copied project does not merge changes automatically.

### 3. Split the file scope before you start (5 min)

Separate folders stop edits from landing in the same working file. When you **merge**, you combine the branches. Changes to the same code can still conflict then. Assign the files before starting:

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

A **subagent** is another agent given a bounded task by the main session. It uses a separate context and returns a report. Use it to investigate one question or review a change without adding all its search output to the main conversation. Give it a file scope too; separate context does not imply separate files or permissions.

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - Each subagent runs in its own context window. ([source](https://code.claude.com/docs/en/sub-agents))
> - `/subtask` hands a side task to a subagent that reports back into this conversation. `/fork` copies the conversation into a new background session. `/branch` branches the current conversation to try a different direction. ([source](https://code.claude.com/docs/en/commands))

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - Ask Codex to use subagents for independent work ([subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)). `/agent` inspects and switches between agent threads while they run; the main thread collects their results. `/fork` creates a new chat and keeps the original transcript. ([source](https://learn.chatgpt.com/docs/codex-manual.md))

### 5. Review before merge (5 min)

Check each result before combining it:

1. **Read the diff.** Does it stay inside its file scope?
2. **Run the checks** in that worktree and look at the output.
3. **Fresh reviewer:** give a new session or subagent the changed files and the "done when" line. Ask: "Report only problems you can show. Label anything untested. If you find no problems, say so and name what you could not check." Confirm findings before fixing them.
4. **Merge one result**, then run the checks again on the combined state before merging the next.

After the result is reviewed, committed and integrated, stop **your own** agent in that worktree. Confirm its state before cleanup:

```bash
git -C ../room-planner-export status --short
git worktree list
```

Only if there is no remaining work and you no longer need the folder:

```bash
git worktree remove ../room-planner-export
```

The branch remains. If Git refuses because the folder is dirty or in use, investigate; do not force removal.

### 6. Watch the costs (2 min)

Each agent uses its own context, so usage grows with every agent you add.

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - The docs state that agent teams use about 7 times more tokens than standard sessions when teammates run in plan mode, because each teammate has its own context window. `/usage` shows usage. ([source](https://code.claude.com/docs/en/costs))

Start with two agents. Check usage after the first round before adding a third. Set a spend cap first, see [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md).

### Exercise (included in the time above)

Take a small change that splits into two independent parts. Write the file assignments, create a separate worktree for each and run one agent in each. Review both results and merge one at a time. If you do not have enough tool allowance, plan the split now and leave the actual parallel run untested.

## Done when

- [ ] You can name one task where parallel helps and one where it hurts.
- [ ] Two agents worked in two separate worktrees. Planning the split alone leaves this check open.
- [ ] Each agent had a written file scope, and neither left it.
- [ ] Each result was reviewed (diff, checks, fresh reviewer) before merge.
- [ ] Checks ran again after each merge.
- [ ] You checked usage after the parallel run.

## Data note

More agents create more copies in worktrees, model input and logs. Keep fictional data only. A worktree is a fresh checkout, so untracked files ignored by `.gitignore`, such as `.env`, are not in it unless copied separately. Claude Code can copy files listed in `.worktreeinclude` ([source](https://code.claude.com/docs/en/worktrees), checked 2026-09-13). Do not copy keys into every worktree. Keep any needed key in the approved secret store and use a spend cap; see [Secrets and keys](../../diy/07-secrets-and-keys.md).

## Next

[Agents in operation](04-agents-in-operation.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
