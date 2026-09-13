# Loop engineering

| | |
|---|---|
| **Prerequisites** | [One work cycle](../05-verify-and-loop/04-one-work-cycle.md), [Context engineering](01-context-engineering.md) |
| **Time** | ~25 min |
| **Outcome** | You can run a small task in repeated steps, check each result and stop the agent at a clear limit. |
| **Last verified** | 2026-09-13 |

## Why this matters

Choose a small task in a copy of your project. Write how you will know it is finished and when the agent must stop if it cannot finish. Try the loop prompt below while you watch the first run.

A **loop** repeats a set of steps. Here the agent reads, plans, builds and checks before continuing. Saving the results lets you see what happened and resume later. A stop limit prevents the same failed attempt from running indefinitely.

## Do it

### 1. The five stages (5 min)

| Stage | What happens | What it leaves behind |
|---|---|---|
| **Research** | The agent reads the files needed for the task. No edits. | Relevant facts and open questions |
| **Plan** | Steps, files to change, and a "done when" line per step. You approve it. | A plan file |
| **Build in steps** | One step at a time. After each: check, then save (commit). | Small diffs you can read |
| **Verify** | Run the check and inspect its output. Use a fresh reviewer when the task needs one. | Check results attached to the plan |
| **Close** | Save what is done, what is open and any useful lesson. Push only if authorised. | Enough information to continue later |

[One work cycle](../05-verify-and-loop/04-one-work-cycle.md) introduces these steps. Here you add a repeatable prompt and a stop limit. One note can hold the plan, results and open questions; separate files are optional.

### 2. Write your loop down (5 min)

Start from the [loop prompt template](../../templates/loop-prompt.md) and adapt it. This example uses separate note files. Read the commit permission before using it: choose whether the agent may commit your reviewed files.

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
```

Save it in your vault or repository. The same text works in Claude Code and Codex. In a browser app builder, run the loop by hand: one change per message, check the preview, save a version before the next change.

### 3. Learnings become rules (5 min)

After a run, keep a short note if something will help with a future task. You do not need a new rule after every run.

- **First time:** it stays a learning note.
- **Second time the same thing happens:** promote it to one line in `AGENTS.md`, with the reason. For example: "Run the test suite before every commit, because two commits broke the export."
- **When a rule stops mattering:** delete it. See [Context engineering](01-context-engineering.md): a rule comes back only when the agent stumbles repeatedly.

Keep required safety and data rules even if recent runs did not exercise them.

### 4. Let the tool keep the loop running

Try one loop while watching before scheduling anything. The reference below is optional; use the entry for your tool. Features and limits change, so check the source before relying on them.

<details>
<summary>Claude Code and Codex commands for repeated or unattended work</summary>

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - `/goal <condition>`: Claude keeps working until the condition is met. After each turn, a small fast model checks the condition. The goal clears when it is met, when the model judges it impossible, or on an error you have to fix. The condition can be up to 4,000 characters. Add a limit such as `or stop after 20 turns`. ([source](https://code.claude.com/docs/en/goal))
> - `/loop`: repeats a prompt on a fixed interval, or self-paced if you leave the interval out; then Claude picks a delay between one minute and one hour. A session holds up to 50 scheduled tasks. Recurring tasks expire 7 days after creation. ([source](https://code.claude.com/docs/en/scheduled-tasks))
> - Routines run on the vendor's cloud on a schedule, on an API call, or on GitHub events. They are in research preview. The minimum schedule interval is one hour. ([source](https://code.claude.com/docs/en/routines))
> - Headless: `claude -p "<task>"` runs one task without the interactive screen. Add `--bare` in scripts to skip auto-discovery of hooks, skills, plugins and servers. ([source](https://code.claude.com/docs/en/headless))
> - A `Stop` hook runs your own check when Claude wants to stop. Shape in `.claude/settings.json`: ([source](https://code.claude.com/docs/en/hooks))
>
> ```json
> {
>   "hooks": {
>     "Stop": [
>       { "hooks": [ { "type": "command", "command": "./scripts/check.sh", "timeout": 30 } ] }
>     ]
>   }
> }
> ```

The hook example assumes that your project already has an executable `scripts/check.sh`. It is not a file supplied by this lesson. Read the linked hook documentation before adding the example to your settings, and test how your check's result affects stopping.

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - `/goal` starts Goal mode in an interactive CLI session. ([source](https://learn.chatgpt.com/docs/codex-manual.md))
> - `codex exec "<task>"` runs non-interactively. `--json` prints a stream of events, `-o <path>` writes the final message to a file, `--output-schema` asks for a final answer that matches a JSON Schema. `--full-auto` is deprecated; use `--sandbox workspace-write` instead. In CI, the docs describe authentication with `CODEX_API_KEY` and warn against setting it as a job-wide variable in workflows that run repository code. ([source](https://learn.chatgpt.com/docs/non-interactive-mode.md))
> - The Codex app can run scheduled tasks, in a dedicated Git worktree or in your local environment. ([source](https://learn.chatgpt.com/docs/codex-manual.md))

</details>

### 5. Guardrails for any loop (5 min)

Before you let a loop run without watching, check:

- [ ] **Stop condition:** a state that can be proven from output ("tests exit 0"), not a feeling ("looks good").
- [ ] **Budget:** a maximum number of turns, steps or hours.
- [ ] **Visible evidence:** the check's command and output appear in the transcript or a file.
- [ ] **Saved steps:** reviewed changes have a saved version you can return to. Commit explicitly reviewed files if commits are authorised.
- [ ] **Read the result:** a run that finished is not a run that succeeded. Read the transcript or the evidence file.
- [ ] **Keys:** a loop that uses an API key uses a key with a spend cap, see [Secrets and keys](../../diy/07-secrets-and-keys.md) and [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md).

## Done when

- [ ] You have a written loop prompt with the five stages and a stop rule.
- [ ] You ran one full loop and inspected the plan, actual check output and any open work.
- [ ] You promoted one repeated learning to a rule, or you can say why none repeated yet.
- [ ] You can name one feature in your tool that keeps a loop running, and its stop condition.

## Data note

Unattended loops must never touch real data. Run them on fake data, in a copy of the project. API keys used by headless runs are secrets: keep them out of the repository and out of logs. A routine or scheduled task that runs in the cloud sends your repository content to that cloud.

## Next

[Parallel agents](03-parallel-agents.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
