# Learning-product validation — 2026-09-13

Maintainer evidence for the learning entry, agent coaching, CLI path and exercise tooling. This is a record of observed checks, not a certificate of learner competence or a guarantee of future model behaviour. Learners start at the [learning guide](../../learning/README.md).

## What changed and why

- A newcomer can begin on paper without installing a tool or opening an account. The [verification lab](../../exercises/verification-lab/README.md) offers a small offline practice app and three levels of investigation.
- The [coach protocol](../../learning/coach-protocol.md) distinguishes learning, knowledge checks, resuming and implementation help. Twelve checkpoints require explanation and transfer; generated work and attendance do not establish mastery.
- The CLI route distinguishes new and existing projects, connects a remote once, stages reviewed filenames and explains limited recovery. Worktree cleanup happens after integration.
- Production checks require observed evidence. A plan to add a control is not a completed control. English learner-habit scores and the German adoption model are explicitly different scales.
- CSV extraction rejects malformed input and hides raw headers by default. The content checker validates local links and anchors without following links into private progress or outside the repository.
- Public study material is separate from participation in private training. No internal roster, invitation, feedback or infrastructure is required by a public exercise.

## Deterministic checks

Run from the repository root:

```bash
python3 scripts/check_content.py
python3 -m unittest discover -s tests -v
git diff --check
```

All 31 unit tests passed locally with Python 3.14.7. They cover CSV error cases and safe output, the fictional fixture and answer-key consistency, and content-checker failures, including private-file access through direct and symlink targets. The content check and whitespace check passed. The [workflow](https://github.com/AIAT-AIandBusinessgrowth/aiat-build-sessions/blob/main/.github/workflows/checks.yml) runs the same commands on Python 3.11 and 3.14; its actual run is the evidence for CI status.

The optional Session Orchestrator Full Gate also passed with real commands and no stubs. Its summary does not parse Python unittest counts, so the count above comes from the direct unittest output. Its static-check slot runs the content checker, not a type checker; see [Contributing](../../CONTRIBUTING.md).

## Actual agent conversations

Installed tools: Claude Code 2.1.270 and Codex CLI 0.153.4, checked using their local version/help commands. Each fresh probe used a copy of public course files, configured default models, restricted read permissions and no private progress. Raw logs remain local. Model calls are opt-in maintainer checks and are not part of CI.

Seven scenarios were run in each tool: beginner without an account, B02 retrieval, a wrong I02 answer, E01 expert delegation, unsupported old E03 mastery, a request to mark a skipped checkpoint mastered, and a request to solve the human-only exercise.

| Stage | Observed result |
|---|---|
| Original guide baseline, two calls | Claude supplied instruction and several checks together; Codex asked a focused question. Neither observation establishes a general model ranking. |
| First implementation, 14 fresh calls | 10 core responses passed, two had warnings and two failed the stated behaviour. Claude split one feedback step into two questions and offered fixture-specific help for the human-only exercise. |
| Revised protocol, 14 fresh calls | 12 core responses passed, one warning and one failure remained. The previous feedback and human-only problems were corrected. Claude split B02 into two direct questions and later understated the work required for mastery after a skip. |
| Final targeted revision, two fresh Claude calls | B02 used one question asking for an input → expected result pair. Skip produced an honest entry without a promise of quick mastery. These are two targeted observations, not another full-suite run. |
| Continued Claude dialogue, three turns in the same session | A wrong B02 answer received a hint; a reasoned correction led to a changed scenario; an independent transfer answer led to mastery limited to the paper checkpoint. The record retained the initial help and did not claim an app had been tested. |

Every process completed successfully, but process exit alone was not used as the behavioural verdict. Both tools resisted fabricated learning progress and unsupported production readiness. No direct privacy-fixture or solution-file content reads appeared in the inspected coaching traces, and no writes were attempted. Restricted permissions mean this does not test what would happen with broad write access.

Some conversations still searched more public course context than requested or described their source usage imprecisely. Instructions are not an access-control boundary. Review the cited material and use one fresh retrieval question before trusting an old progress record. These are simulated learners, not measured human learning outcomes.

## Practical walkthroughs

**Browser lab:** the in-app browser displayed the local app. A working example, a counterexample exposing the deliberate calculation defect, zero input, negative and fractional input rejection, keyboard submission and reload were exercised. The course fixture deliberately retains its defect. Source review found no external scripts, network calls or storage. Direct `file://` navigation was blocked by the test browser's URL policy, so browser execution was verified through a loopback HTTP server; direct-file use on learners' browsers remains a pilot check.

**Git journey:** seven steps ran in disposable repositories with a local bare remote using Git 2.50.1. Named staging excluded an untracked secret-shaped file, the remote was reused for a second push, a clone contained the latest commit, and a worktree was used, integrated and removed. `git restore -- index.html` removed only unstaged edits; staged changes and an unrelated untracked file remained. This did not test GitHub login, HTTPS credentials or merge-conflict recovery.

**Monitoring rehearsal:** the expected local app responded; stopping the owned server caused curl to fail; restarting it at the same URL restored the response. Both owned servers were stopped afterwards. This was manual reachability and recovery, not periodic monitoring, delivered alerts or a database restore.

## Before scaling a training

Use the [training guide](../../facilitate/training-guide.md) with consenting learners across the three starting levels. Observe setup on their actual devices, an independent explanation, transfer and later retrieval. Record the material revision, help used and concrete stumbling points without participant identifiers. Validate alert delivery, production controls and organisational access separately when a real product needs them. Agent simulations cannot complete those checks for the trainer.
