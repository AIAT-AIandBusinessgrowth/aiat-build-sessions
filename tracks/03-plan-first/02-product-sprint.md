# Product sprint: six artefacts and a pitch in 75 minutes

Work in a team of three or four to explain one product idea and build its first small part. You will leave with six things another person can read or see, plus a 60-second explanation of the idea.

| | |
|---|---|
| **Prerequisites** | [Spec interview](01-spec-interview.md) · [Schema first, then synthetic data](../02-data-first/03-schema-then-synthetic-data.md) |
| **Time** | ~75 min, team of 3 to 4 |
| **Outcome** | A README, scope, sample data, picture, name and colour, and three tasks, presented in a 60-second pitch. |
| **Last verified** | 2026-09-13 |

## Why this matters

Someone else needs to understand what your app does, how to open it and what it cannot do yet. The six items below help you explain that. Each person takes a small part, including people who have not built with AI before.

Use 75 minutes as a suggested budget. Decide what to leave out so you have time to show and discuss a first result.

## Do it

### Form teams (before the clock starts)

- Three or four people per team.
- At least one person who has built something with an agent or builder before, and at least one who has not.
- Mix backgrounds: someone who knows the problem, someone who likes pictures, someone who likes lists.
- One laptop drives. Everyone else works on paper, a phone or a second laptop.

### Roles in the team

Assign the jobs below for this session. One person can take more than one: in a team of three, the picture person also pitches. Swap the driver halfway through.

| Role | Does | Owns |
|---|---|---|
| Driver | Types into the tool, reads answers out loud | The build |
| Interviewer | Runs the interview prompt, keeps the spec honest | One sentence, scope |
| Data person | Defines the fields, asks the agent for fake rows, adds edge cases | Sample data |
| Picture person | Sketches the screen, picks name and colour | Picture, name, colour |
| Pitcher and timekeeper | Watches the clock, prepares the 60 seconds | Pitch, three tasks |

### Idea list

If nobody brings a real problem, pick one of these. All of them work with fake data.

- **Room board**: shows which meeting rooms are free in the next two hours.
- **First day**: an onboarding checklist that changes with the new person's role.
- **Where was that**: a search over your own notes that tells you where it found the answer.
- **When works**: suggests a meeting slot for four people from the time windows they typed in.
- **Lunch rota**: who brings what to the team lunch, without the long chat thread.
- **Plant duty**: a watering schedule for office plants, with a reminder view.
- **Book shelf**: a shared shelf where colleagues lend and borrow books.
- **Split it**: splits a shared bill fairly when not everyone had everything.

### The six artefacts

At the end, these six things exist in the builder project, a shared document or a repository.

| # | Artefact | What is in it | Fast way to make it |
|---|---|---|---|
| 1 | One-sentence README | First line: "For *who*, *name* is *what*, instead of *what happens today*." Then up to 20 lines: what it does, for whom, how to open it, what it cannot do yet. | "Write a README, 20 lines, no marketing." Start from the [product README template](../../templates/README-product.md). |
| 2 | Scope | Three points IN and three points deliberately OUT of this version. | The agent drafts it, the team cuts half of IN. Use the [MVP template](../../templates/MVP.md). |
| 3 | Sample data | Field names with types, plus at least 30 invented rows. Include edge cases: an empty cell, one extreme value, a name with accents. | Ask the agent to invent the rows from your field list. See [Schema first, then synthetic data](../02-data-first/03-schema-then-synthetic-data.md). |
| 4 | One picture | A screenshot, a mockup or a photographed paper sketch. Label anything not built yet as "mockup". | Pen, paper, phone camera. Or any drawing tool. |
| 5 | Name and colour | One name and one accent colour as a hex value, written into the README. | Spend about two minutes choosing. You can change them later. |
| 6 | Three tasks | The first one has a "done when" line and can be finished today. | Put them in the tool, a note, or an issue tracker such as GitHub Issues. |

**Plus the pitch:** 60 seconds, three questions. Who is it for? What is IN, and what did you leave OUT on purpose? What can you show? No scrolling through code.

### Time plan

The times are approximate. The timekeeper calls each block.

| Around | Block | Output |
|---|---|---|
| ~0:00 | Teams, roles, pick an idea | One idea, everyone knows their job |
| ~0:08 | Interview with the [spec prompt](01-spec-interview.md#3-paste-the-interview-prompt-15-min) | One sentence, IN, OUT |
| ~0:20 | Data: fields, then fake rows. At the same time: picture, name, colour | Sample data, picture, name, colour |
| ~0:40 | Cut three tasks, build task one | Something that runs, even if small |
| ~1:00 | README, pitch prep | README, pitch notes |
| ~1:05 | Pitches: 60 seconds each, one question from the room | Feedback |
| ~1:15 | End | |

### The outsider test

Show the six items to someone outside your team without explaining them first. Can they tell who the app is for, how to open it and what it does not do? Use their questions to improve the instructions. This checks your explanation; it does not check whether the app itself works.

## Done when

- [ ] The README starts with the one sentence and says how to open the thing.
- [ ] Scope lists three points IN and three points OUT.
- [ ] Sample data has field types and at least 30 invented rows, including the edge cases.
- [ ] One picture exists and is linked or embedded in the README.
- [ ] Name and accent colour (hex) are written down.
- [ ] Three tasks exist, and the first one has a "done when" line.
- [ ] The team pitched in 60 seconds without scrolling code.

## Data note

Use invented data for every part of the sprint. Keep names from your address book, real e-mail addresses and work records out, including your teammates' names. Use `example.com` for invented addresses, for example `alex.sample@example.com`. See [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md).

## Next

[Model, context, agent](../04-the-map/01-model-context-agent.md): understand what the AI can see and do, so you can give it a clearer next task.

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
