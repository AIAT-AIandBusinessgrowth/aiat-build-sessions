# PoC to production checklist

| | |
|---|---|
| **Prerequisites** | [Handover and first users](../06-keep-and-ship/03-handover-and-first-users.md), [Agents in operation](04-agents-in-operation.md) |
| **Time** | ~30 min |
| **Outcome** | You can show which parts of your tool are ready for use, which are untested and who must resolve the open items. |
| **Last verified** | 2026-09-13 |

## Why this matters

Open your tool and its project notes. Start with the backup: find the saved copy and the result of a restore test. If you have only a promise to make backups, mark this as untested.

A **proof of concept (PoC)** shows whether an idea can work. **Production** means people rely on the running tool. You will check ten things needed for that, including access, recovery and costs. This applies to browser-built apps, scripts and coding-agent projects. Your organisation still decides whether the tool may be used; bring the results to its responsible owner and security or data protection contact.

## Do it

### 1. Read the ten checks (10 min)

For each check, find something you can inspect today: a setting, a test result or a working recovery step. Keep plans separate from completed checks.

| # | Check | Evidence you can show | Help |
|---|---|---|---|
| 1 | **Named users and an owner** | A list of users by role; one owner and one backup person | [From prototype to product](../06-keep-and-ship/02-prototype-to-product.md) |
| 2 | **Data rules and data processing agreements** | What data it stores and why; test data is fake; a data processing agreement with every vendor that handles personal data; a deletion rule | [Rule one](../00-orientation/01-rule-one-no-real-data.md), [Does the AI need this?](../02-data-first/01-does-the-ai-need-this.md), [Data processing agreements](../../diy/03-data-processing-agreements.md) |
| 3 | **Secrets out of code** | No keys in the repository or its history; keys in a secret store; you know how to rotate each one | [Secrets and keys](../../diy/07-secrets-and-keys.md) |
| 4 | **Backups and a restore test** | Where backups live (a different place); the date of the last successful restore test; where the backup key lives | [Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md), [Code hosting and backup](../../diy/04-code-hosting-and-backup.md) |
| 5 | **Monitoring and a health check** | An automatic check that it is up; an alert that reaches a person; an alert when a backup fails, not only when it succeeds | [Monitoring and recovery drill](../../diy/08-monitoring-and-recovery.md) |
| 6 | **Error messages** | Users see a plain sentence and a next step, not a stack trace (internal program details); errors are logged without personal data | [From prototype to product](../06-keep-and-ship/02-prototype-to-product.md) (table of what breaks), logging: [Secrets and keys](../../diy/07-secrets-and-keys.md) |
| 7 | **Access control and 2FA** | Who can log in, with which role; two-factor authentication on every admin account (hosting, code, domain, AI vendor) | [Accounts and 2FA](../../diy/01-accounts-and-2fa.md) |
| 8 | **Costs and a spend cap** | A monthly estimate; a hard cap or alert at every paid vendor; who pays | [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md), [Plans and licences](../../diy/02-plans-and-licences.md) |
| 9 | **Instructions for the next person** | A README someone else followed: how to run it, who to ask and what it must never do | [Handover and first users](../06-keep-and-ship/03-handover-and-first-users.md), [product README template](../../templates/README-product.md) |
| 10 | **How it gets switched off** | Who decides; how users get their data out; how data is deleted; which keys are revoked; which plans are cancelled | This unit, step 3 |

<a id="2-score-your-product-15-min"></a>
### 2. Check what is ready (15 min)

Use your existing project notes to record what each check showed. Three labels can help you distinguish the results:

- **green:** checked, with a result and its link or date,
- **yellow:** planned but untested, with a date and a responsible role,
- **red:** missing.

<details>
<summary>Optional note with all ten checks</summary>

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

</details>

Before real users rely on it, every applicable check needs demonstrated evidence. Checks **2, 3, 4 and 7 must be green**; yellow means planned and is not a pass. If a check is not applicable, record why and have the responsible owner review that decision. Until then, keep the result a prototype with fictional data.

Completing this learning checklist is not organisational production approval. The owner must review the evidence, remaining limitations and the organisation's requirements.

You can let an agent help, as long as it checks files and does not guess:

```text
Here is the production checklist. For each line, look for evidence in this
repository (README, config, docs). Cite the file and relevant section.
Separate documented intent from observed behavior. A README saying
"backups run" is not evidence that a restore worked. Require a dated
check result, observed behavior or a verified settings record.
If you cannot observe the check, write "unverified". Do not mark it green.
```

The same prompt works in Claude Code and Codex. In a browser app builder, paste the checklist into the chat and check the settings pages yourself: most evidence for 5, 7 and 8 lives in account settings, not in code.

### 3. Write the switch-off plan (5 min)

Decide who may retire the tool and how they will do it. The five lines below are an example, including the two-week notice period. Adjust the timing and data retention to your organisation's requirements:

```markdown
## Switch-off plan
- Decided by: owner role, after telling users two weeks ahead.
- User data: offered as export, then deleted from app and backups within the retention period.
- Keys: all API keys of this product revoked (list in the secret store).
- Hosting and domain: deleted or transferred; paid plans cancelled.
- Record: one line in the change log with the date.
```

## Done when

- [ ] You reviewed all ten checks and can show what is checked, planned or missing. A planned check has a date and a responsible role.
- [ ] Every applicable check has observed evidence, including green checks 2, 3, 4 and 7, or the result stays a fictional-data prototype.
- [ ] Every yellow line has a date and a responsible role.
- [ ] The switch-off plan exists in the project notes or README.
- [ ] You repeat the check after every big change, and at least once before inviting new users.

## Data note

Use fictional data throughout this course, including this checklist. Green checks do not authorise uploading real records to an agent. For use outside the course, your organisation must decide the legal basis, required data processing agreements and deletion rules before personal data is introduced. Ask its data protection contact when unsure; see [Data processing agreements](../../diy/03-data-processing-agreements.md).

## Next

Back to [START-HERE](../../START-HERE.md) to pick your next track or revisit a unit.
