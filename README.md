# AI:AT Build Sessions

Build your own tools with agents. Every week.

This repository is the self-paced material of the Build Sessions. Short units take you from a first app in the browser to agents whose work you can check, keep and hand over. In every unit you build something, with made-up data.

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

1. [START-HERE.md](START-HERE.md): five minutes, four reading paths.
2. [ready-to-build.md](ready-to-build.md): the self-check before your first build.

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

You organise your own accounts, licences, plans and hosting. Nobody sets them up for you, and there is no setup support. That is on purpose: what you build stays yours.

| Guide | What it covers |
|---|---|
| [Accounts and 2FA](diy/01-accounts-and-2fa.md) | Your own e-mail, a password manager, two-factor authentication, passkeys |
| [Plans and licences](diy/02-plans-and-licences.md) | Subscription or API key, and what the plans include |
| [Data processing agreements](diy/03-data-processing-agreements.md) | Which plans may see personal data, and who decides |
| [Code hosting and backup](diy/04-code-hosting-and-backup.md) | A private repository, connecting your laptop or builder |
| [Deploy and share](diy/05-deploy-and-share.md) | Where your app can run, and what to check before you share the link |
| [Costs, limits and spend caps](diy/06-costs-limits-spend-caps.md) | Usage windows, credits, caps that stop and alerts that do not |
| [Secrets and keys](diy/07-secrets-and-keys.md) | Keeping API keys out of code, repositories and prompts |
| [Tool matrix, September 2026](diy/tool-matrix-2026-09.md) | Free tiers, prices, hosting, export and data notes, with a source and a date per row |

Prices and limits change. Open the vendor link before you pay.

## More material

| Path | What |
|---|---|
| [exercises/find-the-personal-data/](exercises/find-the-personal-data/README.md) | A fake customer list with hidden personal data, two solutions and a schema script |
| [templates/](templates/) | Fill-in files: spec, MVP, AGENTS.md starter, product README, loop prompt, cards, weekly AI news |
| [facilitate/](facilitate/run-a-build-session.md) | For anyone who wants to run a Build Session: format, agenda, table anchors, show and tell |
| [reference/glossary.md](reference/glossary.md) | Terms in plain English, each with a link to the unit that explains it |
| [reference/sources.md](reference/sources.md) | Every external source used in the tracks and guides, grouped by site |
| [modules/de/](modules/de/) | German material: agent basics, scaling, role archetypes, context engineering, customer data and test data, and a glossary |

## Use it with an agent

1. Clone or download the repository: `git clone https://github.com/AIAT-AIandBusinessgrowth/aiat-build-sessions.git`
2. Open the folder with your agent (Claude Code, Codex or similar). Start the agent inside that folder, at the top level of the repository.
3. Ask questions. For example: "I have 30 minutes and use a browser builder. Which unit should I do?" or "Explain the verification ladder with an example from my tool."

Do not paste the exercise file into any AI tool, and do not ask the agent to solve it. The exercise is meant to be done by you, without AI: [exercises/find-the-personal-data/](exercises/find-the-personal-data/README.md).

[AGENTS.md](AGENTS.md) makes the agent a guide. It answers from this material, names the file it used, says when the material does not cover your question, and never asks for real data. Codex and other agents read `AGENTS.md` directly. Claude Code reads [CLAUDE.md](CLAUDE.md), which imports `AGENTS.md` with the line `@AGENTS.md`.

No CLI agent? Read the units on GitHub, or paste one unit into a chat assistant and ask about it.

## Rule one: no real personal data

Before any tool: use made-up data, public data that is not about people, or data about yourself. No names, e-mail addresses, customer files, contracts, health or HR data of other people. Not even to test.

Why, and how to get fake data from the agent: [Rule one: no real data](tracks/00-orientation/01-rule-one-no-real-data.md).

## Contributing

Corrections and additions are welcome as pull requests.

- New units follow [_unit-template.md](_unit-template.md).
- No personal data, no credentials, no internal hostnames. Use `example.com` addresses and roles instead of names.
- Every number (price, limit, date, version) needs a source link and the date you checked it.
- Plain English, short sentences, no marketing.

## Licence

Text and materials: [CC BY-SA 4.0](LICENSE). You may share and adapt them if you give credit and share your changes under the same licence.

## Publisher

AI:AT is the AI Factory Austria: https://ai-at.eu. Contact: aiandbusinessgrowth@ai-at.eu
