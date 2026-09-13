# If something went wrong

| | |
|---|---|
| **Prerequisites** | [Schema first, then synthetic data](03-schema-then-synthetic-data.md) |
| **Time** | ~10 min |
| **Outcome** | After this unit you can take five steps on the same day when real data went into an AI tool, and explain why reporting is better than hiding. |
| **Last verified** | 2026-09-13 |

## Why this matters

It happens to careful people: a screenshot with a customer list in the background, a pasted e-mail thread, a spreadsheet dragged into the chat out of habit.

How much damage follows often depends less on the mistake than on the next few hours. Organisations can have legal deadlines. In the EU, an organisation must as a rule notify its data protection authority of a personal data breach within 72 hours after becoming aware of it, unless the breach is unlikely to put people at risk ([GDPR Article 33](https://eur-lex.europa.eu/eli/reg/2016/679/oj), checked 2026-09-13). Your organisation can only decide what to do if it knows. If you stay silent, it cannot act.

## Do it

### Step 1: Stop

Do not continue the chat. Do not ask the tool to "forget" what you sent: asking deletes nothing. Do not share or forward the conversation.

### Step 2: Delete what you can

- Delete the chat or conversation.
- Delete uploaded files, and the project if the data is in it.
- Check whether the tool has a memory or saved-files section, and remove the data there too.
- **CLI lane or GitHub sync:** if the data went into a repository, make the repository private first. Deleting the file in a new commit does not remove it from the history. Say so in your report instead of trying to rewrite the history alone.

Deleting may not remove every copy at the vendor right away. Delete anyway, and note the time.

### Step 3: Write down the facts, not the data

- **What:** the kind of data and a rough amount. For example: "customer list, about 200 rows, names and e-mail addresses, one notes column with health remarks".
- **When:** date and time.
- **Where:** which tool, which account, personal or business plan, model training on, off or unknown.
- **What you did:** what you deleted, and when.
- **Who else could see it:** nobody, a shared link, a public repository, a team workspace.

Your note describes the data. It never contains a copy of it.

### Step 4: Tell your data protection contact the same day

Tell your organisation's data protection contact today, not after the weekend. If you do not know who that is, ask your manager or search your intranet for "data protection" or "privacy". If you work for yourself and the data belongs to a client, tell the client.

A message you can adapt:

```text
Subject: Possible data incident with an AI tool, <date>

Today at <time> I put <kind of data, rough amount> into <tool>,
using my <personal / business> account. Model training was <on / off / unknown>.

At <time> I deleted <the chat / the file / the project>
<and made the repository private>.

Other people who could have seen it: <nobody / a shared link / a public repository>.
I have not copied the data anywhere else.

Please tell me what else I should do.
```

### Step 5: Find the cause, not the culprit

Write one sentence for yourself: what made this easy to happen? For example: "The real export was in my Downloads folder, next to the sample data, with a similar name." Then change that one thing.

### Report instead of hide

A report that turns out to be harmless costs your data protection contact ten minutes. An incident that someone finds months later costs trust, and it can cost the organisation much more.

Nobody should be blamed for reporting. If someone reports to you, thank them first and ask questions second. People who get blamed for a report stop reporting, and the mistakes do not stop with them.

> **Not legal advice.** This is a first-aid routine. Your organisation's data protection contact decides what happens next, including whether anyone has to be notified.

## Done when

- [ ] I can list the five steps without looking.
- [ ] I know who my data protection contact is, or I know how to find out today.
- [ ] I saved the message template where I can find it quickly.

## Data note

Do not paste examples of the leaked data into your report, and do not paste them into another AI tool to "check how bad it is". That would be a second incident.

## Next

[Spec interview](../03-plan-first/01-spec-interview.md)
