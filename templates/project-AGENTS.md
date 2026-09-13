# AGENTS.md

<!--
Starter for your own project. Copy this file as AGENTS.md into your project's
top folder and replace every <placeholder>. It tells the agent what to work on,
which checks to run and which actions need permission. Keep instructions short
and specific. Remove duplicated or outdated guidance; keep essential data,
access and safety rules even if recent tasks did not exercise them.
Background in the Build Sessions material:
tracks/07-second-brain/01-vault-and-agents-md.md and
tracks/08-advanced/01-context-engineering.md
Delete this comment when you are done.
-->

## What this project is

<Name> <does what> for <role>. Example: Room Board shows which meeting rooms are free in the next two hours, for office assistants.

- Spec: `SPEC.md`
- Scope: `MVP.md`
- Open tasks: `TASKS.md`

## Two hard rules

1. **No personal data and no customer data in this project, ever.** Not in code, data files, tests, notes, commit messages or prompts. Use invented data. E-mail addresses end in `@example.com`.
2. **No secrets in this project, ever.** No passwords, API keys, tokens or recovery codes. Code reads keys from environment variables. `.env` is listed in `.gitignore`. `.env.example` holds fake values only.

## How to run

- Install: `<command>`
- Start: `<command>`, then open `<local address>`
- Check: `<test, build or lint command>`
- Sample data: `data/fake-<name>.csv`

## Conventions

- Work in small stages. Check each change and show the files it affects.
- Commit only when explicitly authorised for this task; stage only reviewed files within its scope.
- Show the command you ran and its output as evidence. Never write "should work".
- Unfinished work goes into `TASKS.md`, each item with a line that says when it is due again.
- Before a new session, read `SPEC.md` and the last state note.
- <Optional project-specific rule: required behaviour or a repeated mistake to avoid, with the reason. Remove this line if none is needed.>

## The agent must never

- Read, write or delete files outside this project folder.
- Delete data or files without asking first.
- Commit, push, deploy, publish or send anything without explicit authorisation for this task. Existing authorisation within the agreed scope remains valid; ask only when it is missing or the scope changes.
- Write a key or password into a source file, a log, a note or a commit.
- Add a new dependency or a paid service without asking first.
- Say "done" before the check has run.

## Claude Code

Claude Code reads `CLAUDE.md`, not `AGENTS.md`. Create a `CLAUDE.md` next to this file with the single line `@AGENTS.md`.
