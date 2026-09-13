# Glossary

Terms used in the tracks and the Do it yourself guides, in plain English. Each entry links to the unit that explains it. German terms are in [modules/de/glossar.md](../modules/de/glossar.md).

## Numbers and A

- **2FA (two-factor authentication):** a second proof at login besides your password, usually a six-digit code from an authenticator app or a passkey. Someone who steals your password still cannot get in. [Accounts and 2FA](../diy/01-accounts-and-2fa.md)
- **Adoption ladder:** five levels of working with AI tools, from 0 (not yet) to 4 (delegating whole tasks with verification). A map, not a ranking. [The adoption ladder](../tracks/04-the-map/03-adoption-ladder.md)
- **Agent:** a model with tools and a loop. It reads, acts, checks the result and repeats until the goal is reached or it asks you. Browser app builders are agents too. [Model, context, agent](../tracks/04-the-map/01-model-context-agent.md)
- **AGENTS.md:** a Markdown file at the top of a project or notes folder with instructions an agent reads before it works. [A vault and AGENTS.md](../tracks/07-second-brain/01-vault-and-agents-md.md)
- **Anonymous data:** data where nobody can identify the people any more, with the means reasonably likely to be used. Deleting the name column is usually not enough. [Does the AI need this?](../tracks/02-data-first/01-does-the-ai-need-this.md)
- **API key:** a secret string that lets a program use a service, paid per use. It keeps working and billing until you revoke it or it hits a cap you set. [Plans and licences](../diy/02-plans-and-licences.md), [Secrets and keys](../diy/07-secrets-and-keys.md)
- **App builder (browser app builder):** an agent in the web browser that builds and hosts a small web app for you, such as Lovable, Bolt or v0. [Which tool for what](../tracks/04-the-map/02-which-tool-for-what.md)
- **Artifact (Claude):** content that Claude creates in its own panel next to the chat, such as a small web page, a document or a piece of code. The tool matrix notes what you can do with it. [Tool matrix, September 2026](../diy/tool-matrix-2026-09.md), [Pick your lane](../tracks/00-orientation/02-pick-your-lane.md)
- **Autonomy slider:** how much an agent may do without you, set per task: propose only, edit with your review, or run until a checked condition holds. More autonomy needs stronger checks. [Context engineering](../tracks/08-advanced/01-context-engineering.md)

## B and C

- **Backup:** a second copy of your work in a place that does not fail together with the first. It counts only after a restore test worked. [Keep your work safe](../tracks/06-keep-and-ship/01-keep-your-work-safe.md)
- **Branch:** a separate line of changes in a Git repository. Work on a branch does not touch the main line until you merge it. [Parallel agents](../tracks/08-advanced/03-parallel-agents.md)
- **Chat assistant:** a chat window with a model, such as Claude, ChatGPT or Gemini. You copy results out by hand. [Which tool for what](../tracks/04-the-map/02-which-tool-for-what.md)
- **CI/CD minutes:** time that a code host's servers spend running automatic checks and deployments for you (continuous integration and continuous delivery). Free plans include a set number of minutes per month. [Code hosting and backup](../diy/04-code-hosting-and-backup.md)
- **CLAUDE.md:** the instruction file Claude Code reads at the start of a session. A line `@AGENTS.md` in it imports AGENTS.md. [A vault and AGENTS.md](../tracks/07-second-brain/01-vault-and-agents-md.md)
- **CLI (command-line interface) and CLI agent:** a CLI is a program you use by typing commands in a terminal. A CLI agent, such as Claude Code or Codex CLI, reads and changes files and runs commands on your computer. [Pick your lane](../tracks/00-orientation/02-pick-your-lane.md)
- **Clone:** copy a repository from a code host into a new folder, with its full history. Also the simplest restore test. [Code hosting and backup](../diy/04-code-hosting-and-backup.md)
- **Commit:** a saved checkpoint of changes in a Git repository, with a short message. It stays on your computer until you push it. [Your first build](../tracks/01-first-build/01-your-first-build.md)
- **Context engineering:** the habit of keeping an agent's context small and relevant: lean instruction files, fresh sessions between tasks, state kept in files. [Context engineering](../tracks/08-advanced/01-context-engineering.md)
- **Context window:** everything a model can see at once: messages, pasted files, tool output, instructions. It is finite, and quality drops as it fills. [Model, context, agent](../tracks/04-the-map/01-model-context-agent.md)
- **Credits (builder):** the unit a browser app builder uses to count your use. One message can cost less or more than one credit, depending on the task. Free plans include only a few. [Costs, limits and spend caps](../diy/06-costs-limits-spend-caps.md)

## D to F

- **Data minimisation:** give a tool only the data it needs for the task. To build something, the AI needs the structure of your data, not the values. [Does the AI need this?](../tracks/02-data-first/01-does-the-ai-need-this.md)
- **Data processing agreement (DPA):** the contract between an organisation and a vendor that processes personal data on its behalf. Personal plans usually come without one for your organisation. [Data processing agreements](../diy/03-data-processing-agreements.md)
- **Deploy:** put your app on a server with a public address, so other people can open it. [Deploy and share](../diy/05-deploy-and-share.md)
- **Done when:** one line that says what you can see or click when a task is finished. Written before the work starts. [Spec interview](../tracks/03-plan-first/01-spec-interview.md)
- **Environment variable:** a named value a program receives when it starts, such as `PAYMENT_API_KEY`. Keys live there, not in the code. Locally they often sit in a `.env` file that `.gitignore` excludes. [Secrets and keys](../diy/07-secrets-and-keys.md)
- **Fork:** a copy of a repository under another account, with its full history. Anything ever committed, including a leaked key, is in every fork too. [Secrets and keys](../diy/07-secrets-and-keys.md)
- **Free tier:** the part of a plan you can use without paying. Its limits change, often without notice. [Tool matrix, September 2026](../diy/tool-matrix-2026-09.md)
- **Frontmatter:** a small block of fields at the top of a note, between two `---` lines, such as `type` and `status`. Agents can filter notes by it. [Notes as a graph](../tracks/07-second-brain/02-notes-as-a-graph.md)

## H to L

- **Handover artefact:** a short document that answers the questions people would otherwise ask you: how to run it, who to ask, what it must never do, how to switch it off. [Handover and first users](../tracks/06-keep-and-ship/03-handover-and-first-users.md)
- **Headless mode:** running an agent on one task without its interactive screen, for example from a script. [Loop engineering](../tracks/08-advanced/02-loop-engineering.md)
- **Health check:** a simple address or command that answers whether an app is running, so that a hosting platform or a monitor can test it automatically. [PoC to production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md)
- **Hook:** a command of your own that the agent tool runs at a set moment, for example a check when the agent wants to stop. [Loop engineering](../tracks/08-advanced/02-loop-engineering.md)
- **Hosting:** the place where your app runs and its data is stored. Browser builders host for you. With a CLI agent you choose a provider yourself. [Deploy and share](../diy/05-deploy-and-share.md)
- **Issue tracker:** a list of tasks, bugs and questions that belongs to a project, such as GitHub Issues. Each entry has a title, a description and a status. [Spec interview](../tracks/03-plan-first/01-spec-interview.md)
- **Kill switch:** one documented and tested step that stops an agent at once, for example disabling its schedule and revoking its key. [Agents in operation](../tracks/08-advanced/04-agents-in-operation.md)
- **Lane:** the browser lane (nothing to install, the tool hosts your app) or the CLI lane (an agent in a terminal on your laptop). [Pick your lane](../tracks/00-orientation/02-pick-your-lane.md)
- **Lethal trifecta:** an agent that has private data, reads untrusted content and can send things out can be tricked into leaking the data. Remove at least one of the three. [Always-on assistants with guardrails](../tracks/08-advanced/05-always-on-assistants-guardrails.md)
- **LFS (Git Large File Storage):** an add-on to Git that keeps large files, such as videos or big data sets, outside the normal repository. Code hosts limit its free storage. [Code hosting and backup](../diy/04-code-hosting-and-backup.md)
- **Loop prompt:** a copy-paste prompt that makes any agent agree the scope first, build in checked stages and write down what is open. [Seven sentences](../tracks/05-verify-and-loop/03-seven-sentences.md), [loop prompt template](../templates/loop-prompt.md)

## M and P

- **MCP (Model Context Protocol):** an open standard for connecting an agent to external tools and data sources, called servers. Every connected server adds tool descriptions to the context. The tracks do not cover MCP in depth. [Context engineering](../tracks/08-advanced/01-context-engineering.md) shows why tools you do not use should be disconnected.
- **Model:** a language model, a text predictor trained on a very large amount of text. It writes fluent answers, and fluent wrong answers. [Model, context, agent](../tracks/04-the-map/01-model-context-agent.md)
- **MVP (minimum viable product):** the smallest version that is useful to someone other than you, with an IN list, an OUT list and a stop date. [From prototype to product](../tracks/06-keep-and-ship/02-prototype-to-product.md), [MVP template](../templates/MVP.md)
- **Passkey:** a way to sign in with your device (fingerprint, face or device PIN) instead of a password. [Accounts and 2FA](../diy/01-accounts-and-2fa.md)
- **Personal data:** any information about a person who can be identified, directly or together with other information. Customer numbers, IP addresses and free-text notes count too. [Rule one: no real data](../tracks/00-orientation/01-rule-one-no-real-data.md)
- **Personal plan:** a tool account in your own name. The contract is between you and the vendor. Your organisation is not part of it. [Data processing agreements](../diy/03-data-processing-agreements.md)
- **Plan mode:** a mode in which an agent analyses and proposes but does not change files. [Spec interview](../tracks/03-plan-first/01-spec-interview.md), [Context engineering](../tracks/08-advanced/01-context-engineering.md)
- **PoC (proof of concept):** a quick build that shows an idea can work. It is not ready for real users or real data. [PoC to production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md)
- **Prompt:** the text you give a model: a question, a task, instructions. [Your first build](../tracks/01-first-build/01-your-first-build.md)
- **Prompt injection:** text the agent reads, such as a web page, a document or a message, contains instructions, and the agent follows them. [Always-on assistants with guardrails](../tracks/08-advanced/05-always-on-assistants-guardrails.md)
- **Pseudonymisation:** replacing identifying details while a way back exists, for example "Customer C-0042" or a hashed e-mail address. Pseudonymous data is still personal data. [Does the AI need this?](../tracks/02-data-first/01-does-the-ai-need-this.md)
- **Pull request:** a proposed change to a repository that its owners review before they merge it. This is how you contribute to this material. [Contributing](../README.md#contributing)
- **Push:** send your commits from your computer to the repository on a code host. Only what you pushed exists there. [Share and export](../tracks/01-first-build/02-share-and-export.md)

## R

- **Region:** where the data centre that runs a service and stores its data is located. With several providers you cannot change it later. [Deploy and share](../diy/05-deploy-and-share.md)
- **Repository:** a project folder under version control with Git, including the history of every change. On a code host it can be private or public. [Code hosting and backup](../diy/04-code-hosting-and-backup.md)
- **Restore test:** getting a backup back into a new place and checking it against a known fact. An untested backup is a guess. [Keep your work safe](../tracks/06-keep-and-ship/01-keep-your-work-safe.md)
- **Role archetypes:** five kinds of impact on a product: Prototyper, Builder, Sweeper, Grower and Maintainer. Hats you wear, not job titles. [Role archetypes](../tracks/04-the-map/04-role-archetypes.md)
- **Rotate (a key):** create a new key, put it where the old one was used, and revoke the old key so it stops working. [Secrets and keys](../diy/07-secrets-and-keys.md)
- **Rule one:** use only fake data, public data that is not about people, or data about yourself. [Rule one: no real data](../tracks/00-orientation/01-rule-one-no-real-data.md)

## S

- **Sandbox:** a separate environment, such as another machine, a virtual machine or a container, where an agent cannot reach your files, keys or accounts. [Always-on assistants with guardrails](../tracks/08-advanced/05-always-on-assistants-guardrails.md)
- **Schema:** the structure of a data set: column names and types, without any values. [Schema first, then synthetic data](../tracks/02-data-first/03-schema-then-synthetic-data.md)
- **Secret:** anything that grants access: passwords, API keys, tokens, recovery codes, private SSH keys. Never in code, commits, notes or prompts. [Secrets and keys](../diy/07-secrets-and-keys.md)
- **Spec:** a one-page description of what you build: one sentence, problem, users, IN, OUT, data (fake), done when, open questions. [Spec interview](../tracks/03-plan-first/01-spec-interview.md), [spec template](../templates/SPEC.md)
- **Spend cap:** a limit that stops usage or billing at an amount you set. An alert only tells you; a cap stops. [Costs, limits and spend caps](../diy/06-costs-limits-spend-caps.md)
- **SSH:** a secure way to connect to another computer or a code host with a key pair instead of a password. The private key stays on your laptop. [Code hosting and backup](../diy/04-code-hosting-and-backup.md)
- **Stack trace:** the list of function calls that an error message prints, showing where in the code the error happened. It can contain file paths and data, so read it before you paste it anywhere. [PoC to production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md)
- **Sub-processor:** a company that a vendor hires to process your data for it, for example a cloud hosting provider. Vendors with a DPA usually publish a list. [Data processing agreements](../diy/03-data-processing-agreements.md)
- **Subagent:** a helper inside one agent session. It works in its own context window and returns only a summary. [Parallel agents](../tracks/08-advanced/03-parallel-agents.md)
- **Subscription:** a plan with a fixed price and usage limits. At the limit you wait or upgrade. [Plans and licences](../diy/02-plans-and-licences.md)
- **Synthetic data:** invented rows that fit the schema of real data but describe nobody. [Schema first, then synthetic data](../tracks/02-data-first/03-schema-then-synthetic-data.md)

## T to W

- **Token (usage unit):** a piece of a word. Context windows are measured in tokens, pay-per-use prices count them, and some builders count your free allowance in tokens. [Model, context, agent](../tracks/04-the-map/01-model-context-agent.md), [Costs, limits and spend caps](../diy/06-costs-limits-spend-caps.md)
- **Token (access token):** a different meaning: a long secret that works like a password, for example a personal access token for GitHub. Treat it like a key. [Code hosting and backup](../diy/04-code-hosting-and-backup.md)
- **Usage window:** the period in which a subscription measures your use. When it ends, the limit resets. [Costs, limits and spend caps](../diy/06-costs-limits-spend-caps.md)
- **Vault:** a folder of Markdown notes that you own and an agent can read, used as a second brain. [A vault and AGENTS.md](../tracks/07-second-brain/01-vault-and-agents-md.md)
- **Verification ladder:** three rungs for checking an agent's result: a check inside the prompt, evidence you look at yourself, and a second opinion from a fresh reviewer. [The verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md)
- **Wikilink:** a link between notes written in double square brackets around the note path, used by Obsidian and other note apps. [Notes as a graph](../tracks/07-second-brain/02-notes-as-a-graph.md)
- **Work cycle:** four steps: check the state, agree the scope, build in stages with a check after each, and finish with a list of what is open. [One work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md)
- **Worktree:** a second folder of the same Git repository, on its own branch, so that two agents cannot overwrite each other's files. [Parallel agents](../tracks/08-advanced/03-parallel-agents.md)
- **WSL (Windows Subsystem for Linux):** a Linux environment that runs inside Windows. Some people run CLI agents there. Claude Code and Codex CLI also install natively in PowerShell, so WSL is optional. [Ready to build](../ready-to-build.md), [Pick your lane](../tracks/00-orientation/02-pick-your-lane.md)
