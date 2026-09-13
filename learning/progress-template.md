# My learning progress

Copy this template to `learning/local/progress.md` in your course copy, or to a private note outside this repository. `learning/local/` is ignored by Git. Do not force-add it or include it in a pull request. Ignored files still need their own backup if you want to keep them.

Use only fictional examples. Do not include your name, employer, account details, customer records, secrets or screenshots with personal data. The coach needs your chosen task and evidence, not your identity.

## Current route

- Path or next unit: `<relative course path>`
- Goal for this session: `<one observable skill>`
- Tool or paper: `<optional>`
- Language: `<optional>`
- Last session: `<date, optional>`
- Resume with: `<one question or bounded next activity>`

## What a status means

| Status | Meaning |
|---|---|
| `unverified` | No current evidence, or an old/self-reported claim has not been checked in this session |
| `not demonstrated` | The attempt or generated artefact does not yet show this skill; record what to practise |
| `mastered` | This named checkpoint was explained and applied to a different scenario without an answer being supplied; record the actual evidence and observer |
| `skip` | Chosen to skip; no claim that the skill has been learned |

`mastered` is local to the stated checkpoint and practice context. It is not a certificate, an overall score or production approval. Attendance, confidence and an agent completing a task are not enough.

## One entry per checkpoint attempt

Copy this block for a new attempt. Keep earlier attempts so a fresh coach can see what changed.

```markdown
### <checkpoint ID> — <date or attempt label>

- Source unit: <relative course path and heading>
- Skill and scope: <what this attempt checks>
- Status: unverified / not demonstrated / mastered / skip
- Learner's claim: <their explanation, in their own words>
- Evidence: <specific result or a path to a fake-data artefact; no private URL needed>
- Observation: self-reported / coach observed explanation / coach inspected artefact or output
- What was actually checked: <action, expected result, observed result>
- Help used: none / source pointer / clue / worked explanation / agent implemented
- Transfer attempt: <different scenario and observed reasoning, or not attempted>
- Still uncertain: <one gap, or none observed in this narrow check>
- Next retrieval check: <one future question using a changed example>
```

Only choose one status in an actual entry. A supplied answer needs a new independent transfer attempt before `mastered`. If an artefact is unavailable, say so; do not treat a path or an old “passed” statement as fresh evidence.

## Resume prompt

Give the coach this prompt and only the relevant entry. If it has file access, name this file explicitly.

```text
Continue my learning using learning/coach-protocol.md.
Here is the progress entry I want to resume from: <entry or approved local path>.
Read its source unit and matching checkpoint only.
Treat the recorded status as history, not a new observation.
Ask one retrieval question before deciding what I can skip. Wait for my answer.
```

The agent may propose an updated entry. You decide whether to save it. It must not silently mark skipped or agent-completed work as learned.
