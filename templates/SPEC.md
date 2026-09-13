# SPEC: Room Board

> **How to use this template.** Describe one task the tool should help someone do, then write how you will check it. A spec is that written description. Use short sentences, or try the interview in [Spec interview](../tracks/03-plan-first/01-spec-interview.md). Replace the invented examples, keep the headings and delete this note. Use the space the task needs; one page is a useful starting point.

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

<!-- List the required behaviour. Three items are shown as an example, not a limit. -->

## OUT

1. Booking rooms.
2. Calendar sync.
3. Logins and user accounts.

<!-- Related tasks left out of this version, if any. Do not remove required behaviour just to shorten the list. -->

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

With the 12 fake rooms in `data/fake-rooms.csv`, the page shows which rooms are free for the requested two-hour period. Compare it with the sample bookings, including a booking that starts or ends at the chosen time. Resolve the overlap question below before building the calculation.

<!-- Something you can see or click, not a feeling. -->

## Open questions

- Should a room count as free if it is booked for only 10 of the next 120 minutes?
- Who updates the room list when a room is renovated?

<!-- Keep unanswered questions here. Resolve any that change the required behaviour before building it. If there are none, say so. -->

## First three tasks

| # | Task | Done when |
|---|---|---|
| 1 | Create `data/fake-rooms.csv` with 12 invented rooms and bookings | The file opens and every contact address ends in `example.com` |
| 2 | Show the room list with free or busy for the next two hours | For three times I type in, the page matches the sample file |
| 3 | Add the filter by room size | Choosing "6 or more seats" hides every smaller room |

<!-- These are planned tasks, not completed work. Keep each small enough to check separately. A first afternoon is an example size, not a deadline. -->
