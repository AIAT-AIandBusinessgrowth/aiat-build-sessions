# Five failure patterns

| | |
|---|---|
| **Prerequisites** | [The verification ladder](01-verification-ladder.md) · [Model, context, agent](../04-the-map/01-model-context-agent.md) |
| **Time** | ~15 min |
| **Outcome** | After this unit you can recognise five common failure patterns in your own chats and sessions, and apply a counter-move for each before it costs you an hour. |
| **Last verified** | 2026-09-13 |

## Why this matters

When an agent goes wrong, the cause is often not the agent. It is how the conversation was run. These five patterns show up in every tool. You recognise them by your own behaviour, not by the agent's.

The names come from Anthropic's guide for Claude Code, section "Avoid common failure patterns" ([Claude Code best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). The descriptions below are adapted so they apply to chat assistants and browser builders too.

## Do it

### 1. Read the five patterns (7 min)

#### The kitchen sink session

- **Symptom:** one chat or session, many unrelated tasks. You start with one thing, ask something else, come back. Answers get muddled. The agent mixes up details from different topics.
- **Why:** the context window is full of things that have nothing to do with the current task.
- **Counter-move:** one chat per task. When the topic changes, start a new chat or session. In a CLI agent, start with a fresh context: `/clear` in Claude Code, `/new` for a new chat in Codex ([Codex manual](https://learn.chatgpt.com/docs/codex-manual.md), checked 2026-09-13). Carry over only a short state note.

#### Correcting over and over

- **Symptom:** you correct the same thing a third time. Each answer is a little worse.
- **Why:** the failed attempts stay in the context and keep steering the next answer.
- **Counter-move:** after two failed corrections, stop. Start fresh with a better first prompt that includes what you learned. The guide gives exactly this threshold: after two failed corrections, clear and rewrite the initial prompt ([source](https://code.claude.com/docs/en/best-practices), checked 2026-09-13).

#### The overstuffed instruction file

- **Symptom:** your project instructions are long. In a builder that is the knowledge or custom instructions area. In a CLI agent it is a file such as `AGENTS.md` or `CLAUDE.md`. The agent ignores rules that are clearly written there.
- **Why:** important rules get lost in the noise.
- **Counter-move:** prune. For every line, ask: "Would removing this cause a mistake?" If not, delete it. If the agent already does something right without the line, delete it.

#### The trust-then-verify gap

- **Symptom:** the result looks right, you accept it, and it breaks later on an edge case: an empty field, a large number, a special character.
- **Why:** you accepted before you checked, or instead of checking.
- **Counter-move:** check before you accept, using the [verification ladder](01-verification-ladder.md). If you cannot check it, do not ship it.

#### The endless exploration

- **Symptom:** you asked the agent to "look into" something. It reads, searches and thinks for a long time and never arrives at a result. Or it returns a huge report nobody asked for.
- **Why:** the task had no scope and no stop condition, so the exploration fills the context.
- **Counter-move:** scope it. Say what question to answer, where to look, what shape the answer should have, and when to stop. For example: "Look only at the three files in the reports folder. Answer in five bullet points. Stop after that."

### 2. Find them in your own work (8 min)

Open your last three chats or sessions. For each pattern, tick if it happened and write the counter-move you will use next time.

```text
Date:
Chats or sessions looked at:

[ ] Kitchen sink session       Next time I will:
[ ] Correcting over and over   Next time I will:
[ ] Overstuffed instructions   Next time I will:
[ ] Trust-then-verify gap      Next time I will:
[ ] Endless exploration        Next time I will:

The pattern that cost me the most time:
```

If you are in a group, tell one other person which pattern cost you the most time, with the real example. Then listen to theirs and check whether it happened to you too.

## Done when

- [ ] You can name the five patterns and one counter-move for each without looking.
- [ ] You checked three of your own recent chats or sessions and ticked the patterns that happened.
- [ ] You applied one counter-move in a real chat or session today, for example starting fresh after two failed corrections.

## Data note

When you look back through old chats, you may find real data you pasted before you knew the rule. Do not copy it anywhere else. Delete the chat if your tool allows it, and if it involved other people's data, see [If something went wrong](../02-data-first/04-if-something-went-wrong.md).

## Next

[Seven sentences](03-seven-sentences.md): seven working rules that prevent most of these patterns, plus a loop prompt to copy.
