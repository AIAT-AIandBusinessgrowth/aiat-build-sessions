<a id="checkpoints-show-what-you-can-do"></a>

# Questions to try

Pick a question and give it a try. If you get stuck, open the linked lesson. You can answer on paper, talk it through with someone, or ask an agent: “Ask me B02.” It should wait for your answer before helping.

All examples below are invented. Choose a different question or skip one whenever you want.

## Beginner

<a id="b01--describe-data-without-sending-the-real-file"></a>

### B01 — Describe the spreadsheet

You want to turn a customer spreadsheet into an app. The agent asks you to upload the file so it can see an example. You have not shared it.

What would you give the agent instead?

[Help: schema first, then synthetic data](../tracks/02-data-first/03-schema-then-synthetic-data.md)

<a id="b02--predict-before-checking"></a>

### B02 — Which rooms should appear?

A room finder should show every room big enough for a group. Cedar has four seats and Maple has eight. The agent says the app is ready.

Choose a group size to try. Which rooms should appear?

[Help: checking an app](../tracks/05-verify-and-loop/01-verification-ladder.md)

<a id="b03--a-link-is-not-a-saved-project"></a>

### B03 — Save a second copy

Your app's public link works. Its code exists only in your builder account; you have not saved a copy anywhere else.

What would you save, and how would you check that the copy contains your latest work?

[Help: share and export](../tracks/01-first-build/02-share-and-export.md)

### B04 — Continue in a fresh chat

Yesterday your app listed rooms correctly, but an empty search still failed. Today you are opening a new chat.

What would you tell the new agent so it can continue from there?

[Help: one work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md)

## Intermediate

<a id="i01--turn-a-wish-into-an-acceptance-check"></a>

### I01 — What does “make booking easy” mean?

Your app lists rooms. Booking was deliberately left out of the first version. Someone now asks you to “make booking easy”, without explaining what should change.

What needs to be agreed before the agent starts changing the app?

[Help: spec interview](../tracks/03-plan-first/01-spec-interview.md)

<a id="i02--evaluate-evidence-not-confidence"></a>

### I02 — Did the export keep everything?

Your app exports a list of invented rooms to CSV. Every row and every accented character must be kept. The agent says it works and shows you a screenshot of the Export button.

What would you look at before calling the export ready?

[Help: checking an app](../tracks/05-verify-and-loop/01-verification-ladder.md)

<a id="i03--restore-something-you-can-identify"></a>

### I03 — Can you recover the latest booking?

You have a ZIP of your code and a separate export of the app's invented data. The running app has a recent test booking, but you do not know whether the export includes it.

How would you find out whether you can recover that booking while keeping the working app safe?

[Help: keep your work safe](../tracks/06-keep-and-ship/01-keep-your-work-safe.md)

<a id="i04--separate-the-checked-result-from-the-next-promise"></a>

### I04 — Can someone else follow the README?

The agent wrote a README saying setup has been tested and users like the app. You have run it yourself, but nobody else has followed the README or tried the app.

What would you correct or check before handing this README to someone else?

[Help: handover and first users](../tracks/06-keep-and-ship/03-handover-and-first-users.md)

## Expert

<a id="e01--decide-what-can-run-in-parallel"></a>

### E01 — Two agents want to change the same file

One agent will add CSV export. Another will change booking validation. Both need to edit the file that defines the booking data. Each has passing tests for its own change.

How would you divide and check the work before merging both changes?

[Help: parallel agents](../tracks/08-advanced/03-parallel-agents.md)

<a id="e02--reconstruct-state-from-conflicting-evidence"></a>

### E02 — The notes disagree about what is finished

You are taking over a project. One note says the test data has been migrated to the new format. The task list says the migration is still open. You cannot find any output showing it was checked.

What would you check, and what would you leave in the project notes for the next agent?

Help: [context engineering](../tracks/08-advanced/01-context-engineering.md), [one work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md)

<a id="e03--a-plan-is-not-operational-evidence"></a>

### E03 — Can these checks be marked complete?

The README says access controls and backup recovery will be tested next week. The project owner wants to mark both as complete today because the plan is written down.

What would need to happen before you could mark those checks complete?

[Help: PoC to production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md)

<a id="e04--bound-an-unattended-loop"></a>

### E04 — An agent keeps repeating a failed test

You asked an agent to “keep improving this practice app until it is good”. It keeps failing the same test and installing more packages. You have not agreed what it may change or when it should stop.

What would you write in its next instruction so it can work on one task and stop at the right point?

Help: [loop engineering](../tracks/08-advanced/02-loop-engineering.md), [always-on assistants](../tracks/08-advanced/05-always-on-assistants-guardrails.md)

## After an attempt

Talk through your answer, then try a different example. If you want to continue later, leave yourself a [short note](progress-template.md). You can also choose another question or return to [the learning guide](README.md).

For coaches: use the [tutor criteria](tutor-criteria.md) after the learner has tried. It also lists suggested follow-up variants, so invent a fresh one if the learner has read that file. Follow the [coach protocol](coach-protocol.md) and keep the answer out of the opening question.
