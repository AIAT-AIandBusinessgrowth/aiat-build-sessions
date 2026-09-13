# From prototype to product

| | |
|---|---|
| **Prerequisites** | [Keep your work safe](01-keep-your-work-safe.md), [Spec interview](../03-plan-first/01-spec-interview.md), or a three-line mini-spec (what, for whom, done when) |
| **Time** | ~20 min |
| **Outcome** | After this unit you can say who your prototype is for, cut its scope, write a README and a feedback path, and list what breaks when someone other than you uses it. |
| **Last verified** | 2026-09-13 |

## Why this matters

A script solves your own problem today. A product solves someone else's problem tomorrow.

That shift sounds small. In practice it costs a few concrete things: a sentence that says what it is, named people who use it, a clear edge, a README, and a way to tell you when it breaks. Without them, you explain the thing again every time, and it stops working the day you are not around.

A useful test: **a product is a script someone else can use without asking you.**

## Do it

### 1. Write the one sentence (5 min)

Fill in:

> For **who**, **name** does **what**, instead of **what happens today**.

Do not write it alone. Let the agent interview you. This works in Claude Code, Codex, and the chat of a browser app builder:

```text
Ask me five questions about the tool I built: who uses it, what they do today,
what the tool changes, what it does not do, and what "working" means for them.
Ask one question at a time. Then give me three versions of this sentence:
"For <who>, <name> does <what>, instead of <what happens today>."
```

Pick one version and cut words until it fits on one line.

### 2. Name your users (3 min)

"Everyone in the team" is not a user. Write down real people who have the problem, and at least one person who is not you.

Keep the list where it belongs: names and contact details go into your private notes. In the repository, describe users by role, for example "office assistant, plans rooms every Monday".

### 3. Cut the scope (5 min)

Write two short lists and a date:

- **In:** three to five things the product does.
- **Out:** at least three things it deliberately does not do. This list matters more than the first one. It stops the product from growing in every direction.
- **Stop date:** when this version is finished, even if not everything is done.

Use the [MVP template](../../templates/MVP.md). A good prompt: "Read my sentence and write MVP.md with In, Out, and a stop date. Then remove half of the In list and tell me why."

### 4. Write the README (3 min)

Four questions, about twenty lines, no marketing:

1. What does it do, in one sentence?
2. Who is it for?
3. How do I start or open it?
4. What can it not do yet?

Prompt: "Write a README from MVP.md. Twenty lines, plain words, no marketing. Include how to start it from a clean machine." Then read it and delete everything that is not true yet. The fuller handover version follows in the next unit, based on the [product README template](../../templates/README-product.md).

### 5. Set a feedback path (2 min)

Decide on exactly one place where a user reports a problem or an idea: an issue tracker, a simple form, or a shared document. Write into the README:

- where to report,
- what to include ("what you tried, what happened, what you expected"),
- who reads it, and how often.

A feedback path nobody reads is worse than none, because users stop trying.

### 6. Find what breaks when someone else uses it (2 min plus homework)

Things that work for you often fail for the second person:

| What breaks | Why | What to do |
|---|---|---|
| "Works on my machine" | Hidden setup: installed tools, settings, file paths only you have | Start it once from a clean folder or a fresh account, following only the README |
| Your login is built in | The app uses your account or your API key | Give users their own access, or a shared key with a spend cap (see [Costs, limits, spend caps](../../diy/06-costs-limits-spend-caps.md)) |
| Blank screen on error | Nobody wrote an error message | Show a sentence that says what went wrong and what to try |
| Unexpected input | Empty fields, very long text, special characters, two people at once | Try each one yourself before users do |
| Costs | Every use spends your credits | Set a cap before you share the link |
| Real data shows up | A user types in real customer details | Say "fake data only" on the first screen, see [rule one](../00-orientation/01-rule-one-no-real-data.md) |

Two ways to find your own list:

- Ask the agent: "Act as a first-time user who has never met me. Use only the README. List the first five places where you get stuck."
- Watch one colleague use it without helping. Write down every question they ask. Each question is a missing README line or a missing message in the app.

## Done when

- [ ] Your one sentence fits on one line.
- [ ] You named at least one user who is not you (names in private notes, roles in the repository).
- [ ] MVP.md has In, Out (at least three items), and a stop date.
- [ ] The README answers the four questions.
- [ ] The README says where to report problems and who reads the reports.
- [ ] You have a list of what breaks for someone else, and the top three are fixed or noted.

## Data note

Feedback often arrives with screenshots, and screenshots often contain real data. Tell users up front: fake data only, and no screenshots that show real names, customers, or messages. When you paste feedback into an agent, remove names first. The agent's vendor sees everything you paste.

## Next

[Handover and first users](03-handover-and-first-users.md)
