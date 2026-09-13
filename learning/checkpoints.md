# Checkpoints: show what you can do

These scenarios check a particular skill, not your overall ability. Use them on paper, with a partner, or through the [coach protocol](coach-protocol.md). Ask for one ID at a time. The time needed depends on the discussion and the evidence you choose.

Try before reading the source. Open the source when you need help and note that help in your [progress record](progress-template.md). These are invented scenarios; the numbers are exercise inputs, not vendor limits.

## Beginner

### B01 — Describe data without sending the real file

Tags: `data`, `scope`. Source: [Schema first, then synthetic data](../tracks/02-data-first/03-schema-then-synthetic-data.md).

You want an app like a customer spreadsheet used at work. An agent asks you to upload the spreadsheet so it can see an example. No file has been shared.

**Question:** What would you give the agent instead, so it can build a useful first version?

### B02 — Predict before checking

Tags: `verification`, `acceptance`. Source: [Verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md).

A fictional Room Board should show rooms with at least the requested number of seats. Cedar has four seats and Maple has eight. The agent says its filter is finished.

**Question:** What single input and expected result would you write down to check that claim?

### B03 — A link is not a saved project

Tags: `sharing`, `backup`. Source: [Share and export](../tracks/01-first-build/02-share-and-export.md).

You built a tool with fake data. Its public link works on your laptop. The source exists only in the builder account, and you have not exported or synced it.

**Question:** What action and observation would convince you that the project has a second usable copy?

### B04 — Continue in a fresh chat

Tags: `context`, `handover`. Source: [One work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md).

Yesterday you built a fictional room filter. It lists rooms correctly, but the empty input still fails. Today you must continue in a fresh chat.

**Question:** What would you put in a short state note so the new agent can take the next useful step?

## Intermediate

### I01 — Turn a wish into an acceptance check

Tags: `scope`, `acceptance`. Source: [Spec interview](../tracks/03-plan-first/01-spec-interview.md).

Your prototype lists fictional rooms. The next task says “make booking easy”, but booking is currently in the spec's OUT list. There is no definition of “easy”.

**Question:** How would you resolve that task into one agreed, checkable next step before the agent edits anything?

### I02 — Evaluate evidence, not confidence

Tags: `verification`, `review`. Source: [Verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md).

A builder says: “CSV export works; I checked the button.” Your requirement says the exported file must preserve every fictional row and its accented characters. You have seen only a screenshot of the button.

**Question:** What evidence would you inspect to decide whether that export meets the requirement?

### I03 — Restore something you can identify

Tags: `backup`, `recovery`. Source: [Keep your work safe](../tracks/06-keep-and-ship/01-keep-your-work-safe.md).

You have a code ZIP and a separate fake-data export. The tool's database has a new test booking that you can identify, but you do not know whether the export includes it.

**Question:** How would you test what you can actually recover without changing the current working project?

### I04 — Separate the checked result from the next promise

Tags: `handover`, `users`. Source: [Handover and first users](../tracks/06-keep-and-ship/03-handover-and-first-users.md).

An agent drafted a README saying setup is tested and user feedback is positive. You have run the tool yourself, but nobody else has followed the README or tried the product.

**Question:** What would you change or collect before treating this as a checked handover?

## Expert

### E01 — Decide what can run in parallel

Tags: `delegation`, `integration`. Source: [Parallel agents](../tracks/08-advanced/03-parallel-agents.md).

Two agent tasks are ready. One adds CSV export; the other changes booking validation. Both propose editing the shared data schema. Each has passing tests for its own change.

**Question:** How would you organise this work so the combined result has a clear owner and meaningful verification?

### E02 — Reconstruct state from conflicting evidence

Tags: `context`, `evidence`. Sources: [Context engineering](../tracks/08-advanced/01-context-engineering.md), [One work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md).

A state note says the fake-data migration is complete. The plan marks it open, and the repository contains no recorded migration check. You join as a fresh agent coordinator.

**Question:** What would you verify and record before choosing the next implementation task?

### E03 — A plan is not operational evidence

Tags: `operation`, `readiness`. Source: [PoC to production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md).

Your prototype has a README saying access control and restore tests will be added next week. The owner asks whether that documentation is enough evidence to mark those controls complete today.

**Question:** What decision would you make from the current evidence, and what would change that decision?

### E04 — Bound an unattended loop

Tags: `automation`, `stop`, `evidence`. Sources: [Loop engineering](../tracks/08-advanced/02-loop-engineering.md), [Always-on assistants with guardrails](../tracks/08-advanced/05-always-on-assistants-guardrails.md).

An agent is asked to “keep improving this fake-data project until it is good”. It repeats the same failed check, adds dependencies, and has no agreed action boundary or stop condition.

**Question:** How would you rewrite its brief so a run has a bounded task, a verifiable finish and a usable handover if it fails?

## After an attempt

Explain your reasoning, then try a changed scenario chosen by your coach. Record the evidence and any help used in [progress-template.md](progress-template.md). You can choose a different level or return to [the learning entry](README.md).

Coaches assess attempts using the separate [tutor criteria](tutor-criteria.md). Do not show those criteria as the answer alongside a checkpoint question.
