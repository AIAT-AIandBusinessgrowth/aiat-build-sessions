# The verification ladder: don't trust, check

| | |
|---|---|
| **Prerequisites** | [Model, context, agent](../04-the-map/01-model-context-agent.md) · [Spec interview](../03-plan-first/01-spec-interview.md), or a three-line mini-spec (what, for whom, done when) |
| **Time** | ~20 min |
| **Outcome** | After this unit you can check an agent's result on three rungs: a check inside the prompt, evidence you look at yourself, and a second opinion from a fresh reviewer. |
| **Last verified** | 2026-09-13 |

## Why this matters

An agent saying "done" is a claim, not a result. Models sound equally sure when they are right and when they are wrong. The output often looks plausible and still misses the empty field, the large number or the name with an accent.

Of all the habits in this material, checking is the one people skip most. Not because it is hard, but because the result looks fine. And every time an unchecked result happens to work, skipping the check the next time feels a little more normal.

Anthropic's guide for its own coding agent is blunt about it: "If you can't verify it, don't ship it" ([Claude Code best practices](https://code.claude.com/docs/en/best-practices), checked 2026-09-13). Simon Willison calls the careful style "vibe engineering": professionals move fast with AI while staying accountable for what they produce ([Vibe engineering, 7 October 2025](https://simonwillison.net/2025/Oct/7/vibe-engineering/), checked 2026-09-13).

The bar is simple: the same as for work done by a person. You would not publish a colleague's report without reading it. Do not accept an agent's result without checking it.

## Do it

Take one thing an agent or builder recently told you was finished. Your own first build is fine. No spec yet because you skipped the [spec interview](../03-plan-first/01-spec-interview.md)? Take five minutes and write three lines: what it is, for whom, and "done when" (one check you can do). Then climb the ladder with it.

### Rung 1: Put the check inside the prompt (5 min)

Tell the agent how you will judge the result, and ask it to tell you how it checked. Add this to the end of your next request:

```text
Before you say it is done:
1. Check the result against what I asked for, point by point.
2. Try these inputs: an empty field, a very large number,
   and a name with accents such as "Zoë Ångström-Łukasz".
3. Tell me exactly how you checked each point, and what you could not check.
Do not write "done" for anything you did not actually check.
```

This does not require another service, but an extra model request can use credits. Ask for actual test output or perform a check yourself when the agent cannot run one. Watch the answer for the last point: "what I could not check" is where the real gaps are.

### Rung 2: Demand evidence and look at it yourself (8 min)

A description of a check is still a claim. Evidence is something you can see.

| Lane | What counts as evidence |
|---|---|
| Browser builder | You click through the preview yourself, with the edge-case inputs from rung 1. You screenshot what breaks. |
| Chat assistant | You copy the result into its real place (the spreadsheet, the document) and try it there. |
| CLI agent | The agent runs the check and shows the actual output: test results, the command and what it printed, the changed files. You read the output, not the summary. |

Then do the one check nobody can do for you: use it once as the person in the spec would. If the spec has a "done when" line, test exactly that line.

Write down what you found in two lines: what worked, what did not.

### Rung 3: Get a second opinion (7 min)

The agent that built something is loyal to its own work. A fresh reviewer is not. Open a **new** chat or session, ideally with a different model, and paste the spec, the result and this prompt:

```text
You are reviewing work you did not write. Your job is to prove it wrong.

Here is what was asked for (the spec):
[paste spec]

Here is the result:
[paste the result, the code, or a description with screenshots]

List:
1. Every point where the result does not match the spec.
2. Inputs or situations it will probably get wrong.
3. Anything you cannot verify from what you were given.

Do not fix anything. Rank your findings by impact, most serious first.
```

Take the top findings back to the builder, one at a time, and check each fix on rung 2.

### Which rung for which task

| Risk if it is wrong | Climb to |
|---|---|
| Low: a draft for yourself, a throwaway experiment | Rung 1 plus one observed check; a claim alone never counts |
| Medium: something others will use or read | Rung 2 |
| High: numbers people decide on, something that is hard to undo | Rung 3 |

This is a teaching sequence: define a check, inspect evidence, then add independent review. The [German verification mechanisms](../../modules/de/07-agenten-grundlagen.md) distinguish prompts, session rules, deterministic checks and independent review. Those are enforcement mechanisms, not equivalent rung numbers. Both require observed evidence. An independent agent review can still be wrong.

## Done when

- [ ] You added a check to a prompt and got an answer that says how it was checked and what was not.
- [ ] You looked at real evidence yourself, including at least one edge-case input, and wrote down two lines of findings.
- [ ] You ran the review prompt in a fresh chat or session and took at least one finding back to the builder.
- [ ] You can say which rung a given task needs, and why.

## Data note

A reviewer needs the same fake data as the builder. When you paste results into a second tool, check first that no real names, addresses or records slipped in along the way, for example in screenshots or error messages. A screenshot is an upload. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Five failure patterns](02-five-failure-patterns.md): the habits that make checking harder, and how to spot them in your own work.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
