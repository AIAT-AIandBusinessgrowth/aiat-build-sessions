# If something went wrong

If you sent real data to an AI tool, stop the chat and tell your data protection contact today. These five steps help you limit further sharing and give that person the facts needed to respond.

| | |
|---|---|
| **Prerequisites** | [Schema first, then synthetic data](03-schema-then-synthetic-data.md) |
| **Time** | ~10 min |
| **Outcome** | Know what to stop, delete, record and report, and how to prevent the same mistake. |
| **Last verified** | 2026-09-13 |

## Why this matters

Real data can be easy to send by accident: a customer list in a screenshot, a pasted e-mail thread or the wrong spreadsheet.

Report promptly because your organisation may have a legal deadline. In the EU, an organisation must as a rule notify its data protection authority of a personal data breach within 72 hours after becoming aware of it, unless the breach is unlikely to put people at risk ([GDPR Article 33](https://eur-lex.europa.eu/eli/reg/2016/679/oj), checked 2026-09-13). Your organisation needs the facts to decide what to do.

## Do it

### Step 1: Stop

Do not continue the chat. Do not ask the tool to "forget" what you sent: asking deletes nothing. Do not share or forward the conversation.

### Step 2: Delete what you can

- Delete the chat or conversation.
- Delete uploaded files, and the project if the data is in it.
- Check whether the tool has a memory or saved-files section, and remove the data there too.
- **CLI lane or GitHub sync:** if the data went into a repository, make the repository private first. Deleting the file in a new commit does not remove it from the history. Say so in your report instead of trying to rewrite the history alone.

Deleting may not remove every vendor copy immediately. Note what you deleted and when.

### Step 3: Write down the facts, not the data

- **What:** the kind of data and a rough amount. For example: "customer list, about 200 rows, names and e-mail addresses, one notes column with health remarks".
- **When:** date and time.
- **Where:** which tool, which account, personal or business plan, model training on, off or unknown.
- **What you did:** what you deleted, and when.
- **Who else could see it:** nobody, a shared link, a public repository, a team workspace.

Your note describes the data. It never contains a copy of it.

### Step 4: Tell your data protection contact the same day

Tell your organisation's data protection contact today. If you do not know who that is, ask your manager or search your intranet for "data protection" or "privacy". If you work for yourself and the data belongs to a client, tell the client.

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

A prompt report gives your organisation time to assess the incident. If someone reports to you, thank them and help gather the facts. Blaming them can discourage future reports.

> **Not legal advice.** This is a first-aid routine. Your organisation's data protection contact decides what happens next, including whether anyone has to be notified.

## Done when

- [ ] I can list the five steps without looking.
- [ ] I know who my data protection contact is, or I know how to find out today.
- [ ] I saved the message template where I can find it quickly.

## Data note

Do not paste examples of the leaked data into your report, and do not paste them into another AI tool to "check how bad it is". That would be a second incident.

## Next

[Spec interview](../03-plan-first/01-spec-interview.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
