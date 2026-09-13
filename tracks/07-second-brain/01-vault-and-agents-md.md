# A vault and AGENTS.md

| | |
|---|---|
| **Prerequisites** | [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md), [Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md) |
| **Time** | ~45 min |
| **Outcome** | After this unit you can set up a folder of notes that an agent reads under two hard rules, write your first project note, ask the agent what it knows and what is missing, and back the folder up. |
| **Last verified** | 2026-09-13 |

## Why this matters

A chat forgets. When the thread is gone, so are the decisions, the prompts that worked, and the reasons behind them. Your notes stay.

A **vault** is simply a folder of Markdown files that you own. When an agent can read that folder, your notes become a second brain: the agent starts each session knowing your projects, your rules, and what you learned last time.

Two things make it safe: rules the agent reads first, and a backup. You set up both today.

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

You do not need a special app. Any folder of Markdown files works, and any text editor can open them. [Obsidian](https://obsidian.md) is an optional free editor that shows links between notes. If you use it, choose "open folder as vault" and select this folder.

A folder synced to a cloud drive is convenient, but sync is not a backup: when you delete a file, the deletion syncs too. Step 5 covers the backup.

### 2. Give the agent rules (10 min)

Open a terminal in the vault folder and start your agent (Claude Code or Codex). Give it this prompt:

```text
Read this folder. It is my personal notes vault.
Write an AGENTS.md with:
- three sentences on what this vault is for,
- the folders and what goes into each,
- two hard rules:
  1. No personal data and no customer data in this vault, ever.
  2. No secrets in this vault, ever: no passwords, API keys, tokens or recovery codes.
Before you write, ask me what I want to use the vault for.
Short, plain English, no filler.
```

Read the result. Delete anything that is not true for you. Keep the file short: every line is something the agent reads at the start of every session.

A good AGENTS.md for a vault is often under twenty lines:

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
Read the vault. Tell me in five points what you know about my project
and what is missing. Name the file each point comes from.
```

Then check:

- Does every point name a real file? Open two of them.
- Did the agent add facts that are not in your notes? That is guessing, not knowing. Tell it so.

Every missing item becomes a new short note in `inbox/`. That is the loop: you write, the agent reads and finds gaps, you write the gaps down.

### 5. Back it up (5 min)

A vault that exists once is not a second brain. It is a risk.

```bash
git init
git add .
git commit -m "Start vault"
```

Then push it to a **private** repository you control. Check the visibility setting before the first push. Options and how to keep a second copy are in [Code hosting and backup](../../diy/04-code-hosting-and-backup.md).

Finish with a restore test from [Keep your work safe](../06-keep-and-ship/01-keep-your-work-safe.md): clone the repository into a new folder and open one note.

## Done when

- [ ] A vault folder with `inbox/`, `projects/`, `learnings/` and `rules/` exists.
- [ ] `AGENTS.md` states the purpose, the folders and the two hard rules, and you edited it yourself.
- [ ] Your tool actually reads it (Claude Code: `CLAUDE.md` imports `@AGENTS.md`).
- [ ] One project note answers what, for whom, where, and what is open.
- [ ] The agent listed what it knows with file names, and the gaps are notes in `inbox/`.
- [ ] The vault is pushed to a private repository and you cloned it once into a new folder.

## Data note

The vault is on your computer, but the agent reads it, and the agent's vendor processes what it reads. Individual subscriptions often come without a data processing agreement (see [Data processing agreements](../../diy/03-data-processing-agreements.md)). That is why the two hard rules exist. Write meeting notes with roles, not names. Never paste a password or key into a note "just for now": the backup will keep it forever.

## Next

[Notes as a graph](02-notes-as-a-graph.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
