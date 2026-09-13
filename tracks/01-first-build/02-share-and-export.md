# Share and export

| | |
|---|---|
| **Prerequisites** | [Your first build](01-your-first-build.md) |
| **Time** | ~15 min |
| **Outcome** | After this unit you can share a working link to your app, keep a copy of your project outside the tool, and check that your last change really arrived there. |
| **Last verified** | 2026-09-13 |

## Why this matters

Work that exists in exactly one place gets lost: a project is deleted by mistake, a free plan ends, a laptop breaks. A share link that only works while you are logged in is not a share link either.

Fifteen minutes now make sure your work exists twice and that other people can open it.

## Do it

### Part A: Test the share link (5 min)

1. In your builder, find the button to publish or share. It is called Publish, Share or Deploy, depending on the tool. The [tool matrix](../../diy/tool-matrix-2026-09.md) says which tools host your app.
2. Copy the link.
3. Open a private browser window:
   - Chrome and Edge: `Ctrl+Shift+N` (Mac: `Cmd+Shift+N`)
   - Firefox: `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
   - Safari: `Cmd+Shift+N`
   - Private windows blocked, for example on a work browser your organisation manages? Open the link in another browser where you are not logged in to the builder, or send it to a colleague and ask what they see.
4. Paste the link. A private window has no login and no stored data, so you see what other people see.
5. Check: does the app load, and does it look like your preview? Entries you saved in your own browser will not be there. That is expected.
6. Check who can open it. Many share links work for anyone who has the link. With fake data, that is fine.

**CLI lane:** your app runs on your laptop, so there is no link yet. Sharing a CLI-lane app is covered in [deploy and share](../../diy/05-deploy-and-share.md). Go on with Part B.

### Part B: Keep a second copy (5 min)

Pick one way:

- **GitHub sync.** Connect your builder to your own GitHub account. Accounts and backups: [code hosting and backup](../../diy/04-code-hosting-and-backup.md).
  1. Start the GitHub connection in your builder. GitHub shows a consent screen with the name of the builder and the access it asks for. Read it before you accept.
  2. When GitHub asks which repositories the builder may use, choose selected repositories only, not all of them. Let the builder create the repository for this project and name it; do not create one on github.com yourself first. If the builder later needs a repository that is not selected, you can add it in your GitHub settings.
  3. Make one small change in the builder, then open the repository on github.com and check that a new commit appears.
- **Download or export.** Look for Export, Download or Download ZIP in the project menu and save the file in a folder that is backed up.
- **Copy the code.** If the tool has neither (some chat canvases), copy the code into a file on your computer and put the date in the file name.

**CLI lane:** create an empty private repository on github.com (without a README), then in your `playground` folder:

```bash
git remote add origin https://github.com/<your-user>/playground.git
git branch -M main
git push -u origin main
```

GitHub Desktop works too: choose "Publish repository" and keep "Keep this code private" ticked.

### Part C: The ritual, open it and look (5 min)

A "synced" or "pushed" message is not proof. Look at the second copy yourself:

1. Open your repository page on github.com, or unpack the downloaded file.
2. Find the change from your third round: in the latest commit message and time, or in the file itself.
3. Only when you can see it, you are done.

Do this at the end of every work session, from now on: **push or export, then open the repository and look.**

## Done when

- [ ] My share link works in a private browser window (browser lane).
- [ ] My project exists in a second place: a GitHub repository, or an exported file outside the tool.
- [ ] I opened that second place and saw my last change.
- [ ] The repository is private, unless I made it public on purpose.

## Data note

A public link and a public repository are visible to anyone. That is one more reason for rule one: with fake data, a sharing mistake costs nothing. Never put passwords or API keys into code you sync ([secrets and keys](../../diy/07-secrets-and-keys.md)).

## Next

[Does the AI need this?](../02-data-first/01-does-the-ai-need-this.md)
