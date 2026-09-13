# Modul 10 — Kontext-Engineering (die Disziplinen hinter dem Skalieren)

> Deutsche Fassung · Stand 2026-09-13 · Englischer Lernpfad: [START-HERE](../../START-HERE.md)

⏱ ~15 min · **Danach kannst du:** beurteilen, was dein Context-Window gerade füllt und was daraus gehört, eine `CLAUDE.md` nach den Pflegeregeln kürzen statt sie wachsen zu lassen, und eine Aufgabe so zuschneiden, dass sie leicht über der Fähigkeit des Agenten liegt statt sie in Schritte zu zerlegen.

**Setzt voraus:** [Modul 7](./07-agenten-grundlagen.md) und [Modul 8](./08-agenten-skalierung.md) — dieses Modul ist aus Modul 8 §6/§7 ausgelagert und liest sich ohne die Befehle dort halb.

## Worum es geht

[Modul 8](./08-agenten-skalierung.md) zeigt die Befehle fürs Skalieren (`/goal`, `/loop`, Worktrees, Workflows). Dieses Modul zeigt die **Denkhaltung dahinter**: Context ist die knappe Ressource, nicht Rechenzeit — und die Disziplin, mit der man sie bewirtschaftet, überlebt jeden Tool-Wechsel, während einzelne Befehle veralten.

Aufhänger dafür ist ein aktueller Auftritt von Boris Cherny (Schöpfer von Claude Code) bei Y Combinator: Anthropic hat **80% des Claude-Code-System-Prompts gelöscht**, weil das aktuelle Modell (Opus 5) die Korrektur-Instruktionen früherer Modelle nicht mehr braucht — „das Modell ist ohne diese Prompts sogar etwas intelligenter". Dieselbe Disziplin gilt für alle, die selbst eine `CLAUDE.md` pflegen: Jede Zeile ist eine Instruktion, die das Modell **jedes Mal** liest — auch wenn sie längst nicht mehr gebraucht wird.

> **Merksatz für Nicht-Devs:** Du musst kein Prompt-Engineering betreiben, um das mitzunehmen. Die Kernfrage überträgt sich 1:1 auf jede Instruktion, die du einem Agenten gibst: „Braucht das Modell diese Anweisung wirklich — oder schleppen wir sie nur aus Gewohnheit mit?"

---

## 1. Die vier Disziplinen (aus Modul 8 §6 ausgelagert)

Skalieren ist weniger eine Frage der Befehle als der Denkhaltung, mit der man Agenten Leine gibt. Vier Disziplinen tragen alles, was in Modul 8 an Mechanik steht:

| Disziplin | Worum es geht | Wofür beim Skalieren |
|---|---|---|
| **Context Engineering** | Context ist die knappe Ressource, nicht Rechenzeit: die richtige **„Altitude"** des System-Prompts (die „Flughöhe" der Instruktion — nicht jeden Schritt diktieren, aber auch nicht zu vage), **Tool-Minimalismus** (wenige, scharf umrissene Tools statt aller) und **JIT-Retrieval** (Wissen erst im Moment des Bedarfs nachladen, statt alles vorab). | je mehr unbeaufsichtigt läuft, desto teurer kostet ein verrauschter Context — sauberer Context hält lange Läufe stabil |
| **Autonomy-Slider** | Pro Task bewusst entscheiden, **wie viel Leine** der Agent bekommt — vom eng beobachteten Ein-Satz-Fix bis zum `/goal`-gesteuerten Mehr-Stunden-Lauf (Andrej Karpathy). Der Slider wird nicht einmal gesetzt, sondern **pro Aufgabe** neu gewählt. Auf der Modell-Achse hilft der **`opusplan`-Alias** (`/model opusplan`): er nutzt **Opus zum Planen, Sonnet zum Ausführen** — teures Reasoning nur dort, wo es zählt, günstige Ausführung für den Rest. *(Quelle: code.claude.com/docs/en/model-config#opusplan-model-setting)* | mappt direkt auf die Permission-Modi und die Verification-Leiter ([Modul 7](./07-agenten-grundlagen.md)): mehr Autonomie ⇒ härteres Gating davor |
| **Long-horizon Memory** | Für Arbeit über **mehrere Tage/Sessions**: strukturiertes **Note-Taking** (Plan/Fortschritt in Dateien, nicht nur im Context) plus eine **Compaction-Strategie** (was beim Verdichten erhalten bleiben muss). | überbrückt `/clear` und Session-Grenzen — der Agent „erinnert sich" über Datei-State, nicht über ein volllaufendes Context-Fenster |
| **„Build for agents"** | Die Codebase **agenten-lesbar** machen: `llms.txt`, AI-lesbare Docs, klare Pfade/Namen, maschinenlesbare Checks. | senkt die FAIL-Rate im Fan-out ([Modul 8](./08-agenten-skalierung.md)) und macht unbeaufsichtigte Läufe zuverlässiger |

> **Merksatz:** Befehle wie `/goal` und `/loop` (Modul 8) sind die Hebel; die vier Disziplinen hier sind die Hand, die sie führt. Erstere veralten, letztere überleben jeden Tool-Wechsel.

## 2. `CLAUDE.md`-Pflege (aus Modul 8 §7 ausgelagert)

Wer im Team teilt, klärt [Modul 8](./08-agenten-skalierung.md#7-org-level-scaling--vom-einzelnen-zum-team) (Global/Team/Persönlich/Monorepo-Hierarchie). Hier die **Pflege-Mechanik** derselben Datei:

- **Kurz halten** (Pruning-Faustregel: „Würde Entfernen dieser Zeile Claude Fehler machen lassen? Wenn nein, raus"). Eine überfüllte `CLAUDE.md` lässt den Agenten Regeln ignorieren.
- **Modular importieren** mit `@path/to/import` — statt eine Datei aufzublähen, gezielt Teildateien einbinden.
- **Compaction-Verhalten tunen**: in der `CLAUDE.md` festhalten, was beim Verdichten erhalten bleiben muss (z.B. „always preserve the full list of modified files").

## 3. Boris Cherny: 80% des System-Prompts gelöscht (YC-Video, 2026-07-27)

Anlässlich des Opus-5-Release erklärt Cherny, warum Anthropic **über 80% des Claude-Code-System-Prompts löschte** (YC-Video, ~04:00): Vieles darin korrigierte Verhalten, das ältere Modelle brauchten — Opus 5 „macht es einfach, ohne dass wir es ihm sagen müssen", und ist laut Cherny „ohne diese Prompts sogar etwas intelligenter". Das ist keine einmalige Aufräumaktion, sondern Dauerzustand: Bei **jedem** neuen Modell werden System-Prompt und Tool-Set neu vermessen, weil sich Modelle zwischen Generationen stark unterscheiden.

**Ablation als Methode (~04:00–06:00):** Statt zu raten, was ein Modell noch braucht, löscht das Team den Prompt komplett und holt Zeile für Zeile zurück, um die Wirkung jeder einzelnen zu messen — dieselbe Grundidee wie ein Eval, nur mit Löschen statt Testen. Ergänzend nennt Cherny **„simple mode"** (Umgebungsvariable `CLAUDE_CODE_SIMPLE=1`, ~05:00): Sie entfernt alle System-Prompts, auch die der Tools. Cherny bezeichnet sie im Video als „kind of this undocumented feature". **Hinweis:** Im Video (2026-07-27) nennt Cherny die Variable „undokumentiert" — inzwischen ist sie offiziell dokumentiert (`code.claude.com/docs/en/env-vars.md`, Stand 2026-07-30), äquivalent zum `--bare`-Flag (Bash/Read/Edit-Tools, keine Auto-Discovery von Hooks/Skills/Plugins/CLAUDE.md).

**Die 6-Monats-Regel (~06:00–08:00):** Für alle, die selbst mit Claude Code arbeiten (nicht nur für Anthropic intern), empfiehlt Cherny: **alle 6 Monate `CLAUDE.md`, Skills und Hooks löschen** und beobachten, was das Modell ohne sie tut. Der Grund ist derselbe wie bei der Ablation: „das Modell liest jede Instruktion jedes Mal" — eine Zeile, die niemand mehr braucht, kostet trotzdem bei jedem Turn. Eine Instruktion kommt erst zurück, wenn das Modell **wiederholt** an derselben Stelle stolpert, nie präventiv „auf Verdacht".

**Eval-Halbwertszeit (~08:00–10:00):** Evals (kuratierte Testfälle, an denen Modellverhalten gemessen wird) überleben länger als Code und Prompts, aber auch sie sind nicht dauerhaft: „ein Eval mag ein, zwei, drei Modellgenerationen leben", dann saturiert er (das Modell besteht ihn durchgehend) und wird durch einen neuen ersetzt.

> **Nicht verwechseln — Eval ≠ Evaluator:** Ein **Eval** hier ist ein kuratierter Testfall-Satz zur Modellbewertung (dieser Abschnitt). Der **Evaluator** in [Modul 8](./08-agenten-skalierung.md) ist das kleine, schnelle Modell, das bei `/goal` nach jedem Turn prüft, ob die Completion-Condition erfüllt ist. Beide Begriffe klingen ähnlich, meinen aber unterschiedliche Dinge auf unterschiedlichen Ebenen — der eine bewertet Modelle über Zeit, der andere bewertet einen einzelnen laufenden Task.

## 4. Kontext-Budget — was füllt das Context-Window?

Was liegt eigentlich alles auf dem Schreibtisch (→ Modul 7)? `/context` zeigt dir die Aufteilung live — die Tabelle unten erklärt die fünf Posten. Context Engineering (Abschnitt 1) bleibt abstrakt, solange unklar ist, *woraus* ein volles Context-Window eigentlich besteht. Grobe Aufschlüsselung (Synthese aus Cherny-Video + Claude-Code-Doku, kein exaktes Anbieter-Schema):

| Posten | Was er kostet | Wie man ihn senkt |
|---|---|---|
| **System-Prompt** | Fixkosten bei **jedem** Turn — je größer, desto mehr „liest" das Modell immer wieder mit | Ablation (Abschnitt 3); `--system-prompt`/`--append-system-prompt`-Flags zum gezielten Ersetzen/Ergänzen testen (primärquellen-belegt: `code.claude.com/docs/en/cli-reference`, Stand 2026-07-30) — für Fortgeschrittene; als normale:r Nutzer:in sind das Fixkosten, die der Anbieter senkt (s. Abschnitt 3) |
| **Tool-Definitionen** | jedes registrierte Tool-Schema lädt bei jedem Turn mit, ob genutzt oder nicht. Ausnahme: Claude Code lädt MCP-Tools ab v2.1.232 per **Tool Search** erst bei Bedarf *(Quelle: code.claude.com/docs/en/mcp, abgerufen 2026-09-13)* | Tool-Minimalismus (Abschnitt 1); ungenutzte MCP-Server abmelden |
| **`CLAUDE.md` / Rules** | wächst mit jeder Regel, die „auf Verdacht" bleibt | Pruning-Test + 6-Monats-Regel (Abschnitt 2/3) |
| **Gesprächsverlauf** | füllt sich über Turns hinweg, besonders bei langen Sessions | `/clear` zwischen unabhängigen Aufgaben, Compaction-Strategie (Abschnitt 1) |
| **Tool-Outputs** | Suchergebnisse, Logs, Diffs — oft der größte Einzelposten bei Recherche-/Fan-out-Aufgaben | Subagents/Dynamic Workflows auslagern, damit nur die Zusammenfassung zurückkommt ([Modul 8](./08-agenten-skalierung.md)) |

## 5. Unhobbling & Product Overhang — Claude Codes Gründungsidee

Cherny nennt zwei Begriffe aus der Anthropic-Forschung, um zu erklären, warum viele Modell-Fähigkeiten ungenutzt bleiben (~10:00–14:00): **Hobbling** ist, wenn ein Produkt einem Modell im Weg steht, obwohl es etwas kann; **Unhobbling** ist das Gegenmittel: die Hindernisse entfernen, die das Produkt dem Modell anlegt. **Product Overhang** ist die Lücke zwischen dem, was ein Modell schon kann, und dem, was ein Produkt davon tatsächlich zulässt. Claude Codes eigene Gründungsgeschichte ist Chernys Beispiel dafür: Als Sonnet 3.5 (damals das stärkste Coding-Modell) schon ganze Dateien schreiben konnte, boten Coding-Produkte noch Autocomplete und reinen Lese-Chat. Die Grundidee hinter Claude Code war, „das gesamte Gerüst drumherum (Scaffolding) wegzunehmen und dem Modell den einfachstmöglichen Harness zu geben" — Terminal-Zugriff statt IDE-Käfig.

Chernys Ableitung für alle, die heute auf Claude bauen: Modelle können regelmäßig mehr, als das umgebende Produkt zulässt. Der produktive Zug ist nicht, vom aktuellen Produktverhalten auf die Modellgrenze zu schließen, sondern dem Modell probeweise etwas leicht zu Schweres zuzutrauen (Abschnitt 6) und zu beobachten, was passiert.

## 6. Aufgaben-Kalibrierung — leicht über Fähigkeit, nicht Schritt-für-Schritt

Chernys wiederkehrender Rat (~14:00, wieder aufgegriffen ~24:00): Gib dem Modell eine Aufgabe, die **etwas schwieriger wirkt, als du ihm zutraust** — und beschreibe **Task, Guardrails und Exit-Kriterien**, statt Schritt 1-2-3 vorzuschreiben. Sein Befund aus vielen Sessions: „erfahrene Engineers überspezifizieren" — gerade wer jahrelang selbst so gearbeitet hat, neigt dazu, dem Modell den eigenen Lösungsweg vorzuschreiben, statt es das Problem lösen zu lassen.

> **Pflicht-Abgrenzung (keine Doktrin-Kollision):** Dieses Material verlangt an anderer Stelle ausdrücklich „Verlange Evidenz, vertraue nicht" ([Modul 7](./07-agenten-grundlagen.md)) und behandelt den Agenten als **fehlbaren Junior**. Chernys Regel widerspricht dem nicht — sie betrifft eine andere Ebene: die **Instruktions-Ökonomie beim Beauftragen** (wie viel du vorab vorschreibst), nicht das **Ergebnis-Vertrauen danach** (ob du dem Output glaubst). Beide Regeln gelten gleichzeitig: weniger Mikromanagement beim Briefen, unverändert volle Verifikationspflicht beim Abnehmen.

## 7. Verification als wichtigster Hebel

Auf die Frage, was die besten Claude-Nutzer:innen von den übrigen unterscheidet, nennt Cherny **Verification** als den entscheidenden Hebel: „the verification I think is probably the single most important thing that people do not get right" (~20:00). Seine Illustration: Er ließ die Electron-basierte Claude-Desktop-App **pixelgenau nach Swift** nachbauen — der komplette Prompt war „baue die App in Swift nach, screenshotte die Electron-Version, vergleiche Pixel für Pixel, hör nicht auf, bis es passt". Der Lauf lief zum Zeitpunkt des Auftritts bereits **über zwei Wochen** mit vermutlich tausenden Agenten (Cherny nennt keine belastbare Zahl — als Behauptung, nicht als Faktum zu lesen). Die Pointe ist nicht die Laufzeit, sondern das Prinzip: **eine Aufgabe, die schwer genug ist, plus ein Weg, das eigene Ergebnis zu prüfen** — den Rest erledigt das Modell selbst, ohne `/goal` oder `/loop` bemühen zu müssen.

Die vollständige Eskalationsleiter dieser Prüf-Härte (Prompt-Level-Check bis Verifikations-Subagent) steht in Modul 7 und wird in Modul 8 auf `/goal`/Stop-Hooks angewendet — hier zählt nur der Grundsatz: Verification ist kein Add-on am Ende, sondern die Voraussetzung dafür, dass eine schwere Aufgabe überhaupt unbeaufsichtigt laufen darf.

## 8. Kurz: Skalierungs-Mechanik, für die Modul 8 zuständig bleibt

Zwei Dinge aus dem Video sind reine Illustration der in Modul 8 bereits beschriebenen Mechanik:

- **Dynamic Workflows als „algebra for agents"** (~26:00) — eine neue Form von Test-Time-Compute (Test-Time-Compute = Rechenaufwand zur Laufzeit einer Anfrage — mehr „Nachdenken" pro Antwort statt größeres Modell): Statt nur mehr Tokens pro Antwort zu generieren, orchestriert ein Workflow Dutzende bis Hunderte Agents in Sequenz und Parallel. Illustrierendes Beispiel: Ein einzelner Dynamic-Workflow-Prompt ließ die Bun-JavaScript-Runtime **von Zig nach Rust neu schreiben** — ein Lauf über **11 Tage** mit Steering unterwegs (Anekdote, keine reproduzierbare Kennzahl). Mechanik dazu steht in [Modul 8](./08-agenten-skalierung.md).
- **Loops/Routines als Selbstwartung** (~28:00–30:00) — Anthropic lässt intern **20 bis 30 tägliche Routines** über die eigenen Codebases laufen: Dead-Code-Cleanup, ausgelaufene Experimente ausbauen, fehlende Tests ergänzen, überflüssige Tests löschen, und die von Cherny so genannte „abstraction police" (nahezu doppelte Abstraktionen im Code vereinheitlichen). Cherny: „we're on the path to fully automating the maintenance of our apps." Mechanik (`/loop`, Cloud-Routines) steht ebenfalls in [Modul 8](./08-agenten-skalierung.md).

> **Merksatz:** Das empirische Mindset trägt alles oben — Cherny nennt es explizit „it's become an empirical science": kein One-weird-trick-Rezept, sondern Aufgabe geben, beobachten wo das Modell stolpert, anpassen, wiederholen (~22:00, ~32:00).

---

## Q&A

**Ich schreibe keine System-Prompts und baue keine Tools — was betrifft mich konkret?**
Mehr als du denkst. **CLAUDE.md-Pruning** (Abschnitt 2): Auch die Team-`CLAUDE.md`, die du mitliest, wird nach derselben Pruning-Faustregel schlank gehalten, damit der Agent Regeln nicht ignoriert. **`/clear`-Hygiene und Kontext-Budget** (Abschnitt 4): Warum du zwischen Themen den Agenten zurücksetzt, ist dieselbe Logik wie hinter jedem vollen Schreibtisch, den du selbst befüllst. **Aufgaben-Kalibrierung** (Abschnitt 6): Wie du einen Auftrag formulierst — Outcome statt Schritt-für-Schritt — betrifft jede:n, die/der einem Agenten etwas aufträgt, nicht nur Devs.

**Was ist der Unterschied zwischen einem Eval und dem `/goal`-Evaluator?**
Ein Eval ist ein kuratierter Testfall-Satz, an dem ein *Modell* über Zeit gemessen wird — er lebt laut Cherny „ein, zwei, drei Modellgenerationen", dann saturiert er und wird ersetzt. Der `/goal`-Evaluator ([Modul 8](./08-agenten-skalierung.md)) ist ein kleines, schnelles Modell, das bei einem *einzelnen laufenden Task* nach jedem Turn prüft, ob die Completion-Condition erfüllt ist. Unterschiedliche Ebene, unterschiedlicher Lebenszyklus — trotz ähnlichem Namen nicht dasselbe.

**Widerspricht „Aufgaben nicht überspezifizieren" nicht dem Grundsatz „Verlange Evidenz, vertraue nicht"?**
Nein, das sind zwei verschiedene Momente derselben Delegation. „Nicht überspezifizieren" gilt fürs **Beauftragen**: lieber Task, Guardrails und Exit-Kriterium beschreiben als Schritt 1-2-3 vorschreiben. „Verlange Evidenz" gilt fürs **Abnehmen**: das Ergebnis bleibt so lange unbewiesen, bis Test-Output, Diff oder Screenshot es belegen. Weniger Mikromanagement vorher heißt nicht weniger Prüfung nachher.

**Ist `CLAUDE_CODE_SIMPLE=1` dasselbe wie `--bare`?**
Laut `code.claude.com/docs/en/env-vars.md` (Stand-Check 2026-07-30) ja: Die Variable ist als äquivalent zum `--bare`-Flag dokumentiert — minimaler System-Prompt, nur Bash/Read/Edit-Tools, keine Auto-Discovery von Hooks, Skills, Plugins, MCP-Servern, Memory oder `CLAUDE.md`. Im YC-Video nennt Cherny sie noch „kind of this undocumented feature" (2026-07-27) — zwischen Aufnahme und heutigem Doku-Stand wurde sie offenbar dokumentiert.

**Muss ich meine `CLAUDE.md` wirklich alle 6 Monate löschen?**
Das ist Chernys Empfehlung als **Experiment**, kein Muss: `CLAUDE.md`, Skills und Hooks probeweise entfernen und beobachten, was das Modell ohne sie tut — nicht jede Instruktion, die vor einem Jahr nötig war, ist es mit dem aktuellen Modell noch. Wieder eingefügt wird nur, was das Modell nachweislich wiederholt braucht (Pruning-Test, Abschnitt 2), nicht auf Verdacht.

**Was hat das Kontext-Budget mit Context Engineering zu tun?**
Context Engineering (Abschnitt 1) ist die Disziplin; das Kontext-Budget (Abschnitt 4) ist die Zutatenliste, auf die sie angewendet wird — System-Prompt, Tool-Definitionen, `CLAUDE.md`/Rules, Gesprächsverlauf und Tool-Outputs. Jede der Context-Engineering-Techniken (Altitude, Tool-Minimalismus, JIT-Retrieval) plus die Compaction-Strategie senkt einen anderen dieser Posten.

**Warum zählt Verification als „wichtigster Hebel", wenn es doch auch `/goal` und Stop-Hooks gibt?**
Weil `/goal` und Stop-Hooks ([Modul 8](./08-agenten-skalierung.md)) selbst nur *funktionieren*, wenn die zugrunde liegende Condition tatsächlich beweisbar ist — sie sind die Mechanik, Verification ist die Voraussetzung dafür, dass die Mechanik überhaupt etwas Sinnvolles prüft. Ein Stop-Hook auf einen ungeprüften Check ist wertlose Automatisierung.

**Was hat „Unhobbling" mit Claude Codes Entstehung zu tun?**
Claude Code selbst ist laut Cherny ein Beispiel für Unhobbling: Sonnet 3.5 konnte schon ganze Dateien schreiben, aber Coding-Produkte der Zeit ließen es nur Autocomplete oder Lese-Chat machen — Product Overhang. Claude Code entfernte diese Scaffolding und gab dem Modell direkten Terminal-Zugriff. Die Lehre daraus ist allgemeiner als die eine Anekdote: Frag bei jedem Produkt, das du auf einem Modell baust, ob es dem Modell im Weg steht (Hobbling) oder ob eine Fähigkeit brachliegt (Overhang) — nicht nur einmal beim Bauen, sondern bei jeder neuen Modellgeneration erneut.

---

## Quellen & Weiterlesen

- Ausgelagert aus: [`08-agenten-skalierung.md`](./08-agenten-skalierung.md) (§6 „Die Disziplinen dahinter", §7 CLAUDE.md-Pflegeregeln)
- Verification-Leiter & Evidenz-Regel: [`07-agenten-grundlagen.md`](./07-agenten-grundlagen.md)
- Begriffe nachschlagen: [`glossar.md`](./glossar.md)
- Boris Cherny (Y Combinator) — „We Cut 80% of Claude Code's Prompt": https://www.youtube.com/watch?v=qyPCVqFUyDo (2026-07-27, 35:51) — Sekundärquelle für alle mit „YC-Video" markierten Aussagen und Anekdoten
- CLI-Referenz (`--system-prompt`, `--append-system-prompt`): https://code.claude.com/docs/en/cli-reference (abgerufen 2026-07-30)
- Umgebungsvariablen (`CLAUDE_CODE_SIMPLE`, `--bare`): https://code.claude.com/docs/en/env-vars (abgerufen 2026-07-30)
- Dynamic Workflows (Primärquelle): https://code.claude.com/docs/en/workflows (abgerufen 2026-07-30)
- Scheduled Tasks / Routines (Primärquelle): https://code.claude.com/docs/en/scheduled-tasks (abgerufen 2026-07-30)
