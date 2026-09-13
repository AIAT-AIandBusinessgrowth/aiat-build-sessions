# Modul 11 — Kundendaten & Testdaten (echte Daten raus, synthetische rein)

> Deutsche Fassung · Stand 2026-09-13 · Englischer Lernpfad: [START-HERE](../../START-HERE.md)

> Rechtsstand EU/Österreich, Stand 07/2026. Arbeitsgrundlage für Prototypen und PoCs, kein Rechtsrat. Im Zweifel fragst du beim Kunden bzw. dessen Datenschutzbeauftragten nach, nicht bei einem Agenten.

⏱ ~15 min · **Danach kannst du:** für eine Kundendatei einen der vier Wege begründet wählen, die Weisungs- und AVV-Frage stellen, *bevor* die Datei auf deinem Rechner liegt, und einen Verdachtsfall melden, ohne dir damit Ärger einzuhandeln.

**Setzt voraus:** nichts Technisches. Das Modul ist rechtlich-organisatorisch und für alle Rollen lesbar.

## Worum es geht

Viele Projekte beginnen mit derselben Szene: Ein Kunde schickt eine Excel-Datei, und darin stehen echte Namen, echte Adressen, echte Umsätze. Dieses Modul beantwortet zwei Fragen: **Wie kommst du von dieser Datei zu Testdaten, mit denen du gefahrlos arbeiten kannst**, und **was muss geklärt sein, bevor die Datei überhaupt auf deinem Rechner liegt**. Es ist bewusst kurz: Der teure Fehler in diesem Feld ist fast nie ein zu schwaches Anonymisierungsverfahren, sondern eine fehlende Genehmigung.

---

## 1. Der Fall, der das Modul trägt — 1.000.000 EUR für eine Testumgebung

Am 11.12.2025 verhängte die französische Aufsichtsbehörde **CNIL** gegen den Marketing-Analytics-Dienstleister **Mobius Solutions** („Optimove") ein Bußgeld von **1.000.000 EUR** (Deliberation SAN-2025-014, [Légifrance](https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000053048614), Zusammenfassung auf [GDPRhub](https://gdprhub.eu/index.php?title=CNIL_%28France%29_-_SAN-2025-014), abgerufen 2026-09-13). Der Sachverhalt ist unspektakulär und genau deshalb lehrreich: Das Unternehmen kopierte nicht-anonymisierte Personendaten von Deezer-Nutzer:innen aus der Produktionsumgebung in seine eigene Nicht-Produktionsumgebung, ausdrücklich *„in order to develop and test possible improvements"*. Betroffen waren rund **46,9 Mio** Nutzer:innen. Sanktioniert wurde in erster Linie **Art. 29 DSGVO** (Verarbeitung außerhalb der Weisung des Verantwortlichen), dazu Art. 28 Abs. 3 lit. g und Art. 30.

Kein Hack, keine Erpressung, keine böse Absicht. Ein Dienstleister wollte sein eigenes Produkt verbessern und hatte dafür keine Weisung.

> **Merksatz:** Der Hebel war nicht „Echtdaten sind verboten", sondern „es gab keine Weisung des Kunden dafür". **Kunden-Genehmigung schlägt Anonymisierungstechnik.**

Drei vergleichbare Fälle, plus der Gegenfall, den Abschnitt 2 ausführt:

| Fall (Behörde, Datum) | Was passiert ist | Ausgang |
|---|---|---|
| **CNIL ./. Mobius Solutions** (FR, 11.12.2025) | Produktionsdaten von ~46,9 Mio Nutzer:innen in die eigene Nicht-Produktionsumgebung kopiert, um Verbesserungen zu entwickeln und zu testen | **1.000.000 EUR**, Kern: Art. 29 (außerhalb der Weisung). [GDPRhub](https://gdprhub.eu/index.php?title=CNIL_%28France%29_-_SAN-2025-014) |
| **UODO ./. Fortum + PIKA** (PL, 19.01.2022) | Bei Systemänderungen des Dienstleisters wurde mit echten Kundendaten gearbeitet; eine neu angelegte Datenbank mit 137.314 Kundendatensätzen wurde kopiert | **4.911.732 PLN (rund 1 Mio EUR)** gegen den Verantwortlichen, dazu rund 53.000 EUR gegen den Dienstleister. [UODO](https://www.uodo.gov.pl/decyzje/DKN.5130.2215.2020) · [GDPRhub](https://gdprhub.eu/index.php?title=UODO_%28Poland%29_-_DKN.5130.2215.2020) |
| **NAIH ./. Robinson-Tours** (HU, 09.12.2020) | Testdatenbank mit Daten von 781 echten Kund:innen, über eine Google-Suche ohne Zugangsprüfung erreichbar | **20.500.000 HUF (rund 55.000 EUR)**. [NAIH](https://www.naih.hu/files/NAIH-2020-0066-21-hatarozat.pdf) · [GDPRhub](https://gdprhub.eu/index.php?title=NAIH_%28Hungary%29_-_NAIH/2020/66/21) |
| **APD/GBA** (BE, Entscheidung 22/2020, 08.05.2020) | Auftragsverarbeiter kopierte eine Produktivdatenbank „for testing purposes" auf einen fehlkonfigurierten AWS-Server; 32.153 Betroffene, inklusive Nationalregisternummern und IBAN | **keine Sanktion**, warum, steht in Abschnitt 2. [APD/GBA](https://www.autoriteprotectiondonnees.be/publications/decision-quant-au-fond-n-22-2020.pdf) · [GDPRhub](https://gdprhub.eu/index.php?title=APD/GBA_%28Belgium%29_-_22/2020) |

Was die vier Fälle gemeinsam haben, ist der Auslöser: **Alle wurden durch einen Sicherheitsvorfall bekannt, keiner durch eine Aufsichtsprüfung.** Diese Beobachtung trägt später die wichtigste einzelne Schutzmaßnahme (Abschnitt 5).

## 2. Der Gegenfall — die drei Dinge zwischen 0 EUR und 1 Mio EUR

Der belgische Fall (APD/GBA, Entscheidung 22/2020) ist der aufschlussreichste des ganzen Sets, weil der Sachverhalt dem CNIL-Fall fast bis ins Detail gleicht und trotzdem **keine Sanktion** erging. Eine Produktivdatenbank mit besonders heiklen Feldern lag offen im Netz. Drei Dinge trugen die Entscheidung:

1. **Der Vertrag untersagte die Praxis ausdrücklich**, im Wortlaut: *„confidential data may not be copied from a production environment to a non-production environment, unless the confidential data is masked"*. Die Regel stand vorher schwarz auf weiß da, der Vorfall war ihr Bruch, nicht ihr Fehlen.
2. **Dokumentierte Risikoanalysen plus jährliche externe Audits**: der Nachweis, dass systematisch hingeschaut wurde, nicht nur im Nachhinein behauptet.
3. **Ordnungsgemäße Breach-Meldung**: Der Vorfall wurde gemeldet, wie er gemeldet werden musste.

> **Merksatz für Nicht-Devs:** Zwischen 0 EUR und 1 Mio EUR steht nicht die Frage, ob etwas schiefgeht, sondern ob vorher eine schriftliche Regel existierte, ob jemand nachweisbar hingeschaut hat, und ob nach dem Vorfall gemeldet wurde. Alle drei kann man vorbereiten. Den Vorfall selbst nicht.

## 3. Die vier Wege — welchen du wann nimmst

Es gibt genau vier Umgangsweisen mit einer Kundendatei. Sie unterscheiden sich weniger im Aufwand als in der Frage, was danach rechtlich noch übrig ist.

| Weg | Was dabei passiert | Danach noch personenbezogen? | Wann du ihn wählst |
|---|---|---|---|
| **Schema-only** | Nur Spaltennamen und Datentypen werden übernommen, sämtliche Werte frei erfunden | Nein, es gab nie einen Personenbezug, weil kein einziger echter Wert mitkommt | **Default** für die meisten Prototypen; der Weg mit dem geringsten Aufwand |
| **Anonymisierung** | Echte Werte werden unumkehrbar entfremdet | Nein, sofern der Risikotest hält (drei Risiken, Abschnitt 4) | Wenn du echte Verteilungen brauchst, etwa für Performance- oder Auswertungs-Tests. Deutlich aufwendiger |
| **Pseudonymisierung** | Werte werden ersetzt, aber eine Mapping-Tabelle erlaubt die Rückführung | **Ja, bleibt personenbezogen**, solange irgendwer den Schlüssel hat | Im PoC fast nie. Sinnvoll erst, wenn eine Rückführung fachlich zwingend ist |
| **Statistisch synthetisch** | Ein Verfahren lernt die Verteilungen der echten Daten und zieht daraus neue Datensätze | Nicht automatisch anonym, das muss eigens geprüft werden | Wenn ein Modell trainiert wird und die Verteilung selbst das Produkt ist |

Der Grund, warum Schema-only der Default ist: Bei den anderen drei Wegen musst du **beweisen**, dass am Ende kein Personenbezug mehr besteht. Bei Schema-only entsteht die Frage gar nicht, es war nie einer da.

> **Merksatz:** Der billigste Weg ist auch der rechtlich sauberste. Nimm Schema-only, bis dich jemand mit einem konkreten fachlichen Grund davon abbringt.

## 4. Die rechtlichen Anker — vier Dinge, die du wissen musst

**Pseudonymisierte Daten bleiben Personendaten.** Das ist der Punkt, an dem die meisten Missverständnisse hängen. ErwGr 26 DSGVO und der EuGH in **C-413/23 P (EDSB ./. SRB, 04.09.2025)** stellen klar: Bestimmbarkeit ist **relativ**, es kommt darauf an, wer über welche Mittel verfügt. Solange irgendwer den Schlüssel hat, sind die Daten personenbezogen. Besonders wichtig, wenn du im Auftrag arbeitest: **Ein Auftragsverarbeiter kann sich nicht darauf berufen, die Daten seien „für ihn anonym"**, wenn der Auftraggeber zurückführen kann.

**Anonymisierung ist selbst eine Verarbeitung.** Die **EDSA Guidelines 02/2026 zur Anonymisierung** (Entwurf vom 07.07.2026, öffentliche Konsultation bis 30.10.2026, ersetzen WP216/2014) halten fest: Das Anonymisieren braucht seinerseits eine Rechtsgrundlage. Wer eine Kundendatei anonymisiert, ohne dafür beauftragt zu sein, hat nicht das Problem gelöst, sondern eines geschaffen. *(Stand 07/2026, Quelle: EDSA Guidelines 02/2026, Entwurfsfassung in Konsultation; der finale Text kann abweichen.)*

Bemerkenswert am selben Entwurf: **Synthetische Daten kommen darin genau einmal substanziell vor, und zwar als Risikofall** (Rn. 82, Inference-Kriterium). Es gibt **keine** EDSA-Aussage, dass synthetische Daten als anonym gelten. Wer das behauptet, zitiert etwas, das nicht existiert.

**Die drei Risiken, an denen Anonymität gemessen wird** (EDSA, übernommen aus WP216/2014). Erst wenn alle drei verneint sind, ist ein Datensatz anonym:

| Risiko | Die Frage, die es stellt | Woran es typischerweise scheitert |
|---|---|---|
| **Singling out** | Lässt sich eine einzelne Person im Datensatz isolieren? | Seltene Kombinationen: die einzige Zeile mit PLZ 9999 und Umsatz über 2 Mio |
| **Linkability** | Lassen sich zwei Datensätze über gemeinsame Merkmale verknüpfen? | Ein „anonymisierter" Datensatz plus ein öffentliches Register ergeben zusammen wieder eine Person |
| **Inference** | Lässt sich ein Attribut einer Person mit hoher Sicherheit ableiten? | Wenn alle Personen einer kleinen Gruppe dasselbe Merkmal tragen, verrät die Gruppenzugehörigkeit das Merkmal |

**Art. 28 DSGVO: der Auftragsverarbeitungsvertrag (AVV) steht vor der ersten Dateiübergabe.** Wenn du oder deine Organisation weisungsgebunden für Kund:innen Daten verarbeitet, seid ihr Auftragsverarbeiter. Und **Art. 28 Abs. 10** ist die Klausel, die den CNIL-Fall erklärt: Wer über die Weisung hinausgeht, etwa Kundendaten für eigene Zwecke nutzt, **wird selbst Verantwortlicher** und haftet voll.

> **Merksatz für Nicht-Devs:** „Anonym" ist kein Zustand, den man einer Datei ansieht, sondern ein Prüfergebnis. Deshalb sicherst du Kund:innen nie zu, dass Daten anonym *sind*. Du dokumentierst das **Verfahren**, mit dem du sie behandelt hast. Diese Dokumentation ist zugleich der Rechenschaftsnachweis nach Art. 5 Abs. 2 DSGVO.

## 5. Verhältnismäßigkeit — was hier *nicht* passiert

Dieses Modul soll keine Angst erzeugen, sondern Handlungsfähigkeit. Drei Beobachtungen, die das Risiko einordnen:

- **Ein EU-Bußgeld gegen ein Unternehmen als *Anwender* eines LLM war bei der Recherche für dieses Modul nicht öffentlich dokumentiert** (Stand 07/2026, ohne öffentliche Quelle). Das bekannte KI-Enforcement richtet sich gegen **Anbieter** von Systemen, nicht gegen Teams, die sie benutzen.
- **Der Samsung/ChatGPT-Vorfall 2023 betraf Geschäftsgeheimnisse, keine Personendaten.** Eine Verwechslungsfalle dazu: Die südkoreanische Datenschutzbehörde PIPC verhängte am 26.07.2023 gegen OpenAI ein Bußgeld von 3,6 Mio KRW (rund 2.800 USD), weil ein Sicherheitsvorfall mit Daten von 687 Nutzer:innen in Südkorea nicht fristgerecht gemeldet wurde. Mit dem Samsung-Vorfall hat das nichts zu tun. *(Quelle: Yonhap, 27.07.2023, https://en.yna.co.kr/view/AEN20230727003800315)*
- **Alle vier Fälle aus Abschnitt 1 wurden durch einen Sicherheitsvorfall ausgelöst, nicht durch eine Prüfung.**

Aus dem letzten Punkt folgt die praktisch wirksamste Einzelmaßnahme: **die Löschfrist**. Sie begrenzt das Zeitfenster, in dem ein Leak überhaupt noch Echtdaten treffen kann. Eine Original-Datei, die nach Projektabschluss gelöscht ist, kann in keinem Vorfall mehr auftauchen, unabhängig davon, wie gut das Anonymisierungsverfahren war.

## 6. Drei Behauptungen, die nicht stimmen

| Behauptung | Was wirklich gilt |
|---|---|
| „Ein Live-System braucht ein Admin-UI, damit es DSGVO-konform ist." | Falsch. Art. 15 (Auskunft), Art. 17 (Löschung) und Art. 20 (Datenübertragbarkeit) verlangen **Erfüllung binnen eines Monats** (Art. 12 Abs. 3 DSGVO), nicht eine Oberfläche. Ein dokumentiertes SQL-Runbook genügt vollständig; ein UI ist Komfort, kein Compliance-Baustein. |
| „Pseudonymisieren reicht, dann sind wir raus." | Falsch. Pseudonymisierte Daten bleiben personenbezogen, solange irgendwer den Schlüssel hat, siehe ErwGr 26 und EuGH C-413/23 P in Abschnitt 4. |
| „Es gibt ein AI-Act-Zertifikat, das man erwerben kann." | Nein, das gibt es nicht. Insbesondere verschafft **ISO 42001 keine Konformitätsvermutung**: CEN/CENELEC JTC 21 hatte bis dahin keine harmonisierte Norm veröffentlicht. *(Stand 07/2026; der Normungsstand ändert sich.)* |

## 7. Praxis — der Übergang von der echten Excel zur Struktur

Der schwierige Teil ist **nicht** das Erzeugen synthetischer Daten. Der schwierige Teil ist der Moment davor: der Übergang von einer echten Excel-Datei zu einer Struktur, mit der man arbeiten kann, ohne dass unterwegs Echtdaten irgendwo hängenbleiben. Vier Regeln:

1. **Die Originaldatei liegt in einem eigenen Ordner, physisch außerhalb jedes Git-Repos.** Nicht bloß in `.gitignore`. Begründung: `.gitignore` schützt nicht gegen ein `git add -f`, und es schützt überhaupt nicht gegen den Agenten-Kontext. Ein Agent, der im Repo-Verzeichnis liest, liest auch ignorierte Dateien.
2. **Genau eine Person öffnet die Datei, lokal, ohne Cloud-Sync.** Dropbox-, OneDrive- und iCloud-synchronisierte Ordner sind tabu: Sie sind ein zweiter Kopiervorgang, den niemand angeordnet hat, also genau die Konstellation aus Abschnitt 1.
3. **Die Extraktion läuft als lokales Skript, nie durch ein LLM.** Eine Excel in ein Chatfenster zu ziehen, um „mal das Schema rauszuziehen", ist eine Übermittlung an einen Dritten. Das Skript liest die Datei, gibt Spaltennamen und Typen aus und rührt die Werte nicht an.
4. **Nur das Schema wandert ins Repo.** Ab diesem Punkt arbeitet das ganze Team mit erfundenen Werten, und die Frage „darf das hier liegen?" stellt sich nicht mehr.

**Werkzeuge:** Für Schritt 3 nimmst du ein eigenes kleines Skript. Lass es vom Agenten schreiben, und zwar an einer **Fake-Datei** mit derselben Spaltenstruktur, damit das Modell nie einen echten Wert sieht. Ein Beispiel: [`exercises/find-the-personal-data/extract-schema.py`](../../exercises/find-the-personal-data/extract-schema.py). Für die Gegenprobe lohnt ein zweiter Check, ein **Leak-Guard**: Er schlägt Alarm, wenn ein Wert aus der Originaldatei doch in der synthetischen Ausgabe auftaucht.

**Faker-Realität für Österreich.** Die Bibliothek Faker deckt mit dem Locale `fakerDE_AT` einiges ab: AT-Postleitzahlen, Bundesland, Ort, IBAN und Firmennamen. Sie deckt **nicht** ab: UID-Nummer, Sozialversicherungsnummer und Firmenbuchnummer. Die musst du selbst nach dem jeweiligen Formatmuster erzeugen. *(Stand 07/2026, Quelle: Faker-Locale-Daten `de_AT`; der Umfang ändert sich zwischen Versionen, deshalb die Faker-Version im Projekt pinnen.)*

Und eine Falle, die regelmäßig übersehen wird: **`faker.internet.email()` transliteriert Umlaute und verwendet echte Provider-Domains.** Aus „Jörg Müller" wird eine plausible Adresse bei einem realen Anbieter, die einer echten Person gehören kann. Setze immer explizit `provider: 'example.com'`. `example.com`, `example.net` und die Endung `.example` sind nach RFC 2606 für genau diesen Zweck reserviert und können niemandem gehören.

## 8. Melden statt vermeiden

Der letzte Abschnitt ist der wichtigste, und er widerspricht dem, was viele Organisationen tun.

**Pflicht-Schulungen allein ändern wenig.** Eine Langzeitstudie mit mehr als 14.000 Beschäftigten über 15 Monate fand, dass die in der Industrie übliche eingebettete Schulung nach simulierten Phishing-Mails Beschäftigte **nicht** widerstandsfähiger machte und sie teils sogar anfälliger werden ließ. *(Quelle: Lain, Kostiainen, Čapkun, „Phishing in Organizations: Findings from a Large-Scale and Long-Term Study", IEEE S&P 2022, https://arxiv.org/abs/2112.07498, abgerufen 2026-09-13.)*

**Was wirkt, ist ein Meldekanal, bei dem Melden sich lohnt.** Das NCSC UK formuliert die dahinterliegende Regel unmissverständlich: *„metrics express an organisation's values, and if you appear to value the absence of reports of problems, you incentivise people to keep quiet about issues."* Und, ebenso knapp: *„Don't reprimand users."* *(Quelle: NCSC, „Phishing attacks: defending your organisation", https://www.ncsc.gov.uk/guidance/phishing, abgerufen 2026-09-13.)*

> **Merksatz:** Die Metrik ist die **Meldequote**, niemals die Fehlerquote. Wer Fehler zählt, bekommt weniger Meldungen, nicht weniger Fehler.

Daraus eine Empfehlung für deine eigene Organisation oder dein Team, festgehalten, bevor etwas passiert:

> **Wer meldet, bekommt innerhalb einer fest vereinbarten, kurzen Frist eine Antwort, auch bei einem Fehlalarm. Es gibt keine Konsequenz für eine Meldung. Es gibt eine für das Verschweigen.**

Ein Fehlalarm kostet ein paar Minuten. Eine Datei, die aus Sorge vor Ärger niemand erwähnt, kann nach Abschnitt 1 bis zu 1.000.000 EUR kosten.

## 9. Fünf Sätze für den Alltag

> 1. **Ohne unterschriebene AVV kommt keine Kundendatei auf meinen Rechner.**
> 2. **Ich lasse mir schriftlich bestätigen, dass der Kunde die Daten übermitteln darf.**
> 3. **Ich verspreche nie „anonym", sondern dokumentiere das Verfahren.**
> 4. **Ich lösche das Original nach Abschluss und schicke eine Löschbestätigung.**
> 5. **Wenn besondere Kategorien drin sind (Gesundheit, Religion, Gewerkschaft, Herkunft, Politik, Sexualleben; Art. 9 DSGVO), frage ich zurück, BEVOR ich die Datei überhaupt öffne.**

---

## Q&A

**Der Kunde schickt mir die Excel einfach per Mail. Was mache ich?**
Nicht öffnen, bevor zwei Dinge stehen: eine unterschriebene AVV (Art. 28) und eine schriftliche Bestätigung, dass der Kunde diese Daten übermitteln darf. Beides ist eine kurze Mail wert, keine Vertragsverhandlung. Der CNIL-Fall in Abschnitt 1 zeigt, dass genau diese fehlende Weisung, nicht die Technik, der sanktionierte Punkt war.

**Reicht es nicht, die Namen durch IDs zu ersetzen?**
Nein. Das ist Pseudonymisierung, und der EuGH hat in C-413/23 P (04.09.2025) bestätigt: Solange irgendwer die Zuordnung zurückführen kann, bleiben die Daten personenbezogen. Du hast dann dieselben Pflichten wie vorher, nur mit mehr Aufwand. Nimm stattdessen Schema-only (Abschnitt 3).

**Sind synthetische Daten automatisch anonym?**
Nein. In den EDSA Guidelines 02/2026 tauchen synthetische Daten genau einmal substanziell auf, **als Risikofall** (Rn. 82, Inference-Kriterium). Eine Aussage „synthetisch = anonym" gibt es von keiner Aufsichtsbehörde. Rechtlich sauber ist der Weg, bei dem nie ein echter Wert eingeflossen ist: Schema-only.

**Ich habe versehentlich eine Kundendatei in ein Repo gelegt. Was jetzt?**
Sofort melden, bei der Stelle, die in deiner Organisation dafür zuständig ist, und nicht heimlich reparieren. Wenn ihr die Empfehlung aus Abschnitt 8 umgesetzt habt, bekommst du schnell eine Antwort und musst keine Konsequenz für die Meldung fürchten. Der Grund für die Eile ist praktisch: Eine Datei aus der Git-Historie zu entfernen ist deutlich einfacher, solange nichts gepusht, geforkt oder gespiegelt wurde.

**Wie viel Aufwand ist realistisch, bevor ich anfangen kann?**
Für den Default-Weg wenig: Schema extrahieren, Generator schreiben, Ergebnis gegenprüfen. Anonymisierung ist deutlich aufwendiger und lohnt nur, wenn echte Verteilungen fachlich gebraucht werden. Wenn jemand „nur schnell mit den echten Daten" arbeiten will, ist das Argument dagegen nicht juristisch, sondern zeitlich: Der Genehmigungspfad dafür dauert meist länger als der synthetische Weg.

**Brauchen wir für DSGVO-Auskünfte im Live-System ein Admin-UI?**
Nein. Art. 15/17/20 verlangen Erfüllung binnen eines Monats (Art. 12 Abs. 3), nicht eine Oberfläche. Ein dokumentiertes SQL-Runbook erfüllt die Anforderung; ein UI ist Komfort und kann später kommen. Details in Abschnitt 6.

**Darf ich einen Agenten die Kundendatei lesen lassen, wenn er lokal läuft?**
Für die Extraktion nein. Regel 3 in Abschnitt 7 ist bewusst hart: Die Extraktion läuft als lokales Skript, nicht durch ein Modell. Der Grund ist nicht Misstrauen gegen den Agenten, sondern der Kontext: Was einmal im Context-Window landet, geht bei den meisten Setups über eine API nach draußen und ist damit eine Übermittlung. Auch wenn du ein Modell in der EU oder auf eigener Infrastruktur betreibst, bleibt die Weisungsfrage aus Abschnitt 4 unberührt.

**Wir sind ein kleines Team und niemand prüft uns. Ist das nicht übertrieben?**
Mag sein, dass niemand prüft. Aber alle vier Fälle in Abschnitt 1 kamen nicht aus einer Prüfung, sondern aus einem Sicherheitsvorfall, und darauf hat Teamgröße keinen Einfluss. Deshalb ist die Löschfrist die Maßnahme mit dem besten Verhältnis von Aufwand zu Wirkung: Sie kostet fast nichts und verkleinert das Zeitfenster, in dem ein Vorfall überhaupt Echtdaten treffen kann.

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
- EuGH, C-413/23 P (EDSB ./. SRB) vom 04.09.2025: relative Bestimmbarkeit bei Pseudonymisierung
- EDSA, Guidelines 02/2026 zur Anonymisierung: Entwurf vom 07.07.2026, Konsultation bis 30.10.2026, ersetzen WP216/2014
- DSGVO: ErwGr 26 · Art. 5 Abs. 2 · Art. 9 · Art. 12 Abs. 3 · Art. 15/17/20 · Art. 28 (insb. Abs. 3 lit. g und Abs. 10) · Art. 29 · Art. 30
- PIPC-Bußgeld gegen OpenAI (26.07.2023): Yonhap, 27.07.2023, https://en.yna.co.kr/view/AEN20230727003800315
- Lain, Kostiainen, Čapkun: „Phishing in Organizations: Findings from a Large-Scale and Long-Term Study", IEEE S&P 2022, https://arxiv.org/abs/2112.07498
- NCSC UK, „Phishing attacks: defending your organisation" (Melde-Metriken, „Don't reprimand users"): https://www.ncsc.gov.uk/guidance/phishing
- RFC 2606: reservierte Domains für Beispiele (`example.com` und verwandte), https://www.rfc-editor.org/rfc/rfc2606
