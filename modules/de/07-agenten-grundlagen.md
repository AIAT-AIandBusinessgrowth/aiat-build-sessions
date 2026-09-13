# Modul 7 — Agenten-Grundlagen (CLI vs MCP, Claude Code/Codex)

> Deutsche Fassung · Stand 2026-09-13 · Englischer Lernpfad: [START-HERE](../../START-HERE.md)
>
> Öffentliche Fassung eines intern gepflegten Moduls: gekürzt und für ein allgemeines Publikum überarbeitet; fortgeschrieben und gepflegt wird der interne Text (Stand 2026-09-13).

⏱ ~40 min mit Vertiefungen · **Danach kannst du:** einem Agenten einen begrenzten Auftrag geben, seine Änderungen prüfen und bei Fehlern sinnvoll weiterarbeiten. Die späteren Abschnitte erklären Tools, Verbindungen und Befehle genauer.

**Setzt voraus:** zum Lesen keine Programmierkenntnisse. Für die Terminal-Beispiele brauchst du einen installierten, angemeldeten Agenten: [Ready to build](../../ready-to-build.md) (englisch).

## Worum es geht

Du möchtest ein Projekt verstehen oder eine kleine Änderung machen. Ein Coding-Agent kann Dateien lesen, Änderungen vorschlagen und sie mit deiner Erlaubnis ausführen. Du beschreibst, was du erreichen willst, und prüfst danach, was tatsächlich passiert ist.

**Erster Versuch, wenn dein Agent bereits eingerichtet ist:** Öffne eine eigene Kopie dieses öffentlichen Repos und bitte Claude Code oder Codex: „Lies die README.md. Erkläre mir in drei Sätzen, wozu dieses Projekt dient, und zeige die passenden Textstellen. Ändere keine Dateien." Lies die Stellen selbst nach: Passt die Erklärung? Nur deine eigene Antwort zeigt, was du verstanden hast; das kann der Agent nicht für dich bestätigen.

Verwende ab der ersten Toolnutzung nur erfundene Daten oder öffentliche Inhalte ohne Personenbezug. Keine echten Kundenlisten, persönlichen Angaben oder Zugangsdaten in Prompts und Übungsdateien.

Für den Einstieg reichen Abschnitte 1, 4 und 6. MCP-Verbindungen, Modelltabellen und eigene Subagents sind zum Nachschlagen da; dafür musst du jetzt nichts zusätzlich einrichten.

Der Hintergrund ist die Frage, welche Aufgaben sich sinnvoll delegieren lassen. Anthropic nennt den Abstand zwischen häufiger KI-Nutzung und vollständig delegierten Aufgaben eine **„Delegation-Gap"**. Die Bezeichnung beschreibt eine Beobachtung, keine Pflicht, mehr Aufgaben abzugeben. *(Quelle: Anthropic, 2026 Agentic Coding Trends Report, https://resources.anthropic.com/2026-agentic-coding-trends-report, Download nach Registrierung, abgerufen 2026-09-13. Prozentwerte nennen wir nicht, weil sie ohne Registrierung nicht nachprüfbar sind.)*

---

## 1. Was ist ein „Agent"? — der Loop

Bei einer einfachen Chat-Aufgabe bekommst du eine Antwort. Mit Werkzeugen kann ein Agent zusätzlich handeln: Dateien lesen, Befehle ausführen, Code ändern und Ergebnisse prüfen. Auch Chat-Produkte können solche Agentenfunktionen anbieten; entscheidend sind die verfügbaren Werkzeuge und Rechte.

Gib zuerst eine kleine Aufgabe und klare Grenzen vor. Ein Agent kann überzeugend erklären, dass etwas erledigt sei, obwohl noch ein Fehler vorhanden ist. Probiere das Ergebnis deshalb selbst aus.

### Der Loop — präzise

**Loop** heißt hier: mehrere Arbeitsschritte wiederholen. Ein typischer Durchgang sieht so aus:

**Context sammeln → planen → handeln (Edit / Run) → verifizieren → wiederholen.**

| Schritt | Was passiert | Alltagsbild |
|---|---|---|
| **Context sammeln** | Agent liest relevante Dateien, Fehlerausgaben, Vorgaben | sich erst die Akte durchlesen |
| **Planen** | Agent überlegt die nächsten Schritte | kurz überlegen, bevor man loslegt |
| **Handeln** | Agent ändert Dateien, führt Befehle aus | tatsächlich arbeiten |
| **Verifizieren** | Agent prüft das Ergebnis (Test laufen lassen, Output ansehen) | gegenprüfen, nicht hoffen |
| **Wiederholen** | nächster Durchlauf, bis das Ziel geprüft erreicht ist oder eine vereinbarte Grenze greift | bei Erfolg aufhören, bei fehlendem Fortschritt stoppen und neu entscheiden |

Diese Schritte helfen in Claude Code, Codex und anderen Agententools. Die genauen Befehle unterscheiden sich; du kannst sie später nachschlagen.

### Mindset-Anker: der Agent ist ein fehlbarer Junior

Das Bild vom Junior soll an nötige Prüfung erinnern. Ein Agent ist jedoch kein Mensch: Er kann eine schwierige Aufgabe lösen und kurz danach eine einfache Angabe erfinden. Dieses ungleichmäßige Können heißt **„jagged intelligence"**.

- Sein Context-Window ist begrenzt. Frühere Informationen helfen nur, wenn sie im aktuellen Kontext oder als nachgeladenes Wissen verfügbar sind.
- Er kann APIs, Abhängigkeiten und Dateipfade nennen, die nicht existieren. Prüfe solche Angaben im Projekt oder in der offiziellen Dokumentation.
- Lass dir zeigen, **was geändert wurde und welcher Check funktioniert hat**. Eine Aussage wie „fertig" reicht dafür nicht.

Beim Beauftragen musst du nicht jeden Arbeitsschritt vorschreiben. Beschreibe Ziel, Grenzen und die Prüfung. Boris Cherny empfiehlt, auch etwas anspruchsvollere Aufgaben begrenzt auszuprobieren; das ist ein Vorschlag zum Experimentieren, kein Grund, Ergebnisse ungeprüft zu übernehmen. *(YC-Video, Boris Cherny, 07/2026 — Cherny spricht von den „letzten ~6 Monaten" Modellfortschritt, keine exakte Modellfamilien-Schwelle.)*

### Der Rahmen: Vibe Engineering, nicht Vibe Coding

Simon Willison verwendet **„Vibe Engineering"** für disziplinierte Arbeit mit Agenten: planen, Änderungen ansehen und Ergebnisse testen. **„Vibe Coding"** bezeichnet in dieser Gegenüberstellung das weitgehend ungeprüfte Übernehmen des erzeugten Codes. Du brauchst diese Begriffe für die Übung nicht; der praktische Unterschied ist die Prüfung.

Wenn ein ungeprüfter Versuch einmal funktioniert, belegt das nicht die Zuverlässigkeit des nächsten. Das schrittweise Gewöhnen an übersprungene Kontrollen nennt man **„Normalization of Deviance"**. Behalte passende Checks bei, auch wenn mehrere Versuche gut liefen. *(Quelle: Willison, „Vibe engineering".)*

### Context ist die knappe Ressource

Das **Context-Window** enthält unter anderem Nachrichten, gelesene Dateien und Befehlsausgaben. Es hat eine feste Größe. Viel irrelevanter Text oder viele Korrekturen können es dem Modell erschweren, die wichtigen Informationen zu nutzen. Anthropic beschreibt abnehmende Leistung bei einem vollen Kontext; dafür begegnet dir auch der Begriff „Context Rot".

Lass den Agenten zunächst nur lesen, was er für die aktuelle Aufgabe braucht. Sichere vor einem Themenwechsel den Arbeitsstand und offene Fragen. Die Befehle `/clear`, `/compact` und `/context` stehen im [Werkzeugkasten](#7-werkzeugkasten--die-flüchtige-schicht), passende Vorgehensweisen im [Context-Management](#9-context-management--wann-eine-neue-session). Mehrere Agenten behandelt Modul 8.

---

## 2. CLI vs. MCP — Analogie und Definition

Zwei Begriffe, die ständig fallen, aber selten erklärt werden. Beide beschreiben, **wie** der Agent an die Außenwelt kommt — auf zwei verschiedenen Wegen.

### Plain-language-Analogie

- **CLI** (*Command-Line Interface*) heißt: ein Programm mit Textbefehlen bedienen, zum Beispiel `gh issue list`. Das Terminal ist das Fenster dafür. Claude Code und Codex CLI laufen darin und können andere installierte Programme verwenden.
- **MCP** (*Model Context Protocol*) ist ein gemeinsames Format, über das ein Agent Werkzeuge und Datenquellen anderer Systeme nutzen kann. Ein MCP-Server stellt diese Zugriffe bereit, etwa auf einen Issue-Tracker oder eine Datenbank.

Beispiel: Der Agent kann GitHub-Aufgaben mit dem CLI `gh` abfragen. Für ein anderes System könnte ein MCP-Server denselben Zweck erfüllen. Entscheidend ist, welcher Zugriff für die Aufgabe vorhanden und zugelassen ist.

### Präzise

- **CLI** ist die Kommandozeilen-Schnittstelle: der Agent läuft im Terminal, liest/ändert Dateien und führt Befehle aus — inklusive bereits installierter CLI-Tools wie `gh` oder `glab`.
- **MCP** ist ein **offener Standard zum Anbinden von Tools und Datenquellen an LLM-Agenten**. In Claude Code fügt man einen Server mit `claude mcp add` hinzu (Syntax unten); der Server stellt dem Agenten strukturierte Tools und Live-Daten bereit. Codex kann MCP-Tools ebenfalls **nutzen** (`codex mcp`). Codex selbst per `codex mcp-server` als MCP-Server anzubieten, geht nicht mehr: deprecated am 2026-08-24, entfernt am 2026-09-05, ausgeliefert mit Codex CLI 0.154.0 am 2026-09-09. Nachfolger ist der experimentelle Codex App Server (`codex app-server`), kein direkter Ersatz für einen MCP-Server. *(Quelle: https://learn.chatgpt.com/docs/changelog, abgerufen 2026-09-13)*

### MCP-Server hinzufügen — konkrete Syntax

Dieser Abschnitt ist optional. Die Beispiele zeigen die Syntax; sie sind kein zusätzliches Setup für die erste Übung. Prüfe vor einer Installation Server, Paketquelle und benötigte Rechte in der Hersteller-Dokumentation. Ein lokal gestarteter MCP-Server kann ebenfalls Netzwerkzugriff haben. Zwei Varianten (**Stand 06/2026**; im Zweifel `claude mcp --help`):

```bash
# Hosted HTTP-Server (z.B. ein Team-Server mit REST-Endpunkt)
claude mcp add --transport http mein-server https://mcp.example.com/server

# Lokaler stdio-Server (wird als Kindprozess gestartet, kein Netzwerk nötig)
claude mcp add jira-lokal -- npx -y @atlassian/mcp-jira
```

**Scopes** — wo die MCP-Konfiguration gespeichert wird:

| Scope | Wer sieht es | Wo gespeichert | Typischer Einsatz |
|---|---|---|---|
| `local` (Default) | nur du, nur dieses Projekt | `~/.claude.json` | persönliche Dev-Tools (eigener Figma-Token o.ä.) |
| `user` | nur du, alle Projekte | `~/.claude.json` | Tools, die du repo-übergreifend nutzt |
| `project` | alle im Team | `.mcp.json` im Repo-Root (eingecheckt) | gemeinsame Server, die alle Teammitglieder brauchen |

```bash
# Scope explizit setzen
claude mcp add --scope project --transport http team-server https://mcp.example.com/server
```

**`.mcp.json` — Minimal-Beispiel** (liegt im Repo-Root, wird eingecheckt und von allen Klonen geteilt):

```json
{
  "mcpServers": {
    "team-server": {
      "type": "http",
      "url": "https://mcp.example.com/server"
    }
  }
}
```

> **Merksatz:** `local` = nur du hier, `user` = nur du überall, `project` = alle im Team. Die Konfiguration lässt sich mit `.mcp.json` teilen; Anmeldung und lokale Voraussetzungen können trotzdem pro Person nötig sein. Keine Zugangswerte in diese Datei committen.

### CLI vs. MCP — Trade-off-Übersicht

| Kriterium | CLI-Builtin (`gh`, `glab`, `aws` …) | MCP-Server |
|---|---|---|
| **Setup** | sofort (Tool schon installiert) | Startup-Overhead + eigene Auth |
| **Reichweite** | Dateien, Shell, bereits installierte CLIs | externe Systeme (Jira, DB, Figma, Browser) |
| **Context-Kosten** | gering (kein Extra-Tool im Context) | in Claude Code ab v2.1.232 gering, weil Tool Search MCP-Tools erst bei Bedarf lädt ([Quelle](https://code.claude.com/docs/en/mcp)); in Agenten ohne Tool Search höher (alle Tool-Definitions dauerhaft im Context) |
| **Auth** | vorhandene CLI-Auth (`glab auth login`) | eigenes Auth-Modell je Server |
| **Best Practice** | Default-Wahl, wenn ein CLI existiert | nur wenn kein brauchbares CLI verfügbar ist |

> **Best Practice:** Nur regelmäßig genutzte Server aktiv lassen. Jeder Server bringt Startzeit, eigene Auth und zusätzliche Angriffsfläche mit, und in Agenten ohne Tool Search auch dauerhaften Context-Verbrauch. *(Tool Search ist in Claude Code ab v2.1.232 Default, Quelle: code.claude.com/docs/en/mcp, abgerufen 2026-09-13.)* `.mcp.json` für Team-Server einchecken; persönliche Server im `local`- oder `user`-Scope belassen.

### Wann CLI, wann MCP?

Die wichtige Nuance für die tiefere Ebene: **CLI-Tools sind der context-effizienteste Weg**, mit externen Diensten zu reden. Anthropic empfiehlt explizit — *„CLI tools are the most context-efficient way to interact with external services"* — also: gibt es ein CLI, **nimm das CLI**. MCP nimmt man, wenn es kein gutes CLI gibt oder strukturierter Zugriff / Live-Daten gebraucht werden.

| Frage | Wähle | Warum | Beispiel |
|---|---|---|---|
| Gibt es ein fertiges CLI (`gh`, `glab`)? | **CLI** | der Agent kann es schon, frisst wenig Context | Issue lesen, MR öffnen via `glab` |
| Kein brauchbares CLI, aber strukturierter Zugriff nötig? | **MCP-Server** | bringt Tools/Live-Daten mit | DB-Queries, Figma, Monitoring-Dashboards |
| Reine Datei-/Shell-Arbeit im Repo? | **CLI** (Default) | das ist der Kern des Agenten | Code lesen/ändern, Tests laufen lassen |

> **Merksatz für Nicht-Devs:** **Erst nach einem CLI suchen, dann an MCP denken.** Nutze zunächst einen bereits passenden und zugelassenen Zugriff. MCP ist eine weitere Möglichkeit, externe Werkzeuge anzubinden.

**MCP ist vertiefendes Wissen** und für den Einstieg nicht nötig.

### Tool-Design — was ein gutes Agenten-Tool ausmacht

Ein MCP-Server (oder ein CLI, das der Agent nutzt) bringt Tools mit — aber nicht jedes Tool ist gleich gut nutzbar. Fünf Kriterien entscheiden, ob ein Tool den Agenten **produktiv** macht oder ihn ausbremst:

| Kriterium | gutes Tool | schlechtes Tool |
|---|---|---|
| **Name** | sprechend, sagt sofort, was es tut (`search_contacts`, `schedule_event`) | generisch/kryptisch (`do_action`, `handler2`) |
| **Description** | knapp und präzise — sie ist **Prompt-Text**, den das Modell **bei jedem Aufruf** mitliest | vage oder redundant zu einer anderen Tool-Description — kostet Context ohne Nutzen |
| **Zuschnitt** | wenige, **mächtige** Tools, die einen ganzen Workflow abdecken (`get_customer_context` statt `get_customer_by_id` + `list_transactions` + `list_notes` einzeln) | viele **schmale** Tools, die 1:1 API-Endpunkte spiegeln — der Agent muss selbst orchestrieren |
| **Überlappung** | jedes Tool hat einen **klaren, eigenen** Zweck | zwei Tools, die (fast) dasselbe tun — der Agent muss raten, welches „richtig" ist |
| **Output** | knapp, nur die relevanten Felder (Namen statt UUIDs, gefilterte statt komplette Listen) | Rohdaten/alles auf einmal — flutet das Context-Window, das Modell muss selbst filtern |

Ein gutes Tool hat einen eindeutigen Zweck, verständliche Parameter und eine brauchbare Fehlermeldung. Mehrere fast gleiche Tools können die Auswahl erschweren.

Auch ohne selbst Tools zu bauen gilt die Konsumenten-Seite: In Agenten ohne Tool Search legt jeder aktivierte MCP-Server alle seine Formulare dauerhaft auf deinen Schreibtisch. Claude Code holt MCP-Tools ab v2.1.232 per Tool Search erst bei Bedarf ([Quelle](https://code.claude.com/docs/en/mcp), abgerufen 2026-09-13). Aktiviere trotzdem nur, was du wirklich brauchst.

*(Quelle: Anthropic Engineering — „Writing effective tools for agents — with agents", `anthropic.com/engineering/writing-tools-for-agents`, publiziert 2025-09-11, abgerufen 2026-07-30; als Tool-Design-Frage eingeordnet im Anschluss an das Kontext-Engineering-Thema — YC-Video, Boris Cherny, 07/2026, mehr dazu in Modul 10 (Kontext-Engineering).)*

---

## 3. Claude Code vs. Codex CLI

Beide sind **agentic coding CLIs** — Werkzeuge, in denen ein Agent denselben Loop (Context → planen → handeln → verifizieren) im Terminal fährt. Sie unterscheiden sich im Hersteller und in Details, **nicht** im Grundprinzip.

| | **Claude Code** | **Codex CLI** |
|---|---|---|
| Hersteller | Anthropic | OpenAI |
| Was es ist | agentic coding CLI; liest/ändert Dateien, führt Befehle aus, arbeitet Probleme autonom durch, während du zusiehst/lenkst | agentic coding CLI; plant Multi-Step-Änderungen über mehrere Dateien, führt Befehle aus, verifiziert. Bietet inzwischen auch Subagents, lokales Code-Review (eigener Agent vor dem Commit), Web-Search, Cloud-Tasks und eine Desktop-Oberfläche (seit 2026-07-09 Teil der ChatGPT-Desktop-App; Codex ist auch in ChatGPT Free und Go enthalten) — unterstreicht „dieselben Loops, andere Tasten" |
| Headless / nicht-interaktiv | `claude -p "…"` (siehe Modul 8) | **`codex exec`** für CI/Scripting (Syntax unten) |
| MCP | unterstützt MCP-Server (`claude mcp add`) | kann MCP-Tools nutzen (`codex mcp` zum Verwalten). Der frühere `codex mcp-server` wurde am 2026-08-24 deprecated und am 2026-09-05 entfernt (Codex CLI 0.154.0, 2026-09-09); Nachfolger ist der experimentelle Codex App Server, kein direkter MCP-Ersatz ([Changelog](https://learn.chatgpt.com/docs/changelog)) |
| Rolle in diesem Material | **gleichwertiger Einstieg** | **gleichwertiger Einstieg** (gleiche Prinzipien, andere Tasten) |

Du kannst mit Claude Code oder Codex anfangen. Auftrag, begrenzte Zugriffe und Ergebnisprüfung brauchst du bei beiden. Claude-Code-Befehle lassen sich jedoch nicht unverändert in Codex eingeben; dafür stehen die jeweiligen Beispiele dabei.

### Modell-Stand (flüchtige Schicht)

> **Achtung — flüchtige Schicht, wie der [Werkzeugkasten](#7-werkzeugkasten--die-flüchtige-schicht):** Modellnamen und -versionen ändern sich häufig. Die Stände gelten **je Tabellenzeile** (Datum in der Zeile); im Zweifel die aktuelle Hersteller-Doku prüfen. Der Loop bleibt — die konkrete Modellversion ist austauschbar.

| Tool | Aktuelle Modelle | Hinweis |
|---|---|---|
| **Claude Code** (Anthropic, direkte API) | **Opus 5** (`claude-opus-5`) · **Sonnet 5** (`claude-sonnet-5`) · **Haiku 4.5** (`claude-haiku-4-5`) *(re-verifiziert 2026-07-30)* | Opus = stärkstes Modell, Haiku = klein/schnell. **Default ist kontoabhängig:** Opus auf Max/Team-Premium, Sonnet auf Pro. Opus 5 setzt Claude Code v2.1.219+ voraus, Sonnet 5 v2.1.197+ ([Model-Config](https://code.claude.com/docs/en/model-config)). |
| **Claude Code**, Sonderfall | **Fable 5.1** über den Alias `fable` (ab Claude Code v2.1.257) *(Stand 2026-09-13)* | Kein Default, wählbar via `/model fable`. Der Alias `best` nimmt das Modell von `fable` (Fable 5.1), wo Fable verfügbar ist, sonst das von `opus` (Opus 5) ([Model-Config](https://code.claude.com/docs/en/model-config)). |
| **Codex CLI** (OpenAI) | **GPT-6 Astra** (Default seit 2026-09-04, setzt Codex CLI ≥ 0.153.4 voraus) *(Stand 2026-09-13)* | umschaltbar via `/model`. **`gpt-5.4` und `gpt-5.4-mini` wurden am 2026-08-31 aus Codex entfernt**; `gpt-5.2` und `gpt-5.3-codex` waren schon vorher deprecated. Skripte und Configs auf ein aktuelles Modell umstellen; die aktuelle Liste steht in der Hersteller-Doku. |

**Provider-Nuance (wichtig):** Über die **direkte Anthropic-API** sind die obigen Defaults aktiv. Läuft Claude Code dagegen über einen **Cloud-Provider** (AWS **Bedrock**, Google Cloud's **Agent Platform** (früher „Vertex"), Microsoft **Foundry**, oder neu **Claude Platform on AWS**), zeigen die `opus`-/`sonnet`-Aliasse **nicht einheitlich** dieselben Versionen wie direkt bei Anthropic — meist hinkt der `sonnet`-Alias hinterher, bei Foundry zusätzlich auch `opus`. **Konkret (Stand 2026-07-30):**

| Provider | `opus`-Alias | `sonnet`-Alias |
|---|---|---|
| Direkte Anthropic-API | Opus 5 | Sonnet 5 |
| AWS **Bedrock** | Opus 5 | Sonnet 4.5 |
| Google Cloud's **Agent Platform** (früher Vertex) | Opus 5 | Sonnet 4.5 |
| Microsoft **Foundry** | Opus 4.6 | Sonnet 4.5 |
| **Claude Platform on AWS** *(neuer 4. Provider)* | Opus 5 | Sonnet 4.6 |

Claude Platform on AWS ist Anthropics eigenes Angebot innerhalb von AWS, getrennt vom AWS-Dienst Bedrock — welche Zeile für dich gilt, hängt davon ab, wie du oder deine Organisation den Zugang eingerichtet habt.

Diese Zahlen ändern sich schnell: Für den **aktuellen Stand direkt beim jeweiligen Provider prüfen** statt auf Doku-Zahlen zu verlassen. Bei abweichenden Modellnamen prüfe, über welchen Anbieter dein Konto tatsächlich verbunden ist.

Für den ersten Versuch brauchst du die Modellnamen nicht auswendig zu kennen. Prüfe die Tabelle erst, wenn du eine konkrete Modell- oder Zugangsfrage hast.

*(Quellen: Claude Models Overview — `platform.claude.com/docs/en/about-claude/models/overview`; Model-Config & Provider-Defaults — `code.claude.com/docs/en/model-config`; Codex-Modelle und Changelog (GPT-6 Astra Default seit 2026-09-04, `gpt-5.4`/`gpt-5.4-mini` entfernt 2026-08-31) — `https://learn.chatgpt.com/docs/models` · `https://learn.chatgpt.com/docs/changelog`, abgerufen 2026-09-13; Codex CLI — https://learn.chatgpt.com/docs/codex/cli. Abgerufen 2026-07-30; Claude-Modellzeile re-verifiziert gegen `code.claude.com/docs/en/model-config` am 2026-07-30, Fable-Alias am 2026-09-13.)*

### `codex exec` — Beispiel-Syntax (Cross-Tool-Block)

`codex exec` ist das **nicht-interaktive Pendant** zu `claude -p` für Skripte. Praktisch heißt das: `codex exec "prompt"` streamt Progress auf **stderr**, die finale Antwort auf **stdout**.

```bash
codex exec "Migriere foo.py auf die neue API. Antworte am Ende mit OK oder FAIL."
# finale Message → stdout, Progress → stderr

codex exec --json "…"
# macht stdout zu einem JSONL-Event-Stream:
# Event-Typen u.a. thread.started, turn.started, turn.completed, turn.failed, item.*, error

codex exec resume --last "Behebe jetzt die failenden Tests"
# Folge-Turn an die letzte Session; auch: resume <SESSION_ID>
```

Weitere nützliche Flags (**flüchtig — Stand 06/2026**): `-o` / `--output-last-message <path>` (finale Message in Datei), `--output-schema <schema.json>` (Schema-konforme Endausgabe für Pipelines), `--sandbox workspace-write` bzw. `--sandbox danger-full-access` (Schreibrechte steuern), `--ephemeral` (keine Rollout-Dateien auf Disk schreiben), `--skip-git-repo-check` (Codex verlangt sonst ein Git-Repo). **Veraltet:** `--full-auto` ist **deprecated** und wirft eine Warnung — stattdessen `--sandbox workspace-write` nutzen. *(Quelle: Codex Manual — https://learn.chatgpt.com/docs/codex-manual.md, abgerufen 06/2026.)*

> **Merksatz:** `codex exec` verhält sich zu Codex wie `claude -p` zu Claude Code — ein Auftrag ohne interaktive Unterhaltung. Prüfe Rückgabestatus und Ergebnis; ein beendeter Prozess kann auch fehlgeschlagen sein. → Headless-Skalierung in Modul 8.

> **Codex-Auth und Windows (flüchtig, Stand 2026-09-13):** Codex CLI meldet sich entweder per **ChatGPT-Login (Browser-OAuth)** oder per **OpenAI API-Key** (`platform.openai.com/api-keys`) an, getrennt vom Anthropic-Zugang für Claude Code. Wer beide nutzt, verwaltet zwei Zugänge. Codex ist inzwischen auch in ChatGPT Free und Go enthalten. Unter Windows installieren sich beide nativ per PowerShell, WSL ist optional: Codex mit `irm https://chatgpt.com/codex/install.ps1 | iex` (https://learn.chatgpt.com/docs/codex/cli), Claude Code mit `irm https://claude.ai/install.ps1 | iex` (https://code.claude.com/docs/en/setup). Setup: [Ready to build](../../ready-to-build.md) (englisch), maßgeblich für die Anmeldung ist die Hersteller-Doku https://learn.chatgpt.com/docs/auth.

---

## 4. „KI-Fragen" an ein Repo stellen — auch ohne Dev-Hintergrund

Ein häufiges Missverständnis: man müsse programmieren können, um einen Agenten an einem Repo arbeiten zu lassen. Muss man nicht. Der Agent benutzt fertige **CLI-Tools stellvertretend für dich** — du sprichst in natürlicher Sprache, er ruft das Werkzeug im Hintergrund auf.

- Für **GitHub** ist das `gh`, für **GitLab** `glab`.
- Du sagst z.B. *„lies Issue 42 und fass mir zusammen, worum es geht"* oder *„öffne dafür einen MR"* — der Agent ruft `glab` bzw. `gh` auf und führt den angefragten Schritt aus. Prüfe bei Veröffentlichungen das Zielrepo und den Inhalt vorher. Anthropic beschreibt das so: Claude *„knows how to use [`gh`] for creating issues, opening pull requests, and reading comments"*.

**Präzise:** Installiere das passende CLI (`gh` bzw. `glab`) und sag dem Agenten, es zu nutzen. Ohne CLI kann der Agent die API zwar direkt ansprechen, läuft aber leicht in (unauthentifizierte) Rate-Limits. Unbekannte CLIs lernt der Agent selbst über `<tool> --help`.

> **Merksatz für Nicht-Devs:** Du **diktierst die Absicht**, der Agent **bedient das Werkzeug**. „Schreib mir auf, was in diesem Repo gerade offen ist" reicht — Tippen übernimmt er.

**Wo liegt dein Repo?** Auf **GitHub** nutzt der Agent `gh`, auf **GitLab.com** oder einer selbst betriebenen GitLab-Instanz `glab`. Welche Plattform du nimmst und wie du dort zu einem Account kommst, organisierst du selbst (Hintergrund: [Code hosting and backup](../../diy/04-code-hosting-and-backup.md), englisch).

### `gh` oder `glab` einrichten — Schritt für Schritt

**1. Einmalig anmelden:**

```bash
# GitHub
gh auth login

# GitLab.com
glab auth login
```

Für eine selbst betriebene Instanz: `glab auth login --hostname <dein-host>`

Beide Befehle fragen interaktiv nach (Browser-Login oder Token). Den Token-Wert tippst du nur dort ein, nie in einen Prompt.

**2. Token-Hygiene (Pflicht, sobald du mit Tokens arbeitest):**

- Token **eng scopen**: Für reines Lesen reicht bei GitLab `read_api`, bei GitHub ein fine-grained Token mit Leserechten auf genau das eine Repo
- **Ablaufdatum setzen**, kein Dauertoken
- Den Token-**Wert** nie in den Chat, in ein Skript oder in ein Repo schreiben
- Token **widerrufen**, wenn er nur für eine Übung angelegt wurde

Mehr zu Schlüsseln und Tokens: [Secrets and keys](../../diy/07-secrets-and-keys.md) (englisch).

**3. Agent instruieren:**

```
# Natürlichsprachlicher Prompt an den Agenten (kein Token im Prompt!):
"Nutze gh (bzw. glab), um die offenen Issues in diesem Repo aufzulisten und mir die drei aktivsten zusammenzufassen."
```

Der Agent kann dafür `gh issue list` bzw. `glab issue list` aufrufen. Vergleiche seine Zusammenfassung mit einem der genannten Issues.

> **Merksatz:** Zeig den **Weg** (Token anlegen, eng scopen, Ablaufdatum setzen), niemals den **Wert**. Begrenzte Rechte und Laufzeit verringern mögliche Folgen. Auch Leserechte können vertrauliche Inhalte offenlegen.

---

## 5. OpenCode — was ist das?

**OpenCode** ist ein Open-Source-Coding-Agent fürs Terminal, der mit Modellen verschiedener Anbieter arbeitet, also ein weiteres **agentic CLI** im Feld. Es passt in dieselbe Cross-Tool-Logik: **gleiche Loops, anderes Tool.** Konkrete Funktionen und Befehle stehen in der Projekt-Doku: https://opencode.ai

Für diesen Kurs brauchst du kein zusätzliches Tool zu installieren, wenn du bereits Claude Code oder Codex nutzt.

---

## 6. Plan Mode — erst denken, dann ändern

Bevor der Agent etwas ändert, kann man ihn im **Plan Mode** laufen lassen: Er recherchiert und plant **ohne** Änderungen vorzunehmen, du siehst den Plan und gibst ihn frei (oder editierst ihn). Mit **`Ctrl+G`** öffnet sich der vorgeschlagene Plan im **Default-Editor** zum direkten Bearbeiten (bestätigt — Quelle: `code.claude.com/docs/en/permission-modes`). Anthropic rahmt das als *„Explore first, then plan, then code"*.

Das benannte Workflow-Pattern dahinter ist **`Explore → Plan → Code → Commit`**: erst erkunden, dann planen, dann bauen, dann committen. Bei größeren Aufgaben lohnt es, den Plan in einer **Datei** festzuhalten — der Agent schreibt ihn in eine `PLAN.md`, die du prüfst, editierst und als Referenz im weiteren Lauf nutzt (verwandt mit dem Spec-first-Pattern (erst Spezifikation, dann Bauen), siehe [Context-Management](#9-context-management--wann-eine-neue-session)). So ist der Plan überprüfbar und überlebt auch ein `/clear`.

**Für einen einzelnen Prompt** muss man nicht in den Modus wechseln: Stell dem Prompt einfach **`/plan`** voran (`/plan Refactor das Auth-Modul`), dann plant der Agent **nur diese eine** Aufgabe und fragt danach um Freigabe. Bei der Freigabe hat man die Wahl, **welche Aktionen** der Agent bei der Umsetzung ausführen darf — von „Approve and start in auto mode" (durchlaufen lassen) über „accept edits" bis „review each edit" (jeden einzelnen Edit einzeln bestätigen). *(Bestätigt — Quelle: `code.claude.com/docs/en/permission-modes`, abgerufen 06/2026.)*

**Wichtig — nicht überdosieren:** Bei trivialen Änderungen ist Plan Mode Overhead. Faustregel von Anthropic: *„If you could describe the diff in one sentence, skip the plan."*

> **Merksatz:** Plan Mode ist das „kurz Innehalten, bevor man loslegt" aus dem Loop — explizit gemacht. Groß genug, dass man sich verlaufen könnte? Plan (oder `/plan` vor den Prompt). Ein-Satz-Diff? Direkt machen.

---

## 7. Werkzeugkasten — die flüchtige Schicht

> **Achtung — austauschbar:** Dies sind **Knöpfe, nicht der Loop.** Befehle und Namen ändern sich zwischen Tool-Versionen; verlasse dich auf den Loop, schlag die genaue Taste im Zweifel mit `--help` oder der Doku nach. (Quelle: Anthropic Best-Practices-Doku, Stand 2026-06.)

| Befehl | Was er tut | Wann nutzen |
|---|---|---|
| **`@datei`** | `@pfad` zeigt direkt auf eine Datei; der Agent liest sie vor der Antwort (ebenso Bilder per Paste/Drag, URLs, `cat error.log \| claude` als Pipe) | wenn du genau weißt, welche Datei/Fehlerausgabe relevant ist |
| **`/init`** | analysiert Build-System, Test-Framework und Patterns des Repos und generiert eine Start-`CLAUDE.md` | einmalig beim Onboarding eines Repos |
| **`CLAUDE.md`** | wird zu Beginn **jeder** Konversation geladen = persistenter Projekt-Context | für Regeln/Konventionen, die immer gelten — **kurz halten** |
| **`/clear`** | setzt den Context komplett zurück | zwischen **unzusammenhängenden** Tasks |
| **`/compact [Instruktionen]`** | verdichtet den bisherigen Verlauf; optional gezielt, z.B. `/compact Focus on the API changes` | wenn der Context voll wird, der Faden aber wichtig bleibt — **früh kompaktieren**, nicht erst wenn er überläuft |
| **`/context`** | zeigt die aktuelle Auslastung des Context-Windows | um zu sehen, wie „voll der Schreibtisch" ist |
| **`SKILL.md`** | lädt **on-demand** ein Stück Domänenwissen (z.B. ein internes Format, eine Konvention) nur dann in den Context, wenn die Aufgabe es braucht | für Spezialwissen, das **nicht** in jede Konversation gehört — entlastet die `CLAUDE.md` von unnötigen Details |
| **Plan Mode / `Ctrl+G`** | Agent plant ohne zu ändern; `Ctrl+G` öffnet den Plan zum Editieren | bei größeren Änderungen; überspringen bei Ein-Satz-Diffs (siehe oben) |
| **`Esc`** | stoppt den Agenten mitten in einer Aktion — **der Context bleibt erhalten** | sofort, wenn er abdriftet, um kurz zu korrigieren |
| **`Esc Esc` / `/rewind`** | öffnet das Rewind-Menü → auf einen früheren **Checkpoint** zurückrollen (Conversation / Code / beides) oder „Summarize from/up to here" | wenn ein Versuch in die Sackgasse lief |

**Zur `CLAUDE.md`-Faustregel:** Viele veraltete oder widersprüchliche Anweisungen können wichtige Regeln verdrängen. Geltende Daten-, Zugriffs- und Freigaberegeln bleiben bestehen. Pruning-Test von Anthropic: *„Würde das Entfernen dieser Zeile Claude Fehler machen lassen? Wenn nein — raus."*

**`CLAUDE.md` vs. `SKILL.md` — wohin gehört Wissen?** Die `CLAUDE.md` lädt **immer** (= teurer, permanenter Context) — dort gehören nur Regeln, die in *jeder* Konversation gelten. Spezialwissen, das nur manche Aufgaben brauchen (ein internes Datenformat, eine seltene Konvention), gehört in eine **`SKILL.md`**: sie wird **on-demand** geladen, wenn die Aufgabe sie braucht, und entlastet so die `CLAUDE.md` von unnötigen Details. Faustregel: *gilt es immer → `CLAUDE.md`; gilt es nur manchmal → `SKILL.md`.*

**Zu Checkpoints:** Jeder Prompt ist ein Checkpoint, und Checkpoints **persistieren über Sessions hinweg** (du kannst also auch in einer späteren Session noch zurückrollen). Erreichbar über **`/rewind`** oder **zweimal `Esc`** (bei leerem Input). **Wichtige Einschränkung:** Checkpoints tracken nur **Claudes eigene File-Edits** — sie sind ein **lokales Undo**, **kein Git-Ersatz** (Git ist die permanente History). **Scharfer Blindspot:** Was Claude per **Shell-Befehl** ändert (`rm`, `mv`, `cp` über Bash), wird **nicht** gecheckpointet und ist per `/rewind` **nicht** wiederherstellbar — ebenso wenig externe oder parallele Edits. Verlass dich also nicht darauf, dass `Esc Esc` ein gelöschtes File zurückholt. Für echte Versionierung bleibt Git zuständig (→ [Keep your work safe](../../tracks/06-keep-and-ship/01-keep-your-work-safe.md), englisch). Checkpoints werden zudem nach **30 Tagen** (konfigurierbar) automatisch aufgeräumt — wer länger zurückkönnen muss, committet in Git. *(Bestätigt — Quelle: `code.claude.com/docs/en/checkpointing`, abgerufen 06/2026.)*

> **Merksatz:** `Esc` = pausieren ohne Gedächtnisverlust. `Esc Esc` / `/rewind` = zurückspulen. `/clear` = Schreibtisch leerfegen. Drei verschiedene Werkzeuge für drei verschiedene Situationen.

---

## 8. Wenn etwas schiefgeht — die Error-Handling-Trias

Wenn etwas falsch läuft, stoppe zunächst die betroffene Aktion. Sichere den aktuellen Stand und notiere den Fehler, bevor du eine Session leerst oder Änderungen zurücknimmst. Drei typische Fälle:

| Fehlerbild | Symptom | Was tun |
|---|---|---|
| **Halluzination** | Agent erfindet eine Dependency, eine API oder einen Pfad, die es nicht gibt | Symptom + Ort + „so sieht behoben aus" präzise beschreiben; **Evidenz verlangen** (Test-Output, `git status`). LLMs scheitern v.a. bei seltenen APIs/Deps |
| **Falsches Tool / Abdriften** | Agent macht etwas anderes als gewollt, läuft in die falsche Richtung | sofort **`Esc`**, kurz korrigieren. **Nach >2 Korrekturen am selben Punkt:** Stand und Fehlversuche sichern, dann `/clear` + klarerer Auftrag |
| **Crash / Sackgasse** | Versuch ist kaputt, Stand unbrauchbar | erst Änderungen ansehen und sichern; dann gezielt **`Esc Esc` / `/rewind`** nutzen. Das stellt nur erfasste Claude-Edits wieder her, keine beliebigen Shell- oder fremden Änderungen |

**Warum nicht ewig korrigieren?** Anthropic: *„A clean session with a better prompt almost always outperforms a long session with accumulated corrections."* Akkumulierte Korrekturen verstopfen den Context — ein sauberer Neustart mit besserem Prompt schlägt das fast immer.

Wiederholte Fehler bedeuten nicht automatisch, dass du schlecht gefragt hast. Es können Informationen fehlen, ein Tool kann nicht passen oder das Modell kann an seine Grenze kommen. Prüfe den Grund und ändere den nächsten Versuch gezielt.

### Die fünf benannten Failure-Patterns

Diese fünf Muster helfen dir, Probleme im Arbeitsablauf zu erkennen. Die englischen Namen sind Suchbegriffe; merken musst du dir die Gegenmaßnahme:

| Muster | Symptom | Gegenmittel |
|---|---|---|
| **Kitchen-Sink-Session** | mehrere unzusammenhängende Tasks in einer Session, Context überfüllt sich | erst Stand sichern, dann `/clear` zwischen unabhängigen Aufgaben |
| **Correcting over and over** | dieselbe Korrektur wieder und wieder, der Faden wird immer schlechter | nach **>2** Korrekturen: Fehlversuche sichern, Ursache prüfen, frische Session mit klarerem Auftrag |
| **Over-specified CLAUDE.md** | aufgeblähte `CLAUDE.md`, Regeln werden ignoriert | Pruning-Test anwenden; Spezialwissen in `SKILL.md` auslagern |
| **Trust-then-verify-Lücke** | Output akzeptiert, *bevor* (oder ohne dass) verifiziert wurde | Verification-Leiter (unten) — Evidenz **vor** Akzeptanz |
| **Infinite Exploration** | Agent recherchiert endlos, kommt nie ins Handeln/Committen | Plan Mode mit klarem Ziel; `Explore → Plan → Code → Commit` abschließen |

### Die Verification-Leiter

**Verifizieren heißt: prüfen, ob das Ergebnis die Aufgabe erfüllt.** Beginne mit einem passenden Check und sieh dir dessen tatsächliche Ausgabe an. Die Tabelle zeigt zusätzliche Möglichkeiten, diesen Check zu automatisieren oder eine zweite Meinung einzuholen. Du musst nicht alle einrichten.

| Stufe | Mittel | Wann |
|---|---|---|
| **1 — Im Prompt** | gib dem Agenten gleich im Prompt einen Check, den er selbst laufen lässt (*„… und beende erst, wenn `pytest` grün ist"*) — und **verlange Evidenz** (Test-Output, `git status`/`git diff`), statt „ist erledigt" zu glauben | für eine Aufgabe mit vorhandenem, passendem Check; nötige Tools müssen eingerichtet sein |
| **2 — Über eine Session** | denselben Check als **`/goal`-Condition** hinterlegen; ein Evaluator prüft nach jedem Turn automatisch | für einen **unbeaufsichtigten** Lauf (→ Modul 8) |
| **3 — Deterministisches Gate** | den Check als **Stop-Hook-Skript** verdrahten | wenn er **exakt/reproduzierbar** sein muss (→ Modul 8) |
| **4 — Zweite Meinung** | ein **Verifikations-Subagent** in eigenem Context-Window prüft Plan/Diff **gegen** das Ziel (Writer/Reviewer) | bei **riskanten** Änderungen — ein frisches Modell soll das Ergebnis widerlegen (→ Modul 8) |

Diese vier technischen Möglichkeiten werden in [Modul 8](./08-agenten-skalierung.md) vertieft. Die [englische Verification-Leiter](../../tracks/05-verify-and-loop/01-verification-ladder.md) fasst das Lernen in drei Schritte: Selbstprüfung des Agenten, eigene Prüfung und frische Gegenprüfung. Die Nummern sind deshalb nicht austauschbar.

Bei jeder Variante gilt: Ein grüner Check belegt nur, was er tatsächlich prüft. Menschen prüfen fachlichen Sinn und mögliche Folgen. Ein zweiter Agent kann Fehler finden, aber weder Richtigkeit noch dein persönliches Verständnis bestätigen.

---

## 9. Context-Management — wann eine neue Session?

Eine neue Session hilft bei einem Themenwechsel. Halte vorher Ziel, letzte Änderungen, durchgeführte Checks und offene Fragen in einer Datei fest. Dann kann der nächste Versuch daran anknüpfen:

- **`/clear` zwischen unabhängigen Aufgaben**, nachdem der Arbeitsstand gesichert ist.
- **Bei einem tiefen Deep-Dive in *ein* komplexes Problem** darf der Context bewusst akkumulieren — hier ist das gesammelte Wissen wertvoll. Mit der Zeit entwickelt man ein Gefühl dafür (*„Develop your intuition"*).
- **Subagents für lese-intensive Recherche/Verifikation:** Sie laufen in einem **eigenen Context-Window** und berichten nur eine Zusammenfassung zurück → der Haupt-Context bleibt sauber (eigener Mini-Abschnitt direkt unten).
- **Spec-first-Pattern:** erst den Agenten *dich interviewen* lassen → das Ergebnis in eine `SPEC.md` schreiben → eine **frische Session** zum Implementieren öffnen. Trennt „Was wollen wir?" sauber von „Bauen wir es".

> **Merksatz:** Eine Session = ein Gedankengang. Wechselt das Thema, wechsle die Session (`/clear`). Bleibt das Thema, bleibt der Context. → Wie man das über viele parallele Agenten skaliert: Modul 8.

### Subagents — Arbeit auslagern, ohne den Schreibtisch zu fluten

Ein **Subagent** ist ein **zweiter Agent**, den der Hauptagent für eine Teilaufgabe startet. Der Clou: Er bekommt ein **eigenes, frisches Context-Window** und gibt am Ende **nur eine Zusammenfassung** an den Hauptagenten zurück — nicht die hunderten Dateien und Befehlsausgaben, die er dabei durchgesehen hat. So bleibt der Haupt-Schreibtisch sauber, obwohl im Hintergrund viel gelesen wurde.

> **Merksatz für Nicht-Devs:** Ein Subagent ist wie ein:e **Assistent:in, die du zum Recherchieren losschickst** — sie liest sich durch einen Aktenberg und kommt mit *einer* Seite Zusammenfassung zurück. Der Aktenberg landet nie auf deinem Tisch.

Wichtig ist die **Lese- vs. Schreibrechte**-Unterscheidung:

- **read-only** (für Recherche und Review passend): Der Subagent darf nur lesen/recherchieren/prüfen — er ändert nichts. Das ist der sichere Default für „schau dir das an und berichte".
- **write-fähig:** Der Subagent darf auch Dateien ändern — mächtiger, aber mehr Aufsicht nötig (die Verantwortung bleibt beim Menschen).

**Wann lohnt ein Subagent?** Drei typische Fälle:

| Einsatz | Wozu | Lese-/Schreibmodus |
|---|---|---|
| **Recherche** | „Finde heraus, wie X im Repo funktioniert" — der Subagent durchforstet viele Dateien, der Hauptagent bekommt nur das Ergebnis | read-only |
| **Review / Verifikation** | ein *frischer* Agent prüft Plan oder Diff **gegen** das Ziel (siehe [Verification-Leiter](#die-verification-leiter), Stufe 4) — mit einem frischen Blick, der trotzdem irren kann | read-only |
| **Fan-out** | mehrere Subagents arbeiten **parallel** an unabhängigen Teilaufgaben → mehr Durchsatz | je nach Aufgabe |

> **Merksatz:** Subagent = ausgelagerte Teilaufgabe in **eigenem Context**, die nur eine **Summary** zurückgibt. Genau dieser Baustein ist es, den [Modul 8](./08-agenten-skalierung.md) **multipliziert** — vom einen Subagent zu vielen parallelen Agenten (Fan-out, Writer/Reviewer). *(Quelle: Anthropic Claude-Code-Doku — `code.claude.com/docs/en/sub-agents`, Stand 06/2026.)*

### Eigene Subagents definieren (`.claude/agents/`)

Wer denselben „Arbeiter-Typ" immer wieder mit denselben Instruktionen losschickt (z.B. einen Code-Reviewer), schreibt ihn einmal als **Markdown-Datei** fest — danach ist er als eigener Agent-Typ aufrufbar.

> **Merksatz für Nicht-Devs:** Ein eigener Subagent ist eine **als Datei gespeicherte Rollen-Beschreibung** („so reviewst du Code — und mehr darfst du nicht"). Einmal geschrieben, ruft man den Helfer beim Namen auf, statt die Anweisung jedes Mal neu zu tippen. Selbst anlegen muss man so eine Datei nur, wenn man eigene Rollen bauen will — nutzen kann man die im Repo eingecheckten sofort.

Zwei Ablageorte entscheiden, wer ihn sieht:

| Ablageort | Wer sieht ihn | Typischer Einsatz |
|---|---|---|
| `.claude/agents/<name>.md` (im Repo, eingecheckt) | alle im Projekt-Team | projektspezifische Rollen, gemeinsam gepflegt |
| `~/.claude/agents/<name>.md` (persönlich) | nur du, in allen deinen Projekten | persönliche Helfer, repo-übergreifend |

Die Datei besteht aus **YAML-Frontmatter** (Konfiguration) plus dem **System-Prompt** als Markdown-Text darunter. Pflichtfelder sind nur `name` und `description`; optional u.a. `tools` (Tool-Allowlist — weggelassen erbt der Subagent alle Tools) und `model` (`sonnet`, `opus`, `haiku`, `fable`, eine volle Modell-ID oder `inherit`; Default ist `inherit` = Modell der Haupt-Session). Ein read-only Code-Reviewer sieht z.B. so aus (aus der Hersteller-Doku abgeleitet):

```markdown
---
name: code-reviewer
description: Reviewt Code auf Qualität, Security und Wartbarkeit. Direkt nach Code-Änderungen einsetzen.
tools: Read, Grep, Glob, Bash
model: inherit
---

Du bist ein Senior-Code-Reviewer. Sieh dir mit `git diff` die letzten
Änderungen an und gib priorisiertes Feedback: kritisch / Warnung / Vorschlag.
```

Weil `tools` weder Edit noch Write enthält, kann dieser Subagent **keine Dateien über die Editier-Tools ändern** — die Lese-/Schreibrechte-Unterscheidung von oben, als Datei festgeschrieben. `Bash` ist bewusst dabei (für `git diff`); streng genommen könnte ein Shell-Befehl trotzdem Dateien anfassen — wer auch das ausschließen will, lässt `Bash` weg. (Weitere Frontmatter-Felder wie `disallowedTools`, `permissionMode` oder `maxTurns`: Hersteller-Doku.)

**Wie kommt ein Subagent zum Einsatz?**

- **Automatisch:** Claude wählt anhand der `description` selbst, wann es an einen passenden Subagent delegiert — deshalb lohnt eine präzise description.
- **Explizit:** den Subagent im Prompt beim Namen nennen („Nutze den code-reviewer-Subagent …") oder per `@`-Mention auswählen — Letzteres garantiert, dass genau dieser läuft.
- **Foreground vs. Background:** Background-Subagents laufen nebenher, während du weiterarbeitest (seit v2.1.198 der Default, [Quelle](https://code.claude.com/docs/en/sub-agents); Permission-Nachfragen erscheinen weiterhin in deiner Haupt-Session); Foreground blockiert die Konversation, bis das Ergebnis da ist.
- **Built-ins:** Claude Code bringt eingebaute Subagents mit — u.a. **Explore** (read-only Codebase-Suche), **Plan** (Recherche im Plan Mode, ebenfalls read-only) und **general-purpose** (mehrstufige Aufgaben mit allen Tools).
- **Fork-Subagent (Abgrenzung):** Ein Subagent, der den **vollen bisherigen Gesprächskontext erbt**, statt frisch zu starten, wird mit **`/subtask`** gestartet. Praktisch, wenn eine Teilaufgabe zu viel Vorgeschichte bräuchte, um sie einem frischen Subagent zu erklären. Zurück kommt trotzdem nur das Endergebnis; der Haupt-Context bleibt sauber. Nicht verwechseln: **`/fork`** kopiert die Session inzwischen in eine neue Background-Session. *(Stand 2026-09-13, Quelle: code.claude.com/docs/en/commands)*

Das ist die Grundlage für das Skalieren in [Modul 8](./08-agenten-skalierung.md) — viele Subagents, Agent Teams, Workflows gehören dorthin. Versions-/Befehlsdetails oben sind flüchtige Schicht, **Stand 2026-07-06**. *(Quelle: https://code.claude.com/docs/en/sub-agents, abgerufen 2026-07-06)*

---

## Q&A

**Ist ein Agent dasselbe wie ChatGPT/ein Chatbot?**  
Ein Agent kann Werkzeuge nutzen und mehrere Arbeitsschritte ausführen. Eine einfache Chat-Aufgabe endet bei der Antwort. Manche Chat-Produkte bieten auch Agentenfunktionen; prüfe deshalb die tatsächlichen Zugriffe.

**Was ist der Unterschied zwischen CLI und MCP — in einem Satz?**  
Eine **CLI** bedienst du mit Textbefehlen im Terminal; **MCP** verbindet einen Agenten über ein gemeinsames Protokoll mit zusätzlichen Tools und Datenquellen.

**Wann nehme ich CLI, wann MCP?**  
**Gibt es ein CLI (`gh`, `glab`)? → CLI** — es ist context-effizient und der Agent kann es bereits. **Kein brauchbares CLI, aber strukturierter Zugriff nötig? → MCP-Server.** CLI ist der Default, MCP die Ausnahme für Spezialfälle.

**Muss ich programmieren können, um einen Agenten an einem Repo zu nutzen?**  
Nein. Du formulierst die Absicht in natürlicher Sprache („lies Issue X", „öffne einen MR"); der Agent ruft das CLI (`gh`/`glab`) für dich auf. Wichtig bleibt: **gegenprüfen** — der Agent ist ein fehlbarer Junior.

**Wie arbeite ich ein Issue (GitHub oder GitLab) mit Claude oder Codex ab?**

Starte Claude Code oder Codex im geklonten Repo und gib dem Agenten das konkrete Issue: „Nutze `gh` (bzw. `glab`), lies Issue #N, fasse Ziel und Akzeptanzkriterien zusammen, schlage einen Plan vor und setze ihn nach Freigabe um." Danach lässt du ihn die passenden Checks ausführen und Evidenz zeigen. Am Ende prüfst du selbst `git diff`, `git status`, Test-/Check-Output und öffnest einen Branch mit Pull Request (GitHub) bzw. Merge Request (GitLab). Prinzip gleich, Tasten unterschiedlich: Claude und Codex folgen beide dem Loop.

**Wie formuliere ich einen guten Auftrag an Claude/Codex?**

Ein guter Auftrag nennt Ziel, Kontext, relevante Dateien oder Issue-Link, Akzeptanzkriterien, Nicht-Ziele und den gewünschten Prüf-Befehl. Beispiel: „Ergänze in `src/utils/date.ts` eine Funktion, die ein Datum als `TT.MM.JJJJ` formatiert. Ändere keine anderen Dateien und beende erst, wenn `npm test` grün ist.“ Wenn du unsicher bist, bitte den Agenten zuerst um Rückfragen oder einen Plan.

**Welche Evidenz soll ich vom Agenten verlangen?**

Verlange belegbare Ausgaben, nicht „ist erledigt": `git diff` bzw. `/diff`, `git status`, Test- oder Check-Output, bei UI-Änderungen einen Screenshot, bei Arbeit auf GitHub oder GitLab den PR-/MR- bzw. Pipeline-Link. Automatische Checks ersetzen nicht, dass ein Mensch fachliche Plausibilität und die Freiheit von Personendaten prüft.

**Claude Code oder Codex — was lernen wir?**  
Beide, gleichwertig. Die Prinzipien (Loop, Context-Knappheit, Verifikation) gelten für Claude Code und Codex genauso wie für Cursor, OpenCode oder die Antigravity CLI. Die Antigravity CLI ersetzt die Gemini CLI, die am 2026-06-18 für Free-Nutzer:innen sowie für Google AI Pro und Ultra abgeschaltet wurde ([Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), abgerufen 2026-09-13). *Dieselben Loops, andere Tasten*: Wer den Loop kann, steigt um. Das Headless-Pendant zu `claude -p` ist `codex exec`. Keine Feature-Vergleichsmatrix.

**Warum „vergisst" der Agent manchmal, was ich vorhin gesagt habe?**  
Weil das **Context-Window** (sein Arbeitsgedächtnis) begrenzt ist und sich schnell füllt — *„performance degrades as it fills"*. Lieber wenige, klare Unterlagen statt alles reinkippen. Zum Aufräumen: `/clear` (zwischen Tasks), `/compact` (verdichten), `/context` (Auslastung sehen).

**Was füllt mein Context-Window eigentlich?**  
Fünf Posten: der System-Prompt des Tools, die Tool-Definitions (jedes verfügbare Tool inkl. seiner Description), `CLAUDE.md`/Regeln, der bisherige Gesprächsverlauf und die Tool-Outputs (was Befehle und Datei-Reads zurückliefern). `/context` zeigt dir, wie sich das aktuell auf diese fünf Posten aufteilt. Mehr dazu in Modul 10 (Kontext-Engineering).

**Der Agent ist mitten in einer falschen Aktion — wie stoppe ich, ohne alles zu verlieren?**  
Drück **`Esc`**: Das stoppt die laufende Aktion, der bisherige Context **bleibt erhalten**. Prüfe, was bereits ausgeführt wurde. Sichere den Stand vor einem **`Esc Esc` / `/rewind`**; dieser Rücksprung erfasst nicht beliebige Shell- oder externe Änderungen.

**Wann sollte ich eine neue Session starten statt weiterzumachen?**  
Bei einer unabhängigen neuen Aufgabe oder wiederholt erfolglosen Korrekturen kann eine frische Session helfen. Sichere vorher Stand und Fehlversuche. Geht es weiter um dasselbe Problem und liefert der Versuch Fortschritte, darf der Kontext erhalten bleiben.

**Brauche ich Plan Mode immer?**  
Nein. Plan Mode lohnt bei größeren Änderungen, in denen sich der Agent verlaufen könnte. Claude Code und Codex haben beide Plan-Mechaniken; wenn die konkrete Taste abweicht, bleibt das Prinzip gleich: erst verstehen und planen, dann ändern. Faustregel: *„If you could describe the diff in one sentence, skip the plan."* — bei Ein-Satz-Diffs direkt machen.

**Welches Modell läuft eigentlich „unter der Haube"?**  
Bei Claude Code über die direkte Anthropic-API je nach Auswahl **Opus 5 / Sonnet 5 / Haiku 4.5** (Stand 2026-07-30), dazu **Fable 5.1** über den Alias `fable` (ab v2.1.257, Stand 2026-09-13, [Model-Config](https://code.claude.com/docs/en/model-config)); der Default ist kontoabhängig, Opus auf Max/Team-Premium, Sonnet auf Pro. Bei Codex ist **GPT-6 Astra** seit 2026-09-04 der Default (ab Codex CLI 0.153.4); `gpt-5.4` und `gpt-5.4-mini` wurden am 2026-08-31 entfernt. **Aber:** Läufst du über einen Cloud-Provider (Bedrock, Google Cloud's Agent Platform, Foundry, oder neu Claude Platform on AWS), bekommst du dort teils andere Defaults — konkreten Stand beim jeweiligen Provider prüfen, nicht auf einzelne Versionsnummern aus der Doku verlassen. Modellnamen sind eine **flüchtige Schicht** — merk dir das Datum, nicht die Version. Der Loop bleibt gleich. (Siehe [Modell-Stand-Kasten](#modell-stand-flüchtige-schicht).)

**Wie lange dauert ein typischer Agenten-Lauf?**  
Stark aufgabenabhängig. Kleine, klar umrissene Tasks sind oft in wenigen Minuten durch; größere Refactorings über mehrere Dateien können deutlich länger laufen. Wichtig ist nicht die Stoppuhr, sondern: Der **Context füllt sich** mit der Zeit (*„performance degrades as it fills"*) — bei einem Themenwechsel daher `/clear`, nicht einfach endlos weiterlaufen lassen.

**Wann definiere ich einen eigenen Subagent statt eines Skills?**  
Ein **Skill** (`SKILL.md`) ist wiederverwendbares Wissen bzw. ein Workflow, der **im selben Context** der Haupt-Session läuft. Ein **Custom Subagent** (`.claude/agents/`) bekommt dagegen ein **eigenes Context-Window**, einen eigenen System-Prompt und eigene Tool-Rechte (z.B. read-only). Faustregel: Geht es nur um *Anweisungen* („so machen wir X") → Skill. Braucht die Aufgabe *Isolation* — viel Lese-Output, der den Haupt-Context fluten würde, oder eine harte Tool-Einschränkung — → Subagent. Und wer denselben Arbeiter-Typ immer wieder mit denselben Instruktionen startet, schreibt ihn als Subagent-Datei fest. *(Quelle: https://code.claude.com/docs/en/sub-agents, abgerufen 2026-07-06)*

**Was ist ein „Fork" — und wann nehme ich ihn statt eines normalen Subagents?**  
Ein normaler Subagent startet mit **frischem** Context und kennt nur den Auftrag, den er mitbekommt. Ein **Fork-Subagent** (gestartet mit `/subtask`) erbt den **kompletten bisherigen Gesprächsverlauf** — gleicher System-Prompt, gleiche Tools, gleiches Modell wie die Haupt-Session. Nimm einen Fork-Subagent, wenn die Teilaufgabe ohne die ganze Vorgeschichte nicht sinnvoll formulierbar wäre (z.B. „schreib parallel Tests für das, was wir gerade gebaut haben"). Zurück kommt in beiden Fällen nur das Endergebnis — der Haupt-Context bleibt sauber. Achtung: `/fork` selbst kopiert die Session inzwischen in eine neue Background-Session (Stand 2026-09-13).

**Kann der Agent versehentlich Daten löschen?**  
Ja — er kann Dateien ändern und löschen, wenn man ihn nicht einschränkt. Genau deshalb gibt es Sicherheitsnetze: **Checkpoints** (`Esc Esc` / `/rewind`, lokal, 30-Tage-Cleanup) für Claudes eigene File-Edits und vor allem **Git-Commits** für echte, dauerhafte Versionierung. **Wichtig:** Checkpoints retten **kein** per Shell-Befehl gelöschtes File (`rm` via Bash wird nicht getrackt) — verlass dich darauf also **nicht**. **Faustregel:** vor riskanten oder unbeaufsichtigten Läufen committen — dann ist jeder Stand wiederherstellbar. (Checkpoints sind **kein** Git-Ersatz, siehe [Werkzeugkasten](#7-werkzeugkasten--die-flüchtige-schicht).)

---

## Quellen & Weiterlesen

- Nächster Schritt — von einem Agenten zu vielen: [`08-agenten-skalierung.md`](./08-agenten-skalierung.md)
- Begriffe nachschlagen: [`glossar.md`](./glossar.md)
- Custom Subagents — Hersteller-Doku (Frontmatter-Felder, Built-ins, Fork): https://code.claude.com/docs/en/sub-agents *(abgerufen 2026-07-06)*
- Tool-Design für Agenten: Anthropic Engineering, „Writing effective tools for agents — with agents" — https://www.anthropic.com/engineering/writing-tools-for-agents *(publiziert 2025-09-11, abgerufen 2026-07-30)*
- Anthropic, 2026 Agentic Coding Trends Report (Download nach Registrierung): https://resources.anthropic.com/2026-agentic-coding-trends-report *(abgerufen 2026-09-13)*
- Claude Code: Model-Config, Permission-Modes, Commands, MCP, Setup: https://code.claude.com/docs/en/model-config · https://code.claude.com/docs/en/permission-modes · https://code.claude.com/docs/en/commands · https://code.claude.com/docs/en/mcp · https://code.claude.com/docs/en/setup *(abgerufen 2026-09-13)*
- Codex: Modelle, Changelog, CLI und Anmeldung: https://learn.chatgpt.com/docs/models · https://learn.chatgpt.com/docs/changelog · https://learn.chatgpt.com/docs/codex/cli · https://learn.chatgpt.com/docs/auth *(abgerufen 2026-09-13)*
- Google Developers Blog, Umstieg von Gemini CLI auf Antigravity CLI: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ *(abgerufen 2026-09-13)*
- OpenCode: https://opencode.ai *(abgerufen 2026-09-13)*
