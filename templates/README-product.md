# Room planner

> **How to use this template.** This is the handover artefact: the questions people would otherwise ask you. Every section must be true today. Test it by giving it to one person and watching them follow it. Each question they ask you is a missing line. Background: [Handover and first users](../tracks/06-keep-and-ship/03-handover-and-first-users.md). The example values are invented. Replace them and delete this note.

**What it does:** Shows free meeting rooms for the next two weeks and lets you book one.
**For whom:** Office assistants who plan rooms every week.
**Name and colour:** Room planner, accent colour `#1F6FEB`

## How to open or run it

1. Open https://rooms.example.com and sign in with your team account.
2. Or run it locally from a clean folder:
   ```bash
   <install command>
   <start command>
   ```
   Then open `<local address>`. Tested from a clean folder on YYYY-MM-DD.

## Who to ask

- Owner: product owner role, reachable at owner@example.com
- Backup: a second person, reachable at backup@example.com

<!-- Roles and example.com addresses only. Keep real contact details in a place with access control. -->

## What it must never do

- Never store real personal data. Use the fake data set in `data/fake-bookings.csv`.
- Never send e-mails to addresses outside the team.
- Never delete a booking without asking for confirmation.

<!-- The section people skip, and the most important one for anyone who takes over, including an agent. -->

## Where data and backups live

- Code: the repository at `<repository link>`.
- Data: `<where the app stores its data>`. Exported weekly to `<second place>`.
- Secrets: in the platform's environment variables and a password manager. Never in the repository.
- Last restore test: YYYY-MM-DD.

## Known limits

- One building only.
- No recurring bookings.

## How to report a problem

- Where: `<issue tracker, form or shared document>`
- Include: what you tried, what happened, what you expected. No screenshots with real names.
- Read by: owner role, every `<day>`.

## How to switch it off

1. Tell users two weeks ahead and offer them an export of their data.
2. Export the bookings, then delete the data from the app and its backups.
3. Delete the hosted app. Cancel paid plans.
4. Revoke its API keys.
5. Write one line with the date into the change log.
