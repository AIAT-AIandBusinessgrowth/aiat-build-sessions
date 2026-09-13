# Notes as a graph

| | |
|---|---|
| **Prerequisites** | [A vault and AGENTS.md](01-vault-and-agents-md.md) |
| **Time** | ~30 min |
| **Outcome** | After this unit you can link notes with a reason, build an index page, add frontmatter an agent can filter, and decide when a graph works better than a list. |
| **Last verified** | 2026-09-13 |

## Why this matters

A folder of notes grows into a pile. After fifty notes you no longer find the decision you made in the spring, and the agent reads everything to answer a small question.

Links turn the pile into a **graph**: a project links to its decisions, a decision links to the learning that caused it. You and the agent can follow the links instead of searching. An index page gives both of you a place to start, which also keeps the agent's context small (see [Context engineering](../08-advanced/01-context-engineering.md)).

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

A link is only useful with a reason in the same sentence:

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

### 3. Add frontmatter (5 min)

Frontmatter is a small block of fields at the very top of a note, between two lines of `---`. Obsidian shows these fields as [properties](https://help.obsidian.md/properties). Agents can filter by them.

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

Keep the field list short and the same across notes. Five fields you always fill beat fifteen you sometimes fill. Then you can ask: "List all notes with `status: active` and `project: room-planner`."

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
4. Give each note two or more links, each with a reason in the sentence.
5. Ask the agent, in Claude Code or Codex:

   ```text
   Start at index.md and follow links only.
   Which learnings apply to the room-planner project?
   Name the path of every note you opened.
   ```

6. Then ask:

   ```text
   List notes that no other note links to. Suggest one link for each,
   with a reason. Do not change any file yet.
   ```

7. Accept only the links you agree with. The agent may suggest relations; you decide which are true.

If you use Obsidian, open the graph view to see the result. It is optional: the links work without it.

## Done when

- [ ] `index.md` exists and `AGENTS.md` tells the agent to start there.
- [ ] Five notes share the same frontmatter fields.
- [ ] Each of the five notes has two or more links with a reason.
- [ ] The agent answered a question by following links and named every file it opened.
- [ ] You reviewed the agent's link suggestions and accepted only the true ones.

## Data note

Links make relations visible, and relations can be personal data too: "who decided what" is information about a person. Do not create notes about real colleagues, customers or contacts. Write decisions with roles ("the product owner decided"). The two hard rules from [A vault and AGENTS.md](01-vault-and-agents-md.md) apply to every note, link and field.

## Next

[Context engineering](../08-advanced/01-context-engineering.md)
