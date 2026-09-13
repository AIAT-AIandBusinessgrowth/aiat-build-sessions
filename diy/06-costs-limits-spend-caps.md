# Costs, limits and spend caps

| | |
|---|---|
| **Prerequisites** | [Plans and licences](02-plans-and-licences.md) |
| **Time** | ~20 min |
| **Outcome** | After this you can read the limits of your plan, set a spend cap and avoid the usual surprises |
| **Last verified** | 2026-09-13 |

## Why this matters

Agents work in loops. One task can mean dozens of model calls, so limits run out faster than you expect, and pay-per-use bills grow while you are not looking. You pay your own bills. Setting the cap is your job, before the first run.

## Do it

### 1. Know your usage window

Subscriptions for coding agents measure use in time windows, not in a fixed number of messages.

- **Claude (Pro, Max, Team):** a five-hour session limit and a weekly limit. Settings > Usage shows how much you have used ([source](https://support.claude.com/en/articles/9797557-usage-limit-best-practices), checked 2026-09-13).
- **OpenAI Codex:** OpenAI publishes estimates of local messages per five-hour period and says they are not fixed limits. Your usage dashboard shows current limits and reset times ([source](https://learn.chatgpt.com/docs/pricing), checked 2026-09-13).
- **Google Antigravity:** without Google AI Pro or Ultra, the quota refreshes weekly. On Google AI Pro it refreshes every five hours until a weekly limit is reached ([source](https://antigravity.google/docs/plans), checked 2026-09-13).
- **GitHub Copilot Free:** 2,000 completions per month plus limited chat and agent use ([source](https://github.com/features/copilot/plans), checked 2026-09-13).

Write down when your window resets. If the weekly limit runs out on Wednesday, you wait until next week or pay more.

### 2. Know your credits

Browser builders count credits or tokens. What one message costs depends on the task.

| Builder | Free allowance | Source |
|---|---|---|
| Lovable | 5 daily build credits, up to 30 per calendar month | [subscription plans](https://docs.lovable.dev/introduction/subscription-plans) |
| Bolt | 300K tokens daily limit, 1M tokens per month | [pricing](https://bolt.new/pricing) |
| v0 | $5 of included monthly credits, 7 messages per day | [pricing](https://v0.app/pricing) |
| Base44 | 25 message credits per month | [pricing](https://base44.com/pricing) |

All checked 2026-09-13. Lovable notes that in Build mode, the cost depends on the complexity of the request and the work completed ([source](https://docs.lovable.dev/introduction/credits-and-usage), checked 2026-09-13). A request like "fix all the bugs" can cost many small ones.

### 3. Set a spend cap

Do this before you use an API key or add a card to a hosting platform.

- **Anthropic API:** spend limits set a maximum monthly cost for an organisation's API usage ([source](https://platform.claude.com/docs/en/api/rate-limits), checked 2026-09-13). Set it low in the Console billing settings.
- **Google Cloud (for example AI Studio apps deployed to Cloud Run):** an alerts-only budget does not cap usage or spending, it only sends alerts. A spend cap budget exists as a preview for supported services ([source](https://docs.cloud.google.com/billing/docs/how-to/budgets), checked 2026-09-13).
- **Vercel:** setting a spend amount does not stop usage by itself. To stop, you must enable the option to pause the production deployment of your projects ([source](https://vercel.com/docs/spend-management), checked 2026-09-13).
- **Netlify Free:** 300 credits per month with a hard limit, no recharge ([source](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/), checked 2026-09-13).
- **Lovable auto top-up:** has a monthly spend limit setting, and "No limit" is one of the options. Check which one is selected ([source](https://docs.lovable.dev/introduction/credits-and-usage), checked 2026-09-13).
- **Any other provider:** search its docs for "spend limit", "budget" or "usage limit". Check whether it is a cap (stops) or an alert (only tells you).

## Done when

- [ ] I know when my usage window resets.
- [ ] I know my free credits and roughly what one request costs.
- [ ] Every API key and every platform with my card has a spend cap, not only an alert.
- [ ] I set a calendar reminder for renewal dates of paid plans.

## Watch out

What surprises people most:

- **An alert is not a cap.** Budgets on several platforms only send e-mails while the bill keeps growing.
- **An API key in an agent loop.** The agent retries on errors. Without a cap, a stuck loop keeps spending.
- **Yearly plans are paid up front.** Example: the pricing page shows Claude Pro at "$17 per month with annual subscription discount ($200 billed up front)" ([source](https://claude.com/pricing), checked 2026-09-13).
- **Auto top-up** refills credits and charges your card without asking again.
- **Free tiers that sleep or pause.** Render spins down free web services after 15 minutes without traffic ([source](https://render.com/docs/free), checked 2026-09-13). Supabase pauses free projects after 1 week of inactivity ([source](https://supabase.com/pricing), checked 2026-09-13).
- **Trials that end.** On Fly.io, apps stop when the trial is used up until you add a payment method ([source](https://fly.io/docs/about/free-trial/), checked 2026-09-13).
- **A free builder that deploys to a paid cloud.** The builder is free, the hosting may not be.

## Sources

- Claude, usage limit best practices: https://support.claude.com/en/articles/9797557-usage-limit-best-practices (checked 2026-09-13)
- Claude pricing: https://claude.com/pricing (checked 2026-09-13)
- OpenAI Codex pricing: https://learn.chatgpt.com/docs/pricing (checked 2026-09-13)
- Google Antigravity plans: https://antigravity.google/docs/plans (checked 2026-09-13)
- GitHub Copilot plans: https://github.com/features/copilot/plans (checked 2026-09-13)
- Lovable subscription plans: https://docs.lovable.dev/introduction/subscription-plans (checked 2026-09-13)
- Lovable credits and usage: https://docs.lovable.dev/introduction/credits-and-usage (checked 2026-09-13)
- Bolt pricing: https://bolt.new/pricing (checked 2026-09-13)
- v0 pricing: https://v0.app/pricing (checked 2026-09-13)
- Base44 pricing: https://base44.com/pricing (checked 2026-09-13)
- Anthropic API rate limits and spend limits: https://platform.claude.com/docs/en/api/rate-limits (checked 2026-09-13)
- Google Cloud, Create budgets: https://docs.cloud.google.com/billing/docs/how-to/budgets (checked 2026-09-13)
- Vercel spend management: https://vercel.com/docs/spend-management (checked 2026-09-13)
- Netlify credit-based pricing plans: https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/ (checked 2026-09-13)
- Render free instances: https://render.com/docs/free (checked 2026-09-13)
- Supabase pricing: https://supabase.com/pricing (checked 2026-09-13)
- Fly.io free trial: https://fly.io/docs/about/free-trial/ (checked 2026-09-13)
