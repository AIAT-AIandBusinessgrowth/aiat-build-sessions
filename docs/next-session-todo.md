# Stand der interaktiven Übungsfassung

Stand 2026-09-13, abends. Maintainer-Notiz, kein Kursmaterial.

Die Übung unter `exercises/verification-lab/index.html` ist neu gebaut: fünf
Runden (8, 9, 12, 5, 15 Personen), Vorhersage vor der Antwort der KI, Punkte,
freies Probieren nach Runde 5, Kopiersatz für Claude Code oder Codex, eigene
Reparaturdatei `notebook-calculator.html`, Szene als SVG mit CSS-Animation,
Design nach ai-at.eu (Geist selbst gehostet, ohne CDN). Der Prototyp
`docs/prototypes/verification-lab-v2.html` ist damit überholt; er bleibt nur
als Referenz für die Runden-Idee liegen.

## Die Leitplanken, an denen sich alles messen lassen muss

1. **Intuitiv.** Ohne Erklärtext verständlich.
2. **Verständlich.** Eine Blickachse von oben nach unten, Zahlen mit Einheit.
3. **Nur visuelle Unterstützung.** Die Person arbeitet mit Claude Code oder
   Codex; die Seite liefert den Satz, mit dem sie den Fehler zurückgibt.
4. **Kursartig.** Die Übung steht in einem Lernpfad (`START-HERE.md`), nicht
   daneben.

## Erledigt am 2026-09-13

- [x] 1. Kopiersatz mit Kopierknopf und Anleitung zum Einfügen in den Agenten.
- [x] 2. Keine Abhängigkeiten: Szene in SVG, Schrift als eigene Dateien unter
      `assets/fonts/` (SIL OFL 1.1, Lizenz liegt daneben).
- [x] 3. Englische Fassung über `?lang=en`, auch in der Reparaturdatei.
- [x] 4. Deployment: Allowlist im Infra-Repo ohne das Slide-Deck, Fonts und
      Reparaturdatei aufgenommen; Live-Stand steht in `/version.json`.
- [x] 5. Einheit „Choose test values" in Track 05, Schritt in den Pfaden B, C, D.
- [x] 6. Fünf Vorbedingungen in `START-HERE.md` abgefangen.
- [x] 7. Stufe 1 und 2 der Übungsentwürfe als „Harder tasks" in der README der
      Übung; die drei leichteren Einstiegsaufgaben sind noch nicht übernommen.
- [x] 8. Freies Probieren nach den fünf Runden.

## Offen

- [ ] Drei leichtere Einstiegsaufgaben (Sortierung, Filter, Eingabeprüfung)
      als eigene Seite, am ehesten zuerst auf Deutsch.
- [ ] `modules/de/glossar.md`: Einträge „Grenzwert" und „Testwerte" nachziehen.
- [ ] `learning/tutor-criteria.md` B05: Transfervariante wählen, die nicht
      schon in der Einheit steht.
- [ ] `scripts/check_content.py` prüft keine Links in HTML-Dateien; als
      Erweiterung erfassen.
- [ ] Stufe 3 und 4 der Übungsentwürfe (Zustandsfehler, Prüfbericht).

## Prüfliste vor dem Abnehmen

Jede Fassung muss das bestanden haben, bevor sie gezeigt wird. Für die Fassung
vom 2026-09-13 wurde jeder Punkt im Browser gemessen und die Screenshots wurden
angesehen; die Vertragstests in `tests/test_verification_lab.py` sichern die
Importer-Bedingungen (Rechenfehler bleibt, keine externen Ressourcen).

- [x] Kompletter Durchlauf ausschließlich mit der Tastatur, inklusive Neustart.
- [x] Leere und ungültige Eingabe erzeugen eine sichtbare Meldung, keinen
      stillen Abbruch und kein veraltetes Ergebnis.
- [x] Kein horizontaler Überlauf bei 390, 768 und 1440 Pixeln Breite.
- [x] Null Kontrastverstöße gegen WCAG AA bei allen drei Breiten.
- [x] Singular und Plural stimmen in jedem erzeugten Satz.
- [x] Bei jeder vorkommenden Personenzahl bleibt die Reihe zählbar und
      vollständig im Bild, auch auf dem Handy.
- [x] Screenshots jedes Zustands wurden angesehen, nicht nur Messwerte
      geprüft.
