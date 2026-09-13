# AI:AT Build Sessions

Learn to build, check and hand over your own tools with agents.

This repository is the self-paced material of the Build Sessions. Short units take you from a first app in the browser to agents whose work you can check, keep and hand over. Each unit leads to a small action or observable check, using made-up data.

**Start with one small step:** [Learn with an agent or on paper](learning/README.md). [Deutsch starten](learning/start-de.md). No account is needed for the first exercise.

This is public, reusable learning material from AI:AT, the AI Factory Austria. You can study independently or use it in separately organised training. It is not registration for an internal working group or a promise of scheduled sessions.

## Who it is for

- People who have never used a coding agent (such as Claude Code or Codex) or a browser app builder (such as Lovable, Bolt or v0).
- People who build small tools for their own work and want them to keep working when others use them.
- People who already use a CLI agent and want better habits for context, loops and parallel work.

You do not need to be a developer. Most units work in the browser, with nothing to install.

## How it works

Every unit has the same shape: why it matters, what to do, a "Done when" checklist and a data note. Most units take 10 to 45 minutes.

You can use the material in two ways:

- **Self-paced.** Pick a reading path in [START-HERE.md](START-HERE.md) and work through the units in order.
- **In a Build Session.** About 10 minutes of input, about 40 minutes of building your own thing at a table, a short round where people show what they built, and a card at the end. Two session formats use this material: Start, for people new to building with AI, and Ship, for people taking their own tool into real use.

Want to run a session yourself? See [facilitate/run-a-build-session.md](facilitate/run-a-build-session.md).

## Start here

1. [Learning guide](learning/README.md): a small first step, knowledge checks and a way to continue next time.
2. [START-HERE.md](START-HERE.md): four longer paths once you know your next skill.
3. [ready-to-build.md](ready-to-build.md): set up only what your chosen lane needs.

## Tracks

| Track | What you learn | Units | Time |
|---|---|---|---|
| [00 Orientation](tracks/00-orientation/01-rule-one-no-real-data.md) | Rule one (no real data), and choosing the browser lane or the CLI lane | 2 | ~20 min |
| [01 First build](tracks/01-first-build/01-your-first-build.md) | A small app with fake data, a share link and a copy outside the tool | 2 | ~1 h |
| [02 Data first](tracks/02-data-first/01-does-the-ai-need-this.md) | Spotting personal data, building from a schema with synthetic data, and what to do if real data slipped in | 4 | ~1 h 20 min |
| [03 Plan first](tracks/03-plan-first/01-spec-interview.md) | A one-page spec from an agent interview, and a product sprint in a team | 2 | ~1 h 45 min |
| [04 The map](tracks/04-the-map/01-model-context-agent.md) | Model, context and agent; which tool for what; the adoption ladder; role archetypes | 4 | ~55 min |
| [05 Verify and loop](tracks/05-verify-and-loop/01-verification-ladder.md) | The verification ladder, five failure patterns, seven working rules and one full work cycle | 4 | ~1 h 30 min |
| [06 Keep and ship](tracks/06-keep-and-ship/01-keep-your-work-safe.md) | Backups and restore tests, from prototype to product, handover and first users | 3 | ~1 h 5 min |
| [07 Second brain](tracks/07-second-brain/01-vault-and-agents-md.md) | A notes vault an agent reads under two hard rules, and notes linked as a graph | 2 | ~1 h 15 min |
| [08 Advanced](tracks/08-advanced/01-context-engineering.md) | Optional, for CLI agents: context engineering, loops, parallel agents, agents in operation, always-on assistants, a production checklist | 6 | ~2 h 25 min |

29 units, about 11 h 35 min in total. The times are the estimates from each unit header.

## Do it yourself: accounts, licences, hosting

You or your organisation arrange accounts, licences, plans and hosting. The guides explain setup and common recovery steps. This repository does not provide accounts or a support service.

| Guide | What it covers |
|---|---|
| [Accounts and 2FA](diy/01-accounts-and-2fa.md) | Your own e-mail, a password manager, two-factor authentication, passkeys |
| [Plans and licences](diy/02-plans-and-licences.md) | Subscription or API key, and what the plans include |
| [Data processing agreements](diy/03-data-processing-agreements.md) | Which plans may see personal data, and who decides |
| [Code hosting and backup](diy/04-code-hosting-and-backup.md) | A private repository, connecting your laptop or builder |
| [Deploy and share](diy/05-deploy-and-share.md) | Where your app can run, and what to check before you share the link |
| [Costs, limits and spend caps](diy/06-costs-limits-spend-caps.md) | Usage windows, credits, caps that stop and alerts that do not |
| [Secrets and keys](diy/07-secrets-and-keys.md) | Keeping API keys out of code, repositories and prompts |
| [Monitoring and recovery](diy/08-monitoring-and-recovery.md) | Practising failure, checking alert delivery and proving a restore |
| [Tool matrix, September 2026](diy/tool-matrix-2026-09.md) | Free tiers, prices, hosting, export and data notes, with a source and a date per row |

Prices and limits change. Open the vendor link before you pay.

## More material

| Path | What |
|---|---|
| [exercises/find-the-personal-data/](exercises/find-the-personal-data/README.md) | A fake customer list with hidden personal data, two solutions and a schema script |
| [exercises/verification-lab/](exercises/verification-lab/README.md) | An offline app with a deliberate defect: predict, check, explain and transfer, at three levels |
| [templates/](templates/) | Fill-in files: spec, MVP, AGENTS.md starter, product README, loop prompt, cards, weekly AI news |
| [facilitate/](facilitate/run-a-build-session.md) | For anyone who wants to run a Build Session: format, agenda, table anchors, show and tell |
| [reference/glossary.md](reference/glossary.md) | Terms in plain English, each with a link to the unit that explains it |
| [reference/sources.md](reference/sources.md) | Every external source used in the tracks and guides, grouped by site |
| [modules/de/](modules/de/) | German material: agent basics, scaling, role archetypes, context engineering, customer data and test data, and a glossary |

## Use it with an agent

1. On GitHub, choose **Code → Download ZIP**, then extract the ZIP. Or, if you use Git, run `git clone https://github.com/AIAT-AIandBusinessgrowth/aiat-build-sessions.git`.
2. Open the extracted or cloned **aiat-build-sessions** folder in Codex, or start Claude Code inside it. This is the course folder. Build your own app in a separate folder.
3. Start a learning conversation:

```text
Help me learn from this repository. I have 20 minutes and use <tool or no tool>.
Ask me one question at a time. Let me try before giving hints or answers.
Use the material and cite the file. Start with one small step.
```

For active knowledge checks, say **“Quiz me on verification”** or **“Prüfe mich zu Context Engineering”**. For a later session, say **“Continue from learning/local/progress.md”** if you chose to save a local record. [Learning guide](learning/README.md) explains the modes and limitations.

[AGENTS.md](AGENTS.md) is the shared guide contract. [CLAUDE.md](CLAUDE.md) imports it for Claude Code. No plugin is required. For a new app, copy [project-AGENTS.md](templates/project-AGENTS.md) into the app folder as `AGENTS.md`, not the course's tutor instructions.

No coding agent? Read on GitHub. You can do the [verification lab](exercises/verification-lab/README.md) on paper or in a browser without an account. A chat assistant only knows files you provide; use the copyable prompt in the [learning guide](learning/README.md).

The [personal-data exercise](exercises/find-the-personal-data/README.md) stays human-only. Do it yourself, then compare with its supplied solutions.

## Rule one: no real personal data

Before any tool: use invented data or public data that is not about people. Keep real personal and customer data out of these exercises, including your own personal information. No customer files, contracts, health or HR records, even to test.

Why, and how to get fake data from the agent: [Rule one: no real data](tracks/00-orientation/01-rule-one-no-real-data.md).

## Contributing

Corrections and additions are welcome as pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and [the training guide](facilitate/training-guide.md) for facilitation and learning evidence.

- New units follow [_unit-template.md](_unit-template.md).
- No personal data, no credentials, no internal hostnames. Use `example.com` addresses and roles instead of names.
- Every number (price, limit, date, version) needs a source link and the date you checked it.
- Plain English, short sentences, no marketing.

## Licence

Text and materials: [CC BY-SA 4.0](LICENSE). You may share and adapt them if you give credit and share your changes under the same licence.

## Publisher

AI:AT is the AI Factory Austria: [ai-at.eu](https://ai-at.eu). Contact: aiandbusinessgrowth@ai-at.eu
