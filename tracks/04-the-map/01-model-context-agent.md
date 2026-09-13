# Model, context, agent: three words that explain most surprises

| | |
|---|---|
| **Prerequisites** | [Your first build](../01-first-build/01-your-first-build.md) |
| **Time** | ~15 min |
| **Outcome** | After this unit you can explain what a model, a context window and an agent are in one sentence each, and use that to decide when to start a fresh chat. |
| **Last verified** | 2026-09-13 |

## Why this matters

Two people use the same tool on the same task. One gets something useful, the other gets nonsense. Most of the time the tool is not the reason. The reason is one of three things: which model was running, what was in its context, and whether it could act and check its own work.

You do not need to know how any of this works inside. You need a working picture, so you know which lever to pull.

## Do it

### 1. The model: a text predictor with a cutoff date

A language model predicts the next piece of text, over and over, based on patterns from a very large amount of training text. That is why it writes fluent answers. It is also why it can write fluent wrong answers.

Three things follow from that:

- **It has a knowledge cutoff.** It learned from text up to a certain date and knows nothing after it, unless a tool looks things up for it. Vendors publish the cutoff per model, for example on [Anthropic's model overview](https://platform.claude.com/docs/en/about-claude/models/overview) (checked 2026-09-13).
- **Different models differ a lot.** Large and small, new and old, fast and careful. Inside one tool you can often switch models. Results change with them.
- **It sounds equally sure when it is wrong.** Confidence in the wording tells you nothing.

> Analogy: a very well-read colleague who has been off the grid since a certain date. Fast, helpful, and sometimes convincingly wrong.

**The model gap.** When your results differ from a colleague's, compare the models first. Then compare the prompts. Blame the tool last.

### 2. The context window: finite working memory

The context window is everything the model can see in one conversation at once:

- your messages and its replies
- files, pages and screenshots you added
- output from tools it ran
- instructions from the tool, the project and you

It is measured in tokens, which are pieces of words. It is large but finite. As of 2026-09-13, Anthropic lists 1M tokens for its larger current models (roughly 555k words) and 200K tokens for its smallest one (roughly 150k words) ([model overview](https://platform.claude.com/docs/en/about-claude/models/overview), checked 2026-09-13). Other vendors publish their own numbers.

Size is not the whole story. Anthropic's own guide puts it this way: "Claude's context window fills up fast, and performance degrades as it fills" ([Claude Code best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). That matches what you will see in any tool:

- early instructions get lost
- old wrong attempts keep steering new answers
- the agent mixes up things from two different topics

**So start fresh on purpose.** When the topic changes, or the chat feels muddled, write the current state into a short file or note (what it is, what is done, what is next). Open a new chat or session. Paste the state. Continue.

> Analogy: the context window is a desk, not an archive. A few clear papers on the desk beat a pile where the important page is at the bottom.

### 3. The agent: model plus tools plus a loop

A **chatbot** answers and waits. You ask, it writes, you do the rest.

An **agent** works in a loop:

1. **Reads**: files, pages, error messages, your spec.
2. **Acts**: writes or edits code, runs a command, clicks, builds a preview.
3. **Checks**: looks at the result, runs a test, reads the error.
4. **Repeats** until the goal is reached or it stops to ask you.

Browser app builders are agents too. They write code, run it, show you a preview and fix their own errors. CLI coding agents do the same with the files on your laptop.

> Analogy: a chatbot is a help desk that gives advice. An agent is an intern with hands and a checklist. You still decide what "done" means, and you still check the work.

### 4. Try it (5 min)

1. Ask your tool: "Which model are you, and what is your knowledge cutoff?"
2. Compare the answer with the vendor's model page. If they disagree, you just saw point 1 in action.
3. Open your longest chat or session. Find one early instruction the tool stopped following. That is point 2.
4. Write one sentence each for model, context window and agent, in your own words, and say them to someone.

## Done when

- [ ] You can explain model, context window and agent in one sentence each, without notes.
- [ ] You know where your tool shows which model is running, and how to switch it if possible.
- [ ] You have started one fresh chat or session with a short state summary instead of continuing a long one.

## Data note

Everything you put into the context window leaves your laptop and goes to the vendor, including pasted files and screenshots. A screenshot is an upload. Keep using made-up data. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Which tool for what](02-which-tool-for-what.md): chat assistant, browser builder, CLI agent or editor, matched to the task.
