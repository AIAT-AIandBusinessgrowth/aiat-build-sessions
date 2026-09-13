# Which tool for what

| | |
|---|---|
| **Prerequisites** | [Model, context, agent](01-model-context-agent.md) · [Pick your lane](../00-orientation/02-pick-your-lane.md) |
| **Time** | ~15 min |
| **Outcome** | After this unit you can tell a chat assistant, a browser app builder, a CLI coding agent and an editor-based agent apart, and pick one for a given task with a one-line reason. |
| **Last verified** | 2026-09-13 |

## Why this matters

There are four families of tools, and they overlap more every month. People lose hours because they pick by hype or by what a colleague uses, not by the task. A browser builder is great for a shareable form and poor for cleaning a spreadsheet that must stay on your laptop. A CLI agent is the other way round.

One rule covers most choices: pick the tool by what you can check, not by what can do the most.

## Do it

### 1. Know the four families (5 min)

| Family | What it is | Examples | Good at | Watch out |
|---|---|---|---|---|
| Chat assistant | A chat window with a model. Some can run small pieces of code or show interactive previews. | Claude, ChatGPT, Gemini | Thinking an idea through, writing a spec, explaining, drafting text, reviewing someone else's result | You copy results out by hand. Nothing is kept as a project unless you save it. |
| Browser app builder | An agent in the browser that builds and hosts a small web app for you. | Lovable, Bolt, v0, Replit, Google AI Studio (Build), Claude artifacts | A shareable app, form, calculator or small dashboard, with no installation | Your app and data live on the vendor's servers. Export and backup are your job. |
| CLI coding agent | An agent in a terminal on your own computer. It reads and changes files and runs commands. | Claude Code, Codex CLI, Antigravity CLI | Work with files on your laptop, repeatable tasks, projects in a Git repository | More power, more things that can break. You install and update it yourself. |
| Editor-based agent | An agent built into a code editor. You see every file and change as it happens. | Cursor, VS Code with GitHub Copilot, Antigravity | Reading and adjusting code alongside the agent | Assumes you are comfortable in a code editor. |

Prices, free tiers and data settings change often. They are in the [tool matrix](../../diy/tool-matrix-2026-09.md), with sources and dates.

### 2. Decide by task type (5 min)

| Your task | First choice | Why |
|---|---|---|
| "I have an idea but no plan" | Chat assistant | Interview and spec first. See [Spec interview](../03-plan-first/01-spec-interview.md). |
| "I want something colleagues can click on today" | Browser app builder | It hosts the result and gives you a link. |
| "I need to transform files that must not leave my laptop" | CLI coding agent, with fake data while building | The finished script runs locally against your own files. |
| "I want to automate a step I repeat every week" | CLI coding agent | Scripts and files stay, and you can run them again. |
| "I want to understand and change existing code" | Editor-based agent or CLI coding agent | You see the files and each change. |
| "I want someone to check a result" | A fresh chat assistant, ideally with a different model | Fresh context, no loyalty to the first answer. See [Verification ladder](../05-verify-and-loop/01-verification-ladder.md). |
| "I am not sure" | The tool you already know, with the smallest possible task | Knowing how to check beats having more features. |

Three questions settle most cases:

1. **Where must the result live?** A link for others, or files on your computer.
2. **Where may the data go?** If nothing may leave your laptop, a hosted builder is out for the real run. Build with fake data either way.
3. **How will you check it?** Pick the tool where you can see the evidence: a preview you can click, output you can read, a file you can open.

### 3. Try it (5 min)

Write down three tasks from your coming week. For each one, pick a family and write one line why. Then pick the smallest of the three and do it in the chosen tool.

```text
Task:
Family:
Why (one line):
How I will check it:
```

## Done when

- [ ] You can name the four tool families and one example of each.
- [ ] You have three tasks from your own week, each with a chosen family and a one-line reason.
- [ ] For each task you wrote down how you will check the result.

## Data note

The choice of tool does not change the data rule. Hosted builders and chat assistants send everything to the vendor. CLI and editor agents also send what they read to the model provider. Only the finished script, run by you, touches your real files. Build with made-up data in every family. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[The adoption ladder](03-adoption-ladder.md): where you are with these tools today, and what moves you up.
