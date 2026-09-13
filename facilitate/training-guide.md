# Run a repeatable training with learning checks

Use this guide when the material becomes a repeated internal training or a course for a new group. It complements [Run a Build Session](run-a-build-session.md), which covers the room, agenda and tool fallbacks.

Public materials can support self-paced learning and independently organised training. They are not an invitation or registration for a private working group. Keep internal cohort plans, invitations, rosters and feedback in their approved internal locations. No public exercise requires access to them.

## Choose an outcome before an agenda

For each training, write one observable outcome and select a linked unit plus a [checkpoint](../learning/checkpoints.md). Use the same skill at different levels when a group is mixed.

| Learner's starting point | Practice | Observe |
|---|---|---|
| New to building | [Paper starter](../learning/README.md), then a first build when setup is ready | Can predict a result and choose a check: B02 |
| Already has a prototype | [Verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md) | Can inspect evidence tied to a requirement: I02 |
| Already delegates to agents | [Parallel agents](../tracks/08-advanced/03-parallel-agents.md) | Can scope work and verify the combined result: E01 |

Ask about the task, not job titles. A developer may need the beginner verification activity. An experienced product owner can work at a high level in a browser. Learners may switch or skip; record what was observed rather than ranking them.

## Prepare a run someone else can repeat

- Record the course commit or release used, linked unit, checkpoint ID, intended outcome and chosen fallback. Tool behaviour changes; follow the dated vendor sources in the [setup material](../ready-to-build.md).
- Do the activity yourself in the tools participants will use. Test the starting link or file and its recovery route. Record an unresolved blocker rather than promising the tool will work.
- Send the relevant minimum setup, not every guide. Follow organisational tool/account rules. Do not promise accounts, licences, setup support or access to private sessions.
- Prepare the [paper starter](../learning/README.md) or paired review for people without an available tool. An account problem need not prevent practising the skill.
- Keep course material separate from each learner's project. Use invented data for the demo and the checks.

## Roles

| Role | Responsibility |
|---|---|
| Host | Chooses the outcome, keeps time, ensures a usable fallback, records material defects |
| Table anchor or partner | Uses the [anchor questions](table-anchor.md), observes without taking the keyboard |
| Learner | Predicts, tries, explains and decides what they need next |
| Agent | Applies the [coach protocol](../learning/coach-protocol.md), asks one question at a time and supports the bounded task |

Small groups can combine host and anchor. Nobody shares credentials or logs in for someone else. The learner controls their project and progress note.

## A suggested session

Use the existing [60 or 75 minute formats](run-a-build-session.md#the-format-60-to-75-minutes). These are planning estimates, not a promise that every task completes in that time. Place the learning checks inside the existing blocks:

1. **Opening:** state the outcome and data rule. Ask one short diagnostic question from the selected checkpoint. Let people answer before the demonstration.
2. **Input:** show one principle from the linked unit. Do not show the answer to the diagnostic scenario.
3. **Build:** learners predict and test a result. The anchor or agent gives a source pointer, then a clue, then an explanation only as needed.
4. **Round:** ask a changed scenario that uses the same principle. Have the learner explain their decision, with evidence where the task requires it.
5. **Close:** record a narrow observation, any help used and the next useful check. Learners keep their own [progress note](../learning/progress-template.md).

For the [find-the-personal-data exercise](../exercises/find-the-personal-data/README.md), people work without AI. Reveal links to the supplied solutions only after their own list exists. Do not ask an agent to process the CSV or generate the debrief answer list.

## Assess the skill without an attendance score

Use the relevant [tutor criteria](../learning/tutor-criteria.md) after an attempt. Do not distribute the answer criteria beside the opening question. A small observation is enough:

| Observed situation | Record | Next step |
|---|---|---|
| Learner attended or read the unit; no attempt observed | `unverified` | Ask a small scenario |
| Learner gives an answer copied from the agent or needs the solution explained | `not demonstrated` | Practise with a different example |
| Learner explains the decision and applies it to a changed scenario without the answer supplied | `mastered`, limited to this checkpoint and context | Schedule a future retrieval check |
| Learner chooses to move on | `skip` | Offer a suitable next activity |

For a practical skill, also record the real check and its result. “Tests passed” in a draft README is a claim. Inspection of output or a watched action is evidence. Note the difference between a learner's report and the coach's observation.

Do not give a blanket score or certificate from these observations. A completed training does not approve a product for operational use; use the [production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md) and the organisation's own decisions.

## Language and access

Ask participants which language they want for discussion. Start German-speaking newcomers at [learning/start-de.md](../learning/start-de.md). The core tracks are English; [modules/de/](../modules/de/) contains selected German reference texts, not a complete translation.

A coach or agent can explain a linked unit in the chosen language while keeping the original path. Ask the learner to explain the key decision in their own words so a translation problem becomes visible. Accept spoken, typed or paper answers. Do not require a camera, public repository or public progress record as evidence of learning.

## Improve the next run

Keep an internal run note without participant identifiers:

```markdown
# Training run
- Material revision:
- Unit and checkpoint:
- Intended outcome:
- Tool or paper route actually used:
- Where learners got stuck:
- Help or fallback that worked:
- Evidence observed in this task:
- Material defect to fix:
- One change for the next run:
```

Use these observations with the existing [retro card](../templates/retro-card.md). Count useful patterns if the group permits it; do not publish individual learning records or quotes that identify people. A repeated question may reveal a missing explanation, prerequisite or example. Recheck the revised activity before the next run.

For public corrections, report the problem in the material with an invented reproduction. Keep private training schedules and cohort details in the internal system.
