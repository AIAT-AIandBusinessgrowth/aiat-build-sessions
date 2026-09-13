# Deploy and share

| | |
|---|---|
| **Prerequisites** | [Code hosting and backup](04-code-hosting-and-backup.md), then [Secrets and keys](07-secrets-and-keys.md). Read Secrets and keys first |
| **Time** | ~30 min to read, longer to deploy |
| **Outcome** | After this you can pick a place to run your app and check five things before you share the link |
| **Last verified** | 2026-09-13 |

## Why this matters

An app on your laptop helps nobody else. To share it, it has to run somewhere with a public address. You choose and set up that place yourself, with your own account and your own card if needed. Nobody deploys for you, and if you attend a session, the session host does not either. This page does not recommend one provider as "the one to use".

## Do it

### 1. Ask criteria before brands

- Where does the app and its data run? Can you pick an EU region, and can you change it later?
- Is there a free tier, and what happens when you exceed it: the app stops, or you get billed?
- Can you set a spend cap?
- Can you keep secrets in the platform settings instead of in the code?
- Is commercial use allowed on the free tier?
- Can you move away: does it deploy from your Git repository?

### 2. Know the five groups

All figures below are vendor statements checked 2026-09-13. Follow the link before you rely on them.

**(a) Browser builders that host for you**

Lovable, Bolt, v0, Replit, Base44 and Google AI Studio can publish your app with one click. This is the easiest path. Check the region and export options in the [tool matrix](tool-matrix-2026-09.md). Google AI Studio deploys to Cloud Run, where Google Cloud pricing may apply ([source](https://ai.google.dev/gemini-api/docs/aistudio-build-mode), checked 2026-09-13).

**(b) Static hosting (HTML, CSS, JavaScript, no server of your own)**

| Provider | Free tier notes | Source |
|---|---|---|
| GitHub Pages | Public repositories on GitHub Free; not intended as free hosting for an online business or commercial software as a service; sites up to 1 GB, soft bandwidth limit 100 GB per month | [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |
| Netlify | Free plan: 300 credits per month with a hard limit | [Netlify credit-based plans](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/) |
| Vercel | Hobby is for personal, non-commercial use; Pro $20 per month; regions include `fra1` (Frankfurt) | [pricing](https://vercel.com/pricing), [regions](https://vercel.com/docs/regions) |
| Cloudflare Pages | Free plan: 500 builds per month | [Pages limits](https://developers.cloudflare.com/pages/platform/limits/) |

**(c) Platforms that run a server for you (PaaS)**

| Provider | Free tier notes | Source |
|---|---|---|
| Render | A free web service spins down after 15 minutes without traffic, the next visit waits for it to start | [Render free](https://render.com/docs/free) |
| Railway | Free plan starts with a 30-day trial with $5 credits, then $1 per month; Hobby has a $5 minimum usage; regions include EU West in Amsterdam | [pricing](https://railway.com/pricing), [regions](https://docs.railway.com/deployments/regions) |
| Fly.io | Free trial: 2 hours of machine runtime or 7 days, whichever comes first, then apps stop until you add a payment method | [free trial](https://fly.io/docs/about/free-trial/) |
| Koyeb | A Free Instance lets you deploy a web service free of charge; Frankfurt is among the regions | [instances](https://www.koyeb.com/docs/reference/instances), [pricing](https://www.koyeb.com/pricing) |

**(d) EU-based cloud providers**

These providers are headquartered in Europe. Most of them sell virtual servers, where you run the operating system, updates and firewall yourself. That is more work and more responsibility than (a) to (c).

- Hetzner Cloud: CX23 costs €5.49 per month excl. VAT in Germany and Finland (new price since the price adjustment of 15 June 2026, excluding IPv4) ([source](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/), checked 2026-09-13). A primary IPv4 address adds €0.50 per month excl. VAT ([source](https://docs.hetzner.com/general/infrastructure-and-availability/ipv4-pricing/), checked 2026-09-13).
- Scaleway: its serverless products include a free tier per account per month ([source](https://www.scaleway.com/en/pricing/serverless/), checked 2026-09-13).
- OVHcloud: Public Cloud free trial with US$200 credit, conditions on the page ([source](https://www.ovhcloud.com/en/public-cloud/prices/), checked 2026-09-13).
- Exoscale: [pricing](https://www.exoscale.com/pricing/).
- Clever Cloud: [pricing](https://www.clever.cloud/pricing/).

**(e) Databases**

| Provider | Free tier notes | Region | Source |
|---|---|---|---|
| Supabase | Limit of 2 active projects; free projects pause after 1 week of inactivity | Pick a specific region such as Central EU (Frankfurt), `eu-central-1`. A general region lets Supabase choose the data centre within that area | [pricing](https://supabase.com/pricing), [regions](https://supabase.com/docs/guides/platform/regions) |
| Neon | Free plan, no credit card required | Regions include AWS Europe (Frankfurt) | [pricing](https://neon.com/pricing), [regions](https://neon.com/docs/introduction/regions) |
| Firebase | Spark plan: no-cost, no payment method needed | Once a Firestore database is created, its location cannot be changed | [pricing](https://firebase.google.com/pricing), [locations](https://firebase.google.com/docs/firestore/locations) |

Choose the region when you create the database. For several providers you cannot move it later without starting over.

### 3. Before you share the URL

1. **Region:** you know where the app and its data run.
2. **Secrets:** API keys are set as environment variables in the platform settings, not in the code and not in the browser. See [Secrets and keys](07-secrets-and-keys.md).
3. **Spend limit:** a cap or a hard limit is set, or you are on a plan that stops at the limit. See [Costs, limits and spend caps](06-costs-limits-spend-caps.md).
4. **Data:** the app contains only made-up data.
5. **Test:** you opened the link in a private browser window, not logged in.

### 4. Internal tools (for your team, not the public)

If only your colleagues should use the app:

- **Restrict access.** Use the login or password protection your host offers. Then open the link in a private browser window and check that you see a login, not the app.
- **Do not publish internal code with GitHub Pages.** On GitHub Free, Pages works only from public repositories, so your code would be public too ([source](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits), checked 2026-09-13).
- **"Personal, non-commercial" plans do not cover work use.** Vercel Hobby is one example (see the table in section 2).
- **Ask first.** Before you host anything with work data, ask your employer's IT or data protection contact. Until they say yes, rule one applies: made-up data only.

## Done when

- [ ] I answered the criteria questions for the provider I picked.
- [ ] My app runs at a public address.
- [ ] I checked all five points in section 3 before sharing.
- [ ] For an internal tool: access is restricted, and I asked IT or data protection before using work data.
- [ ] The link works in a private browser window.

## Watch out

- A public link is public. Anyone who gets it can use your app, and your API quota.
- Free tiers that sleep or pause (Render, Supabase) look broken to a first visitor. Say so when you share.
- "Non-commercial" free tiers (Vercel Hobby, GitHub Pages) do not fit a product you sell.
- Keep the code in your own repository, so you can move to another provider. See [From prototype to product](../tracks/06-keep-and-ship/02-prototype-to-product.md).

## Sources

- Google AI Studio Build mode: https://ai.google.dev/gemini-api/docs/aistudio-build-mode (checked 2026-09-13)
- GitHub Pages limits: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits (checked 2026-09-13)
- Netlify credit-based pricing plans: https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/ (checked 2026-09-13)
- Vercel pricing: https://vercel.com/pricing (checked 2026-09-13)
- Vercel regions: https://vercel.com/docs/regions (checked 2026-09-13)
- Cloudflare Pages limits: https://developers.cloudflare.com/pages/platform/limits/ (checked 2026-09-13)
- Render free instances: https://render.com/docs/free (checked 2026-09-13)
- Railway pricing: https://railway.com/pricing (checked 2026-09-13)
- Railway deployment regions: https://docs.railway.com/deployments/regions (checked 2026-09-13)
- Fly.io free trial: https://fly.io/docs/about/free-trial/ (checked 2026-09-13)
- Koyeb instances: https://www.koyeb.com/docs/reference/instances (checked 2026-09-13)
- Koyeb pricing: https://www.koyeb.com/pricing (checked 2026-09-13)
- Hetzner price adjustment 15 June 2026: https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/ (checked 2026-09-13)
- Hetzner IP pricing: https://docs.hetzner.com/general/infrastructure-and-availability/ipv4-pricing/ (checked 2026-09-13)
- Scaleway serverless pricing: https://www.scaleway.com/en/pricing/serverless/ (checked 2026-09-13)
- OVHcloud Public Cloud prices: https://www.ovhcloud.com/en/public-cloud/prices/ (checked 2026-09-13)
- Exoscale pricing: https://www.exoscale.com/pricing/ (checked 2026-09-13)
- Clever Cloud pricing: https://www.clever.cloud/pricing/ (checked 2026-09-13)
- Supabase pricing: https://supabase.com/pricing (checked 2026-09-13)
- Supabase regions: https://supabase.com/docs/guides/platform/regions (checked 2026-09-13)
- Neon pricing: https://neon.com/pricing (checked 2026-09-13)
- Neon regions: https://neon.com/docs/introduction/regions (checked 2026-09-13)
- Firebase pricing: https://firebase.google.com/pricing (checked 2026-09-13)
- Firestore locations: https://firebase.google.com/docs/firestore/locations (checked 2026-09-13)
