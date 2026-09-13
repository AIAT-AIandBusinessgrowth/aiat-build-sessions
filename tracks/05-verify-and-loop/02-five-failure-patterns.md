# Five failure patterns

| | |
|---|---|
| **Prerequisites** | [The verification ladder](01-verification-ladder.md) · [Model, context, agent](../04-the-map/01-model-context-agent.md) |
| **Time** | ~15 min |
| **Outcome** | You can spot a conversation that is getting stuck and choose a useful next step. |
| **Last verified** | 2026-09-13 |

## Why this matters

Open one recent chat where the work got stuck. Compare it with the examples below and choose one change to try. If you have no old chats, use the examples as practice situations.

Repeating the same request may not fix the problem. A smaller task, a fresh chat or a concrete check can help you see what to change next.

The names come from Anthropic's guide for Claude Code, section "Avoid common failure patterns" ([Claude Code best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). The descriptions below are adapted so they apply to chat assistants and browser builders too.

## Do it

### 1. Read the five patterns (7 min)

#### The kitchen sink session

- **Symptom:** one chat or session, many unrelated tasks. You start with one thing, ask something else, come back. Answers get muddled. The agent mixes up details from different topics.
- **Why it can happen:** the context window, the material available for the next answer, contains unrelated tasks.
- **Counter-move:** one chat per task. When the topic changes, start a new chat or session. In a CLI agent, start with a fresh context: `/clear` in Claude Code, `/new` for a new chat in Codex ([Codex manual](https://learn.chatgpt.com/docs/codex-manual.md), checked 2026-09-13). Carry over only a short state note.

#### Correcting over and over

- **Symptom:** you correct the same thing a third time without getting closer to the requested result.
- **Why it can happen:** the failed attempts remain in the conversation and may influence the next answer.
- **Counter-move:** after two failed corrections, stop. Start fresh with a better first prompt that includes what you learned. The guide gives exactly this threshold: after two failed corrections, clear and rewrite the initial prompt ([source](https://code.claude.com/docs/en/best-practices), checked 2026-09-13).

#### The overstuffed instruction file

- **Symptom:** your project instructions are long. In a builder that is the knowledge or custom instructions area. In a CLI agent it is a file such as `AGENTS.md` or `CLAUDE.md`. The agent ignores rules that are clearly written there.
- **Why it can happen:** long or conflicting instructions make the important requirements harder to follow.
- **Counter-move:** review the instructions for duplication or contradiction. Try removing unnecessary detail in a copy, then check the result. Keep data rules, permissions and requirements even if a small test does not exercise them.

#### The trust-then-verify gap

- **Symptom:** the result looks right, you accept it, and it breaks later on an edge case: an empty field, a large number, a special character.
- **Why it happens:** the result was accepted before this input was tried.
- **Counter-move:** check before you accept, using the [verification ladder](01-verification-ladder.md). If you cannot check it, do not ship it.

#### The endless exploration

- **Symptom:** you asked the agent to "look into" something. It reads, searches and thinks for a long time and never arrives at a result. Or it returns a huge report nobody asked for.
- **Why it can happen:** the request does not say where to look, what to return or when to stop.
- **Counter-move:** scope it. Say what question to answer, where to look, what shape the answer should have, and when to stop. For example: "Look only at the three files in the reports folder. Answer in five bullet points. Stop after that."

### 2. Find them in your own work (8 min)

Look at up to three recent chats, starting with the one you opened. Which pattern, if any, matches what happened? Try its suggested response on a small task. You do not need to find a problem in every chat.

<details>
<summary>Optional note for comparing several chats</summary>

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

</details>

In a group, you can describe one example using invented details. Share what you tried and whether it helped; do not paste old chats with personal data.

## Done when

- [ ] You can explain a pattern that matches your chat, or explain why none does.
- [ ] You tried one suggested response on your task or an invented example and checked whether it helped.
- [ ] Given a different example from this page, you can choose a next step and explain why.

## Data note

When you look back through old chats, you may find real data you pasted before you knew the rule. Do not copy it anywhere else. Delete the chat if your tool allows it, and if it involved other people's data, see [If something went wrong](../02-data-first/04-if-something-went-wrong.md).

## Next

[Seven sentences](03-seven-sentences.md): ways to plan, check and save a piece of work, with a prompt to try.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
