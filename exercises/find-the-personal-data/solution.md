# Solution: find the personal data

Back to the [exercise](README.md) · [one-page version](solution-short.md)

The file has **28 traps**: 9 whole columns (part A) and 19 single findings, mostly in the notes (part B). Part C lists what is *not* personal data, part D what real spreadsheets can hide that a CSV cannot.

Rows are named by `customer_id`. "Sole-trader rows" means the ten rows whose company carries a person's name: CARD-104202, 104205, 104208, 104209, 104211, 104213, 104215, 104217, 104218 and 104220.

> **Not legal advice.** GDPR terms and articles are used as the reference ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)). The exercise is about seeing, not about legal judgement.

## Part A: whole columns (9)

| # | Column | Why it is personal data | What to do instead |
|---|---|---|---|
| A1 | `company` | In the sole-trader rows the business name is the owner's full name, for example "Jordan Sample Plumbing". Data about a sole trader is data about a person. "Harbour Bakery Ltd" is a company, not a person. | For building, the agent needs "company name: text". Invent the names. |
| A2 | `email` | Nine addresses contain a first name or a full name, for example `jordan.sample@example.com` and `casey@mockridge-tutoring.example`. Role mailboxes such as `orders@` are usually not personal data, but you cannot tell safely without checking every row. | Invent addresses ending in `@example.com`. |
| A3 | `phone` | For a sole trader, the business number reaches one person. | Invent clearly invalid numbers. |
| A4 | `street`, `town` | For sole traders the delivery address is often the home address. "Flat 2, 18 Lens Street" (CARD-104211) and "The Old Barn, Little Dummyfield" (CARD-104213) are obviously homes. | Invent addresses. If the app needs regions, use a region code, not a street. |
| A5 | `date_of_birth` | Only people have a birth date, so every filled cell marks a row about a person. Together with town and job title it can identify someone without a name. | Leave it out. If age matters, use an age band such as "40-49". |
| A6 | `customer_id` | The loyalty card number is also the login for the order app. Anyone with access to the app, or holding the card, can connect the row to a person. That makes it a pseudonymous identifier, and pseudonymous data is personal data (GDPR Recital 26). | Invent new IDs. Never reuse real IDs as keys in test data. |
| A7 | `email_sha256` | A hash is not encryption. The same address always gives the same hash, so anyone with a list of addresses can compute the hashes and compare. Try it: `python3 -c "import hashlib; print(hashlib.sha256(b'jordan.sample@example.com').hexdigest())"` and compare the result with row CARD-104202. This is pseudonymisation (GDPR Article 4(5)), not anonymisation. | Leave it out. If you need a key, use an invented running number that is not derived from the address. |
| A8 | `last_login_ip` | IP addresses are online identifiers (GDPR Recital 30). Together with the internet provider's records they point to a connection, often a home. | Leave it out, or use documentation addresses such as `192.0.2.1`. |
| A9 | `photo_file` | `jordan-sample-passport.jpg`, `IMG_robin-dummy-with-kids.png`, `taylor-fakename-headshot.jpg` and `parker-mockup-id-card-scan.pdf` contain names. The files behind them are photos of people and identity documents. | Generic file names such as `attachment-001.jpg`. Do not store copies of identity documents in a sales list at all. |

## Part B: single findings (19)

| # | Row | Column | What | Why it is personal data | What to do instead |
|---|---|---|---|---|---|
| B1 | CARD-104202 | `notes` | National ID number `NID-FAKE-19850312-0042`, copied from a passport | An official identifier. Many real ID formats contain the date of birth, as this one does (it matches `date_of_birth`). Many countries protect national ID numbers specially (GDPR Article 87). | Never in a customer list. A credit check does not need a copy of the number in the notes. |
| B2 | CARD-104203 | `notes` | "Contact Kim Testperson" | The company row looks harmless, but the note names a person. Direct identifier in free text. | "Send invoices to the office." No name needed. |
| B3 | CARD-104203 | `notes` | "off sick after back surgery" | Health data, a special category (GDPR Article 9). | "Contact unavailable until end of month." The reason is nobody's business. |
| B4 | CARD-104204 | `notes` | Licence plate `XX-TEST-42` of "the owner" | A licence plate points to the registered keeper, here a named role with a date of birth. | Leave it out. |
| B5 | CARD-104204 | `notes` | "Union rep for the local drivers" | Trade union membership, a special category (Article 9). | Leave it out. |
| B6 | CARD-104205 | `email`, `email_sha256`, `notes` | E-mail deleted on request, hash kept "to recognise her" | The hash still identifies her (see A7), so the deletion request was not really carried out. The note also reveals the reason for keeping it. | Delete means delete: the hash goes too. |
| B7 | CARD-104206 | `job_title`, `town`, `date_of_birth` | "Retired harbour master" in "Little Dummyfield", born 1962-05-30 | No name, but a small village has one retired harbour master. A rare job title plus a small place plus a birth date is a quasi-identifier. | Generalise ("retired", region instead of village) or leave out. |
| B8 | CARD-104206 | `notes` | IBAN `XX00 0000 1234 5678 90` | A bank account belongs to a person or a small business and links to their bank. Financial data. (The `XX` country code is invalid on purpose.) | Bank details belong in the payment system, not in free text. |
| B9 | CARD-104208 | `notes` | "Type 1 diabetic" | Health data, special category (Article 9). | "Prefers morning appointments." The preference is enough. |
| B10 | CARD-104208 | `photo_file` | `IMG_robin-dummy-with-kids.png` | A photo of children. Children's data needs extra care (GDPR Recital 38). | Do not store private photos with a customer record. |
| B11 | CARD-104209 | `notes` | "No bookings on Saturdays for religious reasons" | Reveals religious belief, special category (Article 9). | "No bookings on Saturdays." |
| B12 | CARD-104210 | `notes` | "Same customer as ticket HD-55821 in the helpdesk tool" | The company itself is not a person, but the reference links this row to another system, where tickets usually contain the name, e-mail and message of whoever called. | No cross-references to other systems in exported or test data. |
| B13 | CARD-104211 | `notes` | "Pregnant, due in November" | Health data, special category (Article 9), with a date that makes it more precise. | "Fewer bookings until end of November." |
| B14 | CARD-104213 | `notes` | Partner "Morgan Lorem" with a private number, "call her privately" | Data about a third person who is not even a customer: name, relationship, private phone. | Leave it out. Use the business contact only. |
| B15 | CARD-104215 | `notes` | "Sits on the town council for a local party" | Political opinion, special category (Article 9). A public office can be public knowledge, but copying it into a sales file and adding "do not send political flyers" is still processing it. | Leave it out. |
| B16 | CARD-104217 | `notes` | "personal bankruptcy last year" | The financial situation of a named person (the company carries the owner's name). | "Pays in instalments." Facts about the account, not about the person's life. |
| B17 | CARD-104218 | `notes` | Van plate `XX-DEMO-7` | Licence plate of a sole trader's van: points to the owner. | Leave it out. |
| B18 | CARD-104218 | `notes` | IBAN `XX99 9999 0000 1111 22` | Bank account of a sole trader: financial data about a person. | Payment system, not notes. |
| B19 | CARD-104220 | `notes` | ID card scan for an age check, ID `NID-FAKE-19871010-0917` | A national ID number plus a copy of the ID document, for a check that needs only one yes or no. | Record "age checked: yes" and the date. Keep neither the number nor the scan. |

## Part C: what is not personal data

Rows CARD-104201, 104207, 104212, 104214, 104216 and 104219 describe limited companies or shops: role mailboxes such as `orders@`, a shop address, notes like "Pays on time" or "Monthly order". Business data about a company is usually not personal data.

This matters. If everything is flagged, people stop taking the rule seriously. The skill is to see the difference, and when you cannot tell, to treat the row as personal data.

Even these rows would not go into an AI tool as real data: they sit in the same file as the other fourteen, and nobody separates them reliably before an upload.

## Part D: what real files can hide that this CSV cannot

A CSV file is plain text, so everything is visible. Real spreadsheets can also carry:

- hidden tabs and hidden columns
- cell comments
- document properties: author, company, "last saved by"
- earlier versions in the version history
- embedded images and screenshots

Checking all of that before every upload is the part people skip under time pressure.

## The lesson

28 traps in 20 rows, in a file someone called "anonymised". The answer is not to clean real files more carefully before every prompt. The answer is a different order:

1. Take only the structure: column names and types, no values ([extract-schema.py](extract-schema.py) does this without printing a single value).
2. Let the agent invent rows that fit the structure.
3. Build and test with the invented rows.

You cannot leak data you never uploaded. Continue with [Schema first, then synthetic data](../../tracks/02-data-first/03-schema-then-synthetic-data.md).

**How did you do?** 0 to 10: normal for a first look. 11 to 18: a good eye. 19 or more: very thorough. In every case, the next unit is the safer path.
