# Modul 9 — Rollen-Archetypen im agentischen Arbeiten

> Deutsche Fassung · Stand 2026-09-13 · Englischer Lernpfad: [START-HERE](../../START-HERE.md)

⏱ ~10 min · **Danach kannst du:** mit dem Selbst-Check benennen, welche Archetypen du gerade trägst, und daraus ableiten, welche Werkzeuge und welchen Autonomiegrad deine aktuelle Arbeit verlangt.

**Setzt voraus:** [Modul 7 — Agenten-Grundlagen](./07-agenten-grundlagen.md) — insbesondere die dort benannte „Delegation-Gap", an die dieses Modul anschließt.

## Worum es geht

[Modul 7](./07-agenten-grundlagen.md) benennt die **„Delegation-Gap"**: Teams nutzen KI in einem Großteil ihrer Arbeit, können aber nur einen Bruchteil der Aufgaben wirklich *voll* an Agenten delegieren — **„Das Tooling ist da, die Arbeitsweise fehlt."** Dieses Modul liefert das **Vokabular für genau diese Arbeitsweise**: Rollen-Archetypen beschreiben, *wie* Menschen arbeiten, wenn Agenten einen wachsenden Teil des Ausführens übernehmen.

Der Meta-Shift dahinter: Die Arbeit verschiebt sich **vom Job-Ausführen zum Managen von Agenten, die den Job ausführen**. Wer früher selbst jede Zeile getippt, jede Folie gebaut, jede Auswertung geklickt hat, briefed heute, prüft und entscheidet — die Archetypen benennen die wiederkehrenden Muster dieser neuen Arbeit.

Zwei Dinge vorab, damit das Modell nicht missverstanden wird:

- **Rollen sind nicht an Jobtitel gebunden.** Bei Anthropic (der Firma hinter Claude, in der Quellen-Autor Boris Cherny arbeitet) matchen Designer, Engineers und PMs quer über alle Archetypen — der Titel sagt nicht, welche Rolle jemand tatsächlich trägt.
- **Die meisten Menschen tragen 2–3 Rollen** gleichzeitig, und der Mix verschiebt sich mit der Lebensphase des Produkts (siehe Lifecycle-Mix unten).

---

## 1. Die fünf Kern-Archetypen (Boris Cherny, Claude-Code-Team)

Boris Cherny (Claude-Code-Team) beschreibt fünf Kern-Archetypen, die er im agentischen Arbeiten immer wieder beobachtet — sie schauen alle **nach innen**, auf das Produkt und seinen Lebenszyklus:

| Archetyp | Was er/sie tut | Woran man ihn/sie erkennt |
|---|---|---|
| **Prototyper** | erzeugt laufend neue Ideen und baut erste lauffähige Versionen — die meisten davon shippen nie | ersetzt endlose Diskussionsphasen durch „schaut her, läuft schon": Gespräche finden am realen Artefakt statt, nicht am Konzeptpapier |
| **Builder** | macht aus einem Prototyp ein production-grade Produkt (= einsatzreif im echten Betrieb) bzw. tragfähige Infrastruktur | denkt an Security, Edge-Cases und Betrieb — genau das, was der Prototyper bewusst ignoriert |
| **Sweeper** | vereinfacht UI, Code und System; shippt Features auch wieder aus (unship); optimiert Performance | Schlüsselwort **optimieren**, nicht bloß aufräumen — eine eigene Denkweise, kein Nebenjob des Builders |
| **Grower** | iteriert am gebauten Produkt Richtung Product-Market-Fit | die erste Rolle, die **nach außen** zeigt — lernt aus echter Nutzung statt aus internen Annahmen |
| **Maintainer** | ownt ein reifes System: sicher, zuverlässig, schnell, effizient im Scale | kategorial andere Arbeit als Neubauen — Stabilität und Effizienz statt Feature-Tempo |

### Warum Agenten diese Rollen sichtbar machen

Die Archetypen gab es als Neigungen schon immer — agentisches Arbeiten macht sie zu **tragenden Rollen**, weil sich der Engpass verschiebt:

| Archetyp | Vorher (ohne Agenten) | Mit Agenten |
|---|---|---|
| **Prototyper** | eine Idee zu bauen kostete Tage — die meisten Ideen blieben Folien | ein Prototyp kostet einen Nachmittag; die Engstelle ist nicht mehr das Bauen, sondern das Auswählen |
| **Builder** | production-grade war die Fortsetzung des Prototyps mit denselben Mitteln | der Abstand Prototyp → Produktion wird zum bewussten Schnitt: je billiger Prototypen, desto wichtiger die Production-Disziplin |
| **Sweeper** | Vereinfachen fiel hinten runter — „keine Zeit" | Agenten senken die Kosten des Optimierens; Unshippen und Performance-Arbeit werden planbar |
| **Grower** | Markt-Iteration war durch Dev-Kapazität begrenzt | Experimente sind billig — der Engpass ist sauberes Lernen aus echter Nutzung |
| **Maintainer** | Wartung konkurrierte mit Features um dieselben Hände | Routine-Wartung ist teilweise delegierbar; der Mensch hält Verantwortung und Blast-Radius im Blick |

### Der Lifecycle-Mix — welche Rollen wann

Der Rollen-Mix folgt der Lebensphase des Produkts, nicht dem Organigramm:

| Phase | Trägt stark | Dazu etwas |
|---|---|---|
| **Pre-PMF** (vor Product-Market-Fit — neu, noch suchend) | Prototyper + Builder + Sweeper | Grower/Maintainer kaum — es gibt noch nichts Reifes zu wachsen oder zu pflegen |
| **Wachsend** | Builder + Sweeper + Grower | etwas Maintainer — erste Teile des Systems werden „Betrieb" |
| **Reif** | Sweeper + Grower + Maintainer | etwas Builder — für neue Fähigkeiten am bestehenden System |

> **Merksatz:** Der Rollen-Mix ist kein Organigramm, sondern folgt der Lebensphase des Produkts — pre-PMF wird prototypt und gebaut, wachsend optimiert und gewachsen, reif gepflegt und verdichtet. Wer seine 2–3 Rollen kennt, erkennt auch, wann sie sich verschieben müssen.

---

## 2. Die außen-zugewandten Rollen (Erweiterung, AI Daily Brief)

Chernys fünf Archetypen schauen auf das Produkt. Der Podcast **AI Daily Brief** erweitert das Bild um Rollen, die entstehen, wenn Bauen durch Agenten billig wird — denn dann verschiebt sich der Engpass **nach außen**: auf Aufmerksamkeit, Markt-Signal, Koordination und Risiko.

| Rolle | Was sie tut | Woran man sie erkennt |
|---|---|---|
| **Editor** | entscheidet, welche der vielen Prototypen weiterleben | kuratiert statt erzeugt — wenn Bauen billig wird, bleibt **Markt-Aufmerksamkeit knapp**; jemand muss Nein sagen |
| **Scout** | holt Signal von draußen rein: Markt, Wettbewerb, Nutzer, Technologie | oft **teilweise agentisch besetzbar** — Agenten sammeln und vorsortieren, der Mensch bewertet |
| **Evangelist** | bringt den Markt zur Sicht der Builder: Content, Conversation, Community | die Gegenrichtung zum Scout — Signal geht nach draußen statt herein |
| **Orchestrator** | koordiniert Rollen-Bündel und Arbeitsströme über Teams hinweg — gemeint ist die **menschliche Rolle**, nicht der technische Orchestrator-Agent (der übergeordnete Agent, der Subagents startet; vgl. Subagents in [Modul 7](./07-agenten-grundlagen.md)) | denkt in Übergaben und Engpässen, nicht in einzelnen Tasks |
| **Conductor** | Orchestrator speziell für **Agenten-Flotten** als „digitale Mitarbeiter" | führt Agenten wie ein Team: briefen, beobachten, Ergebnisse abnehmen |
| **Risk Steward** | antizipiert Risiken Schritte im Voraus, damit das Tempo hält | **Beschleuniger, nicht Gatekeeper** — räumt Risiken weg, bevor sie bremsen |

### Über Produkt-Teams hinaus

Die Archetypen sind nicht auf Software-Produkt-Teams beschränkt. Ein Sales-Team hat seinen Prototyper, sobald jemand mit einem Agenten ein kleines Lead-Qualifizierungs- oder Angebots-Tool für den eigenen Funnel baut. Im Back-Office ist der Sweeper, wer den Rechnungs-Workflow vereinfacht, statt der Excel-Tabelle eine dritte Hilfsspalte zu verpassen — und der Scout, wer regulatorische Änderungen agentengestützt vorsortiert, bevor sie das Team treffen. Der Kernsatz dazu: **„When making gets cheap enough, every function starts to grow a maker"** — jede Funktion bekommt ihren Maker.

> **Merksatz für Nicht-Devs:** Du musst kein Engineer sein, um Prototyper zu sein — wer mit einem Agenten ein kleines Tool für den eigenen Job baut, prototypt bereits.

---

## 3. Rollen und Werkzeuge — die Brücke zu Modul 7 und 8

Die Archetypen sind das *Wer*, die Module 7 und 8 liefern das *Womit*. Typische Paarungen (Orientierung, kein Dogma):

| Rolle | Typisches Werkzeug (Modul 7/8) | Warum es passt |
|---|---|---|
| **Prototyper** | interaktiver Loop, Autonomy-Slider weit offen | Wegwerf-Artefakte, geringes Risiko — Tempo schlägt Absicherung (Modul 10, Abschnitt 1 — Disziplin „Autonomy-Slider") |
| **Builder** | Plan Mode, Verification-Leiter, enge Permission-Modi | production-grade heißt Evidenz verlangen, nicht hoffen (Modul 7) |
| **Sweeper** | Writer/Reviewer-Pattern, Fan-out für Massen-Vereinfachungen | Optimieren über viele Dateien skaliert nur mit frischem Review-Context (Modul 8) |
| **Maintainer** | `/loop` und Cloud-Routines für Routine-Wartung, hartes Gating | Takt statt Endzustand — großer Blast-Radius verlangt enge Leitplanken (Modul 8) |
| **Conductor** | Agent Teams, Worktree-Parallelität, Monitor-Tool | führt Agenten-Flotten über eine gemeinsame Task-Liste statt einzelne Sessions (Modul 8, Abschnitt 7) |

---

## 4. Selbst-Check — welche Rollen trägst du gerade?

Drei Fragen zur Standortbestimmung. Zur Orientierung für Nicht-Dev-Rollen: Wer primär koordiniert, priorisiert und Qualität abnimmt, statt selbst zu bauen, findet sich meist in den außen-zugewandten Rollen aus Abschnitt 2 wieder (etwa Editor, Orchestrator oder Risk Steward) — die drei Fragen helfen beim genaueren Verorten:

1. **Rückblick:** Welche zwei Tätigkeiten der letzten zwei Wochen haben den größten Teil deiner Energie gebunden — und welchem Archetyp entsprechen sie?
2. **Phase:** In welcher Lifecycle-Phase steckt dein wichtigstes Projekt (pre-PMF / wachsend / reif) — und deckt dein aktueller Rollen-Mix das, was die Phase braucht?
3. **Lücke:** Welche Rolle ist in deinem Team gerade unbesetzt — und ist sie teilweise agentisch besetzbar (Scout, Conductor) oder braucht sie zwingend einen Menschen (Editor, Risk Steward)?

Das Ergebnis ist keine Festlegung, sondern eine Standortbestimmung — sie darf sich mit jeder Projektphase ändern.

---

## Q&A

**Muss ich mich auf eine Rolle festlegen?**  
Nein. Die meisten Menschen tragen 1–3 Rollen gleichzeitig, und der Mix ist nicht statisch: Er verschiebt sich mit der Lifecycle-Phase des Produkts (siehe Lifecycle-Mix oben). Nützlicher als Festlegen ist Selbst-Verorten — genau dafür ist der **Selbst-Check (Abschnitt 4)**: welche 2–3 Rollen trägst du gerade, welche braucht das Projekt als Nächstes?

**Ist der Sweeper nicht einfach Teil vom Builder?**  
Nein — der Unterschied ist die Denkweise. Der Builder macht Neues production-grade; der Sweeper **optimiert Bestehendes**: vereinfachen, unshippen, Performance. Wer nur baut, räumt erfahrungsgemäß selten ab — deshalb ist Optimieren als eigene Rolle benannt, nicht als Nebenjob.

**Welche Rollen braucht ein neues Team oder Projekt zuerst?**  
Prototyper + Builder + Sweeper. Pre-PMF gibt es nichts zu wachsen (Grower) und nichts Reifes zu pflegen (Maintainer) — aber sehr wohl schon etwas zu vereinfachen, bevor sich Komplexität festsetzt.

**Wie hängt das mit dem Autonomy-Slider aus Modul 10 zusammen?**  
Die Rolle bestimmt, wie viel Leine typischerweise sinnvoll ist: Ein Prototyper fährt viel Autonomie (Wegwerf-Artefakte, geringes Risiko), ein Maintainer wenig (reifes System, großer Blast-Radius). Rollen-Archetyp und Autonomy-Slider sind zwei Achsen derselben Entscheidung — *was* delegiere ich, und *wie eng* führe ich dabei. → Details in Modul 10, Abschnitt 1 (Disziplin „Autonomy-Slider").

**Was ist mit Governance und Risiko — bremst das nicht alles aus?**  
Dafür gibt es den Risk Steward, und zwar als **Tempo-Halter**: Er antizipiert Risiken Schritte im Voraus (Security, Compliance, Reputation), damit die anderen Rollen nicht an unerwarteten Gates hängen bleiben. Gut besetzt beschleunigt er; als nachgelagerter Gatekeeper wäre er genau die Bremse, die er verhindern soll.

**Wie nutze ich die Rollen in einer Build Session oder beim Arbeiten zu zweit?**

Die Rollen sind **Linsen**, keine Jobtitel. In einer Build Session kannst du mehrere Rollen tragen: Als Prototyper formulierst du ein erstes Issue oder baust den schnellen Entwurf, als Builder machst du daraus einen belastbaren Stand, als Sweeper vereinfachst du, als Reviewer oder Risk Steward prüfst du Diff, Risiken und Evidenz, und als Conductor oder Orchestrator hältst du Übergaben, Reihenfolge und „fertig“ zusammen. Arbeitet ihr zu zweit, hilft die Trennung besonders: Eine Person arbeitet mit dem Agenten, die andere liest Diff, Akzeptanzkriterien und Check-Output. Welche Rollen ihr ausdrücklich verteilt, entscheidet ihr selbst.

**Können Agenten selbst Rollen besetzen?**  
Teilweise. Der Scout ist heute schon teilweise agentisch besetzbar (Signal sammeln und vorsortieren), und den Conductor gibt es genau deshalb, weil Agenten-Flotten als „digitale Mitarbeiter" geführt werden wollen. Die Entscheidungs-Rollen — Editor, Risk Steward — bleiben beim Menschen: Die Accountability wandert nicht mit (vgl. Vibe Engineering in Modul 7).

---

## Quellen & Weiterlesen

Stand der Quellenliste: 2026-09-13.

- Vorwissen — Delegation-Gap & der agentische Loop: [`07-agenten-grundlagen.md`](./07-agenten-grundlagen.md)
- Autonomy-Slider: [`10-kontext-engineering.md`](./10-kontext-engineering.md) (Abschnitt 1) · Org-Level-Scaling: [`08-agenten-skalierung.md`](./08-agenten-skalierung.md) (Abschnitt 7)
- Begriffe nachschlagen: [`glossar.md`](./glossar.md)
- Boris Cherny (Claude-Code-Team): X/Twitter `@bcherny`, Thread ~Ende Juni 2026 — Original der fünf Kern-Archetypen. Das exakte Datum des Threads ist nicht belegt. URL: https://x.com/bcherny/status/2071379474277613732
- AI Daily Brief (Podcast): Episode „The Job Positions of the AI Future", veröffentlicht 2026-07-05, Erweiterung um die außen-zugewandten Rollen: https://podcasts.apple.com/us/podcast/the-job-positions-of-the-ai-future/id1680633614?i=1000775522675 *(abgerufen 2026-09-13)*
