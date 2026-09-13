# Tool matrix, September 2026

| | |
|---|---|
| **Prerequisites** | [Rule one: no real data](../tracks/00-orientation/01-rule-one-no-real-data.md) |
| **Time** | ~15 min |
| **Outcome** | After this you can compare browser builders and coding agents on free tier, price, hosting, export and data handling |
| **Last verified** | 2026-09-13 |

**Prices change. Checked 2026-09-13. Check the link before you pay.**

Prices are in USD per month unless marked, before tax, as shown on the vendor page. "(unverified)" means we could not confirm the statement on the vendor page on that date. This is a comparison, not a recommendation: the authors do not endorse one vendor.

**Where to switch model training off.** Where a vendor documents the setting, the Data notes column says so and the Source column links the page. For every other tool, see the vendor's privacy settings page.

## Why this matters

Vendors change free tiers, prices and data rules several times a year. A dated table with a source per row lets you check what is still true instead of trusting memory or a blog post.

## Do it

Read your candidate's row, open the source, and compare it with the criteria in [Plans and licences](02-plans-and-licences.md) and [Data processing agreements](03-data-processing-agreements.md).

### Browser app builders

| Tool | Free tier | Cheapest paid | Hosts your app | Export | Data notes | Source |
|---|---|---|---|---|---|---|
| Lovable | 5 build credits per day, at most 30 per month, plus 20 Cloud and 4 AI credits per month | Pro from $25 (100 credits), or $21 per month billed yearly | yes | Git sync (GitHub, GitLab, Bitbucket), also on Free | see the vendor's privacy settings page before you build | [subscription plans](https://docs.lovable.dev/introduction/subscription-plans) |
| Bolt | 300K tokens per day, 1M per month, website hosting included | Pro $25 billed monthly | yes, also on free | GitHub or ZIP (unverified) | read the terms (unverified) | [pricing](https://bolt.new/pricing) |
| v0 | $5 credits per month, 7 messages per day | Plus $30 per user | deploys to Vercel | GitHub sync, also on free | training opt-out by default only on Business ($100 per user) | [pricing](https://v0.app/pricing) |
| Replit | Free Mode, limits on the page | Core $20, or $18 billed yearly | yes (publish) | GitHub (unverified) | free publishes to North America; EU publishing from Core; cannot be changed after publishing | [pricing](https://replit.com/pricing), [geography](https://docs.replit.com/features/security/geography) |
| Base44 | 25 message credits per month | Starter $16, billed yearly | yes | GitHub integration listed on paid plans | data stored in the US by default; EU or UK storage only on Elite or Enterprise | [pricing](https://base44.com/pricing), [privacy](https://docs.base44.com/Community-and-support/Privacy-and-security) |
| Google AI Studio, Build | free (Unpaid Services) | paid models and hosting cost per use | deploys to Cloud Run, Google Cloud pricing may apply | GitHub sync | unpaid use is covered by a separate data section in the terms | [build mode](https://ai.google.dev/gemini-api/docs/aistudio-build-mode), [terms](https://ai.google.dev/gemini-api/terms) |
| Claude (chat) | free plan | Pro $20 billed monthly, or $17 per month with the annual discount ($200 billed up front) | shareable artifacts (unverified) | copy the code | consumer plans: used for training only if you allow it | [pricing](https://claude.com/pricing), [training](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training) |
| ChatGPT (chat) | free plan | Go $8 | no (unverified) | copy the code | turn off "Improve the model for everyone" (unverified) | [pricing](https://learn.chatgpt.com/docs/pricing), [data controls](https://help.openai.com/en/articles/7730893-data-controls-faq) |
| Softr (no-code, no code generation) | free plan, 5 users | Basic $19 billed yearly, $25 monthly | yes | no code export (unverified) | check the DPA and hosting page (unverified) | [pricing and plans](https://docs.softr.io/workspace-and-billing/pricing-and-plans) |

### Coding agents (CLI and editor)

None of these host your app. You deploy yourself: see [Deploy and share](05-deploy-and-share.md). Your code lives in your own Git repository: see [Code hosting and backup](04-code-hosting-and-backup.md).

| Tool | Free tier | Cheapest paid | Hosts your app | Export | Data notes | Source |
|---|---|---|---|---|---|---|
| Claude Code | not included in Claude Free | Pro $20 billed monthly, or $17 per month with the annual discount ($200 billed up front) | no | your Git repository | consumer plans: training only if you allow it; commercial terms include a DPA | [pricing](https://claude.com/pricing), [setup](https://code.claude.com/docs/en/setup) |
| OpenAI Codex (CLI, IDE, web) | included in ChatGPT Free | Go $8 | no | your Git repository | Business: no training on business data by default | [pricing](https://learn.chatgpt.com/docs/pricing), [CLI](https://learn.chatgpt.com/docs/codex/cli) |
| Google Antigravity (desktop and CLI) | quota refreshed weekly | Google AI Pro, €21.99 on the Google One page | no | your Git repository | opt out of data collection in Settings | [plans](https://antigravity.google/docs/plans), [FAQ](https://antigravity.google/docs/faq/), [Google One](https://one.google.com/about/plans) |
| Gemini CLI | stopped serving free users and Google AI Pro and Ultra subscribers on 2026-06-18; Antigravity CLI replaces it for them | paid Gemini API key (pay per use), Gemini Code Assist Standard or Enterprise, or Google Cloud | no | your Git repository | see the Gemini API terms | [Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) |
| GitHub Copilot (editor and CLI) | 2,000 completions per month, limited chat and agent use | Pro $10 | no | your Git repository | Free, Pro and Pro+: interaction data used for training from 24 April 2026 unless you opt out | [plans](https://github.com/features/copilot/plans), [data policy](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/) |
| Cursor (editor) | Hobby, limited agent requests | Pro $20 | no | your Git repository | privacy mode: code data not used for training | [pricing](https://cursor.com/pricing) |

Claude Code system requirements: macOS 13.0+, Windows 10 1809+ or Windows Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine Linux 3.19+. On Windows it installs natively from PowerShell with `irm https://claude.ai/install.ps1 | iex` or with WinGet. WSL is optional ([source](https://code.claude.com/docs/en/setup), checked 2026-09-13).

OpenAI Codex CLI also installs natively on Windows, from PowerShell with `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`. WSL is optional ([source](https://learn.chatgpt.com/docs/codex/cli), checked 2026-09-13).

## Done when

- [ ] I opened the source link of the tool I want to use and the numbers still match.
- [ ] I know the free tier, the cheapest paid plan and the data notes of that tool.
- [ ] I know how I get my work out of that tool (export or Git).

## Watch out

- A "(unverified)" cell is a question to check, not a fact.
- Free tiers get smaller over time. Gemini CLI is an example: its free use ended on 2026-06-18.
- A tool that hosts your app also holds your data. Check the region before you share a link.

## Sources

- Lovable subscription plans: https://docs.lovable.dev/introduction/subscription-plans (checked 2026-09-13)
- Bolt pricing: https://bolt.new/pricing (checked 2026-09-13)
- v0 pricing: https://v0.app/pricing (checked 2026-09-13)
- Replit pricing: https://replit.com/pricing (checked 2026-09-13)
- Replit geography: https://docs.replit.com/features/security/geography (checked 2026-09-13)
- Base44 pricing: https://base44.com/pricing (checked 2026-09-13)
- Base44 privacy and security: https://docs.base44.com/Community-and-support/Privacy-and-security (checked 2026-09-13)
- Google AI Studio build mode: https://ai.google.dev/gemini-api/docs/aistudio-build-mode (checked 2026-09-13)
- Gemini API terms: https://ai.google.dev/gemini-api/terms (checked 2026-09-13)
- Claude pricing: https://claude.com/pricing (checked 2026-09-13)
- Anthropic model training: https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training (checked 2026-09-13)
- Claude Code setup: https://code.claude.com/docs/en/setup (checked 2026-09-13)
- OpenAI Codex pricing: https://learn.chatgpt.com/docs/pricing (checked 2026-09-13)
- OpenAI Codex CLI: https://learn.chatgpt.com/docs/codex/cli (checked 2026-09-13)
- OpenAI data controls FAQ: https://help.openai.com/en/articles/7730893-data-controls-faq (could not be loaded for this check, 2026-09-13)
- Softr pricing and plans: https://docs.softr.io/workspace-and-billing/pricing-and-plans (checked 2026-09-13)
- Google Antigravity plans: https://antigravity.google/docs/plans (checked 2026-09-13)
- Google Antigravity FAQ: https://antigravity.google/docs/faq/ (checked 2026-09-13)
- Google One plans: https://one.google.com/about/plans (checked 2026-09-13)
- Google Developers Blog, Gemini CLI to Antigravity CLI: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ (checked 2026-09-13)
- Gemini CLI quotas and pricing: https://geminicli.com/docs/resources/quota-and-pricing (checked 2026-09-13, banner confirms the change)
- OpenAI Codex CLI Windows install script: https://chatgpt.com/codex/install.ps1 (quoted as a command, from the Codex CLI page, checked 2026-09-13)
- GitHub Copilot plans: https://github.com/features/copilot/plans (checked 2026-09-13)
- GitHub Copilot data policy update: https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/ (checked 2026-09-13)
- Cursor pricing: https://cursor.com/pricing (checked 2026-09-13)
