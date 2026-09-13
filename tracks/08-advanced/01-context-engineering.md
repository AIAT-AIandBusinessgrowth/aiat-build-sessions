# Context engineering

| | |
|---|---|
| **Prerequisites** | [Model, context, agent](../04-the-map/01-model-context-agent.md), [A vault and AGENTS.md](../07-second-brain/01-vault-and-agents-md.md) |
| **Time** | ~20 min |
| **Outcome** | After this unit you can say what fills an agent's context, keep instruction files lean, choose between starting fresh and compacting, and set how much autonomy a task gets. |
| **Last verified** | 2026-09-13 |

This track is optional. It assumes you work with a command-line agent such as Claude Code or Codex.

## Why this matters

The context window is the agent's desk. Everything on it is read again on every turn: the vendor's instructions, your instruction files, the conversation so far, every file and log the agent opened. A crowded desk has two effects. The agent follows your rules less reliably, and each turn costs more.

Commands change with every release. The habit of keeping the desk clean does not. Anthropic describes this discipline in [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

## Do it

### 1. See what fills the context (5 min)

| What is on the desk | Where it comes from | How to reduce it |
|---|---|---|
| System instructions and tool descriptions | The vendor, plus every connected tool or server | Disconnect tools you do not use |
| Instruction files | `AGENTS.md`, `CLAUDE.md`, memory files | Keep them short (step 2) |
| Conversation | Everything said so far | Start fresh between unrelated tasks (step 4) |
| Tool output | Search results, logs, diffs, file contents | Let a subagent do the searching and return a summary |
| Attached files | What you paste or point to | Point to the one file needed, not the folder |

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - `/context` shows what is filling the window. `/compact` summarizes the conversation to free space. `/clear` starts fresh on a new task and keeps project memory. ([source](https://code.claude.com/docs/en/commands))
> - `/compact` accepts instructions on what to keep, for example `/compact Focus on the open decisions`. ([source](https://code.claude.com/docs/en/costs))
> - Auto memory is on by default. The docs recommend keeping `CLAUDE.md` under 200 lines. ([source](https://code.claude.com/docs/en/memory))

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - `/compact` summarizes a long chat. Codex also compacts chats automatically. `/fork` creates a new chat and keeps the original transcript. ([source](https://learn.chatgpt.com/docs/codex-manual.md))
> - Codex reads only a limited amount of each `AGENTS.md`; the setting `project_doc_max_bytes` controls how much. ([source](https://learn.chatgpt.com/docs/codex-manual.md))

Try it: run the context command in your tool (or ask the agent "what is in your context right now?") at the start of a session and again after an hour of work. Note the biggest item.

### 2. Keep instruction files lean (5 min)

Instruction files grow. Each problem adds a line, and nobody removes one. Go through yours with one question per line:

> Would removing this line make the agent make mistakes?

If the answer is no, delete the line.

Three habits keep the file small:

- **Rules are written-down mistakes.** A line earns its place because something went wrong without it. "Always be careful" is not a rule.
- **Move detail out.** Put long instructions into separate files (`rules/deploy.md`) and write one line in `AGENTS.md` that says when to open them. The agent loads them only when needed.
- **Say what, not how.** Describe the task, the limits and what "done" means. Do not dictate every step.

### 3. A rule comes back only when the agent stumbles repeatedly

Boris Cherny, who created Claude Code, talks about this in a public interview titled [We Cut 80% of Claude Code's Prompt](https://www.youtube.com/watch?v=qyPCVqFUyDo) (checked 2026-09-13). When a newer model no longer needed many of the old corrections, the team removed them from the system prompt. His advice for users follows the same idea: from time to time (he suggests about every six months), delete your own instruction files, skills and hooks, and watch what the model does without them. A line comes back only when the model stumbles **repeatedly** at the same place, never "just in case".

Exercise, on a copy of a project:

1. Rename `AGENTS.md` to `AGENTS.old.md` (Claude Code: also the `CLAUDE.md` that imports it).
2. Give the agent the same small task twice in fresh sessions.
3. Write down where it went wrong.
4. Bring back only the lines that prevent those mistakes.

### 4. Start fresh or compact?

| Start a fresh session when | Compact when |
|---|---|
| The task changes | The same task continues |
| The history is full of failed attempts | The history holds decisions you still need |
| The agent keeps repeating a wrong approach | You are close to done and want to keep the thread |
| You want an unbiased review of the result | |

Before you start fresh, let the agent write the state into a file: goal, what is done, what is open, next step. A new session reads that file. This is how work survives across days: memory in files, not in a full context window.

### 5. Set the autonomy slider per task

Andrej Karpathy uses the picture of an **autonomy slider** in his public talk [Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) (checked 2026-09-13): for each task, you decide how much the agent may do without you.

| Slider | What the agent may do | Good for |
|---|---|---|
| Low | Propose; you approve each step | Unfamiliar code, anything touching real systems |
| Middle | Edit files; you read the diff before it counts | Normal feature work with tests |
| High | Run until a checked condition holds | Well-tested tasks, in a sandbox, with a stop condition |

The rule: **more autonomy needs stronger checks before it.** Move the slider per task, not once per project. Verification is covered in [The verification ladder](../05-verify-and-loop/01-verification-ladder.md).

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - Permission modes: **Manual** (config value `default`) asks before most edits, commands and network access. **Plan** is for analysis before changes. In **auto** mode, a second model (a classifier) reviews actions instead of you. On supported setups, the built-in default can start a session in auto mode, and Claude Code shows a notice the first time. ([source](https://code.claude.com/docs/en/permission-modes))

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - Plan mode: toggle with `/plan` or Shift+Tab. ([source](https://learn.chatgpt.com/docs/codex-manual.md))
> - `codex exec` runs in a read-only sandbox by default; `--sandbox workspace-write` allows edits. ([source](https://learn.chatgpt.com/docs/non-interactive-mode.md))

## Done when

- [ ] You checked what fills your agent's context and named the biggest item.
- [ ] You applied the "would removing this line cause mistakes?" question to every line of one instruction file.
- [ ] You ran the delete-and-observe exercise once and brought back only lines that prevented real mistakes.
- [ ] You wrote a state file before starting a fresh session.
- [ ] For your current task, you can say where the autonomy slider stands and which check justifies it.

## Data note

Everything in the context is sent to the model vendor, including files the agent opens on its own. A lean context is also a data habit: point the agent at the files it needs, and keep folders with anything sensitive out of its reach. Fake data only, as in [rule one](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Loop engineering](02-loop-engineering.md)
