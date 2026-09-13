# Your first build

Build a small app with made-up data, then change it in three rounds. You will practise telling the AI what you want and checking whether its changes work.

| | |
|---|---|
| **Prerequisites** | [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md), [Pick your lane](../00-orientation/02-pick-your-lane.md), the self-check in [Ready to build](../../ready-to-build.md) |
| **Time** | ~45 min |
| **Outcome** | A first app you can open, with three changes you have tried yourself. |
| **Last verified** | 2026-09-13 |

## Why this matters

Use a task you understand so you can judge the result. Describe it without real records. If you cannot choose an idea yet, try the [notebook calculator](../../exercises/verification-lab/README.md) first. It gives you something small to check without setting up an account.

## Do it

### Step 1: Pick one small annoyance (5 min)

Choose a task that comes up at least once a week, fits on one screen and can use invented data.

- **A list you keep in a spreadsheet:** equipment on loan, who has sent the weekly report, which room is booked when.
- **A text you write every week:** a status update built from bullet points, a meeting summary in the same shape.
- **A calculation you repeat:** travel costs from distance and a rate, hours into working days, a price with discount and tax.

Not for today: anything with a login, payments, sending e-mails, or a connection to another system.

Finish this sentence on paper: *"Every week I ___, and it annoys me because ___."*

### Step 2: Paste the starter prompt (5 min)

Copy this into the chat of your app builder. Replace everything in `<...>`.

```text
Build a small web app for me. Keep it to one screen.

What it is for: <one sentence, e.g. "I track which team members have sent their weekly report">.
How I do it today: <e.g. "a spreadsheet with one row per week and one column per person">.

The app should:
- <thing 1, e.g. "show a table of weeks and people">
- <thing 2, e.g. "let me tick a box when a report arrives">

Data: use made-up sample data only. Invent 8 to 10 rows.
People must be obviously fictional. E-mail addresses must end in @example.com.

Keep it simple: no login, no database, no payments. Data may stay in the browser.
When you are done, explain in three sentences what you built and how I try it.
```

### Step 3: Run it in the preview (5 min)

Open the preview panel of your builder. Try it like a user: add an entry, change a value, reload the page.

Note one thing that works and one thing that does not.

### Step 4: Improve it in three rounds (20 min)

**Check your remaining credits first.** Browser builders limit how many messages or credits a free plan includes. A new request can use part of that allowance. The [tool matrix](../../diy/tool-matrix-2026-09.md) lists each tool's free tier (checked 2026-09-13). If you run out, wait for the reset shown in your account, or use the CLI lane if you already have access to it.

**Change one thing per round.** Several changes at once make it hard to see what broke. Use this shape:

```text
Change only this: <one change>.
Keep everything else as it is.
```

After each round: run it in the preview, check the new thing, and check that one old thing still works.

Ideas if you are stuck:

- **Round 1, what you see:** "Add a column for the due date." or "Sort the list by date, newest first."
- **Round 2, what it does:** "Show the total at the bottom." or "Highlight rows older than seven days."
- **Round 3, keep it:** "Keep my entries when I reload the page, stored in the browser." or "Add a button that downloads the list as a CSV file."

When something breaks, give the AI the action you took and what happened: *"When I click Save, nothing happens and the list is empty."* If two attempts fail, return to the previous version using the builder's version history, where available. Then ask for a smaller change.

### Step 5: Write three lines (5 min)

1. What I built.
2. What surprised me.
3. What I would change next.

### CLI lane

Keep the downloaded course folder separate from your app. Open a terminal in the parent folder where you keep practice projects, **not inside the course or an existing app**.

If `playground` already exists from an earlier setup, open that folder and run `git status --short`. Reuse it if it is your practice project; do not create another `playground` inside it. Otherwise choose a new unused name.

**New project only:** create the folder once:

```bash
mkdir playground
cd playground
git init
```

Set the author name and e-mail once for this folder. Replace the placeholders. Every Git commit includes these details. If the project may become public, use GitHub's no-reply address from your e-mail settings ([GitHub docs](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address), checked 2026-09-13).

```bash
git config user.name "Your Name"
git config user.email "you@example.com"
```

Before starting the agent, copy [project-AGENTS.md](../../templates/project-AGENTS.md) into `playground` as `AGENTS.md`. Replace the placeholders with your app's purpose; remove commands and file references that do not exist. For Claude Code, also create `CLAUDE.md` containing just `@AGENTS.md`.

Start the installed agent inside that app folder: `claude --permission-mode manual` or `codex`. Codex desktop can open the same folder. Inspect the active permissions before approving changes. Folder instructions guide the agent; they are not a filesystem sandbox.

> **Approve with care**
>
> - Read every command the agent proposes before you approve it. If you do not understand it, ask the agent what it does first.
> - Do not turn on auto-approve or auto mode in a folder that contains anything other than this project.
> - Keep keys, passwords and personal files out of the folder.
> - Check that the agent can explain the project rules you copied before it starts building.
>
> **Claude Code:** the starting mode depends on the account and settings. `claude --permission-mode manual` requests Manual mode; check the status bar. `Shift+Tab` cycles modes, so stop when the intended label appears rather than relying on one press ([permission modes](https://code.claude.com/docs/en/permission-modes), checked 2026-09-13).

Paste the same starter prompt and add one line:

```text
Build it as a single index.html file that opens in a browser without installing anything.
```

Open `index.html` in your browser (double-click it in your file manager). That is your preview.

After the first working version, commit the reviewed `index.html`, `AGENTS.md` and, if present, `CLAUDE.md` by filename. After each later round, inspect and save the changed app file:

```bash
git status --short
git diff -- index.html
git add index.html
git diff --cached
git commit -m "feat: add due date column"
```

Read the staged diff: it shows the changes selected for this commit. Include other files only when you intended their changes. The commit saves only the files you staged.

When a round breaks something, save a copy of the failed attempt outside the project first. Then inspect `git status --short` and `git diff -- index.html`. If you choose to discard only the **unstaged edits to index.html**, run this separate recovery command:

```bash
git restore -- index.html
```

It restores that tracked file from the staging area. Staged edits and new untracked files are not removed. If the broken version was already committed or staged, ask the agent to explain the state and a recovery plan before acting. Do not use a folder-wide restore to fix one file ([Git restore](https://git-scm.com/docs/git-restore), checked 2026-09-13).

## Done when

- [ ] My app runs in the preview, or `index.html` opens in my browser.
- [ ] I made three rounds of changes, one thing per round.
- [ ] Every piece of data in the app is invented.
- [ ] I wrote my three lines.

## Data note

The starter prompt asks for invented data. If you want the app to look like your real list, do not paste the list. Describe the columns in words and let the agent invent the rows. [Schema first, then synthetic data](../02-data-first/03-schema-then-synthetic-data.md) shows the full method.

## Next

[Share and export](02-share-and-export.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
