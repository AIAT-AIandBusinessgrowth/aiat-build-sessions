# Context engineering

| | |
|---|---|
| **Prerequisites** | [Model, context, agent](../04-the-map/01-model-context-agent.md), [A vault and AGENTS.md](../07-second-brain/01-vault-and-agents-md.md) |
| **Time** | ~20 min |
| **Outcome** | You can give an agent the files it needs, reduce unnecessary instructions and continue a task in a fresh session. |
| **Last verified** | 2026-09-13 |

This track is optional. It assumes you work with a command-line agent such as Claude Code or Codex.

## Why this matters

Open one small project task. List the files an agent needs to answer it, then give it those paths. After its answer, check which files it actually opened.

The **context window** is the amount of text and other input a model can use for its next answer. It may contain instructions, conversation, files and tool output. Selecting useful input is called **context engineering**. It helps avoid unrelated material and unnecessary processing. Anthropic describes this in [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

## Do it

### 1. See what fills the context (5 min)

| What uses context | Where it comes from | How to reduce it |
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

In Claude Code, try `/context` now and again after some work; an hour is one possible comparison interval. Look for the largest category. If your tool has no context display, inspect the files and tool output in the conversation. Asking the agent may give a useful summary, but it cannot replace a measured usage display.

### 2. Keep instruction files lean (5 min)

Open one instruction file and look for repeated or outdated guidance:

> Would removing this line make the agent make mistakes?

If a line seems unnecessary, test that in a copy. Keep essential data rules, permissions and project requirements; a small test cannot prove they are unnecessary.

Three habits keep the file small:

- **Make rules specific.** "Always be careful" does not tell the agent what to do. State the required behaviour or the mistake to avoid.
- **Move detail out.** Put long instructions into separate files (`rules/deploy.md`) and write one line in `AGENTS.md` that says when to open them. The agent loads them only when needed.
- **Explain the task and its limits.** Include exact steps when they are required for correctness or safety; leave routine choices open.

### 3. A rule comes back only when the agent stumbles repeatedly

Try removing duplicate guidance from a copy of a small fictional-data project. Keep the original instructions available for comparison:

1. Rename the copy's `AGENTS.md` to `AGENTS.old.md`. Write a shorter `AGENTS.md` that still contains all data rules, permissions and required checks. Keep Claude Code's `CLAUDE.md` import pointing at `@AGENTS.md`.
2. Give the agent the same small task twice in fresh sessions with restricted permissions.
3. Compare the results with the requirements. Record any differences; it is possible to find none.
4. Restore guidance that prevents a demonstrated problem. Do not generalise two successful attempts to tasks you did not test.

<details>
<summary>Background: periodically reviewing instructions</summary>

Boris Cherny discusses reducing instructions in [We Cut 80% of Claude Code's Prompt](https://www.youtube.com/watch?v=qyPCVqFUyDo) (checked 2026-09-13). The interview describes removing corrections a newer model no longer needed and suggests reviewing personal instructions, skills and hooks about every six months. The broader delete-and-observe suggestion is not permission to remove security controls. The exercise above tests optional guidance in a copy.

</details>

### 4. Start fresh or compact?

| Start a fresh session when | Compact when |
|---|---|
| The task changes | The same task continues |
| The history is full of failed attempts | The history holds decisions you still need |
| The agent keeps repeating a wrong approach | You are close to done and want to keep the thread |
| You want a review without the building conversation | |

Before starting fresh, save a short file: goal, checked results, open work and next step. Give the new session that file. After compacting, check that important requirements are still present; a summary can omit details.

### 5. Set the autonomy slider per task

**Autonomy** means how much the agent may do without asking you. Choose it for each task. Andrej Karpathy calls this an "autonomy slider" in [Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) (checked 2026-09-13).

| Slider | What the agent may do | Good for |
|---|---|---|
| Low | Propose; you approve each step | Unfamiliar code, anything touching real systems |
| Middle | Edit files; you read the diff before it counts | Normal feature work with tests |
| High | Run until a checked condition holds | Well-tested tasks, in a sandbox, with a stop condition |

Before allowing more actions, check that you can detect a wrong result and stop or undo the work. Tool permissions enforce access limits; a prompt alone does not. See [The verification ladder](../05-verify-and-loop/01-verification-ladder.md).

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - Permission modes: **Manual** (config value `default`) asks before most edits, commands and network access. **Plan** is for analysis before changes. In **auto** mode, a second model (a classifier) reviews actions instead of you. On supported setups, the built-in default can start a session in auto mode, and Claude Code shows a notice the first time. ([source](https://code.claude.com/docs/en/permission-modes))

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - Plan mode: toggle with `/plan` or Shift+Tab. ([source](https://learn.chatgpt.com/docs/codex-manual.md))
> - `codex exec` runs in a read-only sandbox by default; `--sandbox workspace-write` allows edits. ([source](https://learn.chatgpt.com/docs/non-interactive-mode.md))

## Done when

- [ ] You inspected the context display or the visible conversation and can name unnecessary material. If no usage display exists, you did not claim a measured size.
- [ ] You applied the "would removing this line cause mistakes?" question to every line of one instruction file.
- [ ] You tried shorter optional instructions in a copy, kept essential rules and compared the actual results.
- [ ] You wrote a state file before starting a fresh session.
- [ ] For your current task, you can say where the autonomy slider stands and which check justifies it.

## Data note

Everything in the context is sent to the model vendor, including files the agent opens on its own. A lean context is also a data habit: point the agent at the files it needs, and keep folders with anything sensitive out of its reach. Fake data only, as in [rule one](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Loop engineering](02-loop-engineering.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
