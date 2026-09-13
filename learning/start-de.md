# Mit einem kleinen Lernschritt starten

Du brauchst für den Einstieg keinen Account, kein Terminal und kein GitHub-Wissen. Papier oder eine lokale Textdatei reicht. Plane ungefähr 20 Minuten ein; das ist eine Schätzung für die Übung in [learning/README.md](README.md). Wenn du lieber etwas anklickst, wähle stattdessen das [Verification Lab](../exercises/verification-lab/README.md): eine kleine Browser-App mit einem absichtlichen Fehler, auch auf Papier nutzbar.

Das Kernmaterial ist auf Englisch. Dieser Einstieg ist auf Deutsch. Du kannst Codex oder Claude Code bitten, die verlinkten Einheiten auf Deutsch zu erklären. Unter [modules/de/](../modules/de/) liegen weitere deutsche Texte zu Agenten und Daten; sie bilden keinen vollständigen übersetzten Kurs.

## Heute: erst vorhersagen, dann prüfen

Ein erfundenes Raum-Tool soll nur Räume anzeigen, in die die angefragte Gruppe passt. Anfragen müssen positive ganze Zahlen sein. Bei einer leeren oder ungültigen Eingabe soll eine verständliche Meldung erscheinen.

| Erfundenes Zimmer | Plätze |
|---|---|
| Cedar | 4 |
| Maple | 8 |
| Pine | 12 |

1. Schreibe in einem Satz auf, was das Tool tun soll.
2. Notiere zuerst, was du bei einer Anfrage für acht Plätze erwartest. Prüfe dann deine Vorhersage anhand der Tabelle.
3. Wähle eine andere Eingabe, die einen Fehler sichtbar machen könnte. Schreibe das erwartete Ergebnis und den Grund auf.
4. Erkläre mit abgedeckten Notizen, wie du erkennen würdest, ob das Tool funktioniert. Eine Aussage des Agenten allein ist noch kein Beleg.

Damit übst du die [Verification ladder](../tracks/05-verify-and-loop/01-verification-ladder.md): eine Behauptung in eine überprüfbare Beobachtung übersetzen.

## Mit Codex oder Claude Code lernen

Öffne den Kursordner im Agenten und schreibe beispielsweise:

```text
Begleite mich auf Deutsch nach learning/coach-protocol.md.
Ich habe 20 Minuten und arbeite heute nur auf Papier.
Stelle mir genau eine passende Frage und warte auf meinen Versuch.
Gib mir bei Bedarf zuerst einen Hinweis, nicht gleich die Lösung.
```

Hast du schon ein Tool gebaut, kannst du genauer werden:

```text
Prüfe mein Wissen zur Überprüfung von Agentenergebnissen.
Nutze Checkpoint I02 aus learning/checkpoints.md.
Stelle nur die Frage und warte auf meine Antwort.
```

Die [Checkpoints](checkpoints.md) haben Aufgaben für Beginner, Fortgeschrittene und Expert:innen. Die Stufe bezieht sich auf die jeweilige Fähigkeit. Browser und Terminal sind keine Leistungsstufen.

Ohne Coding Agent kannst du die Übung allein oder mit einer zweiten Person machen. Für einen Browser-Chat kopierst du das [Coach-Protokoll](coach-protocol.md) und die betreffende Einheit als Text hinein. Ein Link allein liefert dem Chat möglicherweise nicht den Inhalt.

## Was du selbst übernimmst

Du entscheidest, welches Problem wichtig ist, sagst ein Ergebnis voraus und prüfst, ob es eintritt. Der Agent kann erklären, erfundene Daten erzeugen und Code schreiben. Ein fertiger Code beweist noch nicht, dass du die Fähigkeit selbst anwenden kannst. Eine neue kleine Aufgabe zeigt dir, was schon klappt.

Du darfst pausieren oder überspringen. Dafür gibt es einen eigenen Status, ohne die übersprungene Aufgabe als gelernt zu markieren. Wenn du später weitermachen möchtest, kopiere die [Fortschrittsvorlage](progress-template.md) nach `learning/local/progress.md` oder in eine private Notiz. Der Agent fragt beim Wiedereinstieg kurz nach, statt frühere Aussagen ungeprüft zu übernehmen.

## Kurs und eigenes Projekt trennen

Der Kursordner enthält das Lernmaterial. Deine App kommt in einen separaten Ordner oder ein eigenes Builder-Projekt. Regeln dafür findest du in der [AGENTS.md-Vorlage](../templates/project-AGENTS.md). Lokale Lernnotizen unter `learning/local/` werden von Git ignoriert; sie gehören nicht in einen öffentlichen Pull Request.

Verwende erfundene Daten. Keine Kundendateien, Zugangsdaten oder echten Namen in Aufgaben, Prompts oder Lernnotizen. Die [Datenschutz-Suchübung](../exercises/find-the-personal-data/README.md) löst du selbst ohne AI. Gib ihre CSV nicht an den Agenten; nach deinem eigenen Versuch vergleichst du mit den bereitgestellten Lösungen.

Als Nächstes: [erste App bauen](../tracks/01-first-build/01-your-first-build.md), [vorhandenes Ergebnis prüfen](../tracks/05-verify-and-loop/01-verification-ladder.md) oder [einen Lernpfad wählen](../START-HERE.md).
