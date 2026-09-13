# Modul 8 — Agenten-Skalierung (von einem Agenten zu vielen — ohne Kontrollverlust)

> Deutsche Fassung · Stand 2026-09-13 · Englischer Lernpfad: [START-HERE](../../START-HERE.md)

⏱ ~65 min mit allen Vertiefungen · **Danach kannst du:** für eine längere oder parallele Aufgabe passende Werkzeuge wählen, Zugriffe und Laufzeit begrenzen und die Ergebnisse getrennt prüfen.

**Setzt voraus:** Du hast mit einem Agenten eine kleine Aufgabe bearbeitet und das Ergebnis selbst geprüft. Grundlagen und Plan Mode erklärt [Modul 7](./07-agenten-grundlagen.md).

## Worum es geht

Ein Agent bearbeitet eine Aufgabe. Nun möchtest du vielleicht eine längere Arbeit laufen lassen, auf ein Testergebnis warten oder eine zweite Aufgabe parallel erledigen. Dieses Modul hilft dir zu entscheiden, ob das nützt und wie du den Überblick behältst.

**Ein kleiner erster Versuch:** Lass einen Agenten eine Änderung in deiner Übungskopie vorbereiten. Bitte eine frische Session, nur diese Änderung gegen den Auftrag zu prüfen und konkrete Fehlerstellen zu nennen. Vergleiche die Hinweise selbst mit dem Ergebnis. Das ist das Writer/Reviewer-Verfahren aus Abschnitt 5; zwei Sessions reichen dafür.

Du musst nicht das ganze Modul durcharbeiten. Wähle den Abschnitt zu deiner nächsten Aufgabe:

- **Auf etwas warten oder wiederholt prüfen:** Abschnitt 2.
- **Zwei unabhängige Aufgaben gleichzeitig bearbeiten:** Abschnitt 4.
- **Eine zweite Meinung einholen:** Abschnitt 5.
- **Anweisungen und Zugriffe im Team teilen:** Abschnitt 7.

Vor jedem längeren Lauf klärst du erlaubte Dateien und Aktionen, passende Checks, Kosten- oder Zeitgrenzen und wie du ihn stoppst. Im Kurs bleiben die Daten erfunden oder öffentlich ohne Personenbezug. Agenten dürfen Ergebnisse prüfen, aber nicht behaupten, ein Mensch habe dadurch etwas verstanden.

Die folgenden Tabellen und Befehle sind zum Nachschlagen. Claude-spezifische Befehle funktionieren nicht automatisch in Codex; Codex-Beispiele sind ausdrücklich bezeichnet.

### Einordnung: Die Adoption-Leiter (0–4) — wo steht ein Team?

Diese optionale Tabelle beschreibt ein mögliches Bild von Teamarbeit mit vielen Agenten. Die Zahlen sind **unbelegte Größenordnungen zur Illustration, keine Messwerte und keine Lernziele**. Ein Team mit einem gut eingesetzten Agenten kann passend arbeiten. Mehr Agenten bedeuten zunächst mehr Kosten, Koordination und Prüfaufwand.

Die [englische Adoption-Leiter](../../tracks/04-the-map/03-adoption-ladder.md) beschreibt dagegen Arbeitsgewohnheiten beim Lernen. Ihre Nummern haben eine andere Bedeutung und sind nicht mit dieser Tabelle austauschbar.

| Stufe | Name | Agents | Woran du's erkennst | Dein Engpass |
|---|---|---|---|---|
| 0 | Gated | 0 | Nur Chat-Zugang; Agents/CLI-Tools sind nicht eingerichtet oder nicht freigegeben. | Klären, ob ein zusätzlicher Zugriff gebraucht wird und zulässig ist. |
| 1 | Assisted | ~1 | Du + ein Agent als Pair — du liest praktisch jede Änderung, bevor sie landet; die Arbeit ist synchron (du sitzt daneben). | Aufmerksamkeit und passende Checks für die aktuelle Aufgabe. |
| 2 | Parallel | ~10 | Mehrere Agents parallel, je eigener Worktree (→ Abschnitt 4); der Agent prüft sich selbst (Tests/Build/Lint), du liest finale Diffs statt Tastenanschläge. | Output-Review: du schreibst weniger selbst und prüfst dafür mehrere Ströme — Steering wird der Engpass. |
| 3 | Supervised Autonomy | ~100 | Agents stoßen Arbeit proaktiv an; Wartung/Cleanup läuft kontinuierlich im Hintergrund (→ Abschnitte 1–2). | Vertrauen in den Loop + Entscheidungs-Durchsatz; Token-Effizienz wird zur Führungsaufgabe. |
| 4 | AI-native | ~1.000+ | Der Loop ist geschlossen: die meisten Agents werden von Agents gestartet; du steuerst per Intent und schaust nur bei Ausnahmen hin. | Automatisierbare Arbeit im großen Stil identifizieren und je Arbeitstyp die richtigen Guardrails setzen. |

Der nächste sinnvolle Versuch ist meist klein: zwei getrennte Aufgaben, ein bereits erprobter Check und Zeit für die Prüfung beider Ergebnisse. Passe Zugriffe und Modellwahl an die Aufgabe an. Auto Mode oder höhere Agentenzahlen sind keine Voraussetzung für Fortschritt.

Review, Tests und Datenregeln gelten auch bei mehr Automatisierung. Wenn sich ein Fehler wiederholt, prüfe nicht nur den Prompt: Vielleicht fehlt Information, ein Check ist unzureichend oder das Tool passt nicht. Halte die bestätigte Erkenntnis in den Projektanweisungen fest, damit eine neue Session sie nachlesen kann.

---

## 1. Loops & Headless-Mode — ein Agent ohne Sitzung

Im Normalfall arbeitet man mit einem Agenten **interaktiv**: man tippt, sieht zu, lenkt. Im **Headless-Mode** erhält er einen Auftrag ohne interaktive Unterhaltung, etwa aus einem Skript. Das ist hilfreich für wiederkehrende, bereits erprobte Aufgaben.

| | Interaktiv | Headless / non-interactive |
|---|---|---|
| Aufruf (Claude Code) | `claude` | `claude -p "prompt"` |
| Aufruf (Codex CLI) | `codex` | `codex exec "prompt"` |
| Wer steuert | Mensch, Turn für Turn | ein Skript / eine Pipeline |
| Wofür | normale Arbeit | CI-Pipelines, Pre-Commit-Hooks, Batch-Jobs |
| Output | im Terminal | parsebar: Text, `--output-format json`, `--output-format stream-json --verbose` (Echtzeit) |

**Plain-language:** `claude -p "…"` heißt „nimm diesen einen Auftrag, erledige ihn, gib ein maschinenlesbares Ergebnis zurück und beende dich". Genau das braucht man, um einen Agenten in **automatisierte Abläufe** einzubauen — z.B. vor jedem Commit prüfen lassen, oder denselben Auftrag über viele Dateien wiederholen (siehe Abschnitt 4).

### Headless-Output parsen (die JSON-Struktur kurz)

Damit ein Skript die Agenten-Antwort weiterverarbeiten kann, braucht es ein **maschinenlesbares Format** statt Freitext:

- **`--output-format json`** liefert **ein** Objekt mit u.a. `result` (der Antworttext), `is_error`, `total_cost_usd`, `duration_ms`, `num_turns`, `session_id`. Im Skript zieht man das Ergebnis z.B. mit `jq -r '.result'` heraus, `is_error` entscheidet über Erfolg/Fehlschlag.
- **`--output-format stream-json`** (braucht `--verbose`) emittiert **pro Message ein JSON-Objekt** in Echtzeit: zuerst eine `init`-System-Message, dann User-/Assistant-Messages, am Ende eine `result`-System-Message. Gut, um lange Läufe live mitzulesen, statt aufs Ende zu warten.

### Codex-Pendant: `codex exec` im Detail

`codex exec` dient wie `claude -p` dazu, einen Auftrag ohne interaktive Unterhaltung auszuführen. Die Optionen und Ausgabeformate unterscheiden sich. Es streamt Fortschritt auf **stderr**, die finale Message auf **stdout**:

```bash
codex exec "Migriere foo.py auf die neue API. Antworte mit OK oder FAIL."   # finale Message → stdout
codex exec --json "…"                  # stdout wird JSONL-Event-Stream: thread.started, turn.started,
                                       #   turn.completed, turn.failed, item.*, error
codex exec -o ergebnis.txt "…"         # --output-last-message: letzte Message zusätzlich in Datei schreiben
codex exec --output-schema schema.json "…"   # erzwingt schema-konforme Endausgabe (strukturierter Output)
codex exec resume --last "Behebe die failenden Tests"   # Folge-Turn an die letzte Session
codex exec --sandbox workspace-write "…"      # Sandbox-Stufe wählen (workspace-write | danger-full-access)
codex exec --ephemeral "…"             # keine Rollout-Dateien auf Disk hinterlassen
```

> **Frische-Hinweis (flüchtig, Stand 06/2026):** `codex exec --full-auto` ist **deprecated** — stattdessen die Sandbox-Stufe explizit setzen (`--sandbox workspace-write`). Ergänzend nützlich: `--ephemeral` (keine Rollout-Dateien) und `--skip-git-repo-check` (Codex verlangt sonst ein Git-Repo). *(Quelle: https://learn.chatgpt.com/docs/codex-manual.md)*

> **Merksatz:** Headless = „ein Auftrag rein, ein maschinenlesbares Ergebnis raus, dann Schluss" — die Bausteinform, mit der ein Agent in CI-Pipelines und Pre-Commit-Hooks wandert.

---

## 2. `/goal` & `/loop` — den Agenten bis zum Ziel weiterlaufen lassen

### Welches Werkzeug, wann? — die 4-Wege-Matrix (hier starten)

Bevor wir in die Befehle einsteigen: Vier Werkzeugtypen können Arbeit fortsetzen oder erneut starten. Die Tabelle unterscheidet zuerst, **was die nächste Aktion auslöst**; `/loop` steht mit seinen zwei Varianten darin. Laufzeitumgebung, Kosten und Zugriffsrechte sind weitere Unterschiede:

| Werkzeug | Was triggert die nächste Aktion | Typischer Use-Case |
|---|---|---|
| **`/loop 5m "<prompt>"`** (fester Takt) | ein **Intervall feuert** (Cron-artig, in `s`/`m`/`h`/`d`) | periodisch nachsehen: Deploy beobachten, CI alle paar Minuten abfragen |
| **`/loop "<prompt>"`** (self-paced) | **Claude wählt den Abstand selbst** (1–60 min) und beendet sich, wenn fertig | dynamisches Polling ohne fixen Takt — schaltet intern oft aufs Monitor-Tool um (s.u.) |
| **Monitor-Tool** (Streaming-Event) | **jede neue Output-Zeile** wird zur Notification | Logs/File-Watcher live, ereignisgetrieben reagieren statt blind pollen |
| **Cloud-Routines** (`/schedule`) | ein **Trigger** auf Anthropic-Infra: Cron-Zeitplan (= wiederkehrender Zeitplan, z.B. „täglich 09:00"), API-Call oder GitHub-Event — durabel, sessionlos (Vertiefung unten) | wiederkehrende Automation **ohne** offene Session; Min-Intervall **1 Stunde** |
| **`/goal "<condition>"`** (zielgerichtet) | ein **Evaluator-Modell** sagt „Condition noch nicht erfüllt" | bis ein **Endzustand** hält (Tests grün, Build sauber) — dann löscht es sich selbst |

> **Faustregel in einem Satz:** **`/loop`** pollt (fest oder self-paced), **Monitor** wird *benachrichtigt*, **Routines** laufen *auch ohne dich*, **`/goal`** wartet auf einen *Zustand*. Die Details zu jedem Werkzeug stehen unten; diese Matrix ist die Landkarte. *(Quelle: code.claude.com/docs/en/goal#compare-ways-to-keep-a-session-running · scheduled-tasks#compare-scheduling-options, Stand 06/2026)*

> **Bei Bedarf weiterlesen:** Die folgenden Details helfen beim eigenen Einrichten. Für die Auswahl genügt zunächst die Tabelle. **Channels** sind eine weitere Möglichkeit: Ein externes System schickt ein Ereignis an den Agenten. Das kann wiederholte Abfragen vermeiden, erfordert aber eine passende Anbindung. *(Quelle: code.claude.com/docs/en/scheduled-tasks#compare-scheduling-options, Stand 2026-06-29.)*

> **Tool-Parität:** Claude Code und Codex haben beide ein `/goal`-Konzept. Die folgenden Detailangaben zu `/loop`, Stop-Hooks, Evaluator-Modell, Versionen und Routines sind **Claude-Code-spezifisch**, sofern Codex nicht ausdrücklich genannt ist. Für Codex gilt: `/goal` ist in App/IDE/CLI verfügbar — standardmäßig aktiv; falls deaktiviert, über `features.goals` wieder aktivierbar. Das Headless-Pendant zu `claude -p` heißt bei Codex `codex exec`. *(Quellen: code.claude.com/docs/en/goal · learn.chatgpt.com/docs/codex-manual.md, abgerufen 2026-07-08)*

`/goal` ist ein **echter Claude-Code-Befehl** und benötigt **CC v2.1.139+** (eingeführt mit v2.1.139, Quelle: https://code.claude.com/docs/en/changelog, abgerufen 2026-09-13). Die genaue Versionsnummer gehört zur **flüchtigen Tooling-Schicht** (ändert sich mit Releases). Er setzt eine **Completion-Condition**, eine Bedingung, die erfüllt sein muss, damit „fertig" gilt. Der Agent arbeitet dann **ohne erneutes Prompten** weiter, bis die Bedingung hält oder man `/goal clear` ausführt.

**Bedienung kompakt:** Pro Session ist **ein** Goal aktiv — ein neues `/goal` **ersetzt** das alte. Das Setzen startet **sofort einen Turn** (die Condition selbst ist die Arbeitsanweisung, kein separater Prompt nötig); solange das Ziel läuft, zeigt ein `◎ /goal active`-Indikator die Laufzeit an. **`/goal` ohne Argument** zeigt den Status: Condition, Laufzeit, Zahl der evaluierten Turns, Token-Spend und die letzte Evaluator-Begründung — ein früher in der Session erreichtes Ziel erscheint dort mit derselben Bilanz. *(Quelle: https://code.claude.com/docs/en/goal, abgerufen 2026-07-06)*

**Wie es prüft:** Nach **jedem Turn** schaut ein **separates, schnelles Evaluator-Modell** drauf — ein frischer Blick, nicht das Modell, das die Arbeit gemacht hat. Es ist das konfigurierte „small fast model" (**per Default Haiku**) und gibt eines von **drei Urteilen** zurück: *not met* (noch nicht erfüllt), *met* (erfüllt) oder *impossible* (nicht erreichbar), jeweils mit einer kurzen Begründung; diese Begründung fließt als Guidance in den nächsten Turn. Ist das Ziel erfüllt, **löscht es sich selbst**. *(Drei Urteile: Quelle code.claude.com/docs/en/goal, abgerufen 2026-09-13.)*

> **Wichtiger Evaluator-Caveat:** Der Evaluator **ruft keine Tools auf** und liest **nicht** eigenständig Dateien oder führt Befehle aus — er beurteilt nur, was **Claude im Transcript sichtbar gemacht** hat. Deshalb die Condition so schreiben, dass **Claudes eigener Output** sie belegen kann, z.B. „`npm test` exits 0" oder „`git status` is clean". Maximale Condition-Länge: **4.000 Zeichen**.

> **Checkliste — tragfähige `/goal`-Condition (3 Punkte):** Eine Condition, die über viele Turns hält, hat meist (1) **einen messbaren Endzustand**, (2) **einen benannten Check**, mit dem Claude es beweisen soll (z.B. „`npm test` exits 0", „`git status` is clean"), und (3) **Constraints**, die unterwegs nicht verletzt werden dürfen (z.B. „no other test file is modified"). *(Quelle: code.claude.com/docs/en/goal, Stand 2026-07-07)*

> **Best Practice (langlaufende autonome Sessions):** `/goal` lässt sich mit **Auto Mode** und Modellen für längere Aufgaben kombinieren (Fable, Alias `fable`, ab Claude Code v2.1.257 Fable 5.1; kein Default, muss explizit per `/model` gewählt werden → [Modul 7](./07-agenten-grundlagen.md)) — beschreibe das **Outcome** (den Endzustand), nicht die einzelnen Schritte, setze das Ziel und lass den Agenten turn-über-turn zu Ende arbeiten. Die Arbeitsteilung dabei präzise: **Auto Mode entfernt die Per-Tool-Nachfragen, `/goal` die Per-Turn-Nachfragen** — die beiden sind komplementär, keins ersetzt das andere. *(Quelle: code.claude.com/docs/en/commands · https://code.claude.com/docs/en/model-config · https://code.claude.com/docs/en/goal, abgerufen 2026-07-06; Fable-Alias geprüft 2026-09-13)*

`/loop` ist das **Takt-Geschwister**: statt „bis eine Condition hält" re-triggert es den Agenten **wiederkehrend**. **Faustregel: `/loop` = „prüfe alle N Minuten", `/goal` = „arbeite weiter, bis X stimmt".** `/loop` ist ein **bundled skill** mit drei Modi:

| Aufruf | Verhalten |
|---|---|
| `/loop 5m "<prompt>"` | **Fester Takt** — Intervall + Prompt = klassischer Cron-artiger Lauf. Intervall-Einheiten: `s` / `m` / `h` / `d` (z.B. `5m`, `30m`, `2h`, `1d`). |
| `/loop "<prompt>"` | **Self-paced (dynamisch)** — kein Intervall: Claude wählt die Verzögerung (**1–60 min**) selbst **und kann den Loop selbst beenden**, wenn die Arbeit nachweislich fertig ist (plant dann kein nächstes Wakeup). |
| `/loop` (nur, kein Prompt) | **Maintenance-Modus** — nutzt `.claude/loop.md` (Projekt) ▸ `~/.claude/loop.md` (User) ▸ eingebautes Maintenance-Prompt (in dieser Reihenfolge). |

> **Merksatz für Nicht-Devs — Einmal-Erinnerung? Kein `/loop` nötig:** Für einen einmaligen Reminder beschreibt man den Wunsch einfach in **natürlicher Sprache** — „remind me at 3pm to push the release branch" oder „in 45 minutes, check whether the integration tests passed". Claude legt dafür einen **Single-Fire-Task** an, der sich nach dem Lauf **selbst löscht** (kein Intervall, kein Prompt-Skill nötig). *(Quelle: code.claude.com/docs/en/scheduled-tasks, Stand 2026-07-07)*

> **Warum self-paced oft token-effizienter ist als ein kurzer fester Takt:** Bei einem dynamischen `/loop` schaltet Claude intern **oft aufs Monitor-Tool** um (Doku: *„Claude may use the Monitor tool directly"*) — statt jede Runde den vollen Context neu zu lesen, reagiert es ereignisgetrieben auf neue Output-Zeilen. Ein fixes kurzes Intervall (`/loop 1m`) zahlt dagegen pro Tick eine volle Kontext-Runde, auch wenn nichts passiert ist. *(Quelle: code.claude.com/docs/en/scheduled-tasks#let-claude-choose-the-interval, Stand 06/2026)*

> **Best Practice — Self-paced Loop konvergieren lassen:** Damit `/loop "<prompt>"` (ohne Intervall) sich **selbst beendet**, braucht der Prompt ein klares Abschluss-Kriterium — sonst plant Claude immer ein nächstes Wakeup. Drei Bausteine: (a) ein **expliziter Abschluss-Satz** („Beende den Loop, wenn …"), (b) optional ein **maschinenlesbares Token** im letzten Turn (z.B. `DONE` ausgeben, wenn fertig), (c) eine **Turn-Budget-Klausel als Sicherheitsventil** („… oder nach 10 Iterationen"). Ohne (c) läuft der Loop bis zur 7-Tage-Expiry weiter, falls das Kriterium nie hält. *(Quelle: code.claude.com/docs/en/scheduled-tasks, Stand 2026-06-29)*

> **Praktiker-Muster (nicht im offiziellen Doc benannt):** Als Abschluss-Kriterium ist **„N aufeinanderfolgende saubere Durchläufe"** robuster als ein einzelner grüner Lauf — ein einzelner Pass kann *flaky* sein (Test zufällig grün). Formuliere das Kriterium also z.B. als „beende, wenn die letzten 3 Läufe alle grün waren". *(Sekundärquelle / Praktiker-Heuristik — keine Hersteller-Aussage, Stand 2026-06-29.)*

> **Best Practice — Loops triggern auch gespeicherte Commands/Skills, nicht nur Freitext:** Statt eines Prompt-Strings kann ein Loop **jede Iteration einen Skill/Command** re-runnen, z.B. `/loop 20m /review-pr 1234` (alle 20 min den `/review-pr`-Command auf PR 1234) oder `/loop 5m /code-review`. So kombiniert man CI-/PR-Watch mit einem fertigen Review-Skill, ohne den Prompt jedes Mal auszuschreiben. *(Quelle: code.claude.com/docs/en/scheduled-tasks, Stand 06/2026)*

> **Caveat — nicht jeder Command feuert im Loop:** Ein Scheduled-Fire führt nur Skills aus, die Claude **selbst aufrufen darf**. Als **reiner Text** (statt ausgeführt) landen im Prompt: Built-ins wie `/permissions`, `/model` oder `/clear`; Skills mit `disable-model-invocation: true`; per `skillOverrides`-Setting oder Skill-Deny-Rule gesperrte Skills; MCP-Prompts wie `/mcp__github__list_prs`. Skills, die ein MCP-Server bereitstellt, laufen dagegen weiter. *(Quelle: code.claude.com/docs/en/scheduled-tasks, Stand 2026-07-07)*

**`loop.md` im Detail:** Inhalt über **25.000 Bytes wird abgeschnitten** (truncated — die Datei wird **nicht** abgelehnt, also `loop.md` knapp halten); Edits greifen **live in der nächsten Iteration** (keine Neuanlage des Loops nötig). Loops sind **session-scoped** und enden bei einer neuen Konversation; sie laufen, bis man sie stoppt (`Esc` stoppt einen wartenden Loop) oder die **7-Tage-Expiry** greift (der Loop feuert ein letztes Mal und löscht sich dann selbst).

> **Wann Tasks überhaupt feuern (Session-Scoping):** Scheduled Tasks feuern **nur, solange Claude Code läuft und idle ist** — das Terminal schließen oder die Session beenden stoppt sie. **Backgrounding** der Session trägt `/loop`-Tasks in eine **Background-Session** über, die ohne Terminal weiterläuft. (Background-Bash- und Monitor-Tasks werden beim Resume dagegen **nie** wiederhergestellt.) *(Quelle: code.claude.com/docs/en/scheduled-tasks, Stand 2026-07-07)*

> **Best Practice — Was in `loop.md` gehört:** (a) der **Aufgaben-Scope** (was jede Iteration tun soll), (b) ein **Abbruch-Satz** („Beende, wenn …"), (c) eine **Evidenz-Anforderung**, damit Claude sich anhand nachprüfbarer Ausgaben selbst beenden kann. *(Der Inhalt dieser Datei bestimmt, wann der Agent Feierabend macht.)* *(Quelle: code.claude.com/docs/en/scheduled-tasks, Stand 2026-06-29)*
>
> Ein Beispiel für eine `.claude/loop.md`:
>
> ```markdown
> Prüfe bei jedem Durchlauf, ob `npm test` und `npm run lint` grün sind.
> Ist etwas rot, behebe genau einen Fehler und zeige danach den Output beider Befehle.
> Beende den Loop, wenn beide Befehle zweimal in Folge grün waren, spätestens nach 10 Durchläufen.
> ```

**Guards/Limits (kompakt):** max **50 scheduled tasks pro Session**; `CLAUDE_CODE_DISABLE_CRON=1` schaltet den Scheduler **und** `/loop` ganz ab. Typischer Einsatz: wiederkehrendes/intervallbasiertes **Polling während einer offenen Session** — einen Deploy beobachten, den Status eines PR prüfen. *(Quelle: code.claude.com/docs/en/scheduled-tasks)*

> **Tasks per natürlicher Sprache verwalten:** Man muss keine IDs auswendig lernen — „what scheduled tasks do I have?" listet die laufenden Tasks, „cancel the deploy check job" bricht einen ab. Jeder Task trägt eine **8-Zeichen-ID**, mit der sich ein einzelner Task gezielt canceln lässt. (Intern heißen die Tools dafür `CronCreate` / `CronList` / `CronDelete` — fürs Bedienen genügt die natürliche Sprache.) *(Quelle: code.claude.com/docs/en/scheduled-tasks, Stand 2026-07-07)*

> **Timing-Caveat (Jitter, kein Catch-up):** Wiederkehrende Tasks feuern nicht sekundengenau, sondern mit einem **deterministischen Offset (bis ~30 min) aus der Task-ID** — derselbe Task feuert also immer mit demselben Versatz (das ist gewollt, verteilt die Last). Und: **verpasste Fires werden nicht nachgeholt** — war die Maschine zur Plan-Zeit aus, läuft der Task einfach beim nächsten regulären Termin. Das erklärt, warum ein „9:00-Loop" real z.B. um 9:17 läuft. **Workaround für exaktes Timing (nur Einmal-Tasks):** eine Minute **≠ :00/:30** wählen (z.B. `3 9 * * *` statt `0 9 * * *`; Cron-Syntax: Minute Stunde Tag Monat Wochentag) — das entfernt nur den **One-Shot-Jitter** von Einmal-Remindern; der bis-zu-30-Minuten-Offset **wiederkehrender** Loops ist aus der Task-ID abgeleitet und bleibt. *(Quelle: code.claude.com/docs/en/scheduled-tasks#jitter, Stand 2026-07-07)*

> **Plattform-Hinweis (Stand 2026-09-13):** Früher fiel `/loop` auf Bedrock, Google Cloud's Agent Platform (früher Vertex) und Foundry auf ein festes 10-Minuten-Schema zurück und las kein `loop.md`. Diese Einschränkung gilt seit Claude Code **v2.1.248** nicht mehr. *(Quelle: https://code.claude.com/docs/en/scheduled-tasks, abgerufen 2026-09-13)*

Alternativen für Scheduling: **Cloud-Routines** (`/schedule`, Anthropic-managed), **Desktop Scheduled Tasks** und das **Monitor-Tool** (Event-getrieben statt zu pollen). *(Quelle: code.claude.com/docs/en/scheduled-tasks)*

### Scheduling-Primitive — die Vertiefung (Token-Profil & Min-Intervalle)

Die 4-Wege-Matrix oben ist die Landkarte; diese Tabelle vertieft sie um zwei Achsen, die beim Skalieren über Kosten entscheiden — das **Token-/Kosten-Profil** und das **kleinste sinnvolle Intervall**. Mit dabei zwei Werkzeuge, die in der Landkarte fehlen: **Background-Bash** (ein langer Lauf nebenher) und **Channels** (Event-*Push* statt Pull).

> **Hinweis — Background-Arbeit nicht selbst pollen:** Detached Background-Commands (`run_in_background`) laufen **über Turns hinweg weiter** und **re-invoken den Agenten automatisch beim Exit** — dafür braucht es **keinen** Poll-Loop (häufiger Irrtum: „beobachten" ≠ „pollen"). *(Flüchtige Tooling-Schicht, Stand 2026-06-29.)*

| Primitive | Was startet die nächste Aktion | Token-/Kosten-Profil | Kleinstes Intervall | Wofür typisch |
|---|---|---|---|---|
| **`/loop`** | ein Intervall feuert (fest oder self-paced) | pro Tick ein Turn — bei kurzem Takt teurer | **1 min** | Deploy/CI/PR-Checks periodisch abfragen |
| **`/goal`** | Evaluator-Modell sagt „Condition noch nicht erfüllt" (pro Runde) | pro Runde ein Turn + günstige Haiku-Eval | — (kein Takt, zustandsgetrieben) | bis ein **Endzustand** erreicht ist (Tests grün, Build sauber) |
| **Monitor-Tool** | **jede neue stdout-Zeile** wird zur Notification | **token-effizienter als Polling** (nur bei echten Events aktiv) | — (Streaming, kein Takt) | Logs/File-Watcher live beobachten, ereignisgetrieben reagieren |
| **Channels** | **externes System pusht** das Event in die Session (z.B. CI meldet den Fehler selbst) | nur bei echtem Push — kein Poll-Overhead | — (Push, kein Takt) | wenn das Ereignis von außen kommt und du nicht mal lauschen willst |
| **Background-Bash** (`run_in_background`) | nichts — läuft einmal durch, ohne den Turn zu blocken | ein Aufruf, kein Wieder-Prompten | — (einmaliger Lauf) | einen langen Build/Server starten und nebenher weiterarbeiten |
| **Desktop Scheduled Tasks** | ein lokaler Cron-Trigger (deine Maschine muss laufen) | pro Fire ein Turn | **1 min** | geplante lokale Automation, an die eigene Maschine gebunden |
| **Cloud-Routines** (`/schedule`) | ein Cron-, API- oder GitHub-Trigger (Anthropic-managed; Vertiefung unten) | unabhängig von deiner Session/Maschine | **1 Stunde** | wiederkehrende Automation **ohne** offene Session, robust über Restarts |

> **Merksatz:** Pollen (`/loop`) fragt „ist schon was?", Streamen (Monitor) wird *benachrichtigt*, **Channels** lassen sich das Event *zuschieben*, `/goal` wartet auf einen *Zustand*, Cloud-Routines laufen *auch ohne dich*. Die Leiter geht von Polling → Streaming → Push: jede Stufe spart die leeren Runden der vorigen. **Wichtig fürs Erwartungsmanagement:** Eine Cloud-Routine kann **nicht alle 5 Minuten** pollen — ihr Minimum sind **60 Minuten**; für minütliches Polling braucht es eine offene Session mit `/loop`. *(Quelle: code.claude.com/docs/en/scheduled-tasks#compare-scheduling-options, Stand 06/2026)*

> **Kostenhinweis — Prompt-Cache bei Loops (flüchtig, Stand 2026-06-29):** Anthropic Prompt-Caching hat per Default eine **5-Minuten-TTL**; jede Nutzung **erneuert den Cache kostenlos** (ein 1-Stunden-Cache geht nur gegen Aufpreis). Folge für den Loop-Takt: Ticks **unter 5 Minuten** auseinander treffen einen warmen Cache (billiger Prefix-Read); ein Tick **nach** Ablauf der TTL liest den ganzen statischen Prefix (System-Prompt + `CLAUDE.md` + `loop.md`) **uncached** neu = voller Input-Token-Preis. Faustregel: entweder **unter 5 Minuten** bleiben (warm) **oder** auf **lange Idle-Gaps (20–60 min)** gehen; das teure Mittelfeld (häufig, aber nicht häufig genug) meiden. Greifbar gemacht: ein Task für ~$0.05/Lauf alle 5 Minuten ≈ **$14.40/Tag** (Rechenbeispiel mit angenommenen $0.05 pro Lauf: 288 Läufe pro Tag, ohne öffentliche Quelle, keine Anthropic-Zahl) — „nicht überpollen" ist also auch eine Kostenfrage.
>
> **Als Synthese kennzeichnen:** Kein offizielles Claude-Code-Doc sagt, dass der self-paced `/loop`-Algorithmus auf das Cache-Fenster optimiert. Die Kopplung von Cache-TTL und Loop-Takt ist eine **Engineering-Schlussfolgerung (Inferenz)** aus zwei belegten Fakten — der 5-Minuten-Cache-TTL und der self-paced 1–60-min-Spanne — und **keine Hersteller-Aussage**. *(Quelle Mechanismus: platform.claude.com/docs/en/build-with-claude/prompt-caching · code.claude.com/docs/en/scheduled-tasks, Stand 2026-06-29)*

### Cloud-Routines (`/schedule`) — die Vertiefung

Eine **Routine** ist eine gespeicherte Claude-Code-Konfiguration — Prompt, ein oder mehrere Repositories, Connectors — die **auf Anthropic-managed Cloud-Infrastruktur** läuft: Sie arbeitet weiter, wenn der Laptop zu ist. Status: **Research Preview** (Verhalten, Limits und API können sich ändern); verfügbar auf **Pro/Max/Team/Enterprise** mit aktiviertem „Claude Code on the web". Verwaltet wird über **claude.ai/code/routines** (Web) oder in der CLI mit **`/schedule`** (`list` / `update` / `run`). Wichtige Grenze: Die CLI legt **Schedule-Trigger** an und seit **v2.1.225** auch **GitHub-Trigger** (Stand 2026-09-13, [Quelle](https://code.claude.com/docs/en/routines)); API-Trigger konfiguriert man im Web. *(Quelle: https://code.claude.com/docs/en/routines, abgerufen 2026-07-06)*

> **Merksatz für Nicht-Devs:** Eine Routine ist ein **Dauerauftrag in der Cloud**: einmal beschreiben, was regelmäßig passieren soll — der Rest läuft ohne offenes Terminal und ohne dass jemand daneben sitzt. Genau deshalb ist die Frage „was darf sie erreichen?" wichtiger als bei allem, wobei man live zusieht.

**Drei Trigger-Typen** (kombinierbar an derselben Routine):

| Trigger | Wie er feuert | Wichtigste Einschränkung |
|---|---|---|
| **Schedule** | Presets (hourly / daily / weekdays / weekly) oder One-off-Zeitpunkt; Custom-Cron nachträglich via `/schedule update` | **Min-Intervall 1 Stunde** (häufigere Cron-Expressions werden abgelehnt); Runs starten mit ein paar Minuten Stagger |
| **API** | HTTP-POST auf einen **per-Routine-Endpoint** mit Bearer-Token (= ein geheimer Zugangsschlüssel im Request-Header); ein optionales `text`-Feld gibt dem Run Kontext mit (z.B. einen Alert-Body) | nur im Web anlegbar; das Token wird **einmal** angezeigt; der Endpoint läuft unter einem experimentellen Beta-Header |
| **GitHub-Event** | reagiert auf **Pull-Request-/Release-Events**, optional mit Filtern (Author, Titel, Branch, Labels, Draft/Merged) | die **Claude GitHub App** muss auf dem Repo installiert sein; per-Routine/Account-Hourly-Caps in der Preview |

**One-off-Runs & Kosten:** Ein One-off-Schedule feuert **einmal** zu einem Zeitpunkt (in der CLI per Natural Language, z.B. `/schedule tomorrow at 9am, summarize yesterday's merged PRs`) und deaktiviert sich danach selbst. One-offs zählen **nicht** gegen den **Daily-Run-Cap** pro Account; die Usage selbst zieht wie jede Session von der normalen Subscription ab. *(Quelle: https://code.claude.com/docs/en/routines, abgerufen 2026-07-06)*

**Das Sicherheits-Modell (der wichtigste Absatz):** Routines laufen **autonom, ohne Permission-Prompts** — es gibt keinen Modus-Picker und niemanden, der zwischendrin „Ja" klickt. Die Leitplanke ist deshalb das **Scoping vorab**: nur die wirklich nötigen Repositories und Connectors einbinden und den Network-Access des Cloud-Environments beschränken (Default „**Trusted**": eine Allowlist gängiger Package-Registries und Entwicklungs-Domains, alles andere geblockt). Branch-Schutz: Claude darf per Default **nur auf `claude/`-präfixierte Branches pushen** — außer man aktiviert bewusst „Allow unrestricted branch pushes" pro Repo. Dazu der Doku-Caveat, den man sich merken sollte: **Ein grüner Run-Status heißt nur „ohne Infrastruktur-Fehler beendet", nicht „Task erfolgreich"** — den Transcript des Runs lesen. Und: Eine Routine gehört dem **persönlichen claude.ai-Account** und agiert über die verknüpfte GitHub-Identität — Commits/PRs erscheinen unter deinem Namen. *(Quelle: https://code.claude.com/docs/en/routines, abgerufen 2026-07-06 — primärquellen-belegt)*

> **Einordnung (Synthese, kein Doku-Fakt):** Routines unterstützen **GitHub**-Repos. Liegt dein Code auf einer anderen Plattform als GitHub, sieht eine Routine ihn nur über eine Kopie auf GitHub, und Commits oder PRs, die sie dort erzeugt, fließen nicht automatisch zurück. Für Schreib-Aufgaben ist das ungeeignet, für **Lese-, Analyse- und Report-Aufgaben** auf einer solchen Kopie brauchbar.

### Mechanik (tiefere Ebene)

`/goal` ist im Kern ein **Wrapper über einen prompt-basierten Stop-Hook**: Der Hook **blockt das Ende eines Turns**, solange das Ziel aktiv ist, und gibt erst frei, wenn die Bedingung erfüllt (oder das Ziel gelöscht) ist. `/goal` braucht einen akzeptierten **Trust-Dialog** und ist deaktiviert, wenn Hooks abgeschaltet sind (`disableAllHooks` / `allowManagedHooksOnly`).

**Der einzige echte Low-Level-Runaway-Guard — der Stop-Hook-Override:**

| Mechanismus | Schutz-Grenze | Bedeutung |
|---|---|---|
| **Stop-Hook-Override** (Low-Level) | Claude Code überstimmt den Hook und beendet den Turn nach **mehreren aufeinanderfolgenden Blocks** (Skill-internes Verhalten, in der öffentlichen Doku nicht spezifiziert) | verhindert, dass ein hängender Check den Agenten endlos festhält |
| **Lauf-Begrenzung für `/goal`** | **keine eingebaute Fortsetzungs-Obergrenze** | man begrenzt **in der Condition selbst** — als Turn-/Zeit-Klausel, z.B. „… **or stop after 20 turns**" |

> **Merksatz:** Es gibt **keine** versteckte „X Fortsetzungen"-Grenze für `/goal`. Wer einen Lauf deckeln will, schreibt das **in die Condition** („… or stop after N turns"). Der einzige automatische Notausgang ist der Stop-Hook-Override, der den Turn nach mehreren aufeinanderfolgenden Blocks beendet.

Der **reine Stop-Hook** ist der deterministische Low-Level-Mechanismus: Er führt deinen Check **als Skript** aus und blockt das Turn-Ende, bis er besteht. `/goal` ist die Ein-Zeilen-Bequemlichkeit darüber für Ad-hoc-Aufgaben — kein eigener Guard, sondern derselbe Hook mit prompt-basierter Bedingung.

### Stop-Hook — das kopierbare Skelett (Verification-Leiter Stufe 3)

Stufe 3 der Verification-Leiter (oben) ist der reine Stop-Hook als Skript. So sieht das Minimalgerüst aus. Registriert wird er in `.claude/settings.json` — der Event-Name ist **`Stop`** (großgeschrieben), und die Handler stecken verschachtelt in einem eigenen `hooks`-Array:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": ".claude/hooks/stop.sh", "timeout": 30 }
        ]
      }
    ]
  }
}
```

**Exit-Code-Semantik** (das ist der ganze Steuermechanismus): **exit 0** = erlauben (Claude darf stoppen) · **exit 2** = blockieren (Claude stoppt **nicht**, der `stderr`-Text geht als Feedback zurück an den Agenten) · jeder andere Exit = nicht-blockierender Fehler. Das Skript selbst ist Minimal-Bash:

```bash
#!/usr/bin/env bash
# .claude/hooks/stop.sh — blockiert das Turn-Ende, bis die Tests grün sind
if ! npm test --silent 2>/dev/null; then
  echo "Tests rot — bitte erst reparieren." >&2   # stderr = Feedback an den Agenten
  exit 2   # blockiert: Claude darf NICHT stoppen, arbeitet weiter
fi
exit 0     # erlaubt: Claude darf stoppen
```

> **Endlosschleifen-Schutz (wichtig):** Bei `exit 2` arbeitet Claude weiter — bleibt der Check dauerhaft rot, **loopt der Agent**. Deshalb den Hook deckeln: einen Zähler in einer **State-Datei** mitführen (nach N aufeinanderfolgenden Blocks mit `exit 0` durchwinken) und/oder das `timeout`-Feld nutzen. Das ist die deterministische, selbst-kontrollierte Variante dessen, was der Stop-Hook-Override bei `/goal` automatisch tut.

> **Flüchtige Schicht, Schema geprüft am 2026-09-13 gegen `code.claude.com/docs/en/hooks`.** Event-Name, Feldnamen und Exit-Code-Semantik gehören zur Tooling-Schicht und können sich mit Releases ändern.

### Was startet den nächsten Turn? (drei Mechanismen)

| Mechanismus | Was startet den nächsten Turn | Wofür |
|---|---|---|
| **`/goal`** | Evaluator-Modell sagt „Condition noch nicht erfüllt" | bis ein **Endzustand** erreicht ist |
| **`/loop`** | ein **Takt** feuert (fester Intervall, self-paced oder Maintenance-Prompt) | wiederkehrende Arbeit (z.B. CI-Watch); kann sich self-paced selbst beenden |
| **reiner Stop-Hook** | ein **Skript** (exit-code) blockt das Turn-Ende | wenn der Check **exakt/reproduzierbar** sein muss |

### Headless `/goal`

`/goal` läuft auch headless: `claude -p "/goal …"` fährt den Loop in **einem** Aufruf zu Ende. **Abbruch via `Ctrl+C`.** Bei `--resume`/`--continue` wird das **aktive Ziel wiederhergestellt** (Turn-Count/Timer/Token-Baseline resetten); ein bereits **erreichtes oder gelöschtes** Ziel wird beim Resume **nicht** wiederhergestellt. *(Quelle: https://code.claude.com/docs/en/goal, abgerufen 2026-07-06)*

### Runaway-Abbruch — die Tasten/Befehle konsolidiert

- **Interaktiv:** `Esc` stoppt mitten in der Aktion (Context bleibt erhalten).
- **Headless / `-p`-`/goal`:** `Ctrl+C`.
- **Aktives Ziel löschen:** `/goal clear` (Aliase: `stop`, `off`, `reset`, `none`, `cancel`; auch `/clear` entfernt das Ziel).

> **Hinweis — Runaway-Verhalten hängt vom Loop-Typ ab (fester Takt vs. self-paced):** Bei **festem Takt** (`/loop 5m`) gibt es keinen Low-Level-Runaway-Guard — der Loop läuft, bis man ihn stoppt oder die **7-Tage-Expiry** greift. Ein **self-paced** `/loop "<prompt>"` beendet sich dagegen selbst: Claude ruft `ScheduleWakeup` mit `stop: true` auf und bricht das anstehende Wakeup sofort ab; endet eine Iteration **ohne** neu zu planen oder zu stoppen, plant Claude Code **ein** Fallback-Wakeup (~20 min später) und beendet den Loop, wenn auch diese Iteration nicht neu plant. `Esc` unterbricht eine aktive Iteration bzw. stoppt einen wartenden Loop manuell. Trotzdem gilt: Schreib eine **Turn-Budget-Klausel in den Prompt selbst** („… oder nach N Iterationen") Ein Lauf kann auch durch unzureichende Checks, fehlenden Zugriff oder Toolfehler hängenbleiben. Prüfe die Ursache, statt nur weitere Durchläufe zu erlauben. *(Quelle: code.claude.com/docs/en/scheduled-tasks, Stand 2026-07-07)*

### Wann nutzen — die Verification-Leiter

Die Tabelle zeigt vier technische Möglichkeiten, Ergebnisse zu prüfen. Beginne mit einem passenden Check, dessen Ausgabe du selbst nachvollziehst. Zusätzliche Automatisierung braucht Einrichtung und muss ebenfalls getestet werden. Die drei Lernschritte der [englischen Verification-Leiter](../../tracks/05-verify-and-loop/01-verification-ladder.md) zählen anders; hier geht es um die technischen Werkzeuge.

| Stufe | Mittel | Wann |
|---|---|---|
| 1 | **Im Prompt:** „lauf den Check und iteriere" | für Aufgaben mit einem vorhandenen, geeigneten Check |
| 2 | **Über eine Session:** Check als `/goal`-Condition | Evaluator prüft nach jedem Turn; gut für einen unbeaufsichtigten Lauf |
| 3 | **Deterministisches Gate:** Stop-Hook als Skript | wenn der Check exakt/reproduzierbar sein muss |
| 4 | **Zweite Meinung:** Verifikations-Subagent | frisches Modell widerlegt das Ergebnis (siehe Abschnitt 5) |

> `/goal` und Stop-Hooks können einen Lauf anhand eines Checks fortsetzen oder stoppen. Sie garantieren keine fachliche Richtigkeit: Ein unvollständiger Check kann einen Fehler übersehen.

**Wann NICHT:** Für einen Ein-Satz-Fix oder einen Task, den man ohnehin live beobachtet, ist `/goal` Overkill — der Prompt-Level-Check (Stufe 1) reicht. Und: `/goal` setzt **CC v2.1.139+** voraus (Quelle: https://code.claude.com/docs/en/changelog, abgerufen 2026-09-13) — auf älteren Setups auf reine Stop-Hooks ausweichen.

---

## 3. Lokal vs. Cloud — wo läuft der Agent?

Ein Agent kann auf dem **eigenen Laptop** laufen oder auf einer **entfernten/Cloud-Maschine**. Beides hat Berechtigung.

| Variante | Wo es läuft | Wofür |
|---|---|---|
| **Lokal + Worktrees** | dein Rechner, mehrere CLI-Sessions in isolierten Git-Checkouts | Standard fürs parallele Arbeiten (Abschnitt 4) |
| **Desktop-App** | dein Rechner, mehrere Sessions visuell, je eigener Worktree | mehrere lokale Sessions übersichtlich verwalten |
| **Claude Code on the web** | Anthropic-managed Cloud-Infra in isolierten VMs | Läufe, die nicht an deine Maschine gebunden sein sollen |
| **Agent Teams** (experimental, default off) | automatisierte Koordination mehrerer Sessions (geteilte Tasks, Messaging, Team-Lead) | mehrere Agenten orchestriert zusammenarbeiten lassen (→ Einordnung Abschnitt 4, Vertiefung Abschnitt 7) |
| **Cloud-Routines / Desktop Scheduled Tasks** | Anthropic-managed bzw. lokal geplante, wiederkehrende Läufe (`/schedule`) | geplante/entfernte Automation, die nicht an eine offene Session gebunden ist |

### Cloud heißt nicht automatisch US-Cloud

- Wo ein Agent läuft (lokal oder Cloud) und wo das **Modell** rechnet, sind zwei getrennte Fragen.
- Wenn du oder deine Organisation Vorgaben zum Datenstandort habt, gibt es Alternativen: Modelle, die in der EU gehostet werden, und **Open-Weight-Modelle**, die auf eigener oder EU-gehosteter Infrastruktur laufen können (Beispiele in der Q&A „Welches Modell nehme ich für eine konkrete Aufgabe?“).
- Im Kurs bleiben echte persönliche und vertrauliche Daten draußen. Für genehmigte echte Datenarbeit außerhalb des Kurses müssen zusätzlich Zweck, Verträge und Zugriffe geklärt werden; siehe [Modul 11](./11-kundendaten-testdaten.md).

> **Merksatz:** Cloud ≠ automatisch US-Cloud. Datenstandort ist eine Frage des Modell-Hostings und der Verträge, nicht des Werkzeugs, das du bedienst.

---

## 4. Parallelität & Skalieren — viele Agenten gleichzeitig

### Die vier Parallelisierungs-Wege (Einordnung zuerst)

Claude Code bietet **vier** Wege, mehrere Aufgaben gleichzeitig laufen zu lassen. Sie unterscheiden sich darin, **wer die Arbeit koordiniert** — Claude im Gespräch, du selbst, ein Lead-Agent oder ein Script:

> **Nicht verwechseln:** Die **4-Wege-Matrix in Abschnitt 2** hält *einen* Agenten am Laufen (Frage: *was triggert den nächsten Turn?*). Die vier Wege **hier** lassen *mehrere* Agenten gleichzeitig arbeiten (Frage: *wer koordiniert?*). Zwei verschiedene Vierer-Tabellen für zwei verschiedene Probleme.

| Weg | Was es ist | Wann nehmen |
|---|---|---|
| **Subagents** | delegierte Worker **innerhalb einer Session** — erledigen eine Seitenaufgabe im eigenen Context und liefern nur eine Zusammenfassung zurück (Grundlagen & eigene Subagents als Datei → [Modul 7](./07-agenten-grundlagen.md)) | wenn eine Seitenaufgabe die Haupt-Konversation mit Suchergebnissen/Logs fluten würde |
| **Agent View** (`claude agents`, Research Preview) | **ein Bildschirm** zum Dispatchen und Beobachten von Background-Sessions; jede dispatchte Session bekommt automatisch einen eigenen Worktree | mehrere **unabhängige** Tasks abgeben, Status auf einen Blick prüfen, nur eingreifen, wenn eine Session dich braucht |
| **Agent Teams** (experimental, **default off**) | mehrere koordinierte Sessions mit geteilter Task-Liste und Inter-Agent-Messaging, gemanagt von einem Lead; aktivierbar via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | wenn Claude ein Projekt selbst zerlegen, zuweisen und die Worker synchron halten soll (Vertiefung → Abschnitt 7) |
| **Dynamic Workflows** | ein **Script**, das viele Subagents fährt und Ergebnisse gegeneinander prüft (Vertiefung → unten in diesem Abschnitt) | wenn der Job eine Handvoll Subagents sprengt oder Findings verifiziert werden sollen: Codebase-Audit, 500-Dateien-Migration, cross-checked Research |

Zwei Werkzeuge stützen das, ohne selbst ein „Weg" zu sein: **Worktrees** geben jeder Session einen eigenen Git-Checkout (das Kernmuster gleich unten), und der **`/batch`-Skill** lässt Claude eine große Änderung in **5–30 worktree-isolierte Subagents** zerlegen, die **je einen eigenen PR** öffnen — eine verpackte Kombination aus Subagents + Worktrees, kein eigener Koordinationsstil. Achtung, Verwechslungsgefahr (flüchtig, Stand 2026-07-06): Seit **v2.1.198** öffnet `/agents` **kein Panel mehr** — es zeigt nur noch einen Hinweis auf die Subagent-Dateipfade; **`claude agents`** (Agent View) ist trotz des ähnlichen Namens davon **getrennt**. Und für alle vier Wege gilt: mehr Parallelität = multiplizierter Token-Verbrauch. *(Quelle: https://code.claude.com/docs/en/agents, abgerufen 2026-07-06)*

> **Merksatz:** Die Frage ist nie „wie viele Agenten kriege ich an?", sondern „**wer koordiniert**?" — Claude im Gespräch (Subagents), du selbst (Agent View + Worktrees), ein Lead-Agent (Agent Teams) oder ein Script (Workflows).

### Git-Worktrees (das Kernmuster)

Ein **Worktree** ist ein **separates Arbeitsverzeichnis mit eigenem Branch**, das aber History und Remote des Repos teilt. Steckt jede Session in ihrem eigenen Worktree, **kollidieren die Edits nicht**: Ein Agent baut Feature A, ein zweiter fixt parallel Bug B — ohne sich gegenseitig die Dateien zu überschreiben.

**Die Befehle (Kernablauf):**

```bash
git worktree add -b feat/auth-redesign ../feat-auth # neuen Branch feat/auth-redesign + Worktree in ../feat-auth anlegen
git worktree list                                   # alle aktiven Worktrees anzeigen
git worktree remove ../feat-auth                    # Worktree aufräumen (der Branch bleibt erhalten)
```

Jede `claude`-Session läuft dann in ihrem eigenen Ordner (`cd ../feat-auth && claude`); alle Worktrees teilen History + Remote → paralleles Fan-out **ohne Branch-Wechsel und ohne Konflikte**. `git worktree` selbst ist stabiles Git (kein SaaS, kein Versions-Caveat). *(Quelle: git-scm.com/docs/git-worktree · code.claude.com/docs/en/worktrees)*

> **Flüchtig (Stand 06/2026):** Claude Code bringt als Bequemlichkeit den Shortcut `claude --worktree <name>` mit, der Worktree-Anlage und Session-Start in einem Schritt erledigt — dieser Shortcut gehört zur Tooling-Schicht (prüfen via `code.claude.com/docs/en/worktrees`), die `git worktree`-Befehle darunter nicht.

**Praktische Limits (Erfahrungswerte, ohne öffentliche Quelle):**

- **2–4 parallele Sessions** sind sinnvoll; mehr nur in Ausnahmen (Hardware-/Review-Kapazität klar kalkulieren, 5+ führt schnell zu Rate-Limits und unübersichtlichem Review).
- **Vor dem Start committen oder stashen** — sonst zieht man ungesicherte Änderungen in den neuen Worktree.
- Eine **steckengebliebene Session** (≈10 Min am selben Problem) killen und mit anderer Framing-Variante neu starten, statt sie weiterkämpfen zu lassen.

> Ein Worktree gibt jedem Agenten eine eigene Arbeitskopie. Teile auch die Aufgaben auf und prüfe vor dem Zusammenführen, ob die Änderungen zusammenpassen. Getrennte Ordner lösen inhaltliche Konflikte nicht automatisch.

### Fan-out at scale (Migrationen)

Das Muster für „dieselbe Änderung über sehr viele Dateien" (z.B. eine Framework-Migration über 200 Dateien):

1. Den Agenten **eine Task-Liste generieren** lassen (alle betroffenen Dateien).
2. In einem **Skript über die Liste loopen** — pro Datei ein Headless-Aufruf (`claude -p` bei Claude Code, `codex exec` bei Codex; Abschnitt 1).
3. **Erst an 2–3 Dateien verfeinern**, bis das Ergebnis stimmt — **dann** auf die volle Menge loslassen.
4. Permissions für den unbeaufsichtigten Batch **scopen** mit `--allowedTools`, z.B. `--allowedTools "Edit,Bash(git commit *)"` — der Agent darf dann nur das, was der Job braucht. Prüfe die tatsächlich erlaubten Aktionen; eine Tool-Allowlist ist allein noch keine Begrenzung auf bestimmte Dateien oder einen bestimmten Branch.

### Fehlerbehandlung im Fan-out (Datei 42/200 schlägt fehl)

Bei vielen Aufrufen musst du Fehler erkennen und betroffene Dateien wiederfinden können. Bereite die Erfassung vor dem großen Lauf vor:

- Jeden Aufruf anweisen, **„Return OK or FAIL"** auszugeben. Speichere zusätzlich Dateiname, Rückgabestatus und tatsächlichen Check-Output. Das Endwort allein ist nur eine Behauptung des Agenten.
- Die fehlgeschlagenen Dateien filtern (`grep FAIL` über die gesammelten Outputs) und **gezielt nachfahren** — nicht den ganzen Batch wiederholen.
- Auch nach einem erfolgreichen Versuch an **2–3 Dateien** können systematische Fehler auftreten. Bei wiederholtem gleichen Fehler den Batch stoppen, Ursache prüfen und die betroffenen Ergebnisse erneut kontrollieren.

> Nutze OK/FAIL zum Sortieren. Prüfe auch als OK gemeldete Änderungen anhand der tatsächlichen Checks und des gesamten Diffs; wenige FAILs beweisen nicht, dass der Rest korrekt ist.

### Dynamische Workflows — das Script hält den Plan

Fan-out per Shell-Skript (oben) ist das Do-it-yourself-Muster. **Dynamic Workflows** sind die eingebaute Weiterentwicklung: ein **JavaScript-Script, das Aufgaben auf Subagents verteilt und Ergebnisse zusammenführt** — aber du schreibst es nicht selbst. **Claude schreibt das Script für die Aufgabe, die du beschreibst**, und eine **Laufzeitumgebung (Runtime)** führt es **im Hintergrund** aus, während deine Session frei bleibt. Der entscheidende Architektur-Unterschied: **Zwischenergebnisse leben in Script-Variablen statt im Context Window** — Claudes Context hält am Ende nur das Endergebnis, nicht die 200 Einzelbefunde. Jeder Run schreibt das generierte Script zudem als Datei ins Session-Verzeichnis (`~/.claude/projects/…`) — man kann es lesen, gegen einen früheren Run diffen oder editiert neu starten lassen. *(Quelle: https://code.claude.com/docs/en/workflows, abgerufen 2026-07-06)*

**Wichtig zur Einordnung: Workflows laufen LOKAL** auf deinem Rechner — nicht in der Anthropic-Cloud (das ist der Unterschied zu Cloud-Routines, Abschnitt 2). Diese Laufzeitumgebung begrenzt auf **max. 16 gleichzeitige Agents** (weniger auf Maschinen mit wenigen CPU-Cores) und **1.000 Agents pro Run** (begrenzt die Anzahl gestarteter Agents). Das Script selbst hat **keinen direkten Filesystem-/Shell-Zugriff** — lesen, schreiben und Befehle ausführen tun die Agents, das Script koordiniert nur. Mid-Run-User-Input gibt es nicht: Wer ein Sign-off zwischen Etappen will, fährt jede Etappe als eigenen Workflow.

> **Merksatz für Nicht-Devs:** Ein Workflow ist ein **Arbeitsplan als Programm**: Claude schreibt den Plan einmal auf (welche Helfer, in welcher Reihenfolge, was mit den Ergebnissen passiert), und dann arbeitet eine Maschine den Plan ab — nachlesbar, wiederholbar, und ohne dass die vielen Zwischenschritte das Gespräch fluten.

**„Wer hält den Plan?" — die Abgrenzung** (kompakt eingedeutscht aus der Doku-Tabelle):

| Ansatz | Wer entscheidet den nächsten Schritt | Wo Zwischenergebnisse leben | Skala pro Lauf |
|---|---|---|---|
| **Subagents** | Claude, Turn für Turn | Claudes Context Window | ein paar delegierte Tasks pro Turn |
| **Skills** | Claude, dem Prompt folgend | Claudes Context Window | wie Subagents |
| **Agent Teams** | der Lead-Agent, Turn für Turn | eine geteilte Task-Liste | eine Handvoll langlaufender Peers |
| **Workflows** | **das Script** | **Script-Variablen** | **Dutzende bis Hunderte Agents** |

Weil der Plan im Code liegt, kann ein Workflow auch ein **wiederholbares Qualitätsmuster** fahren, nicht nur „mehr Agents": Unabhängige Agents prüfen die Findings der anderen **adversarial** gegen, bevor sie gemeldet werden — oder ein Plan wird aus mehreren unabhängigen Blickwinkeln entworfen und gegeneinander abgewogen. Das ist die Script-gewordene Form des Writer/Reviewer-Patterns aus Abschnitt 5.

### Workflows bedienen — starten, beobachten, speichern

**Starten (Trigger — flüchtige Schicht, Stand 2026-07-06):**

- **Keyword `ultracode` im Prompt** (z.B. `ultracode: audit every API endpoint under src/routes/ for missing auth checks`) — oder einfach **natürlichsprachlich** („use a workflow …"): Claude behandelt die direkte Bitte als dasselbe Opt-in. **Früher war das wörtliche Trigger-Keyword `workflow`**; Natural Language funktioniert in beiden Fällen. Versehentlich getriggert? `Option+W` (macOS) / `Alt+W` verwirft das Keyword-Highlight für diesen Prompt.
- **`/effort ultracode`** ist das **Session-Setting** darüber: kombiniert `xhigh`-Reasoning-Effort mit automatischer Workflow-Orchestrierung — Claude plant dann **für jede substanzielle Aufgabe** selbst einen Workflow (auch mehrere in Folge: verstehen → ändern → verifizieren). Kostet spürbar mehr Tokens und Zeit; gilt für die laufende Session und resettet danach (`/effort high` zum Zurückschalten).
- **Bundled Workflow `/deep-research <Frage>`:** fächert Web-Suchen über mehrere Blickwinkel auf, prüft die gefundenen Quellen gegeneinander und liefert einen **zitierten Report**, in dem Claims, die den Cross-Check nicht überlebt haben, bereits herausgefiltert sind (setzt das WebSearch-Tool voraus). Der schnellste Weg, einen Workflow live zu sehen.

**Beobachten (`/workflows`):** listet laufende und fertige Runs; die Progress-View zeigt **jede Phase mit Agent-Zahl, Token-Summe und Laufzeit**, mit Drill-down bis in den einzelnen Agent (Prompt, letzte Tool-Calls, Ergebnis). Steuerung: `p` pausiert/resumed den Run, `x` stoppt den gewählten Agent oder den ganzen Workflow, `r` restartet einen laufenden Agent, `s` speichert das Script (siehe unten). Eine Ein-Zeilen-Progress-Anzeige erscheint zusätzlich im Task-Panel unter der Eingabezeile.

**Approval je Permission-Mode (Kurzfassung — die Modi selbst erklärt Abschnitt 7):** In Manual (früher `default`) und `acceptEdits` wird **jeder Run** bestätigt (mit „Yes, and don't ask again"-Option pro Workflow und Projekt); in `auto` nur der **erste Launch** (und unter `/effort ultracode` gar nicht); in `bypassPermissions` / `claude -p` / Agent SDK **nie**. Unabhängig vom Modus gilt: **Die vom Workflow gespawnten Subagents laufen immer in `acceptEdits` und erben deine Tool-Allowlist** — File-Edits sind auto-approved, aber nicht-allowgelistete Shell-/Web-/MCP-Calls können **mid-run** prompten. Vor einem langen Lauf also die benötigten Befehle in die Allowlist aufnehmen.

**Speichern & wiederverwenden:** Im `/workflows`-View den Run wählen und **`s`** drücken → Speicherort per Tab wählen: **`.claude/workflows/`** im Projekt (geteilt mit allen, die das Repo klonen) oder **`~/.claude/workflows/`** (persönlich, in jedem Projekt verfügbar). Danach läuft der Workflow als eigener **`/<name>`-Command**; teilen sich Projekt- und persönlicher Workflow einen Namen, gewinnt der Projekt-Workflow. Input übergibt man beim Aufruf über den **`args`-Parameter** — das Script liest ihn als Global `args` (strukturierte Daten, kein Parsen nötig), z.B. `Run /triage-issues on issues 1024, 1025, and 1030`.

**Resume:** Gestoppte Runs lassen sich fortsetzen — **bereits fertige Agents liefern ihre gecachten Ergebnisse**, der Rest läuft live. Das funktioniert aber **nur innerhalb derselben Session**: Wer Claude Code beendet, startet den Workflow in der nächsten Session frisch.

**Kosten-Praxis, Voraussetzungen, Abschalten:**

- **Erst auf einem kleinen Slice testen** (ein Verzeichnis statt des ganzen Repos, eine enge Frage statt einer breiten) — dann erst die volle Menge. Der `/workflows`-View zeigt den Token-Verbrauch pro Agent live; Stoppen geht jederzeit, ohne fertige Arbeit zu verlieren.
- **`/model` vor großen Runs prüfen:** Jeder Agent nutzt das Session-Modell, sofern das Script keine Stage anders routet.
- Die **Agent-Caps** (16 concurrent / 1.000 pro Run) begrenzen die Anzahl der Agents, sind aber kein Geld- oder Zeitlimit. Runs zählen normal gegen Plan-Usage und Rate-Limits; lege Kosten- und Stoppgrenzen zusätzlich fest.
- **Voraussetzungen (flüchtig, Stand 2026-07-06):** CC **v2.1.154+** (eingeführt mit v2.1.154, [Changelog](https://code.claude.com/docs/en/changelog)), alle **Paid-Plans** (auf **Pro** in `/config` unter „Dynamic workflows" einschalten); auch mit Anthropic-API-Zugang sowie auf Bedrock/Google Agent Platform/Microsoft Foundry.
- **Abschalten:** Toggle in `/config`, `"disableWorkflows": true` in `~/.claude/settings.json`, Umgebungsvariable `CLAUDE_CODE_DISABLE_WORKFLOWS=1` — oder org-weit via Managed Settings. Abgeschaltet heißt: Bundled-Commands weg, `ultracode`-Keyword triggert nicht mehr, `ultracode` fehlt im `/effort`-Menü.

**Beispiel-Prompts (Synthese):**

```text
> use a workflow to audit every Markdown file under docs/ for broken links and stale version claims, and adversarially verify each finding before reporting it
```

```text
> use a workflow: run the test suite and keep fixing the reported errors until it passes or two rounds in a row make no progress
```

```text
> use a workflow to migrate every GitHub Actions workflow in this repo from Node 20 to Node 22, working on each file in its own isolated copy, and verify each result
```

*(Quelle für den gesamten Workflow-Abschnitt: https://code.claude.com/docs/en/workflows, abgerufen 2026-07-06 — primärquellen-belegt; nur die Beispiel-Formulierungen oben sind Synthese.)*

---

## 5. Writer/Reviewer — Verifikation durch frischen Context

**Kernidee:** Ein zweiter Agent prüft die Änderung mit einem frischen Blick. Er kann Fehler finden, die der ersten Session entgangen sind. Auch er kann sich irren oder dieselbe falsche Annahme treffen.

**Writer/Reviewer (zwei Sessions):**

- **Session A** implementiert.
- **Session B** reviewt explizit die geänderte Datei: „look for edge cases, race conditions, consistency with existing patterns".
- **A** bekommt das Feedback und behebt.
- Analog für Tests: ein Agent schreibt die Tests, ein anderer schreibt den Code, der sie besteht.

**Adversarialer Review-Subagent:** Vor „fertig" lässt man einen **Subagent den Diff in frischem Context** gegen den Plan prüfen — er sieht nur **Diff + Kriterien**, nicht das Reasoning, das ihn erzeugt hat. Gebündelt dafür: der **`/code-review`-Skill** (Korrektheits-Check des aktuellen Diffs in frischem Subagent). Er nimmt ein **Effort-Level** (`low|medium|high|xhigh|max|ultra`) und kann mit **`--fix`** die Befunde direkt auf den Arbeitsstand anwenden bzw. mit **`--comment`** als Inline-PR-Kommentare posten. *(Quelle: code.claude.com/docs/en/commands)*

### Reviewer-Kalibrierung (nicht überkritisch)

Ein Reviewer kann auch unbegründete Probleme melden, besonders wenn er ausdrücklich eine lange Liste von Lücken liefern soll. Gib ihm stattdessen einen begrenzten Prüfauftrag:

- Den Reviewer explizit anweisen: **nur konkrete Probleme nennen, die Korrektheit oder die genannten Anforderungen betreffen** — der Rest gilt als optional.
- So vermeidet man **Over-Engineering** als Folgeschaden: zusätzliche Abstraktionen, defensiver Code für unmögliche Fälle, Tests für Situationen, die nie eintreten.

> Verlange Dateistelle, beobachtbares Problem und Begründung. „Keine weiteren Befunde" ist ein gültiges Ergebnis. Stilvorlieben sind kein Fehler.

Prüfe die tatsächlichen Änderungen und Ausgaben: ausgeführter Befehl, Rückgabewert, Test-Output oder Screenshot. Bei wichtigen Ergebnissen führe einen passenden Check selbst erneut aus. Dass zwei Agenten zustimmen, ersetzt diese Prüfung nicht.

---

## 6. Die Disziplinen dahinter (vertiefend)

Wenn lange Läufe unübersichtlich werden, hilft oft eine kleinere Aufgabe oder besser ausgewählte Information. Wie du Projektanweisungen pflegst und Arbeitsstände zwischen Sessions erhältst, erklärt das nächste Modul.

→ **Ausgelagert nach [Modul 10 — Kontext-Engineering](./10-kontext-engineering.md):** die vier Disziplinen Context Engineering, Autonomy-Slider, Long-horizon Memory und „Build for agents" — dazu, neu, Boris Chernys YC-Auftritt zum 80%-System-Prompt-Cut (Ablation, 6-Monats-Regel, Kontext-Budget, Eval-Halbwertszeit, Aufgaben-Kalibrierung, Verification als wichtigster Hebel).

---

## 7. Org-Level-Scaling — vom Einzelnen zum Team

Skalierung ist nicht nur „mehr Agenten", sondern **gemeinsame Standards**, damit alle im Team konsistent arbeiten.

### `CLAUDE.md`-Hierarchie — wer teilt was im Team

`CLAUDE.md` wird zu Beginn **jeder** Konversation geladen = persistenter Projekt-Context. Sie skaliert über eine **Hierarchie**:

| Ebene | Datei | Zweck |
|---|---|---|
| Global | `~/.claude/CLAUDE.md` | persönliche Defaults über alle Projekte |
| Team | `./CLAUDE.md` (ins Git) | Projekt-Standards, gemeinsam kuratiert |
| Persönlich | `./CLAUDE.local.md` (gitignored) | eigene Notizen, nicht geteilt |
| Monorepo | Parent-/Child-Dirs | pro Unterprojekt eigene `CLAUDE.md` |

- **Ins Git.** Das Team kuratiert die `./CLAUDE.md` gemeinsam; sie „compounds in value over time" — je länger gepflegt, desto wertvoller.

> **Merksatz:** Eine gemeinsam gepflegte `CLAUDE.md` hält bestätigtes Projektwissen für neue Sessions fest — die Pflege-Disziplin dahinter (Pruning-Test, modulare Imports, Compaction-Tuning) steht in [Modul 10 — Kontext-Engineering](./10-kontext-engineering.md).

### Geteilte Bausteine & Agent Teams

**Geteilte Skills-/Hooks-Libraries** machen Org-Standards und Konventionen zu wiederverwendbaren Bausteinen — einmal definiert, im ganzen Team nutzbar.

**Plugins — die Verpackung für geteilte Bausteine.** Ein Plugin bündelt mehrere Bausteine zu **einer installierbaren Einheit**: Skills, Hooks, Subagent-Definitionen und MCP-Server-Definitionen liegen gemeinsam in einem Paket. Statt jedes Teammitglied einzeln Skills und Hooks einrichten zu lassen, installiert man **ein** Plugin und hat den ganzen Stack — den Review-Skill, die Pre-Commit-Hooks, die Subagent-Rollen, die MCP-Anbindung. Plugins werden über ein **Marketplace**-Repo verteilt; so wird eine kuratierte Org-Toolchain mit einem Befehl reproduzierbar. Das ist der Org-Level-Hebel über der einzelnen `CLAUDE.md`: nicht nur geteilter *Context*, sondern geteilte *Fähigkeiten*.

**Agent Teams — Subagents, die sich selbst koordinieren.** Bisher hieß Parallelität: *du* startest mehrere Sessions in Worktrees (Abschnitt 4) und reviewst ihre Ergebnisse. Agent Teams heben das auf die nächste Stufe — eine **automatisierte Koordination mehrerer Sessions**: Die Doku beschreibt sie als „automated coordination of multiple sessions with shared tasks, messaging, and a team lead". Konkret heißt das:

- **Shared tasks** — eine gemeinsame Aufgabenliste, aus der sich die Agenten bedienen, statt dass du jeden einzeln briefst.
- **Messaging** — die Agenten **tauschen Nachrichten untereinander** aus (z.B. „Datei X ist fertig, du kannst aufbauen"), statt nur isoliert zu laufen.
- **Team Lead** — ein **koordinierender Agent**, der die Tasks verteilt und die Ergebnisse zusammenführt — die Orchestrierungs-Rolle, die du sonst von Hand machst.

Damit lässt sich z.B. der adversariale Review-Loop (Abschnitt 5) über viele Tasks **am Laufen halten, ohne dass du jede Übergabe manuell taktest**. Status (flüchtig, Stand 2026-07-06): Agent Teams sind **experimental und per Default abgeschaltet** — aktiviert wird über `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` (settings.json oder Env); ohne die Variable wird kein Team aufgesetzt und Claude schlägt keine Teammates vor. Wichtiger Praxis-Caveat: **Teammates sind nicht worktree-isoliert** — die Arbeit so partitionieren, dass jeder Teammate eigene Dateien besitzt (Einordnung gegenüber Subagents/Agent View/Workflows → Tabelle „Die vier Parallelisierungs-Wege" in Abschnitt 4). Es bleibt aber dieselbe Disziplin: mehr automatisierte Koordination = mehr Output, der reviewt werden muss — die Leitplanken aus Abschnitt 5 gelten unverändert. *(Quelle: https://code.claude.com/docs/en/agent-teams · https://code.claude.com/docs/en/agents, abgerufen 2026-07-06)*

### Reibung senken ohne Kontrollverlust

| Mechanismus | Befehl | Was es tut |
|---|---|---|
| **Permission-Allowlist** | `/permissions` | bestimmte sichere Tools dauerhaft erlauben (`npm run lint`, `git commit`) |
| **Auto-Mode** | `claude --permission-mode auto` (oder im Shift+Tab-Zyklus) | ein **server-seitiges Classifier-Modell** prüft Befehle vorab und blockt nur Riskantes — Scope-Escalation, unbekannte Infra, hostile-content-getriebene Aktionen **und explizit destruktive `git`- und IaC-Befehle** (destruktive `git`-Befehle laut [Changelog](https://code.claude.com/docs/en/changelog) seit v2.1.183) (`git reset --hard`, `git checkout -- .`, `git restore .`, `git clean -fd`, `git stash drop/clear`; `terraform/pulumi/cdk/terragrunt destroy`), wenn nicht explizit angefragt. Bei `-p`-Läufen bricht Auto-Mode ab, wenn der Classifier **wiederholt** blockt (Schwelle laut Doku: **3× in Folge ODER 20× insgesamt** → Pause/Fallback; im `-p`-Modus Abbruch, weil kein User zum Zurückfallen da ist; die Schwellen sind nicht konfigurierbar) |
| **Sandboxing** | `/sandbox` | OS-Level-Isolation: Filesystem/Network restringiert |

> **Auto Mode konkret (Stand 2026-09-13):** Auf **Pro, Max und Team** startet Claude Code ab **v2.1.228** (macOS/Linux/WSL) bzw. **v2.1.233** (Windows nativ) im **Auto Mode**; der frühere Modus `default` heißt jetzt **Manual** (Quelle: https://code.claude.com/docs/en/permission-modes, abgerufen 2026-09-13). Auto Mode liegt im **Shift+Tab-Zyklus** der Permission-Modi (`Manual → acceptEdits → plan`; `auto`/`bypassPermissions` am Zyklus-Ende, sofern freigeschaltet). `claude --permission-mode auto` startet die Session **direkt** in diesem Modus. Der vorausprüfende Classifier ist ein **server-seitiges Modell, unabhängig von deiner `/model`-Wahl**; der Modellname wird hier bewusst nicht festgeschrieben (flüchtig). Auf **Bedrock, Google Cloud's Agent Platform (früher Vertex) und Foundry** ist Auto Mode inzwischen **standardmäßig** im Shift+Tab-Zyklus verfügbar; die frühere Pflicht-Variable `CLAUDE_CODE_ENABLE_AUTO_MODE=1` ist **seit v2.1.207 wirkungslos** (No-op, nur noch aus Kompatibilitätsgründen akzeptiert). *(Quelle: https://code.claude.com/docs/en/permission-modes · https://code.claude.com/docs/en/cli-reference, abgerufen 2026-09-13)*

### Die Permission-Modi im Überblick

Permissions sind der zentrale Sicherheitshebel beim Skalieren: Je mehr unbeaufsichtigt läuft, desto bewusster muss man den Modus wählen. **Shift+Tab** zykliert durch die Modi; mit `claude --permission-mode <modus>` startet man direkt in einem.

| Modus | Was er tut | Wofür / Wann |
|---|---|---|
| Manual (früher `default`) | fragt vor jeder nicht erlaubten Aktion nach | wenn du jeden Schritt selbst bestätigen willst |
| `acceptEdits` | Datei-Edits ohne Rückfrage, Befehle weiter mit Nachfrage | wenn die Edits klar sind, Befehle aber kontrolliert bleiben sollen |
| `plan` | **read-only** — nur lesen/planen, keine Schreib- oder Befehlsaktionen | erst verstehen/planen lassen, bevor etwas verändert wird |
| `auto` | Auto-Approve mit **server-seitigen Safety-Checks** (Classifier blockt nur Riskantes) | Startmodus auf Pro/Max/Team ab v2.1.228 (macOS/Linux/WSL) bzw. v2.1.233 (Windows nativ), [Quelle](https://code.claude.com/docs/en/permission-modes); unbeaufsichtigte Läufe mit Leitplanke (siehe Auto-Mode-Box oben) |
| `dontAsk` | fragt nicht nach, **ohne** den server-seitigen Safety-Classifier | nur in kontrollierten Umgebungen — kein Riskanten-Filter |
| `bypassPermissions` | **alle** Permission-Checks aus | **nur in Container/VM** — niemals auf Maschinen mit echten Daten/Keys |

> **Frische-Hinweis (Stand 2026-07-30):** Auto Mode aktiviert man über **`--permission-mode auto`** bzw. den **Shift+Tab-Zyklus** — nicht über ein eigenes Aktivierungs-Flag. (Ein älteres `--enable-auto-mode`-Flag ist laut cli-reference **„Removed in v2.1.111"** — primärquellen-belegt, vom Changelog bestätigt.) Auf **Bedrock, Google Cloud's Agent Platform (früher Vertex) und Foundry** ist es **standardmäßig** im Shift+Tab-Zyklus verfügbar — die frühere Pflicht-Variable `CLAUDE_CODE_ENABLE_AUTO_MODE=1` (ab **v2.1.158 laut Doku**) ist **seit v2.1.207 wirkungslos** (No-op); unterstützt werden dort nur **Sonnet 5, Opus 4.7 or later und Fable 5**. **Plain-language:** Die obere Hälfte der Tabelle (Manual/`acceptEdits`/`plan`/`auto`) eskaliert *behutsam* — mehr Tempo, aber mit Filter. Die untere Hälfte (`dontAsk`/`bypassPermissions`) schaltet die Filter ab und gehört ausschließlich in eine wegwerfbare Sandbox/VM. *(Quelle: https://code.claude.com/docs/en/permission-modes · https://code.claude.com/docs/en/cli-reference · claude.com/blog/auto-mode, abgerufen 2026-07-30; Versionsangaben v2.1.111, v2.1.158 und v2.1.207 geprüft 2026-09-13)*

**Ein allgemeines Prinzip:** Ein Assistent, der nur chatten soll, bekommt auch nur Chat: keine Shell-, Datei- oder Plugin-Operationen, kein Arbeitsverzeichnis, strenger Sandbox-Modus. Mehr Fähigkeiten bekommt er erst, wenn Review und Guardrails mitgewachsen sind.

Je mehr Änderungen entstehen, desto mehr muss geprüft werden. Plane dafür Zeit und passende Checks ein. Anforderungen wie Passwort-Hashing, Schutz vor Injection und sichere Sessions gehören ausdrücklich in die Aufgabe, wenn das Produkt sie braucht.

> **Merksatz:** „Vibe-Coding in Produktion ist riskant." Skalieren multipliziert auch Fehler — die Leitplanken sind kein Add-on, sondern Voraussetzung.

---

## Q&A

> **Nicht-Devs — Lesehilfe:** Viele der folgenden Antworten sind Dev-Mechanik (Befehle, Flags, Versionsnummern). Fürs Konzept genügt die 4-Wege-Matrix am Anfang von Abschnitt 2 — die Q&A hier gezielt nachschlagen, nicht linear durcharbeiten.

### Power-User-Praxis

**Wie halte ich lange Agent-Sessions arbeitsfähig, ohne dass Context und Richtung zerfasern?**

Ich behandle eine lange Session nicht als endlosen Chat, sondern als Abfolge klarer Meilensteine. Nach jedem Meilenstein lasse ich Tests oder andere Checks laufen, prüfe den Diff und sichere einen nachvollziehbaren Zwischenstand. Entscheidungen, offene Punkte und der nächste Schritt gehören in eine Datei oder einen Commit und nicht nur in den Session-Verlauf. Wenn sich das Ziel deutlich ändert, der Context überwiegend aus überholter Vorgeschichte besteht oder ein unabhängiger Review ansteht, starte ich bewusst eine frische Session. Das ist kein Wissensverlust, solange der relevante Stand im Repo dokumentiert ist. Claude Code empfiehlt dafür u.a. `/clear` zwischen unabhängigen Aufgaben; Codex trennt zusammengehörige Long-running Work von unabhängigen Tasks ebenfalls über Chats und Worktrees. *(Quellen: [Claude Code — Kosten und Context verwalten](https://code.claude.com/docs/en/costs) · [Codex — Long-running Work](https://learn.chatgpt.com/docs/long-running-work))*

**Wann lohnt sich ein höheres Max-/Power-Tier?**

Ich sehe ein höheres Tier als **Kapazitätsentscheidung, nicht als Qualitätsversprechen**. Vor einem Upgrade prüfe ich zuerst, ob zu große Scopes, unnötig hoher Reasoning-Effort, ein überdimensioniertes Modell, viele parallele Agents oder wiederholte Fehlversuche den Verbrauch treiben. Erst wenn sinnvoll geschnittene Tasks und passende Modelle vorhanden sind, Usage-Limits aber trotzdem regelmäßig geplante Arbeit unterbrechen, ist mehr Kapazität wirtschaftlich plausibel. Messen statt schätzen: Bei Claude Code zeigt `/usage` die Plan-Nutzung und Session-Statistik; `/cost` ist ein Alias. Die konkreten Tier-Namen, Preise und Limits sind flüchtig und gehören deshalb über die aktuellen Anbieter-Seiten geprüft. *(Quellen: [Claude Code — Kosten verwalten](https://code.claude.com/docs/en/costs) · [Claude — Plans & Pricing](https://claude.com/pricing) · [Claude Code — Model Configuration](https://code.claude.com/docs/en/model-config))*

**Welches Modell nehme ich für eine konkrete Aufgabe?**

Es gibt kein Einheitsmodell für alle Aufgaben. Die wichtigste Regel ist: **Nimm für die konkrete Aufgabe das Modell, das zuverlässig das beste Ergebnis liefert.** Erst wenn die Qualität passt, optimiere auf Geschwindigkeit, Verbrauch oder Betriebsaufwand. Das größte Modell ist nicht automatisch immer das beste: Für einen schwierigen Architekturentscheid lohnt sich mehr Reasoning, für hundert einfache Klassifikationen meist nicht.

| Aufgabe | Gute Startkandidaten | Warum |
|---|---|---|
| Sehr schwieriges Coding, Architektur, hartnäckige Fehlersuche oder lange autonome Läufe | `Claude Fable 5.1` / `Claude Opus 5`, `GPT-6 Astra` | Hier zählen möglichst starke Analyse und verlässliche Arbeit über viele Schritte. |
| Alltägliches Coding, Refactoring und Reviews | `Claude Sonnet 5`, `GPT-5.6 Terra` | Starke Allrounder für die meisten Repo-Aufgaben. |
| Einfache, klar prüfbare oder sehr häufige Aufgaben | `Claude Haiku`, `GPT-5.6 Luna` | Schnellere Modelle sind sinnvoll, sobald ein Test zeigt, dass ihre Qualität ausreicht. |
| Open-weight Coding-Agenten testen | `Devstral 2` / `Devstral Small 2`, `Qwen3-Coder-Next` | Speziell für Coding und Agent-Loops entwickelt; sie können auf eigener oder EU-gehosteter Infrastruktur betrieben werden. |
| Open-weight Reasoning und Tool Use testen | `gpt-oss-120b`, `gpt-oss-20b` | Können auf eigener Infrastruktur laufen und angepasst werden; sie sind nicht Teil von ChatGPT oder der OpenAI API. |

Die Beispiele oben sind **Startpunkte, kein Ranking und keine Freigabeliste**. Die GPT-5.6-Namen stammen vom Stand 2026-07-17, GPT-6 Astra ist seit 2026-09-04 Codex-Default (ab Codex CLI 0.153.4). Modellversionen ändern sich: Aktuelle Anbietermodelle stehen im jeweiligen Model Picker. *(Quellen: [Claude Code — Model Configuration](https://code.claude.com/docs/en/model-config) · [Codex — Models und Usage](https://learn.chatgpt.com/docs/pricing) · [Mistral — Devstral 2](https://mistral.ai/news/devstral-2-vibe-cli/) · [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) · [OpenAI — gpt-oss](https://openai.com/index/introducing-gpt-oss/) · [Codex — Changelog](https://learn.chatgpt.com/docs/changelog); Stand 2026-07-17, Codex-Default geprüft 2026-09-13)*

**Muss ich EU- oder Open-Weight-Modelle nutzen?**

Nicht grundsätzlich. Wähle das Modell, das zur Aufgabe, zu den Daten und zum gewünschten Ergebnis passt. Für Übungen mit erfundenen oder öffentlichen Daten können das zum Beispiel Claude- oder GPT-Modelle sein. Einzelne Projekte, Kund:innen oder Organisationen können aber klare Regeln für Datenstandort und Hosting haben. Wenn du oder deine Organisation solche Vorgaben habt, gehen sie vor.

Open-Weight-Modelle sind interessant, wenn du sie auf kontrollierter Infrastruktur betreiben, anpassen oder unabhängig von einem einzelnen API-Anbieter nutzen willst. Sie sind aber nicht automatisch besser, billiger oder vollständig Open Source. Vergleiche sie deshalb mit starken Anbietermodellen am echten Anwendungsfall, statt dich vorab auf eine Modellfamilie festzulegen. *(Quelle: [OSI — Open Weights und Open Source AI](https://opensource.org/ai/open-weights))*

**Wie teste ich, welches Modell für meinen Fall wirklich besser ist?**

Ich gebe zwei oder drei Kandidaten **dieselbe reale Aufgabe** mit demselben Repo-Stand, denselben Tools und denselben Fertig-Kriterien. Dann prüfe ich nicht nur die erste Antwort, sondern das Ergebnis: Sind die Tests grün? Ist der Diff sauber? Wie viele Wiederholungen und menschliche Korrekturen waren nötig? Bei kritischen oder neuen Aufgaben starte ich mit einem möglichst starken Modell als Vergleichswert. Ein kleineres oder open-weight Modell übernimmt den Job erst, wenn es die nötige Qualität im Vergleich wirklich erreicht.

```text
Vergleiche <Modell A> und <Modell B> für diese Aufgabe: <Aufgabe>.

Für beide gleich:
- Ausgangsstand: <Repo, Branch, Daten>
- Erlaubte Tools: <Liste>
- Fertig, wenn: <Tests und Prüfkriterien>

Berichte je Modell:
- Ergebnis akzeptiert: ja/nein
- fehlgeschlagene Versuche und Wiederholungen
- nötige menschliche Korrekturen
- Laufzeit und auffälliger Rechen-/Context-Bedarf
- Probleme mit Tools, Datenstandort oder Betrieb

Empfiehl zuerst nach Ergebnisqualität. Sind beide gleich gut,
nimm die einfachere und effizientere Variante.
```

**Wie begrenze ich teure oder lange Läufe, ohne sie permanent beobachten zu müssen?**

Jeder größere Lauf bekommt vorab einen kurzen **Auftrag**: betroffene Dateien, überprüfbares Ergebnis, erlaubte Aktionen, ein Zeit- oder Turn-Limit und konkrete Stop-Bedingungen. Ich teste das Vorgehen zuerst an einem kleinen, repräsentativen Teil, bevor ich es auf das ganze Repo oder viele Dateien skaliere. Der Agent muss an vereinbarten Zwischenständen die Ergebnisse zeigen, etwa grüne Tests, einen prüfbaren Diff oder ein aktualisiertes Fortschrittsdokument. Wenn sich der Scope unkontrolliert erweitert, derselbe Fehler wiederholt auftritt oder keine neuen verifizierbaren Ergebnisse entstehen, wird gestoppt und neu geplant. Das folgt demselben Muster wie Codex-Prompts mit **Goal, Context, Constraints und Done when**. *(Quelle: [Codex — Best Practices](https://learn.chatgpt.com/guides/best-practices))*

**Wiederverwendbarer Run-Vertrag:**

```text
Ziel: <welches Ergebnis soll entstehen?>
Scope: <welche Dateien/Systeme gehören dazu — und welche nicht?>
Constraints: <Standards, erlaubte Tools, Sicherheitsgrenzen>
Fertig, wenn: <Tests, Messwerte oder Review-Kriterien>
Budget/Stop: <Zeit-/Turn-Limit; wann abbrechen und rückfragen?>
Checkpoint: <wann Diff, Tests und offene Punkte berichten?>
Abschluss: <Ergebnis, Evidenz und verbleibende Risiken zusammenfassen>
```

**Welche Tools oder Skills helfen dabei?**

| Option | Stärkster Einsatz | Einordnung |
|---|---|---|
| Native Befehle wie `/plan`, `/goal`, `/usage`, `/clear` und `/model` | Einzelne lange oder teure Läufe bewusst steuern | Kein zusätzlicher Installationsaufwand; Scope, Checkpoints und Stop-Kriterien bleiben Handarbeit. |
| [Superpowers](https://github.com/obra/superpowers) | Wiederverwendbare Arbeitsgewohnheiten: Brainstorming, Worktrees, schriftliche Pläne, TDD, Review und Verifikation | Leichtere Skills-/Methodik-Schicht; besonders hilfreich sind [`executing-plans`](https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md) und [`verification-before-completion`](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md). |

Superpowers ist ein optionales Community-Werkzeug. Es ersetzt weder projektspezifische Akzeptanzkriterien noch einen frischen Test- und Diff-Check vor dem Merge.

**Was ist der Unterschied zwischen Headless (`claude -p` / `codex exec`) und `/goal`?**

Headless heißt: ein Agent erledigt **einen** Auftrag ohne UI und beendet sich — gut für Skripte, CI oder Batch-Arbeit. Bei Claude Code heißt das `claude -p "…"`, bei Codex `codex exec "…"`. `/goal` setzt dagegen eine **Completion-Condition** und hält die Session am Ziel, bis der definierte Endzustand erreicht ist. Kurz: Headless = „einmal durchlaufen"; `/goal` = „weiterarbeiten, bis das Ziel hält". Nicht **verwechseln** (Konzept ≠ Befehl): `claude -p` und `codex exec` sind Befehle für non-interactive Runs; `/goal` ist die Zielbedingung innerhalb des jeweiligen Tools — kombinieren geht trotzdem, headless etwa via `claude -p "/goal …"`.

**Läuft mir `/goal` davon, wenn das Ziel nie erfüllt wird?**

Bei langen Goal-Läufen muss die Grenze **in die Aufgabe selbst**: messbarer Endzustand, benannter Check und bei Bedarf eine Turn-/Zeit-Klausel („… or stop after 20 turns"). Die Claude-Code-Mechanik oben in Abschnitt 2 („Mechanik (tiefere Ebene)") beschreibt zusätzlich Evaluator-Verhalten und Stop-Hook-Override — es gibt **keine** eingebaute „X Fortsetzungen"-Obergrenze, der einzige automatische Notausgang ist eben dieser Stop-Hook-Override; das ist Claude-spezifisch. Für Codex gilt dasselbe Arbeitsprinzip: Goal klein genug formulieren, Evidenz verlangen und bei riskanten Läufen menschliche Checkpoints einbauen. Für etwas, das man ohnehin beobachtet, reicht oft ein Prompt-Level-Check: „arbeite, bis `npm test` grün ist, dann stoppe und zeige den Output".

**Was ist bei `/goal` Claude-spezifisch und was Codex-spezifisch?**

Claude Code beschreibt `/goal` als Completion-Condition mit separatem schnellem Evaluator-Modell; der Evaluator ruft keine Tools auf und bewertet nur, was im Transcript sichtbar ist. Details wie Haiku/default small model, Stop-Hook-Mechanik, Condition-Limit (**4.000 Zeichen**, s. Abschnitt 2) und `/loop`-Kopplung gehören zur Claude-Code-Schicht. Codex nutzt ebenfalls `/goal` für ein länger laufendes Ziel mit Abschlusskriterien; dort sind die sichtbaren Befehle und Schalter anders (`/goal` in App/IDE/CLI, ggf. `features.goals`). Für beide gilt: Nicht „mach weiter, bis es gut ist", sondern „fertig, wenn Check X grün ist und Diff Y nicht verletzt".

**Wie schreibe ich eine gute `/goal`-Condition?**

Eine gute Condition nennt vier Dinge: **Endzustand**, **Check**, **Grenzen** und **Stopp-Klausel**. Beispiel: „Ergänze Tests für `src/billing/`. Fertig, wenn `npm test` grün ist, keine Secrets oder Personendaten ergänzt wurden und der Diff nur `src/billing/` und `tests/billing/` betrifft. Stoppe, wenn zwei Prüfrunden in Folge keinen Fortschritt bringen.“ Das funktioniert für Claude und Codex als Muster; die exakte Eingabe ist tool-spezifisch.

**Wann nehme ich `/loop` statt `/goal`?**  
`/goal` zielt auf einen **Endzustand** („fertig, wenn Bedingung X hält"). `/loop` re-triggert den Agenten **wiederkehrend** — gut für einen Takt, z.B. „prüfe alle paar Minuten auf neue CI-Fehler und arbeite sie ab". `/loop` kann dabei mehr als nur fester Cron sein: mit `/loop "<prompt>"` (ohne Intervall) wählt Claude die Verzögerung (1–60 min) **selbst** und **beendet den Loop selbst**, wenn die Arbeit nachweislich fertig ist; `/loop` ohne Prompt führt ein Maintenance-Prompt bzw. `loop.md` aus. Es gilt eine 7-Tage-Expiry, `Esc` stoppt einen wartenden Loop. Für entfernte/geplante Läufe sind **Cloud-Routines** (`/schedule`), **Desktop Scheduled Tasks** oder das **Monitor-Tool** (Event-getrieben) die Alternativen. Faustregel: Endzustand → `/goal`; Takt/Wartung → `/loop`. Die vollständige Gegenüberstellung aller vier Werkzeuge steht in der **4-Wege-Matrix** am Anfang von Abschnitt 2. *(Quelle: code.claude.com/docs/en/scheduled-tasks)*

**Wann nehme ich das Monitor-Tool statt `/loop`?**  
Nimm **Monitor** direkt, wenn es einen **konkreten Prozess oder ein Logfile** gibt, dessen Ausgabe du live mitlesen kannst: Monitor streamt zeilenweise und reagiert auf **jede neue Ausgabezeile**, ohne den Agenten neu zu prompten — ereignisgetrieben statt blind pollen. Nimm **`/loop`**, wenn es **keinen einzelnen Prozess** gibt und Claude die Welt **periodisch neu bewerten** soll (mehrere Quellen abfragen, Zustand zusammensetzen). Kurz: ein Stream, auf den du lauschen kannst → Monitor; eine Runde, die du wiederholen willst → `/loop`. *(Quelle: code.claude.com/docs/en/scheduled-tasks)*

**Wie lasse ich zwei Agenten parallel arbeiten, ohne dass sie sich in die Quere kommen?**  
**Git-Worktrees** — jede Session bekommt ein eigenes Arbeitsverzeichnis mit eigenem Branch, teilt aber History/Remote. So bauen zwei Agenten gleichzeitig an verschiedenen Dingen, ohne dieselben Dateien zu überschreiben. Praxisgrenze (Erfahrungswert, ohne öffentliche Quelle): **2–4** parallele Sessions; vorher committen/stashen.

**Ich muss dieselbe Änderung über 200 Dateien machen — wie, und was, wenn Datei 42 scheitert?**

**Fan-out:** Task-Liste generieren lassen → in einem Skript über die Liste loopen, je Datei ein Headless-Aufruf (`claude -p` bei Claude Code, `codex exec` bei Codex) → **erst an 2–3 Dateien verfeinern**, dann auf alle loslassen. Jeden Aufruf **„Return OK or FAIL"** zurückgeben lassen, dann die wenigen fehlgeschlagenen Dateien herausfiltern und gezielt nachfahren — nicht den ganzen Batch wiederholen. Permissions/Sandbox eng scopen: bei Claude z.B. über `--allowedTools`, bei Codex z.B. über `--sandbox workspace-write` und klare Repo-Grenzen.

**Wann nehme ich einen Dynamic Workflow statt Subagents oder eines Fan-out-Skripts?**  
Wenn die Aufgabe **mehr Agents braucht, als eine Konversation koordinieren kann**, oder die Orchestrierung **wiederholbar** sein soll. Bei Subagents entscheidet Claude Turn für Turn, und jedes Ergebnis landet im Context Window; bei einem Workflow **hält ein Script den Plan**, und Zwischenergebnisse leben in Script-Variablen — Claudes Context bekommt nur das Endergebnis. Dutzende bis Hunderte Agents pro Run sind damit machbar, und das Script kann Findings adversarial gegenprüfen lassen. Getriggert wird per `ultracode`-Keyword oder natürlichsprachlich („use a workflow"); bewährte Runs speichert man im `/workflows`-View mit `s` als eigenen `/`-Command. *(Quelle: https://code.claude.com/docs/en/workflows, abgerufen 2026-07-06)*

**Läuft ein Workflow in der Anthropic-Cloud, und was kostet er?**  
Nein — Workflows laufen **lokal auf deinem Rechner** (max. 16 gleichzeitige Agents, weniger bei wenigen CPU-Cores; hartes Limit 1.000 Agents pro Run). Sie können aber deutlich mehr Tokens verbrauchen als dieselbe Aufgabe im Gespräch, weil viele Agents parallel arbeiten — Runs zählen normal gegen Plan-Usage und Rate-Limits. Kosten-Praxis: erst auf einem kleinen Slice testen, `/model` vor großen Runs prüfen, Token-Verbrauch live im `/workflows`-View beobachten. *(Quelle: https://code.claude.com/docs/en/workflows, abgerufen 2026-07-06)*

**Cloud-Routines laufen ohne Permission-Prompts — wo sind da die Leitplanken?**  
Beim **Scoping vorab**, nicht beim Zusehen: nur die nötigen Repos und Connectors einbinden, den Network-Access des Cloud-Environments beschränken (Default „Trusted"-Allowlist), und der Branch-Schutz lässt Claude per Default nur auf **`claude/`-präfixierte Branches** pushen. Den wichtigsten Caveat einplanen: Ein **grüner Run-Status heißt nicht, dass der Task gelungen ist** — nur, dass die Session ohne Infrastruktur-Fehler endete. Also den Transcript des Runs lesen. *(Quelle: https://code.claude.com/docs/en/routines, abgerufen 2026-07-06)*

**Funktionieren Cloud-Routines, wenn mein Code nicht auf GitHub liegt?**  
Nur eingeschränkt (Synthese, Stand 2026-07-06): Routines unterstützen **GitHub**-Repos. Liegt dein Code auf einer anderen Plattform als GitHub, sieht eine Routine ihn nur über eine Kopie auf GitHub, und ihre Commits oder PRs fließen **nicht** automatisch zurück. Für Schreib-Aufgaben ist das ungeeignet, für **Lese-, Analyse- und Report-Aufgaben** auf einer solchen Kopie brauchbar.

**Wenn der Agent viel mehr Code produziert — wie behalte ich die Qualität?**  
Nutze einen zweiten Agenten zur Gegenprüfung und verlange konkrete Befunde mit Dateistelle und Begründung. Prüfe Diff und Check-Output selbst. Wiederhole wichtige Checks unabhängig; ein Reviewer kann Fehler übersehen oder unbegründete Änderungen verlangen. Die Entscheidung über die Nutzung bleibt beim Menschen.

**Wann nutze ich `codex review`, `/review` oder Writer/Reviewer?**

Immer dann, wenn der Diff nicht trivial ist oder die Aufgabe sichtbare Folgen hat. In Codex kann `codex review` non-interactive prüfen und `/review` den aktuellen Arbeitsstand in der Session reviewen. In Claude Code ist das Muster eher Writer/Reviewer, `/code-review` oder ein frischer Subagent/zweite Session. Das Prinzip ist gleich: Der Reviewer bekommt **Diff + Anforderungen + Akzeptanzkriterien**, nicht die ganze Entstehungsgeschichte, und soll nur Korrektheits-, Sicherheits- oder Anforderungsprobleme melden.

**Heißt „Cloud“ automatisch, dass Daten in die US-Cloud gehen?**  
Nein. Wo der Agent läuft und wo das Modell rechnet, sind zwei getrennte Fragen. Für Übungen mit erfundenen oder öffentlichen Daten ist das unkritisch. Sobald echte Daten ins Spiel kommen, zählen Modell-Hosting, Verträge und [Modul 11](./11-kundendaten-testdaten.md). In der EU gehostete Modelle und Open-Weight-Modelle sind Optionen, wenn du oder deine Organisation Vorgaben zum Datenstandort habt.

**Was kostet intensiver/paralleler Agent-Einsatz — und wie behalte ich die Kosten im Griff?**  
Zwei Abrechnungswege: **Subscription** (Pro/Max — fixer Monatspreis, ein geteilter Pool für Chat *und* Code) gegen **API** (pay-per-token — genaue Kostenkontrolle, gut für CI/Skripte). Bei der Subscription greifen Rate-Limits über ein **rollierendes 5-Stunden-Fenster plus einen wöchentlichen Cap**; Claude Code zeigt die jeweilige Reset-Zeit an. Die Kosten siehst du interaktiv mit **`/cost`** (Session-Überblick), nicht-interaktiv/SDK über das Feld **`total_cost_usd`** in der `ResultMessage` — **Caveat:** das ist eine *client-seitige Schätzung*; verbindlich sind nur die Usage-/Cost-API bzw. das Console-Dashboard. Faustregel: **Headless-Fan-out** (`claude -p` bei Claude Code, `codex exec` bei Codex) ist pro Aufgabe günstiger als viele interaktive Sessions — deshalb skaliert man Batch-Arbeit headless (Abschnitt 1/4), nicht über viele parallele Chat-Fenster. *(Preis-/Limit-Angaben: flüchtige Schicht 06/2026 — Stand: claude.com/pricing · code.claude.com/docs/en/agent-sdk/cost-tracking)*

---

## Quellen & Weiterlesen

- Vorwissen — ein Agent + Loop: [`07-agenten-grundlagen.md`](./07-agenten-grundlagen.md)
- Vertiefung — die Disziplinen dahinter (Context Engineering, Autonomy-Slider, Long-horizon Memory, „Build for agents", Boris Cherny YC-Auftritt 07/2026): [`10-kontext-engineering.md`](./10-kontext-engineering.md)
- Dynamic Workflows (Primärquelle): https://code.claude.com/docs/en/workflows (abgerufen 2026-07-06)
- Parallelitäts-Vergleich Subagents / Agent View / Agent Teams / Workflows: https://code.claude.com/docs/en/agents (abgerufen 2026-07-06)
- Cloud-Routines (Primärquelle): https://code.claude.com/docs/en/routines (abgerufen 2026-07-06)
- `/goal` (Primärquelle): https://code.claude.com/docs/en/goal (abgerufen 2026-07-06)
- Codex Manual (Primärquelle; `codex exec`, `/goal`, `/review`): https://learn.chatgpt.com/docs/codex-manual.md (abgerufen 2026-07-08)
- Claude Code — Kosten, Context und Usage: https://code.claude.com/docs/en/costs sowie https://claude.com/pricing (abgerufen 2026-07-17)
- Codex — Best Practices und Long-running Work: https://learn.chatgpt.com/guides/best-practices sowie https://learn.chatgpt.com/docs/long-running-work (abgerufen 2026-07-17)
- Aktuelle Modellwahl in Claude Code und Codex: https://code.claude.com/docs/en/model-config sowie https://learn.chatgpt.com/docs/pricing (abgerufen 2026-07-17)
- Open-weight Modellbeispiele für Coding und Reasoning: https://mistral.ai/news/devstral-2-vibe-cli/ · https://github.com/QwenLM/Qwen3-Coder · https://openai.com/index/introducing-gpt-oss/ (abgerufen 2026-07-17)
- Open Weights vs. Open Source AI: https://opensource.org/ai/open-weights (abgerufen 2026-07-17)
- Superpowers — Skills für Pläne, Worktrees, Checkpoints und Verifikation: https://github.com/obra/superpowers (abgerufen 2026-07-17)
- Begriffe nachschlagen: [`glossar.md`](./glossar.md)
- Hooks (Stop-Hook-Schema), Permission-Modes, Scheduled Tasks: https://code.claude.com/docs/en/hooks · https://code.claude.com/docs/en/permission-modes · https://code.claude.com/docs/en/scheduled-tasks *(abgerufen 2026-09-13)*
- Codex — Changelog (Modellwechsel): https://learn.chatgpt.com/docs/changelog *(abgerufen 2026-09-13)*
