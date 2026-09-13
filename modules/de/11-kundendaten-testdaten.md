# Modul 11 — Kundendaten & Testdaten (echte Daten raus, synthetische rein)

> Deutsche Fassung · Stand 2026-09-13 · Englischer Lernpfad: [START-HERE](../../START-HERE.md)
>
> Öffentliche Fassung eines intern gepflegten Moduls: gekürzt und für ein allgemeines Publikum überarbeitet; fortgeschrieben und gepflegt wird der interne Text (Stand 2026-09-13).

> Rechtsstand EU/Österreich, Stand 07/2026. Arbeitsgrundlage für Prototypen und PoCs, kein Rechtsrat. Im Zweifel fragst du beim Kunden bzw. dessen Datenschutzbeauftragten nach, nicht bei einem Agenten.

⏱ ~15 min · **Danach kannst du:** für einen Prototyp passende erfundene Testdaten vorbereiten, vor echter Datenarbeit die richtigen Fragen stellen und einen Verdachtsfall an die zuständige Stelle melden.

**Setzt voraus:** nichts Technisches. Das Modul ist rechtlich-organisatorisch und für alle Rollen lesbar.

## Worum es geht

Du willst ein kleines Tool ausprobieren. Dafür brauchst du zum Beispiel die Spalten „Artikel", „Anzahl" und „Preis" — aber keine echte Kundenliste. Beginne mit einer selbst geschriebenen Beschreibung dieser Struktur und erfinde ein paar passende Zeilen. So kannst du Funktionen testen, ohne die Daten echter Menschen weiterzugeben.

**Im ganzen Kurs verwenden wir erfundene Daten oder öffentliche Daten ohne Personenbezug.** Das gilt ab der ersten Toolnutzung, auch für deine eigenen persönlichen Daten. Für diesen Einstieg reichen Abschnitt 3 und die Fragen am Ende.

Die übrigen Abschnitte erklären, was außerhalb des Kurses vor genehmigter Arbeit mit echten Kundendaten geklärt werden muss. Ein AVV ist ein Auftragsverarbeitungsvertrag: Er regelt die Verarbeitung personenbezogener Daten im Auftrag. Ob er und weitere Voraussetzungen vorliegen, klärst du mit den zuständigen Menschen, bevor du eine echte Datei anforderst oder weitergibst.

---

## 1. Der Fall, der das Modul trägt — 1.000.000 EUR für eine Testumgebung

Am 11.12.2025 verhängte die französische Aufsichtsbehörde **CNIL** gegen den Marketing-Analytics-Dienstleister **Mobius Solutions** („Optimove") ein Bußgeld von **1.000.000 EUR** (Deliberation SAN-2025-014, [Légifrance](https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000053048614), Zusammenfassung auf [GDPRhub](https://gdprhub.eu/index.php?title=CNIL_%28France%29_-_SAN-2025-014), abgerufen 2026-09-13). Der Sachverhalt ist unspektakulär und genau deshalb lehrreich: Das Unternehmen kopierte nicht-anonymisierte Personendaten von Deezer-Nutzer:innen aus der Produktionsumgebung in seine eigene Nicht-Produktionsumgebung, ausdrücklich *„in order to develop and test possible improvements"*. Betroffen waren rund **46,9 Mio** Nutzer:innen. Sanktioniert wurde in erster Linie **Art. 29 DSGVO** (Verarbeitung außerhalb der Weisung des Verantwortlichen), dazu Art. 28 Abs. 3 lit. g und Art. 30.

Für das eigene Entwickeln und Testen fehlte die Weisung des Kunden. Ein nützliches Entwicklungsziel war dafür keine Erlaubnis.

> Kläre vor echter Datenarbeit Zweck, Rechtsgrundlage, Weisung und Schutzmaßnahmen. Die Zustimmung eines Kunden ersetzt diese Prüfung nicht; ein Anonymisierungsverfahren erlaubt dir nicht von selbst, seine Datei zu verarbeiten.

Drei vergleichbare Fälle, plus der Gegenfall, den Abschnitt 2 ausführt:

| Fall (Behörde, Datum) | Was passiert ist | Ausgang |
|---|---|---|
| **CNIL ./. Mobius Solutions** (FR, 11.12.2025) | Produktionsdaten von ~46,9 Mio Nutzer:innen in die eigene Nicht-Produktionsumgebung kopiert, um Verbesserungen zu entwickeln und zu testen | **1.000.000 EUR**, Kern: Art. 29 (außerhalb der Weisung). [GDPRhub](https://gdprhub.eu/index.php?title=CNIL_%28France%29_-_SAN-2025-014) |
| **UODO ./. Fortum + PIKA** (PL, 19.01.2022) | Bei Systemänderungen des Dienstleisters wurde mit echten Kundendaten gearbeitet; eine neu angelegte Datenbank mit 137.314 Kundendatensätzen wurde kopiert | **4.911.732 PLN (rund 1 Mio EUR)** gegen den Verantwortlichen, dazu rund 53.000 EUR gegen den Dienstleister. [UODO](https://www.uodo.gov.pl/decyzje/DKN.5130.2215.2020) · [GDPRhub](https://gdprhub.eu/index.php?title=UODO_%28Poland%29_-_DKN.5130.2215.2020) |
| **NAIH ./. Robinson-Tours** (HU, 09.12.2020) | Testdatenbank mit Daten von 781 echten Kund:innen, über eine Google-Suche ohne Zugangsprüfung erreichbar | **20.500.000 HUF (rund 55.000 EUR)**. [NAIH](https://www.naih.hu/files/NAIH-2020-0066-21-hatarozat.pdf) · [GDPRhub](https://gdprhub.eu/index.php?title=NAIH_%28Hungary%29_-_NAIH/2020/66/21) |
| **APD/GBA** (BE, Entscheidung 22/2020, 08.05.2020) | Auftragsverarbeiter kopierte eine Produktivdatenbank „for testing purposes" auf einen fehlkonfigurierten AWS-Server; 32.153 Betroffene, inklusive Nationalregisternummern und IBAN | **keine Sanktion**, warum, steht in Abschnitt 2. [APD/GBA](https://www.autoriteprotectiondonnees.be/publications/decision-quant-au-fond-n-22-2020.pdf) · [GDPRhub](https://gdprhub.eu/index.php?title=APD/GBA_%28Belgium%29_-_22/2020) |

Was die vier Fälle gemeinsam haben, ist der Auslöser: **Alle wurden durch einen Sicherheitsvorfall bekannt, keiner durch eine Aufsichtsprüfung.** Daraus folgt keine Rangliste von Schutzmaßnahmen. Abschnitt 5 erklärt, warum auch die Aufbewahrungsdauer wichtig ist.

## 2. Der Gegenfall — die drei Dinge zwischen 0 EUR und 1 Mio EUR

Im belgischen Fall (APD/GBA, Entscheidung 22/2020) lag eine Produktivdatenbank mit besonders heiklen Feldern offen im Netz; dennoch erging **keine Sanktion**. Die Entscheidung behandelt unter anderem diese drei Punkte. Fälle aus verschiedenen Ländern, Jahren und Vertragsverhältnissen sind nicht direkt vergleichbar; daraus lässt sich keine Garantie gegen ein Bußgeld ableiten:

1. **Der Vertrag untersagte die Praxis ausdrücklich**, im Wortlaut: *„confidential data may not be copied from a production environment to a non-production environment, unless the confidential data is masked"*. Die Regel stand vorher schwarz auf weiß da, der Vorfall war ihr Bruch, nicht ihr Fehlen.
2. **Dokumentierte Risikoanalysen plus jährliche externe Audits**: der Nachweis, dass systematisch hingeschaut wurde, nicht nur im Nachhinein behauptet.
3. **Ordnungsgemäße Breach-Meldung**: Der Vorfall wurde gemeldet, wie er gemeldet werden musste.

Bereite schriftliche Regeln, überprüfte Schutzmaßnahmen und einen bekannten Meldeweg vor. Sie helfen, Fehler zu verhindern und auf Vorfälle zu reagieren. Wie eine Behörde einen konkreten Fall bewertet, entscheidet dieser Kurs nicht.

## 3. Die vier Wege — welchen du wann nimmst

Hier sind vier häufige Wege. Für die Kursübungen nimmst du **Schema-only**: eine Beschreibung der Spalten und Datentypen, dazu vollständig erfundene Werte.

| Weg | Was dabei passiert | Danach noch personenbezogen? | Wann du ihn wählst |
|---|---|---|---|
| **Schema-only** | Die Struktur wird beschrieben, sämtliche Werte frei erfunden. Auch Spaltennamen und Beschreibungen werden auf persönliche Angaben geprüft. | Ohne Bezug zu echten Menschen enthält das Beispiel keine Personendaten. Ein echter Name in einer Überschrift würde das ändern. | Ausgangspunkt für die Übungen und viele Prototypen |
| **Anonymisierung** | Echte Daten werden so verändert, dass Menschen mit vernünftigerweise einsetzbaren Mitteln nicht mehr identifizierbar sind. | Nur bei wirksamer Anonymisierung entfällt der Personenbezug; das muss geprüft werden. | Außerhalb des Kurses, wenn echte Verteilungen fachlich nötig und Verarbeitung und Prüfung genehmigt sind |
| **Pseudonymisierung** | Identifizierende Angaben werden ersetzt; zusätzliche Informationen können eine Zuordnung erlauben. | Hier weiterhin als personenbezogen behandeln; zur rechtlichen Einordnung siehe Abschnitt 4. | Wenn eine spätere Zuordnung fachlich nötig und die Verarbeitung dafür zugelassen ist |
| **Statistisch synthetisch** | Ein Verfahren lernt Verteilungen echter Daten und erzeugt daraus neue Datensätze. | Nicht automatisch anonym; auch daraus können Informationen über Menschen ableitbar sein. | Wenn die Verteilungen nötig sind und Datenschutz sowie Verfahren eigens geprüft wurden |

Die drei Verfahren mit echten Ausgangsdaten benötigen bereits für deren Verarbeitung eine passende Grundlage. Pseudonymisierung kann Risiken verringern, ohne den Personenbezug zu beseitigen. **Vollständig erfundene Beispiele vermeiden diesen Verarbeitungsschritt.**

## 4. Die rechtlichen Anker — vier Dinge, die du wissen musst

**Pseudonymisierte Daten bleiben Personendaten.** **Behandle sie im Kurs und ohne fachliche Prüfung weiterhin so.** Rechtlich ist die Aussage „solange irgendwer einen Schlüssel hat, immer für jeden personenbezogen" zu pauschal. Der EuGH in **C-413/23 P (EDSB ./. SRB, 04.09.2025)** unterscheidet nach den Umständen und den vernünftigerweise verfügbaren Mitteln zur Identifizierung. Das Urteil zur Verordnung (EU) 2018/1725 erklärt auch: Für einen Empfänger können wirksam geschützte Daten anders einzuordnen sein als für den Verantwortlichen mit Zuordnungsinformationen. Das ist keine allgemeine Freigabe für Auftragsverarbeiter. [Urteil, Rn. 75–87 und 100](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0413) · ErwGr 26 DSGVO.

**Anonymisierung ist selbst eine Verarbeitung.** Die **EDSA Guidelines 02/2026 zur Anonymisierung** (Entwurf vom 07.07.2026, öffentliche Konsultation bis 30.10.2026, ersetzen WP216/2014) halten fest: Das Anonymisieren braucht seinerseits eine Rechtsgrundlage. Kläre deshalb den Auftrag vor der Verarbeitung. *(Stand 07/2026, Quelle: EDSA Guidelines 02/2026, Entwurfsfassung in Konsultation; der finale Text kann abweichen.)*

Der Entwurf nennt **synthetische Daten ausdrücklich als möglichen Risikofall** (Rn. 82): Zusätzliche Informationen können Rückschlüsse über einzelne Menschen erlauben. Das Wort „synthetisch" allein belegt daher keine Anonymität. [EDSA-Entwurf](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf)

**Die drei Risiken, an denen Anonymität gemessen wird** (EDSA, übernommen aus WP216/2014). Sie helfen, mögliche Identifizierung zu prüfen. Drei angekreuzte „Nein" ersetzen keine fachliche Bewertung der verfügbaren Mittel und des konkreten Datensatzes:

| Risiko | Die Frage, die es stellt | Woran es typischerweise scheitert |
|---|---|---|
| **Singling out** | Lässt sich eine einzelne Person im Datensatz isolieren? | Seltene Kombinationen: die einzige Zeile mit PLZ 9999 und Umsatz über 2 Mio |
| **Linkability** | Lassen sich zwei Datensätze über gemeinsame Merkmale verknüpfen? | Ein „anonymisierter" Datensatz plus ein öffentliches Register ergeben zusammen wieder eine Person |
| **Inference** | Lässt sich ein Attribut einer Person mit hoher Sicherheit ableiten? | Wenn alle Personen einer kleinen Gruppe dasselbe Merkmal tragen, verrät die Gruppenzugehörigkeit das Merkmal |

**Art. 28 DSGVO: der Auftragsverarbeitungsvertrag (AVV) steht vor der ersten Dateiübergabe.** Wenn du oder deine Organisation weisungsgebunden für Kund:innen Daten verarbeitet, seid ihr Auftragsverarbeiter. Nach **Art. 28 Abs. 10** gilt ein Auftragsverarbeiter, der entgegen der Verordnung selbst Zwecke und Mittel festlegt, für diese Verarbeitung als Verantwortlicher. [DSGVO, Art. 28](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

„Anonym" muss sich begründen lassen. Dokumentiere das Verfahren, das Prüfergebnis und seine Grenzen; eine Verfahrensbeschreibung allein belegt keine Anonymität. Diese Unterlagen können zum Rechenschaftsnachweis nach Art. 5 Abs. 2 DSGVO beitragen.

## 5. Verhältnismäßigkeit — was hier *nicht* passiert

Die folgenden Beobachtungen gehören zur damaligen Recherche. Sie sind keine Aussage darüber, welche Verarbeitung heute erlaubt ist:

- **Ein EU-Bußgeld gegen ein Unternehmen als *Anwender* eines LLM war bei der Recherche für dieses Modul nicht öffentlich dokumentiert** (Stand 07/2026, ohne öffentliche Quelle). Aus diesem begrenzten Rechercheergebnis lässt sich nicht ableiten, dass Anwender von den Regeln ausgenommen wären.
- **Der Samsung/ChatGPT-Vorfall 2023 betraf Geschäftsgeheimnisse, keine Personendaten.** Eine Verwechslungsfalle dazu: Die südkoreanische Datenschutzbehörde PIPC verhängte am 26.07.2023 gegen OpenAI ein Bußgeld von 3,6 Mio KRW (rund 2.800 USD), weil ein Sicherheitsvorfall mit Daten von 687 Nutzer:innen in Südkorea nicht fristgerecht gemeldet wurde. Mit dem Samsung-Vorfall hat das nichts zu tun. *(Quelle: Yonhap, 27.07.2023, https://en.yna.co.kr/view/AEN20230727003800315)*
- **Alle vier Fälle aus Abschnitt 1 wurden durch einen Sicherheitsvorfall ausgelöst, nicht durch eine Prüfung.**

Eine praktisch hilfreiche Maßnahme ist eine vereinbarte **Löschfrist**. Sie begrenzt, wie lange unnötige Originale aufbewahrt werden. Löschen macht eine bereits erfolgte Weitergabe oder Kopien in Backups und Git-Historie jedoch nicht rückgängig. Kläre deshalb auch diese Speicherorte und gesetzliche Aufbewahrungspflichten.

## 6. Drei Behauptungen, die nicht stimmen

| Behauptung | Was wirklich gilt |
|---|---|
| „Ein Live-System braucht ein Admin-UI, damit es DSGVO-konform ist." | Eine bestimmte Oberfläche ist nicht vorgeschrieben. Ein geprüfter manueller Ablauf, etwa ein SQL-Runbook, kann geeignet sein; Dokumentation allein genügt nicht. Art. 12 Abs. 3 verlangt grundsätzlich eine Antwort zu Anträgen binnen eines Monats und regelt begründete Verlängerungen. Rechte und Ausnahmen nach Art. 15/17/20 müssen tatsächlich berücksichtigt werden. |
| „Pseudonymisieren reicht, dann sind wir raus." | Das Ersetzen von Namen erlaubt keine neue Nutzung. Kläre Verarbeitung und Empfängerkreis; die genauere rechtliche Einordnung steht in Abschnitt 4. |
| „Es gibt ein AI-Act-Zertifikat, das man erwerben kann." | Nein, das gibt es nicht. Insbesondere verschafft **ISO 42001 keine Konformitätsvermutung**: CEN/CENELEC JTC 21 hatte bis dahin keine harmonisierte Norm veröffentlicht. *(Stand 07/2026; der Normungsstand ändert sich.)* |

## 7. Praxis — der Übergang von der echten Excel zur Struktur

**Dieser Abschnitt beschreibt genehmigte Arbeit außerhalb des Kurses.** Für die Übung schreibst du die Struktur selbst und verwendest keine echte Excel-Datei. Wenn in einem realen Projekt eine vorhandene Datei geprüft werden muss, klärt ihr zunächst Zweck, Weisung, Vertrag, Zuständigkeit und erlaubte Umgebung.

1. **Originale getrennt und zugriffsbeschränkt ablegen.** Ein Ordner außerhalb des Git-Repos verhindert versehentliches Committen aus diesem Repo. Er ist aber keine Zugriffssperre für Agenten. `.gitignore` verhindert ebenfalls weder Lesen noch ein erzwungenes Hinzufügen mit `git add -f`.
2. **Nur zuständige Menschen erhalten Zugriff.** Verwende die vereinbarte lokale oder betriebliche Umgebung. Cloud-Sync erzeugt weitere Kopien und darf nur Teil einer ausdrücklich geklärten Verarbeitung sein.
3. **Die Extraktion erfolgt mit einem geprüften lokalen Skript, nicht durch ein LLM.** Lass das Skript zunächst an einer erfundenen Datei entwickeln. Es darf keine Zellwerte in Logs, Fehlerausgaben oder die Ausgabe übernehmen. „Lokal gestarteter Agent" bedeutet nicht, dass sein Modell lokal verarbeitet.
4. **Ein Mensch prüft auch das Schema vor der Weitergabe.** Überschriften, Blattnamen und Beschreibungen können echte Namen oder andere vertrauliche Angaben enthalten. Nur eine bereinigte Struktur ohne solche Inhalte darf als Vorlage ins Repo. Alle Beispielwerte werden neu erfunden.

**Werkzeuge:** Das [Beispielskript zur Schema-Extraktion](../../exercises/find-the-personal-data/extract-schema.py) zeigt einen Ansatz. Für den zugehörigen **human-only** Übungsdatensatz bleiben auch Skriptausführung und Sichtung beim Menschen: keinen Agenten die CSV oder die Lösungen lesen oder auswerten lassen. Erklärungen mit einem getrennten, neu erfundenen Beispiel sind möglich.

Ein **Leak-Guard** ist ein zusätzlicher Vergleich: Taucht ein echter Ausgangswert versehentlich in der Ausgabe auf? Ein solcher Check kann Fehler finden, bescheinigt aber keine Anonymität. Er muss in derselben zugelassenen Umgebung bleiben wie die Originaldaten.

**Faker-Realität für Österreich.** Die Bibliothek Faker deckt mit dem Locale `fakerDE_AT` einiges ab: AT-Postleitzahlen, Bundesland, Ort, IBAN und Firmennamen. Sie deckt **nicht** ab: UID-Nummer, Sozialversicherungsnummer und Firmenbuchnummer. Die musst du selbst nach dem jeweiligen Formatmuster erzeugen. *(Stand 07/2026, Quelle: Faker-Locale-Daten `de_AT`; der Umfang ändert sich zwischen Versionen, deshalb die Faker-Version im Projekt pinnen.)*

Und eine Falle, die regelmäßig übersehen wird: **`faker.internet.email()` transliteriert Umlaute und verwendet echte Provider-Domains.** Aus „Jörg Müller" wird eine plausible Adresse bei einem realen Anbieter, die einer echten Person gehören kann. Setze immer explizit `provider: 'example.com'`. `example.com`, `example.net` und die Endung `.example` sind nach RFC 2606 für Beispiele reserviert. Verwende sie, damit Übungsadressen nicht versehentlich echte Postfächer adressieren.

## 8. Melden statt vermeiden

Wenn eine Datei am falschen Ort gelandet ist, hilft schnelles Melden. Kläre vorher, wen du erreichst und welche Angaben diese Person braucht. Kopiere die betroffene Datei nicht in weitere Chats oder Tickets.

**Eine Schulung allein reicht als Schutzmaßnahme nicht.** Eine Langzeitstudie mit mehr als 14.000 Beschäftigten über 15 Monate fand, dass die in der Industrie übliche eingebettete Schulung nach simulierten Phishing-Mails Beschäftigte **nicht** widerstandsfähiger machte und sie teils sogar anfälliger werden ließ. *(Quelle: Lain, Kostiainen, Čapkun, „Phishing in Organizations: Findings from a Large-Scale and Long-Term Study", IEEE S&P 2022, https://arxiv.org/abs/2112.07498, abgerufen 2026-09-13.)*

**Melden soll einfach sein und ernst genommen werden.** Das NCSC UK formuliert die dahinterliegende Regel unmissverständlich: *„metrics express an organisation's values, and if you appear to value the absence of reports of problems, you incentivise people to keep quiet about issues."* Und, ebenso knapp: *„Don't reprimand users."* *(Quelle: NCSC, „Phishing attacks: defending your organisation", https://www.ncsc.gov.uk/guidance/phishing, abgerufen 2026-09-13.)*

Bewertet Meldungen nicht allein nach ihrer Anzahl: Wenige Meldungen können auch bedeuten, dass Menschen den Meldeweg nicht kennen oder Ärger fürchten.

Vereinbart im Team, wer reagiert, wie schnell eine erste Rückmeldung kommt und wie ihr mit gutgläubigen Fehlalarmen umgeht. Die Empfehlung ist ein sachlicher, unterstützender Umgang. Dieser Kurs kann keine personalrechtlichen Folgen zusagen oder ausschließen.

Bei einem Verdacht: weitere Weitergabe stoppen, Zeitpunkt und betroffenen Speicherort notieren und den vorgesehenen Meldeweg nutzen. Die zuständige Stelle entscheidet über weitere Schritte und mögliche gesetzliche Meldepflichten.

## 9. Fünf Sätze für den Alltag

> 1. **Vor personenbezogenen Kundendaten kläre ich Auftrag, Vertrag und erlaubte Umgebung.**
> 2. **Ich lasse mir schriftlich bestätigen, dass der Kunde die Daten übermitteln darf.**
> 3. **Ich behaupte Anonymität erst nach Prüfung und dokumentiere Verfahren, Ergebnis und Grenzen.**
> 4. **Ich halte die vereinbarte Löschfrist ein und dokumentiere, was gelöscht wurde und was aufbewahrt werden muss.**
> 5. **Wenn besondere Kategorien drin sind (Gesundheit, Religion, Gewerkschaft, Herkunft, Politik, Sexualleben; Art. 9 DSGVO), frage ich zurück, BEVOR ich die Datei überhaupt öffne.**

---

## Q&A

**Der Kunde schickt mir die Excel einfach per Mail. Was mache ich?**
Lade sie nicht in einen Agenten und leite sie nicht weiter. Kläre mit der zuständigen Person, ob Empfang und Verarbeitung vorgesehen sind und welche Vereinbarungen fehlen. Bei Auftragsverarbeitung gehört dazu der AVV. Der Eingang einer Mail ist keine Genehmigung für Tests oder KI-Verarbeitung.

**Reicht es nicht, die Namen durch IDs zu ersetzen?**
Nein. Andere Felder oder eine Zuordnungstabelle können Menschen weiterhin erkennbar machen. Für die Übung nimmst du vollständig erfundene Beispiele. Die rechtliche Unterscheidung bei Pseudonymisierung steht in Abschnitt 4.

**Sind synthetische Daten automatisch anonym?**
Nein. Ein Verfahren, das aus echten Daten lernt, kann Informationen über Menschen weitergeben. Verwende im Kurs Werte, die du unabhängig von echten Datensätzen erfindest.

**Ich habe versehentlich eine Kundendatei in ein Repo gelegt. Was jetzt?**
Stoppe weitere Weitergabe und melde den Vorfall über den vorgesehenen Kanal. Teile mit, ob die Datei nur lokal lag oder bereits committed, gepusht oder kopiert wurde. Heimliches Löschen kann wichtige Informationen für die Klärung verlieren; eine Löschung im aktuellen Ordner entfernt auch nicht die Git-Historie.

**Wie viel Aufwand ist realistisch, bevor ich anfangen kann?**
Für eine Übung genügt eine kurze, erfundene Struktur mit wenigen Beispielzeilen. Teste damit zuerst eine Funktion. Ein echtes Datenprojekt benötigt zusätzlich die organisatorische und rechtliche Klärung aus diesem Modul.

**Brauchen wir für DSGVO-Auskünfte im Live-System ein Admin-UI?**
Nicht zwingend. Ihr braucht einen tatsächlich funktionierenden Ablauf für die jeweils geltenden Rechte und Fristen. Eine dokumentierte Befehlsfolge kann dabei helfen, muss aber geprüft, zugriffsbeschränkt und praktisch nutzbar sein. Siehe Abschnitt 6.

**Darf ich einen Agenten die Kundendatei lesen lassen, wenn er lokal läuft?**
Im Kurs nein. Für den beschriebenen Extraktionsweg außerhalb des Kurses wird ein lokales Skript in einer zugelassenen Umgebung verwendet. Ein auf deinem Rechner gestarteter Agent kann seine Eingaben trotzdem an ein externes Modell senden. Auch bei einem vollständig lokalen Modell bleiben Zweck, Weisung und Zugriff zu klären.

**Wir sind ein kleines Team und niemand prüft uns. Ist das nicht übertrieben?**
Auch kleine Teams können Dateien versehentlich weitergeben. Erfundene Testdaten, begrenzter Zugriff, vereinbarte Löschfristen und ein bekannter Meldeweg sind konkrete Schritte, mit denen ihr anfangen könnt.

---

## Quellen & Weiterlesen

Stand der Quellenliste: 2026-09-13.

- Begriffe nachschlagen: [`glossar.md`](./glossar.md)
- Kontext-Disziplin beim Arbeiten mit Agenten (warum Kontext-Inhalt eine Übermittlung sein kann): [`10-kontext-engineering.md`](./10-kontext-engineering.md)
- Rollen: wer im Team diese Fragen trägt (Risk Steward): [`09-rollen-archetypen.md`](./09-rollen-archetypen.md)
- Übung mit Beispielskript zur Schema-Extraktion: [`exercises/find-the-personal-data/extract-schema.py`](../../exercises/find-the-personal-data/extract-schema.py)
- CNIL, Deliberation SAN-2025-014 vom 11.12.2025 (Mobius Solutions / „Optimove"): Art. 29, Art. 28 Abs. 3 lit. g, Art. 30: https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000053048614 *(abgerufen 2026-09-13)*
- APD/GBA (BE), Entscheidung 22/2020 vom 08.05.2020, der Gegenfall ohne Sanktion: https://www.autoriteprotectiondonnees.be/publications/decision-quant-au-fond-n-22-2020.pdf *(abgerufen 2026-09-13)*
- UODO (PL), Entscheidung DKN.5130.2215.2020 vom 19.01.2022 (Fortum + PIKA): https://www.uodo.gov.pl/decyzje/DKN.5130.2215.2020 *(abgerufen 2026-09-13)*
- NAIH (HU), Entscheidung NAIH/2020/66/21 vom 09.12.2020 (Robinson-Tours): https://www.naih.hu/files/NAIH-2020-0066-21-hatarozat.pdf *(abgerufen 2026-09-13)*
- GDPRhub, englische Zusammenfassungen der vier Fälle: https://gdprhub.eu/index.php?title=CNIL_%28France%29_-_SAN-2025-014 · https://gdprhub.eu/index.php?title=UODO_%28Poland%29_-_DKN.5130.2215.2020 · https://gdprhub.eu/index.php?title=NAIH_%28Hungary%29_-_NAIH/2020/66/21 · https://gdprhub.eu/index.php?title=APD/GBA_%28Belgium%29_-_22/2020 *(abgerufen 2026-09-13)*
- EuGH, C-413/23 P (EDSB ./. SRB) vom 04.09.2025: relative Bestimmbarkeit bei Pseudonymisierung, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0413
- EDSA, Guidelines 02/2026 zur Anonymisierung: Entwurf vom 07.07.2026, Konsultation bis 30.10.2026, ersetzen WP216/2014, https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf
- DSGVO: ErwGr 26 · Art. 5 Abs. 2 · Art. 9 · Art. 12 Abs. 3 · Art. 15/17/20 · Art. 28 (insb. Abs. 3 lit. g und Abs. 10) · Art. 29 · Art. 30, https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- PIPC-Bußgeld gegen OpenAI (26.07.2023): Yonhap, 27.07.2023, https://en.yna.co.kr/view/AEN20230727003800315
- Lain, Kostiainen, Čapkun: „Phishing in Organizations: Findings from a Large-Scale and Long-Term Study", IEEE S&P 2022, https://arxiv.org/abs/2112.07498
- NCSC UK, „Phishing attacks: defending your organisation" (Melde-Metriken, „Don't reprimand users"): https://www.ncsc.gov.uk/guidance/phishing
- RFC 2606: reservierte Domains für Beispiele (`example.com` und verwandte), https://www.rfc-editor.org/rfc/rfc2606
