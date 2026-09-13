# Room planner

> **How to use this template.** Write the steps someone needs to open your tool and do its main job. Then try those steps from a clean setup, or watch a willing person follow them. Fix missing instructions and mark untested steps honestly. These are invented examples; replace links, paths and claims with your actual details, then delete this note. Background: [Handover and first users](../tracks/06-keep-and-ship/03-handover-and-first-users.md).

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
   Then open `<local address>`.

Setup check: `<not yet tried / tested from a clean folder on YYYY-MM-DD, with result>`.

## Who to ask

- Owner: product owner role, reachable at owner@example.com
- Backup: a second person, reachable at backup@example.com

<!-- Roles and example.com addresses only. Keep real contact details in a place with access control. -->

## What it must never do

- Never store real personal data. Use the fake data set in `data/fake-bookings.csv`.
- Never send e-mails to addresses outside the team.
- Never delete a booking without asking for confirmation.

<!-- Keep the limits that matter for this tool. Explain them concretely so another person or agent can follow them. -->

## Where data and backups live

- Code: the repository at `<repository link>`.
- Data: `<where the app stores its data>`. Backup arrangement: `<planned or active, frequency, second place>`.
- Secrets: in the platform's environment variables and a password manager. Never in the repository.
- Last restore test: `<not yet tried / YYYY-MM-DD and what was recovered>`.

## Known limits

- One building only.
- No recurring bookings.

## How to report a problem

- Where: `<issue tracker, form or shared document>`
- Include: what you tried, what happened, what you expected. Use fictional details; no screenshots with personal data or secrets.
- Read by: owner role, every `<day>`.

## How to switch it off

<!-- Adapt the example timing and deletion steps to the organisation's requirements. This describes the plan; it does not authorise an agent to execute it. -->

1. Get the product owner's approval. Tell users `<notice period, for example two weeks>` ahead and offer them an export of their data.
2. Export the bookings, then delete the data from the app and its backups according to the agreed retention rules.
3. Delete the hosted app. Cancel paid plans.
4. Revoke its API keys.
5. Write one line with the date into the change log.
