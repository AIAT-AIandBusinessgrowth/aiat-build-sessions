# Solution on one page

[Exercise](README.md) · [Full solution with reasons and fixes](solution.md)

**28 traps:** 9 whole columns, 19 single findings. Six rows have no single-cell findings; the whole-column findings still apply to them.

## Whole columns (9)

- [ ] **A1 `company`**: sole-trader businesses carry the owner's full name
- [ ] **A2 `email`**: addresses with first or full names
- [ ] **A3 `phone`**: a sole trader's number reaches one person
- [ ] **A4 `street`, `town`**: often a home address ("Flat 2", "The Old Barn")
- [ ] **A5 `date_of_birth`**: only people have one; identifies in combination
- [ ] **A6 `customer_id`**: loyalty card number is also the app login, so it links to a person
- [ ] **A7 `email_sha256`**: a hash can be recomputed from the address; pseudonymous, still personal data
- [ ] **A8 `last_login_ip`**: online identifier
- [ ] **A9 `photo_file`**: names in file names; photos and ID scans behind them

## Single findings (19)

| # | Row | What | Kind |
|---|---|---|---|
| B1 | CARD-104202 | national ID number from a passport | official identifier |
| B2 | CARD-104203 | "Kim Testperson" in notes | name in free text |
| B3 | CARD-104203 | off sick after back surgery | health (special category) |
| B4 | CARD-104204 | licence plate of the owner | indirect identifier |
| B5 | CARD-104204 | union rep | trade union (special category) |
| B6 | CARD-104205 | e-mail deleted, hash kept | pseudonymous, deletion not done |
| B7 | CARD-104206 | retired harbour master, small village, birth date | quasi-identifier |
| B8 | CARD-104206 | IBAN in notes | financial |
| B9 | CARD-104208 | type 1 diabetic | health (special category) |
| B10 | CARD-104208 | photo "with kids" | children |
| B11 | CARD-104209 | no Saturdays for religious reasons | religion (special category) |
| B12 | CARD-104210 | helpdesk ticket reference | link to another system |
| B13 | CARD-104211 | pregnant, due date | health (special category) |
| B14 | CARD-104213 | partner's name and private phone | third person |
| B15 | CARD-104215 | town council seat for a party | political opinion (special category) |
| B16 | CARD-104217 | personal bankruptcy | financial |
| B17 | CARD-104218 | van licence plate | indirect identifier |
| B18 | CARD-104218 | IBAN in notes | financial |
| B19 | CARD-104220 | ID card scan and ID number for an age check | official identifier |

## Rows without single-cell findings (6)

CARD-104201, 104207, 104212, 104214, 104216, 104219: limited companies and shops, role mailboxes, business facts only in the notes. The whole-column findings above still apply to these rows.

## Three things to remember

1. **Deleting the name column is not anonymisation.** IDs, hashes, notes, file names and combinations still point to people.
2. **The special categories hide in free text.** Nobody writes a column called "religion".
3. **Do not clean better, upload nothing.** Take the structure, invent the rows: [Schema first, then synthetic data](../../tracks/02-data-first/03-schema-then-synthetic-data.md).
