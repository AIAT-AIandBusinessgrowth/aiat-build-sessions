# Nächste Session: interaktive Übungsfassung fertigstellen

Stand 2026-09-13. Arbeitsgrundlage für die Folgesession. Ziel ist eine
vorführbare Fassung der Verifikationsübung, die neben einem Coding-Agenten
läuft und nicht an seine Stelle tritt.

Der Arbeitsstand liegt in `docs/prototypes/verification-lab-v2.html` und ist
lauffähig (Datei im Browser öffnen). Er ist ein Prototyp, kein Kursmaterial:
er lädt three.js und die Schrift von einem CDN, siehe TODO 2.

## Die Leitplanken, an denen sich alles messen lassen muss

1. **Intuitiv.** Ohne Erklärtext verständlich. Wenn eine Seite den Satz
   „Sieh dir das Bild an" braucht, erklärt das Bild sich nicht selbst.
2. **Verständlich.** Eine Blickachse von oben nach unten, keine gestapelten
   Karten, keine Chips, die nichts erklären. Zahlen immer mit Einheit.
3. **Nur visuelle Unterstützung.** Die Person arbeitet mit Claude Code oder
   Codex. Die Seite zeigt, was der Agent gebaut hat, und liefert den Satz,
   mit dem die Person den Fehler an den Agenten zurückgibt. Sie ersetzt den
   Agenten nicht und ist kein eigenständiges Spiel.
4. **Kursartig.** Die Übung steht in einem Lernpfad, nicht daneben. Sie hat
   Vorbedingung, Zeitangabe, Ziel und ein „Done when" wie jede andere Einheit.

## Die drei Mechaniken, die sich bewährt haben

- **Die Vorhersage wird erzwungen, nicht empfohlen.** Die eigene Zahl steht
  fest, bevor die Antwort der KI sichtbar wird. Der Kurs bittet an vielen
  Stellen darum; hier geht es technisch nicht anders.
- **Der Beweis ist zählbar, nicht erklärt.** Man sieht die Packung mit ihren
  vier Büchern, man sieht die Leute in einer Reihe, man sieht, wer nichts
  bekommt. Zahlen im Text bestätigen nur, was im Bild schon steht.
- **Gegenbeispiele sind Pflicht.** In drei von fünf Runden liegt die KI
  richtig. Sonst lernt die Person „KI rechnet falsch" statt „ein Treffer
  beweist nichts".

## TODO vor der Vorführung

- [ ] **1. Agenten-Anbindung sichtbar machen.** Der fertige Beschreibungssatz
      („Bei 9 Personen brauche ich 3 Packungen. Du hast 2 gekauft, damit fehlt
      eines.") braucht einen Kopierknopf und eine Zeile, die sagt, was damit
      zu tun ist: in Claude Code oder Codex einfügen, die Datei ändern lassen,
      danach dasselbe Beispiel und ein vorher richtiges erneut prüfen. Ohne
      diesen Schritt ist die Seite ein Spiel statt einer Kursübung.
- [ ] **2. Abhängigkeiten klären.** Die deployte Seite läuft unter
      `default-src 'self'`; CDN-Nachladen ist damit verboten. three.js
      minifiziert sind 687 KB, die Schrift 60 KB je Schnitt, die Übung selbst
      23 KB. Entweder beides ins Repo legen oder die Szene in SVG mit
      CSS-Übergängen neu bauen (geschätzt 5 KB, ohne WebGL, druckbar, für
      Screenreader beschriftbar). Empfehlung: SVG. Entscheidung liegt beim
      Maintainer.
- [ ] **3. Englische Fassung.** Der Prototyp ist einsprachig deutsch, die
      bestehende Übung kann beide Sprachen. Ohne EN fällt die Übung hinter
      den heutigen Stand zurück. Muster: `?lang=en` wie in
      `exercises/verification-lab/index.html`.
- [ ] **4. Deployment anstoßen.** `build-sessions.apps.aiat-poc.at` lieferte
      am 2026-09-13 noch den Stand vor Commit `6b1076a` aus (10.257 gegen
      11.363 Bytes). Vor der Vorführung prüfen, ob die Live-Seite den
      Repo-Stand zeigt.

## TODO danach

- [ ] **5. Die eigentliche Lücke des Kurses schließen.** Die
      Verifikationsleiter nennt als ungewöhnliche Eingaben ein leeres Feld,
      eine sehr große Zahl und Sonderzeichen
      (`tracks/05-verify-and-loop/01-verification-ladder.md:27`). Keine davon
      findet den Fehler der eigenen Einstiegsübung, der nur bei 1, 5, 9 und 13
      auftritt. Grenzwerte kommen in Track 05 nur einmal als Symptom vor, nie
      als Methode. Eine Einheit „Prüfwerte wählen" schließt das.
- [ ] **6. Vorbedingungen reparieren.** Fünf Schritte in den Lernpfaden
      verlangen eine Lektion, die im selben Pfad nie vorkommt und in keinem
      Auffangsatz genannt wird. Die gewichtigste: Path D Schritt 16
      (`tracks/08-advanced/05-always-on-assistants-guardrails.md`) setzt
      `diy/07-secrets-and-keys.md` voraus. Vollständige Liste in Projekt 41,
      Issue #50.
- [ ] **7. Übungsentwürfe einarbeiten.** Drei leichtere Einstiegsaufgaben und
      vier Aufbaustufen liegen ausformuliert und nachgerechnet vor, jede mit
      eigener Fehlerklasse. Stufe 1 und 2 passen in den vorhandenen, derzeit
      zugeklappten Block „Want a harder task?" in
      `exercises/verification-lab/README.md`.
- [ ] **8. Freies Probieren anbieten.** Nach den fünf Runden ein Feld für
      beliebige Zahlen. Wer 1, 5, 9, 13 durchspielt, findet das Muster selbst.
      Das ist stärker als jede Auflösung.

## Prüfliste vor dem Abnehmen

Jede Fassung muss das bestanden haben, bevor sie gezeigt wird. Jeder Punkt
davon ist heute mindestens einmal gerissen worden.

- [ ] Kompletter Durchlauf ausschließlich mit der Tastatur, inklusive Neustart.
- [ ] Leere und ungültige Eingabe erzeugen eine sichtbare Meldung, keinen
      stillen Abbruch und kein veraltetes Ergebnis.
- [ ] Kein horizontaler Überlauf bei 390, 768 und 1440 Pixeln Breite.
- [ ] Null Kontrastverstöße gegen WCAG AA bei allen drei Breiten.
- [ ] Singular und Plural stimmen in jedem erzeugten Satz („Ein Notizbuch
      fehlt", nicht „Es fehlen 1 Notizbücher").
- [ ] Bei jeder vorkommenden Personenzahl bleibt die Reihe zählbar und
      vollständig im Bild, auch auf dem Handy.
- [ ] Screenshots jedes Zustands wurden angesehen, nicht nur Messwerte
      geprüft. Zahlen sagen nichts über Verständlichkeit.
