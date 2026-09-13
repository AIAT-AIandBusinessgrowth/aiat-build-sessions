# MVP: Room Board

> **How to use this template.** The MVP is the smallest version that is useful to someone other than you. Fill it in after your [spec](SPEC.md), or let an agent draft it and then cut half of the IN list. Background: [From prototype to product](../tracks/06-keep-and-ship/02-prototype-to-product.md). The example values are invented. Replace them and delete this note.

**One sentence:** For office assistants who plan rooms every week, Room Board shows which rooms are free in the next two hours, instead of walking the floor to check.

## Smallest useful version

One page that lists the rooms and marks each one free or busy for the next two hours, from a fake sample file.

<!-- What is the least it must do so that one real user would use it next week? -->

## Scope

**IN** (three to five things it does)

1. List all rooms.
2. Show free or busy for the next two hours.
3. Filter by room size.

**OUT** (at least three things it deliberately does not do)

1. Booking rooms.
2. Calendar sync.
3. Logins.
4. A mobile app.

<!-- The OUT list matters more. It stops the product from growing in every direction. -->

**Stop date:** YYYY-MM-DD

<!-- This version is finished on this date, even if not everything is done. Open items go to the task list. -->

## First users

| Role | What they do today | Why they will try it |
|---|---|---|
| Office assistant | Plans rooms every Monday from a spreadsheet | Saves the Monday walk around the floor |
| Team member | Asks around for a free room | Wants a room in the next hour |

At least one user who is not you. Names and contact details stay in your private notes, not in this file.

## How you know it works

- **Check before users:** with the fake file `data/fake-rooms.csv`, the page shows the correct free rooms for three times you type in.
- **Check with users:** three people from the table above use it with fake data for 15 minutes each, without your help.
- **Signal after two weeks:** at least one of them opens it again without being asked.

<!-- Something you can observe, not a feeling. -->

## Feedback path

- Where to report: `<issue tracker, form or shared document>`
- What to include: what you tried, what happened, what you expected.
- Who reads it, and how often: `<role>`, every `<day>`.
