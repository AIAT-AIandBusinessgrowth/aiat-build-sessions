# SPEC: Room Board

> **How to use this template.** Fill in each section in short sentences, or let an agent interview you with the prompt from [Spec interview](../tracks/03-plan-first/01-spec-interview.md). The example values are invented. Replace them, keep the headings, and delete this note. One page is enough.

**One sentence:** For people who book shared meeting rooms, Room Board shows which rooms are free in the next two hours, instead of walking the floor to check.

<!-- Shape: For <who>, <name> does <what>, instead of <what happens today>. -->

## Problem

Finding a free room means walking from door to door or asking around. Rooms that are booked often stand empty, and people give up and meet in the kitchen.

<!-- Two or three sentences: what is annoying today, and for whom. -->

## Users

- First users: office assistants who plan rooms every week (role, no names).
- Later: anyone on the floor who needs a room at short notice.

## IN

1. A list of all rooms.
2. Free or busy for the next two hours.
3. A filter by room size.

<!-- The three things it must do. Not more. -->

## OUT

1. Booking rooms.
2. Calendar sync.
3. Logins and user accounts.

<!-- At least three items. At least one of them should hurt a little. -->

## Data (fake)

| Field | Type | Values |
|---|---|---|
| `room_id` | text | R-01 to R-12 |
| `room_name` | text | invented names, such as "Blue Room" |
| `seats` | whole number | 2 to 20 |
| `busy_from` | time | 08:00 to 18:00 |
| `busy_until` | time | after `busy_from` |
| `contact` | text | role address, such as `rooms@example.com` |

Sample rows are invented. No real names, no real addresses, no real bookings.

<!-- Field names, types and value ranges only. Never paste a real row. -->

## Done when

With the 12 fake rooms in `data/fake-rooms.csv`, the page shows the correct free rooms for any time I type in.

<!-- Something you can see or click, not a feeling. -->

## Open questions

- Should a room count as free if it is booked for only 10 of the next 120 minutes?
- Who updates the room list when a room is renovated?

<!-- "I don't know yet" belongs here. An empty list usually means someone guessed. -->

## First three tasks

| # | Task | Done when |
|---|---|---|
| 1 | Create `data/fake-rooms.csv` with 12 invented rooms and bookings | The file opens and every contact address ends in `example.com` |
| 2 | Show the room list with free or busy for the next two hours | For three times I type in, the page matches the sample file |
| 3 | Add the filter by room size | Choosing "6 or more seats" hides every smaller room |

<!-- Each task fits into one afternoon and has its own "done when" line. -->
