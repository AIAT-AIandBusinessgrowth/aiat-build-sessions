# Rule one: no real data

| | |
|---|---|
| **Prerequisites** | None. If you have not read it yet, start with [START-HERE](../../START-HERE.md). |
| **Time** | ~10 min |
| **Outcome** | After this unit you can tell which data may go into an AI tool on a personal plan, spot personal data that has no name on it, and ask the agent for fake data instead. |
| **Last verified** | 2026-09-13 |

## Why this matters

You will type things into AI tools from the first minute. Everything you type, paste or upload leaves your computer and goes to the vendor of the tool.

Most people who learn with this material use a personal plan: a free or paid account in their own name. That account is a contract between you and the vendor. Your organisation is not part of it. So there is no data processing agreement between your organisation and the vendor that covers what you put in, and your organisation cannot allow you to put its customer, staff or partner data there. [Data processing agreements](../../diy/03-data-processing-agreements.md) explains what such an agreement is and which kinds of plans offer one.

Many consumer plans also use your input to improve their models unless you switch that off. Which tool does what, with sources, is in the [tool matrix](../../diy/tool-matrix-2026-09.md).

That is why rule one comes before any tool.

## Do it

**Rule one for these exercises: use invented data or public data that is not about people. Keep real personal and customer data out, including your own personal information.**

### 1. Know which data belongs in a learning exercise (2 min)

- **Fake data.** Invented for the purpose: "Jordan Sample, jordan.sample@example.com".
- **Public data that is not about people.** Opening hours of a public library, published statistics, a public holiday calendar. A person's public profile is still personal data.
- **For a personal example, invent it too.** A fictional shopping list teaches the same skill without sending your own personal details. A team holiday plan contains data about other people and stays out.

Never names, e-mail addresses, customer files, contracts, health or HR data of other people. Not even "just to test".

### 2. Spot personal data, also without a name (3 min)

Personal data is any information about a person who can be identified, directly or together with other information ([GDPR Article 4](https://eur-lex.europa.eu/eli/reg/2016/679/oj)).

| Kind | Examples |
|---|---|
| Direct | name, e-mail address, phone number, home address, photo, ID card number, bank account number |
| Indirect | customer number, loyalty card number, IP address, licence plate, device ID, a hashed e-mail address |
| Combinations | date of birth plus postcode, a rare job title plus a small town, "the only night-shift nurse on ward 3" |
| Hidden | free-text notes, file names like `jordan-sample-passport.jpg`, screenshots, e-mail signatures |

Data about a company (a limited company's switchboard number, its registered address) is usually not personal data. Data about a sole trader, whose business carries their own name, is.

### 3. Know the special categories (2 min)

Some personal data gets extra protection. [GDPR Article 9](https://eur-lex.europa.eu/eli/reg/2016/679/oj) lists:

- racial or ethnic origin
- political opinions
- religious or philosophical beliefs
- trade union membership
- genetic data, and biometric data used to identify someone
- health data
- data about sex life or sexual orientation

These rarely sit in a column called "religion". They hide in notes: "off sick after surgery", "union rep", "no meetings on Friday afternoons for prayers".

Also keep out, even though they are not on that list: salaries and performance reviews, data about children, criminal records, bank and card details, passwords and API keys ([secrets and keys](../../diy/07-secrets-and-keys.md)).

### 4. Ask the agent for fake data (2 min)

Generating fake data is part of the skill, not a workaround. Keep this prompt ready and paste it whenever you need sample data:

```text
Create 10 rows of sample data for <what your app is about>.
All people and companies must be obviously fictional.
E-mail addresses must end in @example.com.
Phone numbers must be clearly invalid, for example +00 555 0101.
Do not use real towns, real companies or real people.
```

`example.com` and the `.example` ending are reserved for examples ([RFC 2606](https://www.rfc-editor.org/rfc/rfc2606)), so no real person owns an address there.

### 5. Switch training off (1 min)

In every tool you use, look for the setting that lets the vendor use your chats to improve its models, and switch it off where the option exists. To find it, check the vendor's privacy settings page (linked in the [tool matrix](../../diy/tool-matrix-2026-09.md)). Write down for each tool: off, on, or no option.

### When your real work needs real data

Not with a personal plan, and not in these tracks. Real data needs a tool your organisation has approved, usually with a business plan and a data processing agreement. Talk to your organisation's data protection contact before, not after.

> **Not legal advice.** This is a working rule for learning. The EU General Data Protection Regulation (GDPR) serves as the reference; many other countries have similar rules. When in doubt, ask your organisation's data protection contact, not an AI tool.

## Done when

- [ ] I can explain which invented or non-personal public data fits the exercise, and why personal information stays out.
- [ ] I can name five examples of personal data that do not contain a name.
- [ ] I can name at least four special categories, or I know where to look them up.
- [ ] I switched model training off (or noted "no option") in the tool I will use first.
- [ ] I saved the fake-data prompt where I can paste it.

## Data note

This unit is the data note for all other units. Each of them repeats it in a line or two, because the habit matters more than the rule.

## Next

[Pick your lane](02-pick-your-lane.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
