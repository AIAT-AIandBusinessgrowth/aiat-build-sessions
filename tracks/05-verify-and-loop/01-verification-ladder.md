# Check an agent's work

| | |
|---|---|
| **Prerequisites** | [Model, context, agent](../04-the-map/01-model-context-agent.md) · [Spec interview](../03-plan-first/01-spec-interview.md), or a three-line mini-spec (what, for whom, done when) |
| **Time** | ~20 min |
| **Outcome** | You can ask an agent to check its work, try the result yourself and get a fresh review. |
| **Last verified** | 2026-09-13 |

## Why this matters

Open something you built, or try the [notebook calculator](../../exercises/verification-lab/README.md). Write one sentence saying what should happen. You will ask the agent to check it, try it yourself, and ask a fresh session to review it.

An export button can look finished while the downloaded CSV is empty. These checks help you find the difference between a feature that appears complete and one that does the requested job.

## Do it

For example: “The CSV should contain every row currently shown in the table.” Use your sentence for the checks below.

### Rung 1: Put the check inside the prompt (5 min)

Tell the agent how you will judge the result, and ask it to tell you how it checked. Add this to the end of your next request:

```text
Before you say it is done:
1. Check the result against what I asked for, point by point.
2. Try an unusual input that fits this task: for example an empty field,
   a very large number, or a name with accents such as "Zoë Ångström-Łukasz".
3. Tell me exactly how you checked each point, and what you could not check.
Do not write "done" for anything you did not actually check.
```

Read the check output. If the agent cannot run a check, try it yourself. Extra agent requests may use credits.

### Rung 2: Demand evidence and look at it yourself (8 min)

Open the preview or the exported file. Check what it actually contains.

| Your tool | What to look at |
|---|---|
| Browser builder | Click through the preview with the unusual inputs from rung 1. Keep a screenshot if it helps explain a problem. |
| Chat assistant | You copy the result into its real place (the spreadsheet, the document) and try it there. |
| CLI agent | The agent runs the check and shows the actual output: test results, the command and what it printed, the changed files. You read the output, not the summary. |

Use it once as its intended user would. Check the sentence you wrote at the start.

If you need to return to this later, note what worked and what remains open.

### Rung 3: Get a second opinion (7 min)

Open a **new** chat or session so the review starts without the building conversation. Give it your request and result:

```text
Check whether this result meets the request. Report problems you can show;
do not invent findings if you find none.

Here is what was asked for:
[paste the request]

Here is the result:
[paste the result, the code, or a description with screenshots]

List:
1. Any mismatch, with the example or evidence that shows it.
2. Suspected problems that still need a check, clearly labelled as untested.
3. Anything you cannot check from what you were given.

Do not fix anything. Rank your findings by impact, most serious first.
```

Check whether the findings hold up. Take confirmed problems back to the builder, then try each fix yourself. If the reviewer found no problems, record that along with what it could not check.

### Which rung for which task

| Risk if it is wrong | Checks to use |
|---|---|
| Low: a draft for yourself, a throwaway experiment | Rung 1 plus one observed check; a claim alone never counts |
| Medium: something others will use or read | Rung 2 |
| High: numbers people decide on, something that is hard to undo | Rung 3 |

These are starting points for choosing checks. Another agent can miss a problem too.

<details>
<summary>If you also use the German reference material</summary>

The [German verification mechanisms](../../modules/de/07-agenten-grundlagen.md) describe prompts, session rules, deterministic checks and independent review. Their numbers describe different mechanisms, not the three steps here. Both require looking at actual results.

</details>

## Done when

- [ ] You added a check to a prompt and got an answer that says how it was checked and what was not.
- [ ] You tried the result yourself, including one unusual input, and can explain what the check showed.
- [ ] You ran a fresh review and checked its findings, or recorded that it found no problems and what remained unchecked.
- [ ] You can say which rung a given task needs, and why.

## Data note

A reviewer needs the same fake data as the builder. When you paste results into a second tool, check first that no real names, addresses or records slipped in along the way, for example in screenshots or error messages. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Five failure patterns](02-five-failure-patterns.md): the habits that make checking harder, and how to spot them in your own work.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
