# Notes as a graph

| | |
|---|---|
| **Prerequisites** | [A vault and AGENTS.md](01-vault-and-agents-md.md) |
| **Time** | ~30 min |
| **Outcome** | You can connect related notes and ask an agent to find the project decisions without reading the whole folder. |
| **Last verified** | 2026-09-13 |

## Why this matters

Open your project note and add a link to a decision that explains how the project works. If the decision has no note yet, write a short one with invented details.

Connected notes form a **graph**: the notes are the items, and links show their relationships. An index gives you and the agent a place to start. You will connect a few notes and check whether the agent can follow them to answer a question.

## Do it

### 1. Link notes, with a reason (5 min)

There are two common link styles:

| Style | Works in |
|---|---|
| Wikilink | Obsidian and several other note apps |
| Markdown link | Every Markdown viewer, including code hosting sites |

This is what each style looks like inside a note:

```text
Wikilink:      [[learnings/export-before-deploy]]
Markdown link: [export before deploy](../learnings/export-before-deploy.md)
```

Pick one style per vault and stay with it. Agents can follow both.

A short reason helps the reader decide whether to follow a link:

- Weak: "See also [[learnings/export-before-deploy]]."
- Strong: "We export the data before every deploy because a deploy once reset the database, see [[learnings/export-before-deploy]]."

Rule of thumb: link when you would otherwise explain the same thing twice.

### 2. Build an index page (5 min)

An index page (often called a map of content) is a note that lists other notes, one line each. Create `index.md` at the top of the vault:

```markdown
# Index

## Projects
- [[projects/room-planner]]: booking tool for office assistants, in test with three users

## Decisions
- [[decisions/fake-data-only]]: why the test app never stores real bookings

## Learnings
- [[learnings/export-before-deploy]]: export data before every deploy
- [[learnings/first-restore-test]]: what the first restore test showed
```

Add one line to `AGENTS.md`: "Start at index.md and follow links. Do not read the whole vault unless I ask."

The paths above are examples. Create the notes you use, including `decisions/` if you keep that example, and remove entries for notes that do not exist. An index with working links helps keep the agent's context small; see [Context engineering](../08-advanced/01-context-engineering.md).

### 3. Add frontmatter (5 min)

**Frontmatter** is a small block of labelled fields at the top of a note, between two lines of `---`. Use it when you want to find notes by project, date or status. Obsidian shows these fields as [properties](https://help.obsidian.md/properties). You can ask an agent to find notes with matching fields.

```markdown
---
type: learning
status: active
project: room-planner
created: 2026-09-13
updated: 2026-09-13
---

# Export before deploy

A deploy reset the test database. Since then we export the data first.
```

Use the same field names across related notes. Try: "List all notes with `status: active` and `project: room-planner`." Check the returned files yourself.

### 4. Decide: graph or list?

Not everything needs links.

| Use a **list** when | Use a **graph** when |
|---|---|
| The order matters: to-dos, steps, a change log | Things relate across time: project, decision, learning |
| The notes are short-lived | You ask "why did we decide this?" months later |
| You ask "what is next?" | You ask "what is connected to this?" |
| One person reads it top to bottom | The agent should find context on its own |

A list inside a note is fine. A graph is what connects the notes.

### 5. Exercise: connect five notes (15 min)

1. Pick five notes from your vault. If you have fewer, write short ones now (fake project, one decision, three learnings).
2. Add the same frontmatter fields to all five.
3. Add them to `index.md`, one line each.
4. Add links where two notes are related and explain the connection. Do not invent a relationship to reach a link count.
5. Ask the agent, in Claude Code or Codex:

   ```text
   Start at index.md and follow links only.
   Which learnings apply to the room-planner project?
   Name the path of every note you opened.
   ```

6. Then ask:

   ```text
   Look only in this exercise folder for notes with no incoming links.
   Suggest links where a real connection exists and explain it.
   It is fine for a note to have no useful connection. Do not edit yet.
   ```

7. Accept only the links you agree with. The agent may suggest relations; you decide which are true.

If you use Obsidian, open the graph view to see the result. It is optional: the links work without it.

## Done when

- [ ] `index.md` exists and `AGENTS.md` tells the agent to start there.
- [ ] Five notes share the same frontmatter fields.
- [ ] Related notes have working links with reasons; unrelated notes are not forced together.
- [ ] The agent answered a question by following links and named every file it opened.
- [ ] You reviewed the agent's link suggestions and accepted only the true ones.

## Data note

Links make relations visible, and relations can be personal data too: "who decided what" is information about a person. Do not create notes about real colleagues, customers or contacts. Write decisions with roles ("the product owner decided"). The two hard rules from [A vault and AGENTS.md](01-vault-and-agents-md.md) apply to every note, link and field.

## Next

[Context engineering](../08-advanced/01-context-engineering.md)

Following a chosen path? Return to [START-HERE](../../START-HERE.md); the link above is the default track order.
