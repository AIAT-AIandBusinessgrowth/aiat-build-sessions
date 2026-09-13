# Share and export

Open your app as someone else would, then save a copy outside the builder. Check that your latest change is in that copy so you can recover your work later.

| | |
|---|---|
| **Prerequisites** | [Your first build](01-your-first-build.md) |
| **Time** | ~15 min |
| **Outcome** | A checked share link for a browser app, and a second project copy containing your latest change. |
| **Last verified** | 2026-09-13 |

## Why this matters

You could lose the only copy if a project is deleted, a plan ends or a laptop breaks. A second copy gives you a way back. Testing the share link separately checks whether someone else can open the app without your login.

## Do it

### Part A: Test the share link (5 min)

1. In your builder, find the button to publish or share. It is called Publish, Share or Deploy, depending on the tool. The [tool matrix](../../diy/tool-matrix-2026-09.md) says which tools host your app.
2. Copy the link.
3. Open a private browser window:
   - Chrome and Edge: `Ctrl+Shift+N` (Mac: `Cmd+Shift+N`)
   - Firefox: `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
   - Safari: `Cmd+Shift+N`
   - Private windows blocked, for example on a work browser your organisation manages? Open the link in another browser where you are not logged in to the builder, or send it to a colleague and ask what they see.
4. Paste the link in a new private session without logging in. It does not use your normal browser login or saved app data.
5. Check: does the app load, and does it look like your preview? Entries you saved in your own browser will not be there. That is expected.
6. Check who can open it. Many share links work for anyone who has the link. Check that the code and settings contain no secrets before publishing, even with fake data.

**CLI lane:** your app runs on your laptop, so there is no link yet. Sharing a CLI-lane app is covered in [deploy and share](../../diy/05-deploy-and-share.md). Go on with Part B.

### Part B: Keep a second copy (5 min)

Pick one way:

- **GitHub sync.** Connect your builder to your own GitHub account. Accounts and backups: [code hosting and backup](../../diy/04-code-hosting-and-backup.md).
  1. Start the GitHub connection in your builder. GitHub shows a consent screen with the name of the builder and the access it asks for. Read it before you accept.
  2. When GitHub asks which repositories the builder may use, choose selected repositories only, not all of them. Let the builder create the repository for this project and name it; do not create one on github.com yourself first. If the builder later needs a repository that is not selected, you can add it in your GitHub settings.
  3. Make one small change in the builder, then open the repository on github.com and check that a new commit appears.
- **Download or export.** Look for Export, Download or Download ZIP in the project menu and save the file in a folder that is backed up.
- **Copy the code.** If the tool has neither (some chat canvases), copy the code into a file on your computer and put the date in the file name.

**CLI lane:** either copy your project folder to a separate backed-up location, or connect a private GitHub repository. For GitHub, stay in your existing `playground` and first inspect:

```bash
git status --short
git remote -v
```

If `origin` already points to your intended private repository, keep it and run `git push`. Do not add it again. If a different destination appears, stop and identify the project before changing anything.

Only when there is **no origin yet**, create an empty private repository on github.com (without a README), then follow [Code hosting and backup, variant (a)](../../diy/04-code-hosting-and-backup.md#4-tell-git-who-you-are-then-push-and-check).

GitHub Desktop works too: choose "Publish repository" and keep "Keep this code private" ticked.

### Part C: The ritual, open it and look (5 min)

Check the second copy yourself, even if the tool says "synced" or "pushed":

1. Open your repository page on github.com, or unpack the downloaded file.
2. Find the change from your third round: in the latest commit message and time, or in the file itself.
3. Confirm that the copy contains that change.

At the end of each work session, push or export and check the saved copy.

## Done when

- [ ] My share link works in a private browser window (browser lane).
- [ ] My project exists in a second place: a GitHub repository, or an exported file outside the tool.
- [ ] I opened that second place and saw my last change.
- [ ] The repository is private, unless I made it public on purpose.

## Data note

A public link or repository can expose keys, private code or paid resources even when the app uses invented data. Never put passwords or API keys into code you sync ([secrets and keys](../../diy/07-secrets-and-keys.md)).

## Next

[Does the AI need this?](../02-data-first/01-does-the-ai-need-this.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
