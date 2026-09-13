# Plans and licences

| | |
|---|---|
| **Prerequisites** | [Accounts and 2FA](01-accounts-and-2fa.md) |
| **Time** | ~20 min |
| **Outcome** | After this you can tell a subscription from an API key, and pick a plan that fits what you want to build |
| **Last verified** | 2026-09-13 |

## Why this matters

You pay for your own tools, or your employer does. Nobody hands out licences or seats, and if you attend a session, the session host does not either. Before you enter a card number, know what kind of plan you are buying, because the two kinds fail in opposite ways: a subscription stops when you hit the limit, an API key keeps going and keeps billing.

## Do it

### 1. Know the two ways to pay

| | Subscription | API key |
|---|---|---|
| How you pay | Fixed monthly or yearly price | Pay per use (per token or per request) |
| What happens at the limit | You wait until the limit resets, or upgrade | Nothing stops you, the bill grows |
| Good for | Learning, daily work with a coding agent | Apps that call a model, automation |
| Main risk | Hitting the limit mid-task | A surprise invoice |

- Example subscription limits: Claude Pro, Max and Team plans have a five-hour session limit and a weekly limit, shown under Settings > Usage ([source](https://support.claude.com/en/articles/9797557-usage-limit-best-practices), checked 2026-09-13). OpenAI publishes Codex usage estimates per five-hour period and says they are not fixed limits ([source](https://learn.chatgpt.com/docs/pricing), checked 2026-09-13).
- An API key has no cap unless you set one. See [Costs, limits and spend caps](06-costs-limits-spend-caps.md) before you create one.

### 2. Ask criteria before brands

Before you pick a vendor, answer these for your use:

- Does the plan include the coding agent, or only the chat?
- What happens at the limit: wait, pay extra, or auto top-up?
- Is there a data processing agreement, and can training on your data be switched off? See [Data processing agreements](03-data-processing-agreements.md).
- Can you export your work, or push it to Git?
- Monthly or yearly: a yearly plan is paid up front.

### 3. What the plans include for coding agents

Prices are in USD per month unless marked, before tax, as shown on the vendor page on 2026-09-13.

| Tool | Free plan | Cheapest paid plan that includes the agent | Higher plans | Source |
|---|---|---|---|---|
| Claude Code | Not included in Claude Free | Pro: $20 if billed monthly, or "$17 per month with annual subscription discount ($200 billed up front)", as the pricing page words it | Max from $100; Team standard seat $25 monthly or $20 yearly | [claude.com/pricing](https://claude.com/pricing) |
| OpenAI Codex | Included in ChatGPT Free ($0) | Go: $8 | Plus $20; Pro from $100; Business $25 per user billed monthly | [learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing) |
| Google Antigravity (desktop and CLI) | Included, quota refreshed weekly | Google AI Pro: quota refreshed every five hours until a weekly limit; €21.99 per month on the Google One plans page | Google AI Ultra | [antigravity.google/docs/plans](https://antigravity.google/docs/plans), [one.google.com/about/plans](https://one.google.com/about/plans) |
| GitHub Copilot | Free: 2,000 completions per month, limited chat and agent use | Pro: $10 | Pro+ $39; Max $100 | [github.com/features/copilot/plans](https://github.com/features/copilot/plans) |
| Cursor (editor) | Hobby: limited agent requests | Pro: $20 | Ultra $200 | [cursor.com/pricing](https://cursor.com/pricing) |

**Gemini CLI.** In a post dated 2026-05-19, Google announced that Gemini CLI stops serving free users (Gemini Code Assist for individuals) and Google AI Pro and Ultra subscribers on 2026-06-18. Antigravity CLI replaces it for them. Gemini CLI stays available with paid Gemini API keys, with Gemini Code Assist Standard or Enterprise licences, and through Google Cloud ([Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), checked 2026-09-13). The Gemini CLI quota page still shows an older free quota table, but its banner says the same as the blog ([source](https://geminicli.com/docs/resources/quota-and-pricing), checked 2026-09-13). Do not plan on a free Gemini CLI quota.

The Google AI Pro price depends on your country. The €21.99 figure is what the Google One page showed on 2026-09-13.

### 4. Free options

- ChatGPT Free includes Codex.
- Antigravity has a free weekly quota.
- GitHub Copilot Free and Cursor Hobby have small free allowances.
- Browser app builders have free tiers too: see the [tool matrix](tool-matrix-2026-09.md).

Free is enough to learn. It is not enough to depend on: free limits change without notice.

### 5. Team and business plans

- Team and business plans are bought by an organisation, not by you. They usually come with admin controls, a data processing agreement and different training defaults. Example: OpenAI states "No training on your business data by default" for ChatGPT Business ([source](https://learn.chatgpt.com/docs/pricing), checked 2026-09-13).
- If you want to use company or customer data, a business plan is the minimum, and your employer decides. See [Data processing agreements](03-data-processing-agreements.md).

## Done when

- [ ] I can explain the difference between a subscription and an API key in one sentence.
- [ ] I picked one plan and wrote down what happens when I reach its limit.
- [ ] I know whether I pay monthly or yearly, and when it renews.
- [ ] I did not create an API key without a spend cap.

## Watch out

- The same product name can mean different things: "Claude" the chat is free, "Claude Code" needs a paid plan.
- Prices on this page are a snapshot. Open the source link before you pay.
- If your employer pays, ask which plan they approve before you subscribe privately and expense it.

## Sources

- Claude pricing: https://claude.com/pricing (checked 2026-09-13)
- Claude, usage limit best practices (five-hour session and weekly limits): https://support.claude.com/en/articles/9797557-usage-limit-best-practices (checked 2026-09-13)
- Claude Code setup: https://code.claude.com/docs/en/setup (checked 2026-09-13)
- OpenAI Codex pricing: https://learn.chatgpt.com/docs/pricing (checked 2026-09-13)
- Google Antigravity plans: https://antigravity.google/docs/plans (checked 2026-09-13)
- Google One plans: https://one.google.com/about/plans (checked 2026-09-13)
- Google Developers Blog, Transitioning Gemini CLI to Antigravity CLI: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ (checked 2026-09-13)
- Gemini CLI quotas and pricing: https://geminicli.com/docs/resources/quota-and-pricing (checked 2026-09-13)
- GitHub Copilot plans: https://github.com/features/copilot/plans (checked 2026-09-13)
- Cursor pricing: https://cursor.com/pricing (checked 2026-09-13)
