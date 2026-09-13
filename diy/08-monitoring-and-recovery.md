# Monitoring and recovery: practise a failure before users find it

| | |
|---|---|
| **Prerequisites** | [Deploy and share](05-deploy-and-share.md), [Keep your work safe](../tracks/06-keep-and-ship/01-keep-your-work-safe.md) |
| **Time** | ~25 min to plan and rehearse; provider setup can take longer. Estimate. |
| **Outcome** | After this you can define a useful health check, rehearse a failure, and distinguish a written plan from a delivered alert and a working recovery. |
| **Last verified** | 2026-09-13 |

## Why this matters

An app being reachable does not prove its main task works. A monitor being configured does not prove anybody receives an alert. Practise both failure and recovery with a disposable copy using fictional data.

## Do it

### 1. Define health before choosing a service

Write one expected observation for each layer that your app needs:

| Layer | Example check | What it does not prove |
|---|---|---|
| Reachable | The expected page responds successfully | The right app was served or its data is correct |
| Useful | A synthetic test action produces the expected result | Every user or edge case works |
| Recoverable | A backup restores the latest known synthetic record into a separate copy | Future backups will keep succeeding |
| Noticed | A test alert reaches the responsible person through the agreed route | They can recover the service without instructions |

For a local-only HTML file, a remote uptime monitor is not applicable. Record that reason. The checks for behaviour, saved copies and a responsible owner still matter.

### 2. Rehearse one failure in a disposable copy

**Browser lane:** use a duplicate of your fictional-data app. In your hosting provider's documented monitoring or health-check settings, find the target, frequency, failure threshold and alert destination. Use only an approved service; check billing before enabling anything paid. Provider interfaces differ, so follow that provider's current help page.

Trigger its **test alert** first. Record whether the intended recipient actually received it. Then rehearse an agreed failure on the disposable copy, never on a service others use. A preview URL going down may be expected when a development session ends; use the intended deployed target when testing a real monitor.

**CLI lane, optional reachability rehearsal:** in a disposable folder containing only your fictional `index.html`, start your own server:

```bash
python3 -m http.server 3100 --bind 127.0.0.1
```

If the port is occupied, use an unused one and update the URL below. Do not stop another process to free the port. In another terminal:

```bash
curl --fail --max-time 5 http://127.0.0.1:3100/
```

On Windows, use `py -3` instead of `python3` if that is your installed Python command, and use `curl.exe` instead of `curl`. Windows PowerShell 5.1 uses `curl` as an alias for a different command; [Microsoft documents the distinction](https://learn.microsoft.com/en-us/windows/curl/) (checked 2026-09-13).

Check that the response is your expected app. Stop **the server you just started**, with `Ctrl+C` in its terminal, and repeat the request. Observe the failure. Restart your server and observe recovery.

This is a manual local rehearsal, not an installed monitor or a delivered alert. For operational use, configure an approved periodic check and alert route and run the same failure-and-recovery drill. Record those as pending until tested. The commands use [Python's local HTTP server](https://docs.python.org/3/library/http.server.html) and [curl's failure and timeout options](https://curl.se/docs/manpage.html), checked 2026-09-13. Python's development server is not production hosting.

### 3. Record what actually happened

```text
Target and expected application:
Synthetic action and expected result:
Check frequency and failure threshold (chosen for this app):
Owner role and backup role:
Failure triggered in disposable copy:
Observed failed check:
Test alert delivered to intended person: yes / no / not tested
Recovery action and observed result:
Backup failure notification tested: yes / no / not tested
What remains unverified:
Next check and its trigger:
```

Keep actual contact details in an access-controlled operational record, not this public course. A screenshot of a settings page alone is not evidence that an alert arrived. Do not simulate sending an alert by writing “sent” in a note.

### 4. Practise the backup separately

Restore into a different folder or disposable environment. Check for a specific recent fictional record, not just the presence of files. Include database exports and configuration if your app needs them. Then test the backup system's own failure notification using its documented test mechanism. Never delete the working source to test a backup.

## Done when

- [ ] I defined a health check that identifies the intended app and a useful synthetic action.
- [ ] I observed failure and recovery in a disposable copy, or explicitly marked execution pending.
- [ ] I distinguished a manual request from periodic monitoring and a delivered alert.
- [ ] I recorded which alert and restore checks were actually observed and which remain unverified.

## Data note

Use fictional inputs. Keep tokens, real records, private URLs and personal contact details out of shared logs. Monitoring services may receive URLs and response data; the organisation approves their use.

## Watch out

Never stop a shared or production service to rehearse this lesson. A passing reachability check is not evidence that a calculation, backup or access rule works.

## Sources

- [Python HTTP server](https://docs.python.org/3/library/http.server.html), checked 2026-09-13. Local development server only.
- [curl manual](https://curl.se/docs/manpage.html), checked 2026-09-13. Failure status and bounded request time.
- [Microsoft: curl on Windows](https://learn.microsoft.com/en-us/windows/curl/), checked 2026-09-13. Use `curl.exe` to avoid the Windows PowerShell alias.

## Next

Return to the [production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md). Mark monitoring green only when all applicable operational checks have evidence; completing this lesson alone does not make it green.
