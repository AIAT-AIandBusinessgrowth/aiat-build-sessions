# Learn by trying, explaining and checking

| | |
|---|---|
| **Prerequisites** | None for the paper activity below. An agent is optional. |
| **Time** | ~20 min, an estimate for the starter activity |
| **Outcome** | After this activity you can write one useful requirement, predict a result and design a check before asking an agent to build. |
| **Last verified** | 2026-09-13 |

[Deutsch starten](start-de.md) · [All reading paths](../START-HERE.md)

## Why this matters

A working result and a learned skill are different things. Your agent can write the code. You still choose what it should do, predict a result and check whether it happened. The [verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md) teaches that habit.

Start at the level that fits this task. You can be experienced in your job and new to a terminal. Browser or CLI is a tool choice, not a grade.

## Do it

### 1. Try a small task without an account (5 min)

Use paper or a local text file. No download, login or paid plan is needed to do this activity. Prefer something you can click? Try the [verification lab](../exercises/verification-lab/README.md): a small browser app with an intentional defect, also usable on paper. Choose either starter for today.

**Fictional brief:** Room Board lists rooms large enough for a requested group. A request must be a positive whole number. Empty or invalid requests should show a useful message.

| Invented room | Seats |
|---|---|
| Cedar | 4 |
| Maple | 8 |
| Pine | 12 |

Write one sentence saying what this tool should do. Then decide what it should show for a request for eight seats. Write your prediction before checking the table.

### 2. Make the result checkable (5 min)

Choose an input that could expose a mistake. Write the input, what you expect to see, and why that result follows from the brief. Include a case different from the eight-seat request.

You can read [Spec interview](../tracks/03-plan-first/01-spec-interview.md) for examples of a useful “done when” line. Do not build yet.

### 3. Explain it without the brief (5 min)

Cover the brief and your notes. Explain to a partner, an agent, or aloud to yourself:

> How would you tell whether Room Board works, even if its author says it is finished?

Open your notes and check what you left out. If nobody observed your check, record it as your own report, not independent verification.

### 4. Pick the next useful step (5 min)

| Your situation | Next activity | What you keep |
|---|---|---|
| First build | [Your first build](../tracks/01-first-build/01-your-first-build.md), after its minimum setup | A small app and one check you can explain |
| You have a prototype | [Verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md) | Expected result, observed result and one defect or limitation |
| You already use agents | [One work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md), then [parallel agents](../tracks/08-advanced/03-parallel-agents.md) when tasks are independent | A bounded change, review evidence and a useful handover |
| No tool available today | Repeat this paper activity with your own fictional brief | A spec and test plan ready for a later build |

For a knowledge check, choose a scenario in [checkpoints.md](checkpoints.md). You can skip one; skipped is different from demonstrated.

## Learn with Codex or Claude Code

Open this course folder in your agent. The root [AGENTS.md](../AGENTS.md) and [CLAUDE.md](../CLAUDE.md) point it to the material. The agent uses the [coach protocol](coach-protocol.md). You do not need the Session Orchestrator plugin.

Try this prompt, with only the details you want to add:

```text
Help me learn from learning/README.md using learning/coach-protocol.md.
I have <time> and use <tool, or paper only>.
Start with one suitable question. Wait for my answer before giving hints.
Help me check a result myself. Do not complete the exercise for me.
```

To test a specific skill:

```text
Check my knowledge using learning/checkpoints.md and the coach protocol.
Start with checkpoint <ID>. Ask only its question and wait for my attempt.
```

The agent should reply in your language, use details you already gave, and ask one question at a time. If it shows the answer too early, ask for a different scenario. Do not count the revealed answer as your own successful attempt.

**Browser chat:** paste the [coach protocol](coach-protocol.md) and the relevant unit as text, then the prompt. Tell it to use only that material. A link alone may not give it the file contents. Without the separate tutor criteria, it can guide you but should leave a formal checkpoint unverified.

## Keep the course and your project separate

| Place | Put here |
|---|---|
| This course folder | The material you read and ask about |
| A separate folder or builder project you own | Your app, its spec, fake data and project rules from the [AGENTS.md template](../templates/project-AGENTS.md) |
| Optional `learning/local/progress.md` in a downloaded course copy | Your private learning notes, copied from [progress-template.md](progress-template.md) |

The course ignores `learning/local/` in Git. Keep it local; do not force-add or submit it in a pull request. Ignored does not mean encrypted or backed up. Paper or a private note outside the repository works too.

When you switch from the course to building, open the separate project folder and carry over only the relevant spec and rules. When you return to learning, give the agent only the small fake-data example or evidence needed for the question.

## Done when

- [ ] You wrote a requirement and a prediction before checking the sample table.
- [ ] You wrote a second input with an expected result and a reason.
- [ ] You explained how to check the result without relying on the author's claim.
- [ ] You chose a next activity, or recorded where to resume.

## Data note

Use invented scenarios and data only. Learning notes need no name, employer, customer details, credentials or account screenshots. The [find-the-personal-data exercise](../exercises/find-the-personal-data/README.md) stays human-only: do not give its CSV to an agent or ask it to solve the exercise.

## Next

[Choose a checkpoint](checkpoints.md), or return to [your reading path](../START-HERE.md).
