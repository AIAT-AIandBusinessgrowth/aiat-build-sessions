# Run a Build Session

Choose one small task for people to try together. This page helps you prepare the room, activity and backup plan for a team, class or meetup. Start with one session; repeat it if useful. For an app build, people need a suitable tool and laptop. The [paper exercise](../learning/README.md) also works without either.

## What a Build Session is

People use AI to build or improve a small tool, with time to try it themselves. The host shows one example, then helps people get started. Keep explanations short enough that most of the session is spent practising.

## Two formats

Two suggested formats help you choose suitable activities. **Start** is for people new to building with AI: a browser exercise, then a first small app with fake data. **Ship** is for people preparing a tool for others to use: the input comes from [Keep and ship](../tracks/06-keep-and-ship/01-keep-your-work-safe.md), [Verify and loop](../tracks/05-verify-and-loop/01-verification-ladder.md) and the [PoC to production checklist](../tracks/08-advanced/06-poc-to-production-checklist.md), and the build time goes into each person's own product. Use separate sessions when the groups need different help. These format names do not enrol anyone in an internal working group.

## The format: 60 to 75 minutes

| Block | 60 min version | 75 min version | What happens |
|---|---|---|---|
| Start and rule one | ~3 min | ~3 min | Welcome, the data rule, today's unit |
| Input | 10 min at most | 10 min at most | One idea from one unit, shown live in a tool. One prompt to copy. |
| Build | ~34 min | ~45 min | Everyone works on their own thing, at tables of 4 to 5 |
| Round | ~8 min | ~12 min | Show and tell: a few people show what they built |
| Retro card | ~5 min | ~5 min | Three optional questions on a card; learners choose whether to hand it in |
| **Total** | **60 min** | **75 min** | |

A fill-in agenda for both versions is in [session-skeleton.md](session-skeleton.md). With more time, make the build block longer, never the input.

## A suggestion for ten weeks

Use this as an example sequence, not a published schedule. Change it when people need different practice. The input shows one idea from the listed units; people read the rest on their own.

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

Check the necessary setup before the session. If someone cannot get access in time, have a paper task or paired activity ready so they can still take part.

- [ ] Before the first session: clear the use of personal AI plans with your organisation's IT or data protection contact.
- [ ] Send one invitation per session: topic, time, what to bring, and the link to [ready-to-build.md](../ready-to-build.md). Ask people to do only the setup their chosen activity needs before they come. A fill-in text is in the [invitation template](../templates/invitation.md).
- [ ] Explain how accounts, licences and hosting are arranged by participants or their organisation. Say where to get help with access; the public course does not provide accounts or a help desk. The [Do it yourself guides](../diy/01-accounts-and-2fa.md) help.
- [ ] Pick one unit for the input, for example from the [suggestion for ten weeks](#a-suggestion-for-ten-weeks). Do it yourself once, in a browser tool and, if people use one, in a CLI agent.
- [ ] Copy the one prompt people should start with into a place everyone can reach: a shared note, a slide with only that prompt, or a printout.
- [ ] Find one table anchor per table: someone who has tried the activity and can help others get unstuck. See [table-anchor.md](table-anchor.md). **No experienced anchors?** Host plus pairs works: people work in twos and the host walks around. An anchor should try today’s activity and its necessary [setup](../ready-to-build.md) beforehand.
- [ ] Print retro cards: [retro card template](../templates/retro-card.md). Optional: [show-and-tell cards](../templates/show-and-tell-card.md), [weekly AI news](../templates/weekly-ai-news.md) as an input.
- [ ] Prepare the fallbacks below.

## During the session

### Start and rule one (~3 min)

Remind people of the data rule before they use a tool. For example:

> "Rule one, as every time: fake data only. No real names, no customer files, no screenshots with real data, not even to test. If your task needs real data, describe the columns and let the agent invent the rows."

Details: [Rule one: no real data](../tracks/00-orientation/01-rule-one-no-real-data.md). If real data ends up in a tool anyway: [If something went wrong](../tracks/02-data-first/04-if-something-went-wrong.md).

### Input (10 minutes at most)

- One idea, one example, one prompt. Show it live in a tool. If something goes wrong, use it to show how you check and recover; you do not need to create a failure.
- Link the unit so people can read the rest on their own.
- Finish within 10 minutes and leave time for people to try it. Put further explanation in the linked lesson.
- Optional: once in a while, use the [weekly AI news template](../templates/weekly-ai-news.md) as the input instead of a unit. It has to fit into the same 10 minutes.

### Build

About 34 minutes in the 60-minute version, about 45 in the 75-minute version.

- In the first five minutes, every person has a task. Anyone without an idea picks one from the [idea list](../tracks/03-plan-first/02-product-sprint.md#idea-list).
- People build their own thing. Anchors help at their table.
- Nobody logs in with their own account for someone else, and nobody installs software on someone else's laptop.
- The host walks around, watches the clock and looks out for real data on screens.
- Five minutes before the end, ask everyone to save a second copy by export or push, then open it and check the latest change.

**When the unit is the exercise** ([find the personal data](../tracks/02-data-first/02-exercise-find-the-personal-data.md)): people work in pairs on the same file, without AI. Discuss the answers with people, not an agent. Use the round as a debrief: each pair names one finding and says why it is personal data. Reveal the solution only at the end, so nobody reads ahead.

### Round (~8 or ~12 min)

A few people show what they built, three minutes each, without scrolling through code. How to run it: [show-and-tell.md](show-and-tell.md).

### Retro card (~5 min)

Offer three questions on a card. Learners may keep their answers, share one point or hand in the card; participation is optional.

## When tools fail

Something will fail. Decide the fallback before the session, not in it.

| What fails | Fallback |
|---|---|
| A builder is down or out of credits | Switch to a chat assistant for today, or join a neighbour as the person who reads and checks |
| Someone cannot log in (no phone for 2FA, forgotten password) | Pair with someone at the table today. Fix the account at home with [Accounts and 2FA](../diy/01-accounts-and-2fa.md) |
| A CLI agent will not install | Use the browser lane today. Install at home with [Ready to build](../ready-to-build.md) |
| The network is slow or gone | Work on paper: answer the questions from the [spec interview](../tracks/03-plan-first/01-spec-interview.md) and write the spec by hand |
| The agent keeps getting it wrong | After two failed corrections, save the current attempt and note what last worked, what failed and what to try next. Start a fresh chat with that note. See [Five failure patterns](../tracks/05-verify-and-loop/02-five-failure-patterns.md) |
| The usage limit is reached | Switch to another tool with a free tier, or review someone else's result with the [verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md) |
| Real data appears on a screen | Stop that person's work calmly, and follow [If something went wrong](../tracks/02-data-first/04-if-something-went-wrong.md). Thank them for noticing. |

## After the session

- Read the feedback cards on the same day. Note where people got stuck and what helped, without putting participant details in this public repository.
- Pick one thing to change for the next session, based on the cards.
- Send the links to the unit and the templates, not slides.
- For a next session, send a clear invitation with its activity and any preparation people need.

## Data rule, once more

Repeat it every session: at the start, when you walk around, and in the invitation. Show only fake data in your own demo. A host who pastes a real customer e-mail "just to show it quickly" teaches the opposite of rule one.
