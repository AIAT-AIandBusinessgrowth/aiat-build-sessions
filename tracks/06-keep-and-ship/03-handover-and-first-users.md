# Handover and first users

| | |
|---|---|
| **Prerequisites** | [From prototype to product](02-prototype-to-product.md) |
| **Time** | ~25 min |
| **Outcome** | After this unit you can write a handover artefact someone else can follow without you, set up a first test with three real users, and turn their feedback into a task list once the tests are done. |
| **Last verified** | 2026-09-13 |

## Why this matters

A product that only works while you are in the room is still a script with an audience. The day you are sick, on holiday, or busy with the next thing, nobody knows how to start it, whom to ask, or what it must never do.

A handover artefact fixes that. It is a short document that answers the questions people would otherwise ask you.

First users do the second half of the job. They show you what is really missing. Their feedback only helps if it ends up as tasks, not as a vague feeling that "people liked it".

## Do it

### 1. Write the handover artefact (10 min)

Start from the [product README template](../../templates/README-product.md). Make sure these sections exist and are true today:

```markdown
# Room planner

**What it does:** Shows free meeting rooms for the next two weeks and lets you book one.
**For whom:** Office assistants who plan rooms every week.

## How to open or run it
1. Open https://rooms.example.com and sign in with your team account.
2. Or run it locally: see "Local setup" below. Tested from a clean folder.

## Who to ask
- Owner: product owner role, reachable at owner@example.com
- Backup: a second person, reachable at backup@example.com

## What it must never do
- Never store real personal data. Use the fake data set in `data/fake-bookings.csv`.
- Never send emails to addresses outside the team.
- Never delete a booking without asking for confirmation.

## Where data and backups live
- Code: the repository. Data export: weekly, see "Backups".
- Last restore test: 2026-09-13.

## Known limits
- One building only. No recurring bookings.

## How to switch it off
- Export the bookings, delete the hosted app, revoke its API key.
```

The section "What it must never do" is the one people skip. It is the most important one for anyone who takes over, including an agent that works on the code later.

**The test:** give the document to one person and watch them follow it. Every time they ask you something, the answer belongs in the document.

### 2. Set up a test with three real users (5 min to plan)

This unit sets the test up. The tests themselves happen over the following days, when your users have time.

Pick three people who actually have the problem. Friends who will say "nice" do not count.

Ask each of them for fifteen minutes with a real task, using fake data:

1. "Please try to do this task with the tool." (Say what, not how.)
2. Watch without helping, or ask them to write down where they got stuck.
3. Ask three questions afterwards:
   - What did you try to do?
   - Where did you get stuck?
   - Would you use it next week, and for what?

A short invitation you can adapt:

```text
Hi, I built a small tool for planning meeting rooms and need three people
to try it for 15 minutes. It uses fake data only, so please do not enter
real names. Could you try it this week? Link: https://rooms.example.com
```

### 3. Turn feedback into a task list (10 min, after the tests)

Do this step when the notes from the tests are in. Try the prompt now with two invented notes, so you know it works. Collect all raw notes in one place first. Remove names and anything personal. Then ask the agent to structure them. The same prompt works in Claude Code, Codex, or the chat of a browser app builder:

```text
Here are raw feedback notes from three test users (no names).
Turn them into tasks. For each task write:
- a short title,
- the user problem in one sentence,
- a "done when" line I can check.
Group the tasks into: blocker, annoying, idea.
Do not invent feedback that is not in the notes. Quote the note each task comes from.
```

Then decide, yourself:

- **Blockers** go into the next work cycle.
- **Annoying** items get a date or get dropped.
- **Ideas** go onto a later list. Most of them stay there, and that is fine.

Store the list where you will see it again: an issue tracker, a `TASKS.md` in the repository, or a note in your second brain.

### 4. Close the loop with users

When you fix something a user reported, tell them in one line. People who see their feedback land keep giving it.

## Done when

- [ ] The handover artefact has: what it does, for whom, how to run it, who to ask, what it must never do, where data and backups live, known limits, how to switch it off.
- [ ] One person followed it without asking you, or you added the answers to their questions.
- [ ] Three real users agreed to a test with fake data, and each of them has the task, the link and a day.

After the tests, over the following days:

- [ ] Three real users tried the product with fake data, and you have their notes without names.
- [ ] Their feedback is a task list grouped into blocker, annoying, idea, each with a "done when" line.
- [ ] You told at least one user what changed because of their feedback.

## Data note

Handover documents live in repositories, and repositories get copied. Use roles and `example.com` addresses in them, and keep real contact details in a place with access control. Feedback notes use roles, not names. Remove personal data from screenshots before you store or paste them. Anything you give an agent is visible to its vendor.

## Next

[A vault and AGENTS.md](../07-second-brain/01-vault-and-agents-md.md)
