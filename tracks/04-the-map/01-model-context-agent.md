# Model, context, agent: three words that explain most surprises

Check which model your tool uses, what information it can see and what actions it can take. You will learn when to look up a fact, give clearer instructions or start a fresh chat.

| | |
|---|---|
| **Prerequisites** | [Your first build](../01-first-build/01-your-first-build.md) |
| **Time** | ~15 min |
| **Outcome** | Explain model, context window and agent in plain words, and start a fresh chat with the information it needs. |
| **Last verified** | 2026-09-13 |

## Why this matters

The same tool can give different results when the model, supplied information or available actions change. Knowing these three parts helps you find what to change when an answer is wrong or a task gets stuck.

## Do it

### 1. The model: a text predictor with a cutoff date

A language model generates text by predicting the next piece, based on patterns learned during training. A fluent answer can still be wrong.

Three things follow from that:

- **It has a knowledge cutoff.** Its training does not reliably cover events after that date. Newer facts need to come from information you provide or a tool that looks them up. Vendors publish the cutoff per model, for example on [Anthropic's model overview](https://platform.claude.com/docs/en/about-claude/models/overview) (checked 2026-09-13).
- **Models differ.** They vary in speed and capabilities. Many tools let you switch models, which can change the result.
- **Confident wording does not prove accuracy.** Check the answer itself.

**The model gap.** If you and a colleague get different results, compare the models, prompts and supplied files.

### 2. The context window: finite working memory

The context window holds the information available to the model for a response:

- your messages and its replies
- files, pages and screenshots you added
- output from tools it ran
- instructions from the tool, the project and you

It is measured in tokens, which are pieces of words. It is large but finite. As of 2026-09-13, Anthropic lists 1M tokens for its larger current models (roughly 555k words) and 200K tokens for its smallest one (roughly 150k words) ([model overview](https://platform.claude.com/docs/en/about-claude/models/overview), checked 2026-09-13). Other vendors publish their own numbers.

More room does not guarantee a better answer. Anthropic warns that performance can get worse as the context fills ([Claude Code best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). In a long chat, watch for:

- early instructions no longer being followed
- new answers repeating an earlier mistake
- the agent mixing up two different topics

**Start fresh when needed.** When the topic changes or the chat mixes things up, write a short note: what the project is, what is done and what comes next. Paste it into a new chat or session.

### 3. The agent: model plus tools plus a loop

A **chatbot** can answer a question and wait for you to act. Some chat tools also offer agent features.

An **agent** works in a loop:

1. **Reads**: files, pages, error messages, your spec.
2. **Acts**: writes or edits code, runs a command, clicks, builds a preview.
3. **Checks**: looks at the result, runs a test, reads the error.
4. **Repeats** until the goal is reached or it stops to ask you.

Browser app builders are agents too. They write code, run it, show you a preview and fix their own errors. CLI coding agents do the same with the files on your laptop.

You still decide what the result must do and check that it does it.

### 4. Try it (5 min)

1. Ask your tool: "Which model are you, and what is your knowledge cutoff?"
2. Compare the answer with the model shown in the tool and the vendor's model page. If they disagree, do not rely on the model's claim about itself.
3. In a long practice chat, look for an earlier instruction that is no longer followed. You may not find one; do not invent a failure.
4. Save the current project state in a short note and use it to start a fresh chat.
5. Explain model, context window and agent in one sentence each, using your own words.

## Done when

- [ ] You can explain model, context window and agent in one sentence each, without notes.
- [ ] You know where your tool shows which model is running, and how to switch it if possible.
- [ ] You have started one fresh chat or session with a short state summary instead of continuing a long one.

## Data note

Everything you put into the context window leaves your laptop and goes to the vendor, including pasted files and screenshots. A screenshot is an upload. Keep using made-up data. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Which tool for what](02-which-tool-for-what.md): chat assistant, browser builder, CLI agent or editor, matched to the task.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
