# My learning progress

This note is optional. Use it if you want to pick up where you left off another day. Four lines are enough:

```text
What I tried:
What worked:
What is still open:
Next time:
```

Name the exercise or page so you can find it again. Keep the note private, with invented examples and no names, customer details or keys. In your course copy, save it as `learning/local/progress.md`; Git ignores that folder. Do not add it to a public contribution. Keep a separate backup if you need one.

## Resume prompt

Give an agent the note, or tell it which local file it may read:

```text
Help me continue from this note: <paste it or name the file>.
Use learning/coach-protocol.md.
Ask me a short question about where I stopped, then help me take the next step.
```

The agent should check with you before updating the note. A previous “passed” entry is something to revisit, not a new test result.

<details>
<summary>Optional: a more detailed record for a coach</summary>

Use this only when keeping individual attempts will help you plan the next exercise. Ask the learner before saving it. The short note above is enough for everyday use.

## Current route

- Exercise or source page:
- Tool or paper:
- Next question:

## What a status means

| Status | Meaning |
|---|---|
| `unverified` | Not checked here yet. This includes old notes and reports you have not revisited. |
| `not demonstrated` | The attempt does not yet show the skill. Note what to practise. |
| `mastered` | The learner explained the answer and applied it to a new example without being given the answer. Record what you observed. |
| `skip` | The learner chose to move on. The question has not been passed. |

`mastered` applies to this question and practice context. It is not a certificate or permission to put an app into production. An agent solving the task does not show that the learner can solve it.

## One entry per checkpoint attempt

Copy this block when you need a detailed entry. Keep earlier attempts so the next coach can see what changed.

```markdown
### <checkpoint ID> — <date or attempt label>

- Source unit: <relative course path and heading>
- Skill and scope: <what the learner is practising>
- Status: unverified / not demonstrated / mastered / skip
- Learner's claim: <their answer, in their own words>
- Evidence: <specific result or a path to the invented-data example>
- Observation: self-reported / coach observed explanation / coach inspected artefact or output
- What was actually checked: <action, expected result, observed result>
- Help used: none / source pointer / clue / worked explanation / agent implemented
- Transfer attempt: <new example and the learner's explanation, or not attempted>
- Still uncertain: <what needs more practice>
- Next retrieval check: <one question to revisit next time>
```

Choose one status. If you supplied the answer, use a new example before considering the skill `mastered`. Note whether you saw a check run, inspected its output, or heard the learner describe it. If you cannot access a result, leave that check unverified.

When resuming, read only the entry the learner has shared or named and the relevant lesson. An old entry records past work. Ask a short question before deciding which material to skip; do not silently promote a previous status.

</details>
