# Agents in operation

| | |
|---|---|
| **Prerequisites** | [Loop engineering](02-loop-engineering.md), [Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md) |
| **Time** | ~25 min |
| **Outcome** | You can try one recurring job in read-only mode and show how a person would check, undo and stop its changes. |
| **Last verified** | 2026-09-13 |

## Why this matters

Use the fictional bakery example below. Ask an agent to propose a change to Saturday's opening hours without editing the page. Compare its proposed change with the request.

A recurring job runs again on a schedule or when an event occurs. If it makes a mistake, that mistake can repeat. You will practise checking a proposed change, saving a copy before applying it and restoring that copy if the check fails.

## Do it

### 1. The operating loop (10 min)

Use these seven parts to set up this job. The request and results can live in one project note; a separate ticket system is optional.

| Step | What it means | Evidence |
|---|---|---|
| **Ticket** | A written request: what, why, done when, who approved it. It may be an issue or a note. | Request link |
| **Agent** | The agent reads the ticket, plans, and prepares the change as a diff or preview. | Plan and diff |
| **Backup before write** | Before changing anything, the agent saves the exact thing it will change, in a different place, named with date and ticket. | Backup file name |
| **Verify** | After the change, check against "done when": the page loads, the value shows, the count matches. | Command and output, or screenshot |
| **Change log** | One line per run, append only: when, ticket, what changed, backup location, verify result. | The log line |
| **Rollback plan** | How to undo a change by restoring the backup, who can do it and how long it takes. Write and test this before the first run. | A successful restore check |
| **Audit** | A person regularly reads the log and checks a few runs against their requests. | Date and what was checked |

A change-log line can be this simple:

```text
2026-09-13T09:12Z | ticket 42 | opening hours page: Saturday 9-13 -> 9-14 | backup: backups/2026-09-13-ticket-42-hours.html | verify: page shows "9-14", HTTP 200
```

### 2. Walk through a fake example (5 min)

The example is a small website for a fictional bakery at `bakery.example.com`; that address is a placeholder. Create a separate exercise folder with an `hours.html` file containing `Saturday: 9-13`. Use this local file for the practice run. The agent's job is to propose new hours when a request arrives.

1. **Ticket:** "Change Saturday hours to 9-14 from next week. Approved by: shop owner role."
2. **Agent:** reads the ticket, finds the file, shows the diff. Nothing is changed yet.
3. **Backup:** copies the current page to `backups/2026-09-13-ticket-42-hours.html`, outside the website folder.
4. **Write:** applies the change.
5. **Verify:** loads the page, checks that "9-14" appears and nothing else changed.
6. **Change log:** appends one line.
7. **If verify fails:** restores the backup, writes the failure to the log, comments on the ticket, and stops. It does not retry on its own.

The rollback plan says: "Copy the backup file named in the change log back over the page." In your own exercise folder, try the copy and check the restored hours. A written instruction does not prove the restore works.

### 3. Start read-only, then widen (5 min)

Start with read-only access. In the first stage, you apply the proposed change and restore it yourself. Allow more access only after you have checked the results and can undo them:

| Stage | The agent may | You do |
|---|---|---|
| 1. Read-only | Read, analyse, propose the change as a text or diff | Apply the change yourself |
| 2. Draft | Write to a copy or staging version | Compare and publish |
| 3. Live with gate | Write to the running service after the required approval, with backup before and a check after | Approve the action, then inspect the log and sample results |

Decide beforehand which successful checks and how many observed runs are required to move up. Write this alongside the rollback plan. A count alone does not prove readiness. After an incident, reduce access and investigate before resuming.

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - Plan mode is for analysing before making changes, a good fit for stage 1. ([source](https://code.claude.com/docs/en/permission-modes))
> - Routines run autonomously on a schedule, on an API call or on GitHub events, so their prompt must say exactly what to do and what success looks like. ([source](https://code.claude.com/docs/en/routines))

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - `codex exec` runs in a read-only sandbox by default. Allow edits only when needed with `--sandbox workspace-write`. ([source](https://learn.chatgpt.com/docs/non-interactive-mode.md))

### 4. Give it its own, small access (5 min)

- **Its own account**, not yours. It should have only the rights this job needs.
- **Its own API key** with a spend cap, stored as a secret, never in the repository. See [Secrets and keys](../../diy/07-secrets-and-keys.md) and [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md).
- **Not on your main computer.** Run it in a separate environment, such as a container or a small separate machine.
- **A stop procedure**, often called a kill switch: document how to stop the active run, disable its schedule and revoke its key when needed. Disabling a schedule alone may leave a current run active. Test the procedure on your own job.

## Done when

- [ ] You picked one recurring job and wrote the seven steps for it.
- [ ] The backup location is outside the place the agent changes.
- [ ] The rollback plan exists, and you restored a backup once.
- [ ] One actual run on the fictional example produced a log line. In read-only mode, you applied and checked the change yourself.
- [ ] The job starts in stage 1 (read-only), with a written rule for moving up.
- [ ] Before scheduling the job, it has its own limited account and key, and you tested how to stop it. If you only tried it manually, scheduling remains untested.

## Data note

Operational agents often sit next to real systems, which usually means real data. In this course, practise only on fake systems and fake data. Before an agent touches anything with personal data, the rules from [From prototype to product](../06-keep-and-ship/02-prototype-to-product.md) and [PoC to production checklist](06-poc-to-production-checklist.md) apply, including a data processing agreement with every vendor involved. Change logs and backups must not copy personal data into places with weaker protection.

## Next

[Always-on assistants with guardrails](05-always-on-assistants-guardrails.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
