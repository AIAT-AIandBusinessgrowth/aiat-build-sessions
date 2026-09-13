# Run a Build Session

For anyone who wants to run a weekly hands-on session with this material: in a team, a company, a school or a meetup. You need a room or a video call, people with their own laptops, and one unit from `tracks/`.

## What a Build Session is

People build their own small tools with AI agents, at tables, while the host keeps time. There are no slides and no course. The input is short. The building is the point.

Spend your effort on making the first build work for everyone in the room, not on follow-up messages.

## Two formats

The same session shape works for two different groups. **Start** is for people who are new to building with AI: browser tools first, the tracks in order, fake data only. **Ship** is for people who take their own tool into real use: the input comes from [Keep and ship](../tracks/06-keep-and-ship/01-keep-your-work-safe.md), [Verify and loop](../tracks/05-verify-and-loop/01-verification-ladder.md) and the [PoC to production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md), and the build time goes into each person's own product. Run the two as separate sessions, so the input fits everyone in the room.

## The format: 60 to 75 minutes

| Block | 60 min version | 75 min version | What happens |
|---|---|---|---|
| Start and rule one | ~3 min | ~3 min | Welcome, the data rule, today's unit |
| Input | 10 min at most | 10 min at most | One idea from one unit, shown live in a tool. One prompt to copy. |
| Build | ~34 min | ~45 min | Everyone works on their own thing, at tables of 4 to 5 |
| Round | ~8 min | ~12 min | Show and tell: a few people show what they built |
| Retro card | ~5 min | ~5 min | Three questions on a card, handed in before leaving |
| **Total** | **60 min** | **75 min** | |

A fill-in agenda for both versions is in [session-skeleton.md](session-skeleton.md). With more time, make the build block longer, never the input.

## A suggestion for ten weeks

A plan, not a rule. Change it when the retro cards ask for something else. The input shows one idea from the listed units; people read the rest on their own.

| Week | Input from | Note |
|---|---|---|
| 1 | [Rule one: no real data](../tracks/00-orientation/01-rule-one-no-real-data.md) and [Your first build](../tracks/01-first-build/01-your-first-build.md) | Everyone leaves with a running prototype |
| 2 | [Does the AI need this?](../tracks/02-data-first/01-does-the-ai-need-this.md) and the [exercise: find the personal data](../tracks/02-data-first/02-exercise-find-the-personal-data.md) | Exercise in pairs, see [Build](#build) |
| 3 | [Spec interview](../tracks/03-plan-first/01-spec-interview.md) | |
| 4 | [Model, context, agent](../tracks/04-the-map/01-model-context-agent.md), [Which tool for what](../tracks/04-the-map/02-which-tool-for-what.md), [The adoption ladder](../tracks/04-the-map/03-adoption-ladder.md) | |
| 5 | [Product sprint](../tracks/03-plan-first/02-product-sprint.md) | The sprint takes about 75 minutes on its own: plan extra time |
| 6 | [Keep your work safe](../tracks/06-keep-and-ship/01-keep-your-work-safe.md) and [From prototype to product](../tracks/06-keep-and-ship/02-prototype-to-product.md) | |
| 7 | [The verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md) and [Five failure patterns](../tracks/05-verify-and-loop/02-five-failure-patterns.md) | |
| 8 | [Seven sentences](../tracks/05-verify-and-loop/03-seven-sentences.md) and [One work cycle](../tracks/05-verify-and-loop/04-one-work-cycle.md) | |
| 9 | Show and tell for everyone: [show-and-tell.md](show-and-tell.md) | Longer round, shorter build |
| 10 | [Closing card](../templates/closing-card.md) | Hand it out instead of the retro card |

## Before the session

Setup happens before the session, not during it. A session spent installing tools ends with nothing built.

- [ ] Before the first session: clear the use of personal AI plans with your organisation's IT or data protection contact.
- [ ] Send one invitation per session: topic, time, what to bring, and the link to [ready-to-build.md](../ready-to-build.md). Ask people to work through it before they come. A fill-in text is in the [invitation template](../templates/invitation.md).
- [ ] Say plainly that everyone organises their own accounts, licences and hosting, and that the session offers no setup support. The [Do it yourself guides](../diy/01-accounts-and-2fa.md) help.
- [ ] Pick one unit for the input, for example from the [suggestion for ten weeks](#a-suggestion-for-ten-weeks). Do it yourself once, in a browser tool and, if people use one, in a CLI agent.
- [ ] Copy the one prompt people should start with into a place everyone can reach: a shared note, a slide with only that prompt, or a printout.
- [ ] Find one table anchor per table: a person who helps and does not teach. See [table-anchor.md](table-anchor.md). **No experienced anchors?** Host plus pairs works: people work in twos and the host walks around. An anchor is anyone who finished [ready-to-build.md](../ready-to-build.md).
- [ ] Print retro cards: [retro card template](../templates/retro-card.md). Optional: [show-and-tell cards](../templates/show-and-tell-card.md), [weekly AI news](../templates/weekly-ai-news.md) as an input.
- [ ] Prepare the fallbacks below.

## During the session

### Start and rule one (~3 min)

Say the data rule at the start of every session, even when everyone has heard it before. The habit matters more than the rule. For example:

> "Rule one, as every time: fake data only. No real names, no customer files, no screenshots with real data, not even to test. If your task needs real data, describe the columns and let the agent invent the rows."

Details: [Rule one: no real data](../tracks/00-orientation/01-rule-one-no-real-data.md). If real data ends up in a tool anyway: [If something went wrong](../tracks/02-data-first/04-if-something-went-wrong.md).

### Input (10 minutes at most)

- One idea, one example, one prompt. Show it live in a tool, including one thing that goes wrong.
- Link the unit so people can read the rest on their own.
- Stop at 10 minutes, even mid-sentence. Every extra minute comes out of the building time.
- Optional: once in a while, use the [weekly AI news template](../templates/weekly-ai-news.md) as the input instead of a unit. It has to fit into the same 10 minutes.

### Build

About 34 minutes in the 60-minute version, about 45 in the 75-minute version.

- In the first five minutes, every person has a task. Anyone without an idea picks one from the [idea list](../tracks/03-plan-first/02-product-sprint.md#idea-list).
- People build their own thing. Anchors help at their table.
- Nobody logs in with their own account for someone else, and nobody installs software on someone else's laptop.
- The host walks around, watches the clock and looks out for real data on screens.
- Five minutes before the end, remind everyone of the ritual: export or push, then open the second copy and look.

**When the unit is the exercise** ([find the personal data](../tracks/02-data-first/02-exercise-find-the-personal-data.md)): people work in pairs on the same file. Use the round as a debrief: each pair names one finding and says why it is personal data. Reveal the solution only at the end, so nobody reads ahead.

### Round (~8 or ~12 min)

A few people show what they built, three minutes each, without scrolling through code. How to run it: [show-and-tell.md](show-and-tell.md).

### Retro card (~5 min)

Everyone fills in three questions and hands in the card before leaving.

## When tools fail

Something will fail. Decide the fallback before the session, not in it.

| What fails | Fallback |
|---|---|
| A builder is down or out of credits | Switch to a chat assistant for today, or join a neighbour as the person who reads and checks |
| Someone cannot log in (no phone for 2FA, forgotten password) | Pair with someone at the table today. Fix the account at home with [Accounts and 2FA](../diy/01-accounts-and-2fa.md) |
| A CLI agent will not install | Use the browser lane today. Install at home with [Ready to build](../ready-to-build.md) |
| The network is slow or gone | Work on paper: answer the questions from the [spec interview](../tracks/03-plan-first/01-spec-interview.md) and write the spec by hand |
| The agent keeps getting it wrong | After two failed corrections, start a fresh chat with a better first prompt. See [Five failure patterns](../tracks/05-verify-and-loop/02-five-failure-patterns.md) |
| The usage limit is reached | Switch to another tool with a free tier, or review someone else's result with the [verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md) |
| Real data appears on a screen | Stop that person's work calmly, and follow [If something went wrong](../tracks/02-data-first/04-if-something-went-wrong.md). Thank them for noticing. |

## After the session

- Count the retro cards on the same day. Write down the numbers, not your memory of the mood.
- Pick one thing to change for the next session, based on the cards.
- Send the links to the unit and the templates, not slides.
- Send one invitation per session. Put the time you would spend on reminders into preparing the next unit.

## Data rule, once more

Repeat it every session: at the start, when you walk around, and in the invitation. Show only fake data in your own demo. A host who pastes a real customer e-mail "just to show it quickly" teaches the opposite of rule one.
