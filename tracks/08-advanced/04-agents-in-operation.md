# Agents in operation

| | |
|---|---|
| **Prerequisites** | [Loop engineering](02-loop-engineering.md), [Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md) |
| **Time** | ~25 min |
| **Outcome** | After this unit you can design a recurring agent job with a ticket, a backup before every write, verification, a change log, a rollback plan and an audit, and start it safely in read-only mode. |
| **Last verified** | 2026-09-13 |

## Why this matters

Sooner or later an agent does a job again and again: updating website content, triaging incoming requests, writing a weekly report from a spreadsheet. At that point it is no longer an experiment. It is operations.

In operations, mistakes repeat automatically. Nobody reads each run. The questions change from "can the agent do this?" to "what happens when it gets it wrong on a Friday night, and how do we notice and undo it?"

## Do it

### 1. The operating loop (10 min)

Every run of an operational agent follows the same seven steps:

| Step | What it means | Evidence |
|---|---|---|
| **Ticket** | Every job starts from a written request: what, why, done when, who approved it. No ticket, no run. | Ticket link |
| **Agent** | The agent reads the ticket, plans, and prepares the change as a diff or preview. | Plan and diff |
| **Backup before write** | Before changing anything, the agent saves the exact thing it will change, in a different place, named with date and ticket. | Backup file name |
| **Verify** | After the change, check against "done when": the page loads, the value shows, the count matches. | Command and output, or screenshot |
| **Change log** | One line per run, append only: when, ticket, what changed, backup location, verify result. | The log line |
| **Rollback plan** | Written before the first run: how to restore the backup, who can do it, how long it takes. | The plan, tested once |
| **Audit** | Regularly, a person reads the change log and checks a few runs in detail. | Audit note with date |

A change-log line can be this simple:

```text
2026-09-13T09:12Z | ticket 42 | opening hours page: Saturday 9-13 -> 9-14 | backup: backups/2026-09-13-ticket-42-hours.html | verify: page shows "9-14", HTTP 200
```

### 2. Walk through a fake example (5 min)

A small website for a fictional bakery at `bakery.example.com`. The agent's job: update opening hours when a ticket arrives.

1. **Ticket:** "Change Saturday hours to 9-14 from next week. Approved by: shop owner role."
2. **Agent:** reads the ticket, finds the file, shows the diff. Nothing is changed yet.
3. **Backup:** copies the current page to `backups/2026-09-13-ticket-42-hours.html`, outside the website folder.
4. **Write:** applies the change.
5. **Verify:** loads the page, checks that "9-14" appears and nothing else changed.
6. **Change log:** appends one line.
7. **If verify fails:** restores the backup, writes the failure to the log, comments on the ticket, and stops. It does not retry on its own.

The rollback plan for this job is one sentence plus a tested command: "Copy the backup file named in the change log back over the page."

### 3. Start read-only, then widen (5 min)

Do not give an operational agent write access on day one. Widen in stages, and only after clean runs you checked yourself:

| Stage | The agent may | You do |
|---|---|---|
| 1. Read-only | Read, analyse, propose the change as a text or diff | Apply the change yourself |
| 2. Draft | Write to a copy or staging version | Compare and publish |
| 3. Live with gate | Write live, with backup before write and verify after | Read the change log, audit samples |

Decide beforehand how many clean runs move a job to the next stage, and write that number into the rollback plan. Move back one stage after any incident.

> **As of 2026-09-13 in Claude Code** (checked 2026-09-13)
> - Plan mode is for analysing before making changes, a good fit for stage 1. ([source](https://code.claude.com/docs/en/permission-modes))
> - Routines run autonomously on a schedule, on an API call or on GitHub events, so their prompt must say exactly what to do and what success looks like. ([source](https://code.claude.com/docs/en/routines))

> **As of 2026-09-13 in Codex** (checked 2026-09-13)
> - `codex exec` runs in a read-only sandbox by default. Allow edits only when needed with `--sandbox workspace-write`. ([source](https://learn.chatgpt.com/docs/non-interactive-mode.md))

### 4. Give it its own, small access (5 min)

- **Its own account**, not yours. It should have only the rights this job needs.
- **Its own API key** with a spend cap, stored as a secret, never in the repository. See [Secrets and keys](../../diy/07-secrets-and-keys.md) and [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md).
- **Not on your main computer.** Run it in a separate environment, such as a container or a small separate machine.
- **A kill switch:** one documented step that stops it now (disable the schedule, revoke the key). Test it once.

## Done when

- [ ] You picked one recurring job and wrote the seven steps for it.
- [ ] The backup location is outside the place the agent changes.
- [ ] The rollback plan exists, and you restored a backup once.
- [ ] The change log format is defined, and one real (fake-data) run produced a line.
- [ ] The job starts in stage 1 (read-only), with a written rule for moving up.
- [ ] The agent has its own account and key, and the kill switch was tested.

## Data note

Operational agents often sit next to real systems, which usually means real data. In this course, practise only on fake systems and fake data. Before an agent touches anything with personal data, the rules from [From prototype to product](../06-keep-and-ship/02-prototype-to-product.md) and [PoC to production checklist](06-poc-to-production-checklist.md) apply, including a data processing agreement with every vendor involved. Change logs and backups must not copy personal data into places with weaker protection.

## Next

[Always-on assistants with guardrails](05-always-on-assistants-guardrails.md)
