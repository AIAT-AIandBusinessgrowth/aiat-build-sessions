# Modul 9 — Rollen-Archetypen im agentischen Arbeiten

> Deutsche Fassung · Stand 2026-09-13 · Englischer Lernpfad: [START-HERE](../../START-HERE.md)
>
> Öffentliche Fassung eines intern gepflegten Moduls: gekürzt und für ein allgemeines Publikum überarbeitet; fortgeschrieben und gepflegt wird der interne Text (Stand 2026-09-13).

⏱ ~10 min · **Danach kannst du:** benennen, welche Arbeit dein Projekt gerade braucht und welche Aufgaben ein Agent dabei übernehmen kann.

**Setzt voraus:** keine Programmierkenntnisse. Wie ein Agent arbeitet, erklärt [Modul 7](./07-agenten-grundlagen.md).

## Worum es geht

Eine erste Idee ausprobieren, sie zuverlässig zum Laufen bringen und sie später betreuen: Das sind verschiedene Aufgaben. Ein Agent kann bei allen helfen. Jemand muss aber entscheiden, was gebraucht wird und ob das Ergebnis passt.

Dieses Modul gibt diesen Tätigkeiten Namen. **„Archetyp" heißt hier: ein wiederkehrendes Arbeitsmuster.** Die Namen helfen euch, Aufgaben zu verteilen; sie sind keine neuen Jobtitel.

Denk zuerst an eine konkrete Aufgabe aus deiner letzten Arbeitswoche. Suche in den Tabellen die Tätigkeit, die dazu passt. Du darfst mehrere wählen. Für einen kurzen Einstieg reichen die erste Tabelle und der [Selbst-Check](#4-selbst-check--welche-rollen-trägst-du-gerade).

---

## 1. Die fünf Kern-Archetypen (Boris Cherny, Claude-Code-Team)

Boris Cherny aus dem Claude-Code-Team beschreibt fünf Muster, die er bei der Arbeit an Produkten beobachtet. Das ist eine Orientierung aus seiner Praxis, keine allgemeingültige Einteilung von Menschen. Designer, Entwickler und Produktverantwortliche können dieselben Tätigkeiten übernehmen.

| Archetyp | Was er/sie tut | Woran man ihn/sie erkennt |
|---|---|---|
| **Prototyper** | baut eine kleine erste Version einer Idee | Andere können sie ausprobieren und sagen, was daran nützlich ist. Manche Versuche werden danach verworfen. |
| **Builder** | macht eine erste Version für den tatsächlichen Einsatz bereit | prüft etwa Sicherheit, ungewöhnliche Eingaben und Betrieb; auch ein Prototyp braucht Schutz für Daten und Zugänge |
| **Sweeper** | vereinfacht ein bestehendes Produkt | entfernt unnötige Funktionen, macht die Bedienung klarer oder verbessert die Geschwindigkeit |
| **Grower** | verbessert das Produkt anhand echter Nutzung | prüft, ob es ein Problem so gut löst, dass Menschen es wieder verwenden wollen; das nennt man Product-Market-Fit |
| **Maintainer** | betreut ein bestehendes System | behebt Fehler, aktualisiert es und hält es bei mehr Nutzung zuverlässig |

### Warum Agenten diese Rollen sichtbar machen

Agenten können einen Teil der Ausführung übernehmen. Dadurch kann mehr Zeit für Auswahl, Prüfung und Rückmeldungen bleiben. Wie viel Zeit das spart, hängt von Aufgabe, Werkzeug und notwendiger Kontrolle ab.

| Archetyp | Vorher (ohne Agenten) | Mit Agenten |
|---|---|---|
| **Prototyper** | setzt einen Entwurf selbst um | kann mehrere kleine Entwürfe erstellen lassen und den aussichtsreichsten ausprobieren |
| **Builder** | ergänzt und prüft die nötigen Funktionen | lässt Teile umsetzen, prüft aber weiterhin Anforderungen, Datenzugriffe und Fehlerfälle |
| **Sweeper** | sucht und vereinfacht umständliche Stellen | kann Vorschläge sammeln lassen und prüfen, ob eine Vereinfachung das Verhalten erhält |
| **Grower** | entwirft und wertet Nutzungsversuche aus | kann Varianten schneller vorbereiten; echte Rückmeldungen bleiben nötig |
| **Maintainer** | erledigt wiederkehrende Wartungsaufgaben | kann geeignete Aufgaben delegieren, mit begrenzten Rechten und einem Plan für Fehler |

### Der Lifecycle-Mix — welche Rollen wann

Welche Tätigkeiten gerade viel Zeit brauchen, hängt vom Stand des Produkts ab. Die Tabelle zeigt ein mögliches Muster, keine Personalvorgabe. Auch ein neues Projekt braucht Rückmeldungen von möglichen Nutzer:innen und jemanden, der Fehler behebt.

| Phase | Trägt stark | Dazu etwas |
|---|---|---|
| **Pre-PMF** (vor Product-Market-Fit — neu, noch suchend) | Prototyper + Builder + Sweeper | Grower für frühe Rückmeldungen; Maintainer für bereits genutzte Teile |
| **Wachsend** | Builder + Sweeper + Grower | Maintainer — mehr Teile müssen im Alltag verlässlich laufen |
| **Reif** | Sweeper + Grower + Maintainer | Builder — für neue Fähigkeiten am bestehenden System |

Prüfe den Mix erneut, wenn sich die Nutzung ändert. Eine gute erste Version kann später vor allem Wartung brauchen.

---

## 2. Die außen-zugewandten Rollen (Erweiterung, AI Daily Brief)

Der Podcast **AI Daily Brief** ergänzt Tätigkeiten rund um Auswahl, Kommunikation, Koordination und Risiko. Sie helfen zu klären, was überhaupt gebaut werden soll und wer die Folgen einer Entscheidung trägt.

| Rolle | Was sie tut | Woran man sie erkennt |
|---|---|---|
| **Editor** | entscheidet, welche Ideen weiterverfolgt werden | vergleicht Nutzen und Aufwand und beendet Versuche, die nicht weiterhelfen |
| **Scout** | sammelt Hinweise zu Markt, Wettbewerb, Nutzung und Technik | lässt bei Bedarf Agenten vorsortieren und prüft Quellen und Bedeutung selbst |
| **Evangelist** | erklärt das Produkt nach außen | zeigt mögliche Anwendungen und spricht mit Interessierten |
| **Orchestrator** | koordiniert Menschen und Aufgaben über Teams hinweg | klärt Reihenfolge, Übergaben und offene Entscheidungen; hier ist die **menschliche Rolle** gemeint, nicht der Agent, der Subagents startet |
| **Conductor** | koordiniert mehrere Agenten | verteilt begrenzte Aufgaben, beobachtet die Arbeit und prüft die Ergebnisse |
| **Risk Steward** | prüft früh mögliche Schäden und notwendige Schutzmaßnahmen | klärt etwa Datenzugriffe, Freigaben und Zuständigkeiten, bevor ein Problem entsteht |

### Über Produkt-Teams hinaus

Diese Tätigkeiten gibt es auch außerhalb der Softwareentwicklung. Wer einen Entwurf für ein kleines Angebotstool ausprobiert, prototypt. Wer einen umständlichen Rechnungsablauf vereinfacht, arbeitet als Sweeper. Wer Änderungen von Regeln recherchiert und für das Team einordnet, übernimmt eine Scout-Aufgabe.

Du brauchst dafür keinen neuen Titel. Benenne die konkrete Arbeit, die du übernehmen willst. In den Kursübungen bleiben alle Beispiele frei von echten Kunden- und Personendaten.

---

## 3. Rollen und Werkzeuge — die Brücke zu Modul 7 und 8

Wähle Werkzeuge nach der Aufgabe und ihrem Risiko. Die folgenden Paarungen sind Beispiele. Eine Rolle allein rechtfertigt keine zusätzlichen Zugriffsrechte.

| Rolle | Typisches Werkzeug (Modul 7/8) | Warum es passt |
|---|---|---|
| **Prototyper** | interaktiver Loop: Auftrag geben, ausprobieren, ändern | schnelle Rückmeldung an einer kleinen, entbehrlichen Kopie; Daten- und Kostengrenzen bleiben nötig |
| **Builder** | Plan Mode, Verification-Leiter, begrenzte Permissions | vorab klären, was gebraucht wird; danach nachprüfen, ob es funktioniert ([Modul 7](./07-agenten-grundlagen.md)) |
| **Sweeper** | Writer/Reviewer-Pattern; bei unabhängigen Aufgaben Fan-out | ein Agent ändert, ein frischer Agent prüft; viele Dateien erst nach einem erfolgreichen kleinen Versuch bearbeiten ([Modul 8](./08-agenten-skalierung.md)) |
| **Maintainer** | `/loop` und Cloud-Routines für wiederkehrende Aufgaben | nur klar begrenzte Arbeiten automatisieren und einen Fehler- und Stoppweg vorbereiten ([Modul 8](./08-agenten-skalierung.md)) |
| **Conductor** | Agent Teams, Worktrees, Monitor-Tool | Aufgaben getrennt halten, Fortschritt beobachten und Ergebnisse zusammenführen ([Modul 8](./08-agenten-skalierung.md), Abschnitt 7) |

---

## 4. Selbst-Check — welche Rollen trägst du gerade?

Nimm dein aktuelles Projekt und beantworte drei Fragen in deinen eigenen Worten. Die englischen Rollennamen darfst du nachschlagen.

1. **Rückblick:** Welche zwei Tätigkeiten haben dich zuletzt am meisten beschäftigt? Welche Rollen passen dazu?
2. **Phase:** Probiert ihr noch eine Idee aus, wächst die Nutzung oder betreut ihr ein bestehendes Produkt? Welche Arbeit braucht gerade mehr Aufmerksamkeit?
3. **Lücke:** Was bleibt liegen? Wer entscheidet darüber, und welchen begrenzten Teil könnte ein Agent vorbereiten?

Das Ergebnis soll eine nächste Aufgabe klarer machen. Es ist keine Bewertung deiner Person.

---

## Q&A

**Muss ich mich auf eine Rolle festlegen?**  
Nein. Du kannst morgens einen Entwurf bauen und nachmittags ein bestehendes System betreuen. Ordne die Tätigkeit ein, nicht die Person.

**Ist der Sweeper nicht einfach Teil vom Builder?**  
Eine Person kann beides tun. Die getrennten Namen erinnern daran, neben neuen Funktionen auch Vereinfachung einzuplanen.

**Welche Rollen braucht ein neues Team oder Projekt zuerst?**  
Meist müssen Menschen zunächst Ideen ausprobieren, brauchbare Teile fertigstellen und unnötige Komplexität entfernen. Holt dabei früh Rückmeldungen ein. Schon genutzte Teile brauchen Betreuung, auch wenn das Projekt noch neu ist.

**Wie hängt das mit dem Autonomy-Slider aus Modul 10 zusammen?**  
Der Begriff beschreibt, wie viel ein Agent selbst entscheiden und ausführen darf. Eine erfundene Übung in einer Kopie erlaubt mehr als eine Änderung am laufenden Kundensystem. Entscheidend sind mögliche Folgen und überprüfbare Grenzen, nicht der Rollenname. → [Modul 10](./10-kontext-engineering.md), Abschnitt 1.

**Was ist mit Governance und Risiko — bremst das nicht alles aus?**  
Früh geklärte Zuständigkeiten und Datenregeln ersparen spätere Umwege. Der Risk Steward macht solche Fragen sichtbar. Wenn das Risiko zu groß ist, gehört auch ein begründetes Stopp zur Aufgabe.

**Wie nutze ich die Rollen in einer Build Session oder beim Arbeiten zu zweit?**

Teilt zunächst nur die nächste Tätigkeit auf: Eine Person arbeitet mit dem Agenten, die andere prüft die Änderungen und probiert das Ergebnis aus. Danach könnt ihr wechseln. Zusätzliche Rollennamen braucht ihr erst, wenn sie euch bei der Verteilung helfen.

**Können Agenten selbst Rollen besetzen?**  
Sie können Teile davon übernehmen: Informationen sammeln, Entwürfe erstellen oder Tests ausführen. Menschen entscheiden weiterhin über Ziele, Nutzung und Freigabe. Ein Agent kann sein Ergebnis prüfen, aber die Verantwortung nicht übernehmen.

---

## Quellen & Weiterlesen

Stand der Quellenliste: 2026-09-13.

- Vorwissen — Delegation-Gap & der agentische Loop: [`07-agenten-grundlagen.md`](./07-agenten-grundlagen.md)
- Autonomy-Slider: [`10-kontext-engineering.md`](./10-kontext-engineering.md) (Abschnitt 1) · Org-Level-Scaling: [`08-agenten-skalierung.md`](./08-agenten-skalierung.md) (Abschnitt 7)
- Begriffe nachschlagen: [`glossar.md`](./glossar.md)
- Boris Cherny (Claude-Code-Team): X/Twitter `@bcherny`, Thread ~Ende Juni 2026 — Original der fünf Kern-Archetypen. Das exakte Datum des Threads ist nicht belegt. URL: https://x.com/bcherny/status/2071379474277613732
- AI Daily Brief (Podcast): Episode „The Job Positions of the AI Future", veröffentlicht 2026-07-05, Erweiterung um die außen-zugewandten Rollen: https://podcasts.apple.com/us/podcast/the-job-positions-of-the-ai-future/id1680633614?i=1000775522675 *(abgerufen 2026-09-13)*
