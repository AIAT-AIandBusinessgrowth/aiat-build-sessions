# Pick your lane

| | |
|---|---|
| **Prerequisites** | [Rule one: no real data](01-rule-one-no-real-data.md) |
| **Time** | ~10 min |
| **Outcome** | After this unit you can choose between the browser lane and the CLI lane for your situation and know what you need to set up for it. |
| **Last verified** | 2026-09-13 |

## Why this matters

There are two ways to build with AI in this material. Both teach the same habits. The difference is what you have to install and what can break.

A first session spent installing things usually ends with nothing built. Pick the lane that lets you build something today. You can switch later, and every unit gives the steps for both lanes.

## Do it

### 1. Compare the two lanes (3 min)

| | Browser lane (default) | CLI lane (optional) |
|---|---|---|
| **What it is** | An app builder in your web browser, for example Lovable, Bolt, v0, Replit, Google AI Studio or Claude artifacts | A coding agent in a terminal on your laptop, for example Claude Code, Codex CLI or Antigravity CLI |
| **What you install** | Nothing | A terminal (already on your computer), git, and the agent |
| **Where your app runs** | On the vendor's servers. You get a link to share. | On your laptop. Sharing it is a separate step ([deploy and share](../../diy/05-deploy-and-share.md)). |
| **Where your code lives** | Inside the tool, until you export it or sync it to GitHub | In a folder on your laptop, and in your GitHub account once you push |
| **What can break** | Credits run out; the project exists only inside the tool | Installation, permissions, paths; the agent can change or delete files in the folder you start it in |
| **Good for** | A small web app with a link, today | Working with files, scripts and data on your computer; more control |

Prices, free tiers and data settings per tool are in the [tool matrix](../../diy/tool-matrix-2026-09.md). This unit repeats none of them, because they change.

### 2. Answer five questions (3 min)

1. Can you install software on the laptop you will use? Work laptops often do not allow it. **No: browser lane.**
2. Have you typed commands in a terminal before, even once? **No: browser lane for now.**
3. Do you want a link you can send to someone today? **Yes: browser lane.**
4. Is your idea about files on your computer (rename a folder of documents, clean up a CSV, a small script) rather than a web page? **Yes: CLI lane.**
5. Are you ready to pay for a plan if the free tier is not enough? Check the [tool matrix](../../diy/tool-matrix-2026-09.md) and [plans and licences](../../diy/02-plans-and-licences.md). **Not sure: pick a tool with a free tier.**

If two or more answers point to the browser lane, start there.

### 3. Set up only what your lane needs (3 min to plan, setup in your own time)

You organise your own accounts, plans and hosting. Nobody sets them up for you. That is on purpose: everything stays yours when you finish these tracks.

**Browser lane**

- [ ] A personal account with two-factor authentication, not a shared mailbox ([accounts and 2FA](../../diy/01-accounts-and-2fa.md))
- [ ] One app builder account, logged in
- [ ] Model training switched off where the option exists
- [ ] A GitHub account for backups (recommended, see [code hosting and backup](../../diy/04-code-hosting-and-backup.md))

**CLI lane**

- [ ] One approved agent account, with two-factor authentication and training settings reviewed. A browser builder account is not required.
- [ ] A terminal you can open (macOS: Terminal; Windows: PowerShell). Claude Code and Codex both install natively on Windows from PowerShell; WSL is optional ([Claude Code setup](https://code.claude.com/docs/en/setup), [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), checked 2026-09-13).
- [ ] `git --version` prints a version
- [ ] One agent installed, and `<agent> --version` prints a version
- [ ] Logged in to the agent with your own account

The full self-check for both lanes is in [Ready to build](../../ready-to-build.md).

### 4. Write it down (1 min)

One line each: lane, tool, whether access works, where to check remaining usage, training setting. Do not write an e-mail address, account identifier or credentials into the learning record.

## Done when

- [ ] I picked one lane and one tool.
- [ ] I can log in to that tool with my own account, with two-factor authentication on.
- [ ] I worked through the self-check for my lane in [Ready to build](../../ready-to-build.md).
- [ ] I know where the tool shows how much of my plan's limit is left.

## Data note

Use an account in your own name, not a shared login. When a tool asks for access to other services, grant only what you need: a GitHub connection for backups, yes; your mailbox or your cloud drive, no.

## Next

[Your first build](../01-first-build/01-your-first-build.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
