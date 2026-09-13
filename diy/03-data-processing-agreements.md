# Data processing agreements

| | |
|---|---|
| **Prerequisites** | [Rule one: no real data](../tracks/00-orientation/01-rule-one-no-real-data.md). Optional background: [Plans and licences](02-plans-and-licences.md) |
| **Time** | ~20 min |
| **Outcome** | After this you can tell whether a tool and plan may see personal data, and who has to decide that |
| **Last verified** | 2026-09-13 |

This page explains the principle. It is not legal advice. For real decisions, ask your organisation's data protection contact.

## Why this matters

When you type into an AI tool, the vendor processes what you type. If that text contains personal data about other people (names, e-mail addresses, customer records, health or HR information), the law cares who the vendor is, what contract exists and what the vendor does with the data.

Most people learning here are on a personal plan. A personal plan is a contract between you and the vendor. Your organisation is not part of it.

## Do it

### 1. Understand the one legal idea you need

Under the GDPR, the organisation that decides why personal data is processed is the controller. A vendor that processes the data on its behalf is a processor. Article 28 says the controller "shall use only processors providing sufficient guarantees", and that the processing "shall be governed by a contract or other legal act" ([GDPR Art. 28](https://gdpr-info.eu/art-28-gdpr/), checked 2026-09-13). That contract is usually called a data processing agreement (DPA).

In practice: if a tool will see your company's or your customers' personal data, your organisation needs a DPA with that vendor. You cannot sign that for them on a personal plan.

### 2. Know the difference between personal and business plans

| | Personal plan | Business or commercial plan |
|---|---|---|
| Contract with | You | Your organisation |
| DPA | Usually none for your organisation | Often part of the terms |
| Training on your input | Depends on the vendor and your settings | Often off by default |
| Who decides | You, for your own data | Your organisation |

### 3. Check the training default of your tool

Vendor statements on 2026-09-13:

- **Claude Free, Pro and Max (including Claude Code on those plans):** Anthropic uses chats and coding sessions to improve its models if you choose to allow it, or if a conversation is flagged for safety review ([source](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training), checked 2026-09-13). Commercial products are covered by the Commercial Terms, which incorporate Anthropic's Data Processing Addendum ([source](https://www.anthropic.com/legal/commercial-terms), checked 2026-09-13).
- **ChatGPT Free, Plus and Pro:** the data controls let you turn off "Improve the model for everyone" (unverified: the OpenAI help page could not be loaded for this check, open it yourself: https://help.openai.com/en/articles/7730893-data-controls-faq). For ChatGPT Business, OpenAI states "No training on your business data by default" ([source](https://learn.chatgpt.com/docs/pricing), checked 2026-09-13).
- **GitHub Copilot Free, Pro and Pro+:** from 24 April 2026, interaction data (inputs, outputs, code snippets, context) is used to train and improve GitHub's AI models unless you opt out in your GitHub account settings ([source](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/), checked 2026-09-13).
- **Google Antigravity:** you can opt out of data collection in the Settings panel ([source](https://antigravity.google/docs/faq/), checked 2026-09-13).
- **Google AI Studio and the unpaid Gemini API:** these count as "Unpaid Services", and the terms have a separate section on how Google uses the content you submit. Read it before you type anything ([source](https://ai.google.dev/gemini-api/terms), checked 2026-09-13).
- **Cursor:** with privacy mode on, Cursor states that code data is not used for training by Cursor or its model providers ([source](https://cursor.com/pricing), checked 2026-09-13).
- **v0:** "Training opt-out by default" is listed on the Business plan ($100 per user per month) ([source](https://v0.app/pricing), checked 2026-09-13).

### 4. Check where the data is stored

- **Base44:** all servers are in the United States, and data is stored in the US by default. Since 16 April 2026, Elite and Enterprise plans can choose EU or UK storage for new apps ([source](https://docs.base44.com/Community-and-support/Privacy-and-security), checked 2026-09-13).
- **Replit:** publishing geography can be chosen on Core, Pro and Enterprise. Free users publish to North America. The geography cannot be changed after publishing ([source](https://docs.replit.com/features/security/geography), checked 2026-09-13).
- **Any other tool:** the material only lists the builders above. For your tool, "unknown" is a valid answer at first. Then ask the vendor, or check its privacy page for where data is stored.

### 5. Apply the rule of thumb

- **Personal plan = practice with made-up data.** Your own harmless data is fine too.
- **Company or customer personal data only in a plan with a DPA**, and only if your employer says yes. That decision belongs to your organisation, usually the data protection contact, not to you and not to anyone who runs a session.
- If you are unsure whether something counts as personal data, treat it as personal data.

Before you ask a vendor or your employer, collect the answers to these questions:

- Is there a DPA, and who signs it?
- Can training on our data be switched off, and is it off by default?
- In which region is the data stored and processed?
- Is there a list of sub-processors?
- How long is data kept, and can we delete it?
- Can we export our data?

## Done when

- [ ] I know whether my plan is a personal plan or a business plan.
- [ ] I checked the training setting in my tool and switched it off where possible.
- [ ] I know where my tool stores data, or I wrote down "unknown" and asked the vendor or checked its privacy page.
- [ ] I know who in my organisation decides about real data.
- [ ] I will build with made-up data on a personal plan.

## Watch out

- "We do not train on your data" is not the same as "we have a DPA with your organisation". You need both answers.
- A setting you switched off can be switched on again by a policy change. Re-check after vendor announcements.
- Pasting a customer e-mail "just to test the prompt" is already processing personal data.
- More on handling data: [Does the AI need this?](../tracks/02-data-first/01-does-the-ai-need-this.md), [Schema first, then synthetic data](../tracks/02-data-first/03-schema-then-synthetic-data.md), [If something went wrong](../tracks/02-data-first/04-if-something-went-wrong.md).

## Sources

- GDPR Article 28, Processor: https://gdpr-info.eu/art-28-gdpr/ (checked 2026-09-13)
- Anthropic, Is my data used for model training?: https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training (checked 2026-09-13)
- Anthropic Commercial Terms: https://www.anthropic.com/legal/commercial-terms (checked 2026-09-13)
- OpenAI, Data controls FAQ: https://help.openai.com/en/articles/7730893-data-controls-faq (could not be loaded for this check, 2026-09-13)
- OpenAI Codex pricing (Business training default): https://learn.chatgpt.com/docs/pricing (checked 2026-09-13)
- GitHub Blog, Updates to GitHub Copilot interaction data usage policy: https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/ (checked 2026-09-13)
- Google Antigravity FAQ: https://antigravity.google/docs/faq/ (checked 2026-09-13)
- Gemini API Additional Terms of Service: https://ai.google.dev/gemini-api/terms (checked 2026-09-13)
- Cursor pricing (privacy mode): https://cursor.com/pricing (checked 2026-09-13)
- v0 pricing: https://v0.app/pricing (checked 2026-09-13)
- Base44, Privacy and security: https://docs.base44.com/Community-and-support/Privacy-and-security (checked 2026-09-13)
- Replit, Geography: https://docs.replit.com/features/security/geography (checked 2026-09-13)
