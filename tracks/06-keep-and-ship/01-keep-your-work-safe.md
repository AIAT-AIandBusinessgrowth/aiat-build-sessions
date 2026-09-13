# Keep your work safe

| | |
|---|---|
| **Prerequisites** | [Rule one: no real data](../00-orientation/01-rule-one-no-real-data.md), [One work cycle](../05-verify-and-loop/04-one-work-cycle.md) |
| **Time** | ~20 min |
| **Outcome** | After this unit you can name what in your project exists exactly once, give it a second copy in a place that does not fail together with the first, and prove that you can get it back. |
| **Last verified** | 2026-09-13 |

## Why this matters

A prototype often lives in exactly one place: one browser tab of an app builder, one folder on one laptop, one chat thread. When the laptop dies, the account gets locked or the chat is deleted, the work is gone.

Most backup plans fail because they try to save everything. That is slow, so it never gets done. Start the other way round: sort first, then save only what exists once. That set is usually small.

## Do it

### 1. Find what exists exactly once (5 min)

Answer this question in two sentences, in writing:

> If this laptop does not start tomorrow, or I lose access to this account, what exactly is gone, and how long until I can work again?

Walk through the usual places:

| Place | What typically lives there only once |
|---|---|
| Browser app builder | The project itself, its built-in database, settings you typed into the builder |
| Chat thread | Prompts that worked, decisions, the spec you talked through |
| Laptop folder | Code that was never pushed, a project without any remote, local notes |
| Hidden files | `.env` files, API keys, a local database file |
| Downloads and exports | Files you received or produced and never stored anywhere else |

Write the list down. This is your inventory. Without it, every later step is a guess.

### 2. Sort into three classes (5 min)

Everything on your list belongs to one of three classes. Each class needs a different second copy.

| Class | Examples | Where the second copy comes from | Watch out |
|---|---|---|---|
| **Code** | Source files, config, prompts saved as files, README | A Git remote, or an export (ZIP) stored in a second place | Only what you pushed or exported is safe |
| **Data** | The content your app stores: entries, uploads, database, spreadsheets, notes | An export from the app or database, stored in a second place | A code export usually does not contain it |
| **Secrets and keys** | API keys, passwords, `.env` values, SSH keys, the password of your backup | A password manager that has its own recovery | Never in Git, never in a chat, never in a shared export |

There is a fourth kind of file that needs no backup at all: things one command recreates, such as installed packages and build output. Leave them out.

### 3. A Git remote is not a backup of data or secrets

A push copies code. It does not copy:

- commits you have not pushed yet,
- changes you have not committed,
- files your `.gitignore` excludes, which by design are the sensitive ones (`.env`, local databases, raw files),
- the database of a hosted app,
- projects that have no remote at all.

A commit is not a backup. A push is a copy of your code, and only of your code.

If you work in a Git folder, this one-minute self-test shows what exists only locally:

```bash
git status --porcelain                      # empty = nothing uncommitted
git log --branches --not --remotes --oneline # empty = everything pushed
git remote -v                                # empty = no remote: the whole project exists once
```

Options for where to push, and how to keep a copy of a hosted repository, are in [Code hosting and backup](../../diy/04-code-hosting-and-backup.md).

### 4. Export from a browser app builder

Builders differ, and their menus change. The pattern stays the same:

1. **Find the code export.** Look for "export", "download", or "sync to GitHub". Which builder offers what is listed in the [tool matrix](../../diy/tool-matrix-2026-09.md).
2. **Export the data separately.** A code export usually leaves out the content of the built-in database. Look for a table view with CSV or JSON export.
3. **List the secrets by name.** Keys you entered in the builder's settings are not in the export. Store their names and values in your password manager, not in the export file.
4. **Store the export in a second place.** Not in the same downloads folder on the same laptop. A cloud drive, an external disk, or a private repository all count, as long as it is a different place.
5. **Write the date on it.** `project-export-2026-09-13.zip` beats `export (3).zip`.

A copy on the same disk is not a copy. Aim for two copies in places that do not fail together.

### 5. Restore test: try to get it back (5 min)

An untested backup is a guess. Do this once now, then again after big changes:

1. Take the real copy, not a fresh one you make for the test.
2. Open it in a new place: clone the repository into a new folder, unzip the export somewhere else, or import it into a new empty project.
3. Check it against something you know. "It opened without errors" is not a result. "The fake customer list has 50 rows, like the original" is a result.
4. Delete the test copy.

Note the date of the last successful restore test in your project notes.

### 6. Where does the key live?

If your backup is encrypted or protected by a password, the password is part of the backup. A backup you cannot open is noise.

- Store the password or key in a password manager, not only in a text file on the same laptop.
- Make sure the password manager itself survives the loss of this laptop (its own account recovery, a recovery code on paper).
- Test once that the stored password really opens the backup.
- Never delete an old key while backups made with it still exist.
- Store account recovery codes the same way. See [Accounts and 2FA](../../diy/01-accounts-and-2fa.md).

## Done when

- [ ] You wrote down what exists exactly once in your project.
- [ ] Every item is sorted into code, data, or secrets and keys.
- [ ] Code has a second copy (pushed or exported) in a different place.
- [ ] Data has its own export in a different place.
- [ ] Secrets are in a password manager, not in Git and not in an export.
- [ ] You restored one copy into a new place and checked it against a known fact.
- [ ] You know where the key or password of your backup lives, and you tested that it works.

## Data note

In this course you only use fake data, so exports of your data are harmless. Keep that habit when you copy things: an export is a full copy of whatever the app stores. If an app ever holds real personal data, every export and every backup is also a copy of personal data. It then needs the same protection and the same deletion rules as the original. Check [Data processing agreements](../../diy/03-data-processing-agreements.md) before any real data enters a tool. Never put secrets into an export you share with anyone.

## Next

[From prototype to product](02-prototype-to-product.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
