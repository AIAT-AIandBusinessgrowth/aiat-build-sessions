# Handover and first users

| | |
|---|---|
| **Prerequisites** | [From prototype to product](02-prototype-to-product.md) |
| **Time** | ~25 min |
| **Outcome** | You can write instructions for someone else to use the tool, prepare a user test and turn observed problems into clear tasks. |
| **Last verified** | 2026-09-13 |

## Why this matters

Open your README and try following its starting instructions from a clean folder or fresh account. Add any missing step. These instructions are your **handover document**, sometimes called a handover artefact.

It helps someone use the tool when you are unavailable. You will also prepare a short user test. Watching someone try a task shows where the tool or its instructions need work.

## Do it

### 1. Write the handover artefact (10 min)

Start from the [product README template](../../templates/README-product.md). The example below is fictional; replace its link, file paths and claimed checks with your actual project details. Include only checks you ran:

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

Keep "What it must never do" specific. It tells a person or agent maintaining the project which changes need extra care.

**The test:** give the document to a willing person and watch them follow it. If they need help, improve the relevant instruction or app behaviour. If nobody is available, try a clean setup yourself and leave the check with another person pending.

### 2. Set up a test with three real users (5 min to plan)

This unit prepares the test. The tests themselves happen later, when users have time. No deployed link yet? Use a local walkthrough with your fictional-data app, or complete [Secrets and keys](../../diy/07-secrets-and-keys.md) and [Deploy and share](../../diy/05-deploy-and-share.md) before sending a remote invitation. Preparation can be complete while user validation remains pending.

For this exercise, aim for three people who have the problem the tool addresses. Three is a practice target, not evidence of demand. Start with one if that is who is available.

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

Do this step after the tests. For practice now, use two invented notes. Keep actual feedback in an approved private place and rewrite each problem with fictional details before giving it to an agent. You can use this prompt in Claude Code, Codex or a browser app builder:

```text
Here are feedback notes rewritten with fictional details and no personal data.
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
- **Ideas** go onto a later list unless you decide they solve a more urgent problem.

Store the list where you will see it again: an issue tracker, a `TASKS.md` in the repository, or a note in your second brain.

### 4. Close the loop with users

When you fix something a user reported, tell them what changed and how to try it. Send the message yourself, or explicitly authorise an agent to send it.

## Done when

- [ ] The handover document has: what it does, for whom, how to run it, who to ask, what it must never do, where data and backups live, known limits, how to switch it off.
- [ ] You tried the instructions from a clean setup and corrected missing steps. A check by another person is complete or clearly pending.
- [ ] I prepared a fictional-data test task and a usable way to run it (a working link or local walkthrough instructions).
- [ ] I recorded user validation as pending until real people agree and try it. If working alone, I can continue the course with that limitation visible.

To complete user validation, over the following days:

- [ ] Three real users agreed to a test with fake data and received the task, access instructions and a day. The suggested count is an exercise target, not proof of market demand.

- [ ] Three real users tried the product with fake data, and you have their notes without names.
- [ ] Their feedback is a task list grouped into blocker, annoying, idea, each with a "done when" line.
- [ ] If you changed something because of feedback, you told the person who reported it.

## Data note

Handover documents live in repositories, and repositories get copied. Use roles and `example.com` addresses in them, and keep real contact details in a place with access control. Feedback notes use roles, not names. Remove personal data from screenshots before you store or paste them. Anything you give an agent is visible to its vendor.

## Next

[A vault and AGENTS.md](../07-second-brain/01-vault-and-agents-md.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
