# Loop engineering

| | |
|---|---|
| **Prerequisites** | [One work cycle](../05-verify-and-loop/04-one-work-cycle.md), [Context engineering](01-context-engineering.md) |
| **Time** | ~25 min |
| **Outcome** | After this unit you can run work as a repeatable loop (research, plan, build in steps, verify, close), turn repeated learnings into rules, and know which tool features keep a loop running. |
| **Last verified** | 2026-09-13 |

## Why this matters

One prompt, one result: sometimes that works, and you cannot tell why. A loop you can repeat is a method. Each round leaves files behind (a plan, evidence, a learning), so the next round starts smarter, even in a fresh session.

The tools now offer features that keep an agent working without you pressing enter. They only help when the loop underneath is sound. A loop without a stop condition and a real check just produces mistakes faster.

## Do it

### 1. The five stages (5 min)

| Stage | What happens | What it leaves behind |
|---|---|---|
| **Research** | The agent reads code, notes and docs. No edits. | A short findings note |
| **Plan** | Steps, files to change, and a "done when" line per step. You approve it. | A plan file |
| **Build in steps** | One step at a time. After each: check, then save (commit). | Small diffs you can read |
| **Verify** | Evidence, not claims: test output, a command and its result, a screenshot. Ideally a fresh reviewer. | Evidence attached to the plan |
| **Close** | What is done, what is open, one learning. Push. | Task list for next time, a learning note |

[One work cycle](../05-verify-and-loop/04-one-work-cycle.md) shows this at small scale. Here the point is to make it a habit you write down.

### 2. Write your loop down (5 min)

Start from the [loop prompt template](../../templates/loop-prompt.md) and adapt it. A compact version:

```text
Work in this loop until the plan is done or you are blocked.
1. Research: read what you need. Do not edit yet. Write findings to notes/findings.md.
2. Plan: write notes/plan.md with steps, files and a "done when" line per step.
   Stop and wait for my approval.
3. Build: do one step. Run the check for that step. Commit with a clear message.
4. Verify: show me the command you ran and its output. Do not say "should work".
5. Close: update notes/plan.md (done / open), and add one learning to learnings/.
Stop after 5 steps or when a check fails twice in a row, and tell me why.
```

Save it in your vault or repository. The same text works in Claude Code and Codex. In a browser app builder, run the loop by hand: one change per message, check the preview, save a version before the next change.

### 3. Learnings become rules (5 min)

Every loop ends with one learning: a short note on what went wrong or what worked.

- **First time:** it stays a learning note.
- **Second time the same thing happens:** promote it to one line in `AGENTS.md`, with the reason. For example: "Run the test suite before every commit, because two commits broke the export."
- **When a rule stops mattering:** delete it. See [Context engineering](01-context-engineering.md): a rule comes back only when the agent stumbles repeatedly.

This keeps the instruction file made of real mistakes, not of wishes.

### 4. Let the tool keep the loop running

These features change often. Check the source links before you rely on a number.

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

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - `/goal` starts Goal mode in an interactive CLI session. ([source](https://learn.chatgpt.com/docs/codex-manual.md))
> - `codex exec "<task>"` runs non-interactively. `--json` prints a stream of events, `-o <path>` writes the final message to a file, `--output-schema` asks for a final answer that matches a JSON Schema. `--full-auto` is deprecated; use `--sandbox workspace-write` instead. In CI, the docs describe authentication with `CODEX_API_KEY` and warn against setting it as a job-wide variable in workflows that run repository code. ([source](https://learn.chatgpt.com/docs/non-interactive-mode.md))
> - The Codex app can run scheduled tasks, in a dedicated Git worktree or in your local environment. ([source](https://learn.chatgpt.com/docs/codex-manual.md))

### 5. Guardrails for any loop (5 min)

Before you let a loop run without watching, check:

- [ ] **Stop condition:** a state that can be proven from output ("tests exit 0"), not a feeling ("looks good").
- [ ] **Budget:** a maximum number of turns, steps or hours.
- [ ] **Visible evidence:** the check's command and output appear in the transcript or a file.
- [ ] **Small steps:** each step is committed, so you can go back.
- [ ] **Read the result:** a run that finished is not a run that succeeded. Read the transcript or the evidence file.
- [ ] **Keys:** a loop that uses an API key uses a key with a spend cap, see [Secrets and keys](../../diy/07-secrets-and-keys.md) and [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md).

## Done when

- [ ] You have a written loop prompt with the five stages and a stop rule.
- [ ] You ran one full loop and it left a plan, evidence and one learning.
- [ ] You promoted one repeated learning to a rule, or you can say why none repeated yet.
- [ ] You can name one feature in your tool that keeps a loop running, and its stop condition.

## Data note

Unattended loops must never touch real data. Run them on fake data, in a copy of the project. API keys used by headless runs are secrets: keep them out of the repository and out of logs. A routine or scheduled task that runs in the cloud sends your repository content to that cloud.

## Next

[Parallel agents](03-parallel-agents.md)
