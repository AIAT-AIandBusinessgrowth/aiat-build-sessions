# MVP: Room Board

> **How to use this template.** List what someone needs to try the main job with your tool. This is your MVP, the smallest useful version. Use your [spec](SPEC.md) or ask an agent to draft it. Leave out work only when the main job still works without it. The examples below are invented plans, not completed checks. Replace them and delete this note. Background: [From prototype to product](../tracks/06-keep-and-ship/02-prototype-to-product.md).

**One sentence:** For office assistants who plan rooms every week, Room Board shows which rooms are free in the next two hours, instead of walking the floor to check.

## Smallest useful version

One page that lists the rooms and marks each one free or busy for the next two hours, from a fake sample file.

<!-- What is the least it must do so that one real user would use it next week? -->

## Scope

**IN** (what this version needs to do; the three items below are examples)

1. List all rooms.
2. Show free or busy for the next two hours.
3. Filter by room size.

**OUT** (related work left for another version, if any)

1. Booking rooms.
2. Calendar sync.
3. Logins.
4. A mobile app.

<!-- Keep required work in IN. Do not invent exclusions to reach a count. -->

**Stop date:** YYYY-MM-DD

<!-- On this date, review what is ready and what remains open. A date does not make unfinished work complete. Save open items with their next step. -->

## First users

| Role | What they do today | Why they will try it |
|---|---|---|
| Office assistant | Plans rooms every Monday from a spreadsheet | Saves the Monday walk around the floor |
| Team member | Asks around for a free room | Wants a room in the next hour |

Choose someone other than you who has the problem. Names and contact details stay in approved private notes, not in this file. Until someone tries the tool, the reasons above are assumptions to check.

## How you know it works

- **Check before users:** compare the page with `data/fake-rooms.csv` for three example times, including a booking that starts or ends at the chosen time. Result: `<not yet tried / date and what happened>`.
- **Check with users:** ask people with the problem to try the main task using fake data. Three people for 15 minutes each is an exercise target; start with one if that is who is available. Result: `<not yet tried / date and what happened>`.
- **Follow-up:** after two weeks, check whether testers used it again and what for. Result: `<not yet checked / what happened>`. A lack of repeat use is useful information too.

<!-- Something you can observe, not a feeling. -->

## Feedback path

- Where to report: `<issue tracker, form or shared document>`
- What to include: what you tried, what happened, what you expected.
- Who reads it, and how often: `<role>`, every `<day>`.
