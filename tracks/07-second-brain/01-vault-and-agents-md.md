# A vault and AGENTS.md

| | |
|---|---|
| **Prerequisites** | [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md), [Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md) |
| **Time** | ~45 min |
| **Outcome** | You can save project notes, give an agent only the notes it needs and recover the folder from a second copy. |
| **Last verified** | 2026-09-13 |

## Why this matters

Create a new folder called `notes-vault`. Put one note about an invented project in it. You will ask an agent to answer from that note and check its answer against the file.

A **vault** is a folder of text notes. Here the notes use **Markdown**, plain text with simple formatting such as `#` for a heading. Saving decisions in files lets a fresh session read them without the old chat. You will add data rules and a backup; instructions alone do not prevent an agent from accessing the wrong files.

## Do it

### 1. Create the vault (5 min)

Create a folder you will find again, for example `notes-vault` in your documents. Inside it, create four folders:

```text
notes-vault/
  inbox/       quick notes, not sorted yet
  projects/    one note per project
  learnings/   one short note per lesson
  rules/       longer rules the agent opens when needed
```

You do not need a special app. Any text editor can open Markdown files. [Obsidian](https://obsidian.md) is an optional editor that can show links between notes. If you use it, choose "open folder as vault" and select this folder.

A folder synced to a cloud drive is convenient, but sync is not a backup: when you delete a file, the deletion syncs too. Step 5 covers the backup.

### 2. Give the agent rules (10 min)

Open a terminal in this new folder and start Claude Code or Codex. Use only the invented notes you created for this exercise. Do not point the agent at an existing personal notes folder. Give it this prompt:

```text
Read only this exercise folder. It contains notes about an invented project.
Write an AGENTS.md with:
- three sentences on what this vault is for,
- the folders and what goes into each,
- two hard rules:
  1. No personal data and no customer data in this vault, ever.
  2. No secrets in this vault, ever: no passwords, API keys, tokens or recovery codes.
Before you write, ask me what I want to use the vault for.
Short, plain English, no filler.
```

Read the result. Remove anything that does not match the folder. `AGENTS.md` holds the project's instructions; the tool-specific box below explains how to load them.

This example is under twenty lines:

```markdown
# AGENTS.md

This vault holds my project notes, decisions and learnings.
Read it to understand my projects before you answer.
Write new notes only into inbox/ unless I ask otherwise.

## Folders
- inbox/: unsorted notes
- projects/: one note per project
- learnings/: one short lesson per note
- rules/: longer rules, open them when a task needs them

## Hard rules
1. No personal data and no customer data in this vault, ever.
2. No secrets in this vault, ever: no passwords, API keys, tokens or recovery codes.
```

> **As of 2026-09-13: which file does your tool read?** (checked 2026-09-13)
> - **Codex** reads `AGENTS.md` before doing any work. ([source](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md))
> - **Claude Code** reads `CLAUDE.md`, not `AGENTS.md`. Create a `CLAUDE.md` next to it that contains the line `@AGENTS.md` to import it, or create a symlink. ([source](https://code.claude.com/docs/en/memory))
> - **Browser chat apps** usually cannot read a folder. If yours has a field for project instructions, paste the two hard rules there, and paste only the notes you need into the chat.

### 3. Write your first note (10 min)

Create `projects/<your-project>.md`. Answer four questions:

```markdown
# Room planner

**What it does:** Shows free meeting rooms and lets people book one.
**For whom:** Office assistants (role, no names).
**Where it lives:** Repository link, hosted link https://rooms.example.com
**What is open:**
- Recurring bookings are missing.
- No restore test yet, see [[learnings/first-restore-test]].
```

A link to a note that does not exist yet, like `[[learnings/first-restore-test]]`, is allowed. It marks something you still want to write down.

### 4. Ask the agent about your notes (10 min)

Give the agent this prompt:

```text
Read projects/<your-project>.md. Summarise what the note says about the
project and list any unanswered questions. Name the file and section for
each statement. Do not treat a written plan as proof that work is complete.
```

Then check:

- Does each statement point to the section that supports it? Open the note and compare two statements with their source sections.
- Did the agent add facts that are not in your notes? Ask it to remove them or label them as unverified.

If a question matters to your project, add it to `inbox/`. You can leave irrelevant questions out. Then change one fact in the project note and ask again: does the answer reflect the updated file?

### 5. Back it up (5 min)

Save a second copy so that losing this folder does not lose the notes. Run the commands below from the new `notes-vault` folder. Review every file you stage; use your actual project-note filename:

```bash
git init
git status --short
git add AGENTS.md projects/room-planner.md
git diff --cached
git commit -m "Start vault"
```

If you created `CLAUDE.md`, review it and add it explicitly before the commit too. Empty folders are not stored by Git; they appear in a clone once they contain tracked notes. Do not add private files or secrets.

Then push it to a **private** repository you control. Check the visibility setting before the first push. Options and how to keep a second copy are in [Code hosting and backup](../../diy/04-code-hosting-and-backup.md).

Finish with a restore test from [Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md): clone the repository into a new folder and open one note.

## Done when

- [ ] A vault folder with `inbox/`, `projects/`, `learnings/` and `rules/` exists.
- [ ] `AGENTS.md` states the purpose, the folders and the two hard rules, and you edited it yourself.
- [ ] Your tool actually reads it (Claude Code: `CLAUDE.md` imports `@AGENTS.md`).
- [ ] One project note answers what, for whom, where, and what is open.
- [ ] You compared the agent's answer with the note and checked that it noticed an updated fact. Useful open questions are saved in `inbox/`.
- [ ] The vault is pushed to a private repository and you cloned it once into a new folder.

## Data note

The folder is on your computer, but a cloud model service receives content the agent sends to it. Use invented projects and roles, with no personal or customer data. Keep passwords and keys out of notes: deleting them later does not remove earlier Git versions or backups. Account and contract requirements are covered in [Data processing agreements](../../diy/03-data-processing-agreements.md).

## Next

[Notes as a graph](02-notes-as-a-graph.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
