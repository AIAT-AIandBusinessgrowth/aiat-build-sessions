# Verification lab: a confident handover with a missing check

| | |
|---|---|
| **Prerequisites** | None. Use fictional quantities only. |
| **Time** | ~20 min for the basic lab; extensions take longer. Estimates. |
| **Outcome** | After this lab you can predict a result, find a gap in an agent's evidence and choose a test that catches it. |
| **Last verified** | 2026-09-13 |

## Why this matters

An agent can show a passing example and still miss the requirement. You need to decide what the evidence proves. The lab deliberately contains a calculation defect; the rest of the learning material explains how to investigate it.

## Do it

### 1. Choose browser or paper

**Browser:** download the repository using GitHub's **Code → Download ZIP**, extract it, and double-click `exercises/verification-lab/index.html`. GitHub's file page shows source code; it does not run the app. No server, package installation or account is required. The form sends nothing and stores nothing.

**Paper:** use the requirement and handover below. The supplied implementation divides the participant count by four and rounds to the nearest whole number. You can compare that rule with the requirement without running code.

### 2. Predict before clicking

The requirement: each participant needs one kit. Packs contain four kits and cannot be split. Use the fewest whole packs that cover everyone. Zero participants need zero packs.

The agent's handover: “I tried eight participants and got two packs. Ready for every workshop.”

Choose another fictional count. Write your expected result and your reason **before** trying it. Then compare the actual result with your prediction. Do not ask an agent to solve this step for you.

### 3. Choose your challenge

| Starting point | Your work | Agent's work, if available | Evidence |
|---|---|---|---|
| Beginner | Predict, click or calculate, explain one failure | Ask one question or give a small hint after your attempt | Expected versus actual result in your own words |
| Intermediate | Write an acceptance check and a boundary case; save a copy | Fix only the calculation in your copy | The previous failure now passes; an earlier success still passes |
| Expert | Write a bounded implementation brief and an independent review brief; challenge the handover | One agent implements, a fresh agent reviews against your criteria | Review of the combined result, not only each agent's summary |

Do not split this tiny calculation across several coding agents. Independent review is the useful second task here. For a genuinely parallel implementation exercise use [Parallel agents](../../tracks/08-advanced/03-parallel-agents.md).

Copy the lab into your own practice folder before modifying it. The course's version keeps its intentional defect for the next learner. Add your own [project instructions](../../templates/project-AGENTS.md) there. Ask the agent to show the changed file and the actual check output. No model access? Write the proposed fix and test plan on paper, and mark execution as pending.

### 4. Transfer

Change the fictional pack size. What changes in the test and what stays the same? Explain why trying just the original successful example would miss the defect. If you used hints, record that honestly.

## Done when

- [ ] I made a prediction before running or calculating an example.
- [ ] I can explain what the handover proves and what it does not.
- [ ] I found a failing example and stated the expected and actual result.
- [ ] I proposed a check for a different pack size; I labelled unexecuted work as pending.

## Data note

Use invented counts. Do not enter participant names, workshop rosters or real event information. This lab is open to agent-assisted review after your prediction. The separate [personal-data exercise](../find-the-personal-data/README.md) stays human-only.

## Next

[Verification ladder](../../tracks/05-verify-and-loop/01-verification-ladder.md), or return to the [learning guide](../../learning/README.md) and choose one knowledge check.
