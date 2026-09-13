# PoC to production checklist

| | |
|---|---|
| **Prerequisites** | [Handover and first users](../06-keep-and-ship/03-handover-and-first-users.md), [Agents in operation](04-agents-in-operation.md) |
| **Time** | ~30 min |
| **Outcome** | After this unit you can check a proof of concept against ten production questions, show evidence for each, and name what is still missing before real users rely on it. |
| **Last verified** | 2026-09-13 |

## Why this matters

A proof of concept answers "can this work?". Production answers "can people rely on this, and can we cope when it breaks?". The gap between the two is rarely more code. It is ownership, data rules, backups, access, costs, and a way to switch it off.

This checklist is provider-neutral. It works for an app from a browser builder, a script on a small server, or a product built with a coding agent. It does not replace the rules of your organisation; if you have a data protection or security contact, bring this list to them.

## Do it

### 1. Read the ten checks (10 min)

For each check, write the evidence you can show today. "We plan to" is not evidence.

| # | Check | Evidence you can show | Help |
|---|---|---|---|
| 1 | **Named users and an owner** | A list of users by role; one owner and one backup person | [From prototype to product](../06-keep-and-ship/02-prototype-to-product.md) |
| 2 | **Data rules and data processing agreements** | What data it stores and why; test data is fake; a data processing agreement with every vendor that handles personal data; a deletion rule | [Rule one](../00-orientation/01-rule-one-no-real-data.md), [Does the AI need this?](../02-data-first/01-does-the-ai-need-this.md), [Data processing agreements](../../diy/03-data-processing-agreements.md) |
| 3 | **Secrets out of code** | No keys in the repository or its history; keys in a secret store; you know how to rotate each one | [Secrets and keys](../../diy/07-secrets-and-keys.md) |
| 4 | **Backups and a restore test** | Where backups live (a different place); the date of the last successful restore test; where the backup key lives | [Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md), [Code hosting and backup](../../diy/04-code-hosting-and-backup.md) |
| 5 | **Monitoring and a health check** | An automatic check that it is up; an alert that reaches a person; an alert when a backup fails, not only when it succeeds | Not covered in this material yet |
| 6 | **Error messages** | Users see a plain sentence and a next step, never a stack trace; errors are logged without personal data | [From prototype to product](../06-keep-and-ship/02-prototype-to-product.md) (table of what breaks), logging: [Secrets and keys](../../diy/07-secrets-and-keys.md) |
| 7 | **Access control and 2FA** | Who can log in, with which role; two-factor authentication on every admin account (hosting, code, domain, AI vendor) | [Accounts and 2FA](../../diy/01-accounts-and-2fa.md) |
| 8 | **Costs and a spend cap** | A monthly estimate; a hard cap or alert at every paid vendor; who pays | [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md), [Plans and licences](../../diy/02-plans-and-licences.md) |
| 9 | **Handover artefact** | A README someone else followed without asking you: run, ask, must never do | [Handover and first users](../06-keep-and-ship/03-handover-and-first-users.md), [product README template](../../templates/README-product.md) |
| 10 | **How it gets switched off** | Who decides; how users get their data out; how data is deleted; which keys are revoked; which plans are cancelled | This unit, step 3 |

### 2. Score your product (15 min)

Copy this block into your project notes and mark each line:

- **green:** evidence exists, with a link or date,
- **yellow:** planned, with a date and a person (role),
- **red:** missing.

```markdown
## Production check (date: YYYY-MM-DD)

- [ ] 1 Named users and owner:            green / yellow / red  | evidence:
- [ ] 2 Data rules and DPAs:              green / yellow / red  | evidence:
- [ ] 3 Secrets out of code:              green / yellow / red  | evidence:
- [ ] 4 Backups and restore test:         green / yellow / red  | evidence:
- [ ] 5 Monitoring and health check:      green / yellow / red  | evidence:
- [ ] 6 Error messages:                   green / yellow / red  | evidence:
- [ ] 7 Access control and 2FA:           green / yellow / red  | evidence:
- [ ] 8 Costs and spend cap:              green / yellow / red  | evidence:
- [ ] 9 Handover artefact:                green / yellow / red  | evidence:
- [ ] 10 Switch-off plan:                 green / yellow / red  | evidence:
```

A reasonable minimum before real users rely on it: **no red on 2, 3, 4 and 7.** Those four protect people's data and your ability to recover.

You can let an agent help, as long as it checks files and does not guess:

```text
Here is the production checklist. For each line, look for evidence in this
repository (README, config, docs). Quote the file and line you found.
If you find nothing, write "no evidence". Do not mark anything green
without a quote.
```

The same prompt works in Claude Code and Codex. In a browser app builder, paste the checklist into the chat and check the settings pages yourself: most evidence for 5, 7 and 8 lives in account settings, not in code.

### 3. Write the switch-off plan (5 min)

Most products never get one, and then they run forever with nobody responsible. Five lines are enough:

```markdown
## Switch-off plan
- Decided by: owner role, after telling users two weeks ahead.
- User data: offered as export, then deleted from app and backups within the retention period.
- Keys: all API keys of this product revoked (list in the secret store).
- Hosting and domain: deleted or transferred; paid plans cancelled.
- Record: one line in the change log with the date.
```

## Done when

- [ ] All ten checks are marked green, yellow or red, each with evidence or a date.
- [ ] Checks 2, 3, 4 and 7 are not red, or real users do not rely on the product yet.
- [ ] Every yellow line has a date and a responsible role.
- [ ] The switch-off plan exists in the project notes or README.
- [ ] You repeat the check after every big change, and at least once before inviting new users.

## Data note

Moving to production is usually the moment real data arrives. Until checks 2, 3, 4 and 7 are green, keep using fake data only. Real personal data needs a legal basis, a data processing agreement with every vendor that processes it, and a deletion rule. When unsure, ask your organisation's data protection contact before the first real record goes in.

## Next

Back to [START-HERE](../../START-HERE.md) to pick your next track or revisit a unit.
