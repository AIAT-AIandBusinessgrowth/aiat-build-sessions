
# Ready to build

Set up your own accounts before your first build. There are two steps: a **minimum start** that is enough for your first app in the browser, and a **full setup** for everything after that. Accounts, licences and hosting are your own. Nobody sets them up for you, and if you attend a session, the session host does not either. That is on purpose: you keep everything you build.

Before you use a personal AI account for work, or install a tool on a work laptop, check your employer's IT rules. Some organisations do not allow it, and they decide.

The [Do it yourself guide](diy/01-accounts-and-2fa.md) explains each step in detail.

## Rule one, before any tool: no personal or customer data

Every tool below runs on a personal plan. Personal plans come without a data processing agreement between your organisation and the vendor, and several of them use what you type to improve their models unless you switch that off. So:

- Use made-up data, public data or your own data only. Never names, e-mails, customer files, contracts, health or HR data. Not even "just to test".
- Ask the agent to generate fake data for you. That is part of the skill.
- Switch off model training in the tool's settings where the option exists (see the [tool matrix](diy/tool-matrix-2026-09.md)).
- If your real job needs real data, talk to your organisation's data protection contact before real data goes into any tool. Why: [Data processing agreements](diy/03-data-processing-agreements.md).

## Pick your lane

**Browser lane (default, nothing to install).** The tool hosts your app, you share a link. Works on any laptop, no admin rights.

**CLI lane (optional, for people with their own laptop and a terminal).** A coding agent on your machine, code in your own GitHub account. More power, and more things that can break. You fix them yourself, with the vendor's help pages and your agent.

Both lanes need your own accounts with two-factor authentication: [Accounts and 2FA](diy/01-accounts-and-2fa.md). What a plan includes and what it costs: [Plans and licences](diy/02-plans-and-licences.md).

## Tools, short list

**Browser lane:** Lovable, Base44, Bolt, v0, Replit, Google AI Studio (Build), or a chat assistant such as Claude or ChatGPT for a quick page.

**CLI lane:** Claude Code (needs a paid Claude plan), OpenAI Codex CLI (included in ChatGPT Free), Google Antigravity CLI (free weekly quota), GitHub Copilot CLI (Copilot Free), or the Cursor editor.

Gemini CLI stopped serving free users and Google AI Pro and Ultra subscribers on 2026-06-18. Antigravity CLI replaces it for them. Gemini CLI still works with paid Gemini API keys, with Gemini Code Assist Standard or Enterprise, or through Google Cloud ([source](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), post dated 2026-05-19, checked 2026-09-13).

Free tiers, prices, hosting, export and data notes with a source for every row: **[tool matrix, September 2026](diy/tool-matrix-2026-09.md)**. Prices change, check the link before you pay.

**If you do not want to choose:** take an app builder with GitHub sync for an app, or a chat assistant that can share a page by link for a quick interactive thing.

## Minimum start (~20 min)

Enough for [Your first build](tracks/01-first-build/01-your-first-build.md) in the browser lane.

1. Pick one builder from the short list. Create an account with your own e-mail address and turn on two-factor authentication ([Accounts and 2FA](diy/01-accounts-and-2fa.md)).
2. Read rule one above.
3. Switch model training off in the builder's settings, where the option exists.
4. Write down your free limit.

**Save your free credits for the build.** Free builder credits are small. Example: Lovable's Free plan gives 5 build credits per day, at most 30 per month ([source](https://docs.lovable.dev/introduction/subscription-plans), checked 2026-09-13). Do not spend them on the self-check prompt on the same day as your first build. Try the self-check on an earlier day, or skip that one line and go straight to Your first build.

## Full setup (~75 min)

Do this before [Share and export](tracks/01-first-build/02-share-and-export.md) and the tracks after it.

1. **Your own mailbox with 2FA.** Not a shared mailbox ([Accounts and 2FA](diy/01-accounts-and-2fa.md)).
2. **A password manager**, with your recovery codes in it.
3. **A GitHub account with 2FA** ([Code hosting and backup](diy/04-code-hosting-and-backup.md)).
4. **Browser lane:** connect your builder to GitHub and let the builder create the private repository, for example `playground`. Do not create it by hand first.
5. **CLI lane:** install one agent (next section), create a folder called `playground`, and push it to a new, empty private repository. Follow variant (a) in section 4 of [Code hosting and backup](diy/04-code-hosting-and-backup.md).

## Install a CLI agent (CLI lane)

Install from the vendor's page. If the page says something different from this list, the page wins.

- **Claude Code:** [install page](https://code.claude.com/docs/en/setup). Needs a paid Claude plan. On Windows it installs natively from PowerShell with `irm https://claude.ai/install.ps1 | iex`. WSL is optional (checked 2026-09-13).
- **OpenAI Codex CLI:** [install page](https://learn.chatgpt.com/docs/codex/cli). On Windows it installs natively from PowerShell with `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`. WSL is optional (checked 2026-09-13).

Only run install commands that you copied from the vendor's own page.

## Where your code lives

Use a free personal [GitHub](https://github.com/pricing) account: unlimited private repositories, no cost (checked 2026-09-13). Connect your builder to it, or use GitHub Desktop if you are on the CLI lane. Step by step: [Code hosting and backup](diy/04-code-hosting-and-backup.md). GitLab.com, Codeberg and Bitbucket work too. Note that the GitLab.com free tier limits private top-level groups to five users ([source](https://docs.gitlab.com/user/free_user_limit/), checked 2026-09-13).

Work disappears when it exists exactly once, in one browser tab or on one laptop. So the ritual at the end of every work session is: export or push, then open the repository page and check that the last change is there. More: [Keep your work safe](tracks/06-keep-and-ship/01-keep-your-work-safe.md).

## Self-check, browser lane

Minimum start:

- [ ] I have a builder account with my own e-mail address and two-factor authentication.
- [ ] I picked a builder, logged in, and wrote down my free limit.
- [ ] I switched model training off in the tool settings, where the option exists.
- [ ] I read rule one and I will build with fake data.
- [ ] Optional, not on the day of my first build: I asked it for "a to-do list with three entries" and the app runs in the preview.

Full setup:

- [ ] My e-mail account is personal, not shared, and has two-factor authentication.
- [ ] My passwords and recovery codes are in a password manager.
- [ ] I have a GitHub account with two-factor authentication.
- [ ] I connected the builder to GitHub, it created a private repository, and I can see a commit there (or I exported a ZIP).
- [ ] I opened my app's share link in a private browser window and it works.

## Self-check, CLI lane

- [ ] I can open a terminal (macOS: Terminal, Windows: PowerShell) and run `whoami`.
- [ ] `git --version` works (GitHub Desktop is fine too).
- [ ] I installed one agent from its vendor's install page, and it starts in the terminal.
- [ ] I logged in with my own account.
- [ ] In a folder called `playground` I ran `git init` and asked the agent to "create a README.md with three sentences".
- [ ] I pushed that folder to a new, empty private GitHub repository and can see it on github.com ([Code hosting and backup](diy/04-code-hosting-and-backup.md), section 4, variant a).
- [ ] I switched model training off in my account settings.
- [ ] I keep API keys in `.env`, never in a commit and never in a prompt: [Secrets and keys](diy/07-secrets-and-keys.md).
- [ ] I read rule one and I will build with fake data.

## Your first session

If you work self-paced, you can skip the laptop line.

- If you attend a session: your laptop, charged, and the accounts you set up.
- One small thing from your own work you would like to have as a tool: a list you keep in Excel, a text you write every week, a calculation you repeat. That is what you build in [Your first build](tracks/01-first-build/01-your-first-build.md).
