# Tutor criteria

For a coach after selecting a checkpoint. Learners should make their own attempt in [checkpoints.md](checkpoints.md) first. This file is public and can be read, but seeing a criterion is not an independent demonstration.

Use the [coach protocol](coach-protocol.md). Read only the relevant section. Assess the principle and evidence, not exact wording. Cite the linked source in feedback. Ask one transfer question only after the original attempt has been discussed.

## B01

Source: [Schema first, then synthetic data](../tracks/02-data-first/03-schema-then-synthetic-data.md).

A sound answer describes field names, types and useful value ranges without real records, then asks for obviously fictional examples. Merely deleting names or uploading a “cleaned” real file does not demonstrate the skill. A useful transfer changes the source from a spreadsheet to a contract; ask for the minimum description needed to build a fake-data prototype.

## B02

Source: [Verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md).

The learner gives a specific input and its correct expected output, based on the “at least” rule. For example, an exact-capacity case tests the boundary. Other correct cases are valid; do not demand the coach's favourite input. For transfer, change room sizes or ask the learner to choose an input that distinguishes “at least” from “strictly more”. A prediction alone does not prove that a real implementation was run.

## B03

Source: [Share and export](../tracks/01-first-build/02-share-and-export.md).

The answer chooses export, code copy or repository sync and then inspects the second copy for a known last change. A working public link or a “synced” message alone is insufficient. For transfer, make the app contain stored fake entries and ask what the code copy does not establish. Use [Keep your work safe](../tracks/06-keep-and-ship/01-keep-your-work-safe.md) for the distinction between code and data backups.

## B04

Source: [One work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md).

Look for the goal or scope, verified current state, remaining failure and one next check. Distinguish observations from guesses. The learner need not paste the full transcript. For transfer, add a failed attempted fix and ask what belongs in the note so it is not repeated blindly.

## I01

Source: [Spec interview](../tracks/03-plan-first/01-spec-interview.md).

The learner notices the scope conflict and resolves it with the person responsible for the product rather than silently expanding the task. The selected task has a concrete observable result, with the remaining work explicitly out of scope or open. For transfer, introduce a new desired feature midway through a work cycle and ask how to retain an honest IN/OUT boundary.

## I02

Source: [Verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md).

Look for an actual generated file compared with known fake input, including row preservation and accented characters. A screenshot of a button proves neither. They may propose a suitable automated check as well as inspection; require actual output before claiming it ran. For transfer, replace CSV with a saved report that omits a section and ask for evidence tied to that requirement.

## I03

Source: [Keep your work safe](../tracks/06-keep-and-ship/01-keep-your-work-safe.md).

The learner restores the existing copies into a separate place and compares against a known fact, such as the identifiable fake booking. They keep code and data distinct and preserve the current project. A newly made export would test a different backup. For transfer, make code recover but the data export omit the last entry; ask what the recovery claim can truthfully say.

## I04

Source: [Handover and first users](../tracks/06-keep-and-ship/03-handover-and-first-users.md).

The answer removes unsupported claims and arranges or performs a fresh-use check based only on the document. Planned user tests remain planned until observed feedback exists. A README draft is not proof that setup works for another person. For transfer, give one invented feedback note and ask for a task that can be checked without inventing a second user's opinion.

## E01

Source: [Parallel agents](../tracks/08-advanced/03-parallel-agents.md).

The learner identifies the shared schema dependency, establishes ownership or sequences that change, and scopes independent work. Separate worktrees alone do not resolve semantic conflicts. Look for review of each diff, actual checks and checks after integration. For transfer, introduce a passing isolated change that breaks the combined behavior and ask who owns the diagnosis and what evidence they need.

## E02

Sources: [Context engineering](../tracks/08-advanced/01-context-engineering.md), [One work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md).

The learner treats both notes as claims, locates the relevant code/state and runs or requests a suitable non-destructive check using fake data. They record the observed result and reconcile the notes without inventing certainty. For transfer, remove access to the runtime: the truthful outcome is an unresolved verification item, not “complete” from the newest note alone.

## E03

Source: [PoC to production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md).

Plans are not completed controls. Look for specific evidence of access behaviour and an actual restore, while the prototype stays within its approved fake-data use. A quoted promise in README is not enough. Organisational approval remains separate from a course checkpoint. For transfer, provide a successful code restore but no data restore and ask how narrowly the evidence supports readiness.

## E04

Sources: [Loop engineering](../tracks/08-advanced/02-loop-engineering.md), [Always-on assistants with guardrails](../tracks/08-advanced/05-always-on-assistants-guardrails.md).

Look for a bounded change, allowed actions/files, a checkable stop condition, a resource budget, a response to repeated failure and a handover with evidence/open work. An instruction to “try harder” or a time limit alone does not define success. For transfer, make the check require an unavailable service; the agent should leave an honest blocked item rather than inventing evidence or broadening access.
