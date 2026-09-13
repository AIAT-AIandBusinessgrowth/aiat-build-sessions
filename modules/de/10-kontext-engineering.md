# Modul 10 — Kontext-Engineering (die Disziplinen hinter dem Skalieren)

> Deutsche Fassung · Stand 2026-09-13 · Englischer Lernpfad: [START-HERE](../../START-HERE.md)

⏱ ~15 min · **Danach kannst du:** einem Agenten die nötigen Informationen geben, veraltete Anweisungen erkennen und einen Auftrag mit klaren Grenzen und einer passenden Prüfung formulieren.

**Setzt voraus:** die Grundidee eines Agenten aus [Modul 7](./07-agenten-grundlagen.md). Die Befehle für längere und parallele Arbeit erklärt [Modul 8](./08-agenten-skalierung.md); du kannst sie bei Bedarf dort nachschlagen.

## Worum es geht

Ein Agent soll eine Datei ändern, liest aber noch lange Protokolle und Anweisungen zur vorherigen Aufgabe mit. Das kann ihn ablenken. **Context Engineering heißt: dafür sorgen, dass er die passenden Informationen zur aktuellen Aufgabe bekommt.** Sein Context-Window ist die begrenzte Menge Text und Tool-Ausgabe, die er auf einmal verarbeiten kann.

Beginne mit einer kleinen Prüfung deiner Projektanweisungen: Welche Zeile erklärt eine wichtige Regel? Welche beschreibt nur einen alten Sonderfall? Markiere eine möglicherweise veraltete Zeile und prüfe ihre Wirkung in einer gesicherten Kopie, bevor du sie entfernst. Datenschutz-, Zugriffs- und Freigaberegeln bleiben bestehen.

Abschnitte 1, 2 und 4 helfen bei dieser Arbeit. Die übrigen Abschnitte erklären Hintergründe und Beispiele aus einem Vortrag von Boris Cherny; du musst sie für den ersten Versuch nicht vorab lesen.

---

## 1. Die vier Disziplinen (aus Modul 8 §6 ausgelagert)

Vier Gewohnheiten helfen, wenn Aufgaben länger dauern oder mehrere Agenten beteiligt sind. Die Fachbegriffe stehen dabei, damit du sie in anderer Dokumentation wiedererkennst.

| Disziplin | Worum es geht | Wofür beim Skalieren |
|---|---|---|
| **Context Engineering** | Informationen passend auswählen: Ziel und Grenzen deutlich beschreiben („Altitude"), nur benötigte Tools bereitstellen und Detailwissen bei Bedarf nachladen („JIT-Retrieval"). | Weniger irrelevanter Text; wichtige Regeln und Dateien sind leichter zu finden. |
| **Autonomy-Slider** | Pro Aufgabe festlegen, was der Agent selbst tun darf: nur vorschlagen, Dateien ändern oder länger selbstständig arbeiten (Andrej Karpathy). Die Modellwahl ist eine weitere Entscheidung: **`opusplan`** (`/model opusplan`) nutzt **Opus zum Planen, Sonnet zum Ausführen**. *(Quelle: code.claude.com/docs/en/model-config#opusplan-model-setting)* | Je größer die möglichen Folgen, desto wichtiger sind begrenzte Rechte und passende Prüfungen ([Modul 7](./07-agenten-grundlagen.md)). |
| **Long-horizon Memory** | Für mehrere Sessions Ziel, Fortschritt und offene Fragen in Dateien festhalten. Vor dem Kürzen des Gesprächs („Compaction") sichern, was erhalten bleiben muss. | Eine neue Session kann den Stand nachlesen, statt alles aus dem alten Chat rekonstruieren zu müssen. |
| **„Build for agents"** | Projekte verständlich beschreiben: klare Dateinamen, Startanleitung, ausführbare Checks und bei Websites etwa eine `llms.txt`. | Ein frischer Agent findet die zuständigen Dateien und kann sein Ergebnis selbst prüfen. |

## 2. `CLAUDE.md`-Pflege (aus Modul 8 §7 ausgelagert)

Wer im Team teilt, klärt [Modul 8](./08-agenten-skalierung.md#7-org-level-scaling--vom-einzelnen-zum-team) (Global/Team/Persönlich/Monorepo-Hierarchie). Hier geht es darum, diese Datei aktuell zu halten:

- **Kurz halten** (Pruning-Faustregel: „Würde Entfernen dieser Zeile Claude Fehler machen lassen? Wenn nein, raus"). Viele widersprüchliche oder veraltete Regeln können wichtige Anweisungen verdrängen. Entferne eine Regel erst nach Prüfung; Sicherheits- und Freigabevorgaben sind kein optionales Zusatzwissen.
- **Längere Themen in eigene Dateien auslagern** mit `@path/to/import` — statt eine Datei aufzublähen, gezielt Teildateien einbinden.
- **Wichtige Informationen beim Kürzen erhalten**: in der `CLAUDE.md` festhalten, was beim Verdichten erhalten bleiben muss (z.B. „always preserve the full list of modified files").

## 3. Boris Cherny: 80% des System-Prompts gelöscht (YC-Video, 2026-07-27)

Anlässlich des Opus-5-Release erklärt Cherny, warum Anthropic **über 80% des Claude-Code-System-Prompts löschte** (YC-Video, ~04:00): Vieles darin korrigierte Verhalten, das ältere Modelle brauchten — Opus 5 „macht es einfach, ohne dass wir es ihm sagen müssen", und ist laut Cherny „ohne diese Prompts sogar etwas intelligenter". Das ist keine einmalige Aufräumaktion, sondern Dauerzustand: Bei **jedem** neuen Modell werden System-Prompt und Tool-Set neu vermessen, weil sich Modelle zwischen Generationen stark unterscheiden.

**Ablation als Methode (~04:00–06:00):** Ablation heißt hier: Teile entfernen und die Wirkung vergleichen. Statt zu raten, was ein Modell noch braucht, löscht das Team den Prompt komplett und holt Zeile für Zeile zurück, um die Wirkung jeder einzelnen zu messen — die Wirkung wird an Testfällen gemessen. Ergänzend nennt Cherny **„simple mode"** (Umgebungsvariable `CLAUDE_CODE_SIMPLE=1`, ~05:00): Im Vortrag beschreibt er sie als stark reduzierten Betriebsmodus. Cherny bezeichnet sie im Video als „kind of this undocumented feature". **Hinweis:** Im Video (2026-07-27) nennt Cherny die Variable „undokumentiert" — inzwischen ist sie offiziell dokumentiert (`code.claude.com/docs/en/env-vars.md`, Stand 2026-07-30), äquivalent zum `--bare`-Flag (Bash/Read/Edit-Tools, keine Auto-Discovery von Hooks/Skills/Plugins/CLAUDE.md).

**Die 6-Monats-Regel (~06:00–08:00):** Für alle, die selbst mit Claude Code arbeiten (nicht nur für Anthropic intern), empfiehlt Cherny: **alle 6 Monate `CLAUDE.md`, Skills und Hooks löschen** und beobachten, was das Modell ohne sie tut. Der Grund ist derselbe wie bei der Ablation: „das Modell liest jede Instruktion jedes Mal" — eine Zeile, die niemand mehr braucht, kostet trotzdem bei jedem Turn. Eine Instruktion kommt erst zurück, wenn das Modell **wiederholt** an derselben Stelle stolpert, nie präventiv „auf Verdacht".

**Für dein Projekt:** Probiere ein solches Weglassen nur in einer gesicherten, isolierten Kopie aus. Es ist keine Anweisung, geltende Projekt-, Datenschutz- oder Freigaberegeln zu löschen. Vergleiche Ergebnisse an denselben Aufgaben und behalte Änderungen erst nach Prüfung.

**Eval-Halbwertszeit (~08:00–10:00):** Evals (kuratierte Testfälle, an denen Modellverhalten gemessen wird) überleben länger als Code und Prompts, aber auch sie sind nicht dauerhaft: „ein Eval mag ein, zwei, drei Modellgenerationen leben", dann saturiert er (das Modell besteht ihn durchgehend) und wird durch einen neuen ersetzt.

> **Nicht verwechseln — Eval ≠ Evaluator:** Ein **Eval** hier ist ein kuratierter Testfall-Satz zur Modellbewertung (dieser Abschnitt). Der **Evaluator** in [Modul 8](./08-agenten-skalierung.md) ist das kleine, schnelle Modell, das bei `/goal` nach jedem Turn prüft, ob die Completion-Condition erfüllt ist. Beide Begriffe klingen ähnlich, meinen aber unterschiedliche Dinge auf unterschiedlichen Ebenen — der eine bewertet Modelle über Zeit, der andere bewertet einen einzelnen laufenden Task.

## 4. Kontext-Budget — was füllt das Context-Window?

Mit `/context` siehst du in Claude Code, wie sich der verfügbare Platz verteilt. Suche zunächst den größten unnötigen Anteil. Die Tabelle ist eine grobe Einordnung aus Vortrag und Dokumentation, kein exaktes Abrechnungsschema des Anbieters.

| Posten | Was er kostet | Wie man ihn senkt |
|---|---|---|
| **System-Prompt** | Fixkosten bei **jedem** Turn — je größer, desto mehr „liest" das Modell immer wieder mit | Ablation (Abschnitt 3); `--system-prompt`/`--append-system-prompt`-Flags zum gezielten Ersetzen/Ergänzen testen (primärquellen-belegt: `code.claude.com/docs/en/cli-reference`, Stand 2026-07-30) — für Fortgeschrittene; als normale:r Nutzer:in sind das Fixkosten, die der Anbieter senkt (s. Abschnitt 3) |
| **Tool-Definitionen** | jedes registrierte Tool-Schema lädt bei jedem Turn mit, ob genutzt oder nicht. Ausnahme: Claude Code lädt MCP-Tools ab v2.1.232 per **Tool Search** erst bei Bedarf *(Quelle: code.claude.com/docs/en/mcp, abgerufen 2026-09-13)* | Tool-Minimalismus (Abschnitt 1); ungenutzte MCP-Server abmelden |
| **`CLAUDE.md` / Rules** | wächst mit jeder Regel, die „auf Verdacht" bleibt | Pruning-Test + 6-Monats-Regel (Abschnitt 2/3) |
| **Gesprächsverlauf** | füllt sich über Turns hinweg, besonders bei langen Sessions | erst Arbeitsstand und offene Fragen sichern, dann `/clear` zwischen unabhängigen Aufgaben; Compaction-Strategie (Abschnitt 1) |
| **Tool-Outputs** | Suchergebnisse, Logs, Diffs — oft der größte Einzelposten bei Recherche-/Fan-out-Aufgaben | Subagents/Dynamic Workflows auslagern, damit nur die Zusammenfassung zurückkommt ([Modul 8](./08-agenten-skalierung.md)) |

## 5. Unhobbling & Product Overhang — Claude Codes Gründungsidee

Cherny nennt zwei Begriffe aus der Anthropic-Forschung, um zu erklären, warum viele Modell-Fähigkeiten ungenutzt bleiben (~10:00–14:00): **Hobbling** ist, wenn ein Produkt einem Modell im Weg steht, obwohl es etwas kann; **Unhobbling** ist das Gegenmittel: die Hindernisse entfernen, die das Produkt dem Modell anlegt. **Product Overhang** ist die Lücke zwischen dem, was ein Modell schon kann, und dem, was ein Produkt davon tatsächlich zulässt. Claude Codes eigene Gründungsgeschichte ist Chernys Beispiel dafür: Als Sonnet 3.5 (damals das stärkste Coding-Modell) schon ganze Dateien schreiben konnte, boten Coding-Produkte noch Autocomplete und reinen Lese-Chat. Die Grundidee hinter Claude Code war, „das gesamte Gerüst drumherum (Scaffolding) wegzunehmen und dem Modell den einfachstmöglichen Harness zu geben" — direkter Terminal-Zugriff als zusätzliche Handlungsmöglichkeit.

Chernys Ableitung für alle, die heute auf Claude bauen: Modelle können regelmäßig mehr, als das umgebende Produkt zulässt. Für die eigene Arbeit lässt sich daraus eine Frage ableiten: Fehlt dem Modell die Fähigkeit, oder fehlt ihm ein passendes Werkzeug? Prüfe das mit einer begrenzten Aufgabe (Abschnitt 6). Zusätzliche Zugriffe müssen zur Aufgabe passen.

## 6. Aufgaben-Kalibrierung — leicht über Fähigkeit, nicht Schritt-für-Schritt

Chernys wiederkehrender Rat (~14:00, wieder aufgegriffen ~24:00): Gib dem Modell eine Aufgabe, die **etwas schwieriger wirkt, als du ihm zutraust** — und beschreibe **Aufgabe, erlaubte Grenzen und ein überprüfbares Ende**, statt Schritt 1-2-3 vorzuschreiben. Sein Befund aus vielen Sessions: „erfahrene Engineers überspezifizieren" — gerade wer jahrelang selbst so gearbeitet hat, neigt dazu, dem Modell den eigenen Lösungsweg vorzuschreiben, statt es das Problem lösen zu lassen.

Du kannst dem Agenten die Wahl der einzelnen Schritte überlassen und trotzdem klare Grenzen setzen. Prüfe anschließend Änderungen und Ergebnis selbst. Eine anspruchsvollere Aufgabe rechtfertigt weder unbegrenzte Rechte noch einen Lauf ohne Stoppmöglichkeit.

## 7. Verification als wichtigster Hebel

Auf die Frage, was die besten Claude-Nutzer:innen von den übrigen unterscheidet, nennt Cherny **Verification** als den entscheidenden Hebel: „the verification I think is probably the single most important thing that people do not get right" (~20:00). Seine Illustration: Er ließ die Electron-basierte Claude-Desktop-App **pixelgenau nach Swift** nachbauen — der komplette Prompt war „baue die App in Swift nach, screenshotte die Electron-Version, vergleiche Pixel für Pixel, hör nicht auf, bis es passt". Der Lauf lief zum Zeitpunkt des Auftritts bereits **über zwei Wochen** mit vermutlich tausenden Agenten (Cherny nennt keine belastbare Zahl — als Behauptung, nicht als Faktum zu lesen). Die Pointe ist nicht die Laufzeit, sondern das Prinzip: **eine Aufgabe, die schwer genug ist, plus ein Weg, das eigene Ergebnis zu prüfen** Eine solche Anekdote ist keine Zusage, dass ein anderer Lauf ebenso endet oder dieselben Ressourcen braucht.

Wie du Ergebnisse selbst prüfst und einen zweiten Agenten zur Gegenprüfung nutzt, steht in Modul 7. Modul 8 ergänzt automatisierte Prüfungen mit `/goal` und Stop-Hooks. Lege vor einem längeren Lauf fest, woran du Erfolg und Fehler erkennst.

## 8. Kurz: Skalierungs-Mechanik, für die Modul 8 zuständig bleibt

Zwei Dinge aus dem Video sind reine Illustration der in Modul 8 bereits beschriebenen Mechanik:

- **Dynamic Workflows als „algebra for agents"** (~26:00) — eine neue Form von Test-Time-Compute (Test-Time-Compute = Rechenaufwand zur Laufzeit einer Anfrage — mehr „Nachdenken" pro Antwort statt größeres Modell): Statt nur mehr Tokens pro Antwort zu generieren, orchestriert ein Workflow Dutzende bis Hunderte Agents in Sequenz und Parallel. Illustrierendes Beispiel: Ein einzelner Dynamic-Workflow-Prompt ließ die Bun-JavaScript-Runtime **von Zig nach Rust neu schreiben** — ein Lauf über **11 Tage** mit Steering unterwegs (Anekdote, keine reproduzierbare Kennzahl). Mechanik dazu steht in [Modul 8](./08-agenten-skalierung.md).
- **Loops/Routines als Selbstwartung** (~28:00–30:00) — Anthropic lässt intern **20 bis 30 tägliche Routines** über die eigenen Codebases laufen: Dead-Code-Cleanup, ausgelaufene Experimente ausbauen, fehlende Tests ergänzen, überflüssige Tests löschen, und die von Cherny so genannte „abstraction police" (nahezu doppelte Abstraktionen im Code vereinheitlichen). Cherny: „we're on the path to fully automating the maintenance of our apps." Mechanik (`/loop`, Cloud-Routines) steht ebenfalls in [Modul 8](./08-agenten-skalierung.md).

Die praktische Empfehlung aus diesen Beispielen: Gib eine begrenzte Aufgabe, beobachte das Ergebnis und passe den nächsten Versuch an. „Empirisch" bedeutet hier schlicht: durch solche Versuche lernen (~22:00, ~32:00 im Video).

---

## Q&A

**Ich schreibe keine System-Prompts und baue keine Tools — was betrifft mich konkret?**
Du kannst veraltete Projektanweisungen markieren, vor einem Themenwechsel den Arbeitsstand sichern und Aufträge genauer formulieren. Beginne mit einer dieser Änderungen und prüfe, ob sie beim nächsten Versuch hilft.

**Was ist der Unterschied zwischen einem Eval und dem `/goal`-Evaluator?**
Ein Eval ist ein kuratierter Testfall-Satz, an dem ein *Modell* über Zeit gemessen wird — er lebt laut Cherny „ein, zwei, drei Modellgenerationen", dann saturiert er und wird ersetzt. Der `/goal`-Evaluator ([Modul 8](./08-agenten-skalierung.md)) ist ein kleines, schnelles Modell, das bei einem *einzelnen laufenden Task* nach jedem Turn prüft, ob die Completion-Condition erfüllt ist. Unterschiedliche Ebene, unterschiedlicher Lebenszyklus — trotz ähnlichem Namen nicht dasselbe.

**Widerspricht „Aufgaben nicht überspezifizieren" nicht dem Grundsatz „Verlange Evidenz, vertraue nicht"?**
Nein, das sind zwei verschiedene Momente derselben Delegation. „Nicht überspezifizieren" gilt fürs **Beauftragen**: lieber Task, Guardrails und Exit-Kriterium beschreiben als Schritt 1-2-3 vorschreiben. „Verlange Evidenz" gilt fürs **Abnehmen**: das Ergebnis bleibt so lange unbewiesen, bis Test-Output, Diff oder Screenshot es belegen. Weniger Mikromanagement vorher heißt nicht weniger Prüfung nachher.

**Ist `CLAUDE_CODE_SIMPLE=1` dasselbe wie `--bare`?**
Laut `code.claude.com/docs/en/env-vars.md` (Stand-Check 2026-07-30) ja: Die Variable ist als äquivalent zum `--bare`-Flag dokumentiert — minimaler System-Prompt, nur Bash/Read/Edit-Tools, keine Auto-Discovery von Hooks, Skills, Plugins, MCP-Servern, Memory oder `CLAUDE.md`. Im YC-Video nennt Cherny sie noch „kind of this undocumented feature" (2026-07-27) — zwischen Aufnahme und heutigem Doku-Stand wurde sie offenbar dokumentiert.

**Muss ich meine `CLAUDE.md` wirklich alle 6 Monate löschen?**
Nein. Das ist eine Empfehlung zum Experimentieren, keine Kursaufgabe. Teste vermutete Altlasten nur in einer gesicherten Kopie, ohne geltende Schutzregeln aufzuheben. Behalte die Änderung erst, wenn die Vergleichsaufgaben weiterhin korrekt funktionieren.

**Was hat das Kontext-Budget mit Context Engineering zu tun?**
Das Kontext-Budget zeigt, was den verfügbaren Platz belegt. Context Engineering ist die Arbeit daran: Unnötiges entfernen und benötigte Informationen im richtigen Moment bereitstellen.

**Warum zählt Verification als „wichtigster Hebel", wenn es doch auch `/goal` und Stop-Hooks gibt?**
Weil `/goal` und Stop-Hooks ([Modul 8](./08-agenten-skalierung.md)) selbst nur *funktionieren*, wenn die zugrunde liegende Condition tatsächlich beweisbar ist — sie sind die Mechanik, Verification ist die Voraussetzung dafür, dass die Mechanik überhaupt etwas Sinnvolles prüft. Teste deshalb auch den Check: Erkennt er einen bekannten Fehler und lässt er ein korrektes Ergebnis durch?

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
