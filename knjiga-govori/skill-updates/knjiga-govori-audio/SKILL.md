---
name: "knjiga-govori-audio"
description: "Erstellt die kroatische Sprachaufnahme (Audio) für ein Knjiga Govori Skript in Google AI Studio mit der Stimme Enceladus und liefert nummerierte Audioteile. Nutzen, wenn Pavo Audio, Voiceover, Sprecher, TTS oder „Audio machen“ für ein Skript will."
---

# Knjiga Govori: Audio (Voiceover) in Google AI Studio

Vorher den Skill `knjiga-govori-kanal` laden. Grundlage ist immer das von Pavo freigegebene Skript (`<Naslov knjige> - Scenarij*.docx`).

## Browser

In Pavos eigenem Chrome arbeiten (Claude in Chrome), dort ist er bei Google angemeldet. Vorher den Skill `chrome-browser` laden. Einen neuen Tab öffnen. Passwörter nie selbst eingeben.

## Feste Einstellungen (genau so, Stand November 2026)

1. Öffnen: `https://aistudio.google.com/generate-speech?model=gemini-2.5-flash-preview-tts`
2. Modell prüfen: **Gemini 2.5 Flash Preview TTS** (`gemini-2.5-flash-preview-tts`). Nicht das neuere Standardmodell nehmen.
3. Beispielkarte **„The Patient Teacher“** anklicken (Bereich „Explore Text to speech“, ggf. nach rechts blättern). Ansicht **Composer**.
4. Alle Beispiel Sprechblöcke bis auf **einen** löschen („Delete speech block“). Nur ein Sprecher.
5. **Scene:** leer lassen.
6. **Sample Context:** `read in croatian`
7. **Stimme:** Speaker 1 über „Open voice settings“ auf **Enceladus** (Breathy, Lower pitch) stellen. Die übrigen Speaker Einstellungen der Vorlage (Audio Profile, Style, Pace, Accent) unverändert lassen.
8. **Model settings → Temperature:** `1.1`

## Text vorbereiten

* Den ganzen Skripttext vorlesen lassen, auch die Überschriften (Hook Titel, Abschnittstitel, Lektionstitel).
* Lektionsüberschriften in GROSSBUCHSTABEN vorher in normale Schreibweise umwandeln (z. B. „Karakter nije sudbina, nego navika mišljenja.“), damit die Stimme sie nicht buchstabiert.
* Marker „Savjet 1:“, „Korak 1:“, „Greška 1:“, „Pitanje 1:“ bleiben stehen.
* **Aufteilen: ein Teil = eine Überschrift mit ihrem Text** (Pavos Vorgabe, 15. Nov 2026). Jede Überschrift im Skript (Hook Titel H1, jeder Abschnitt H2, jedes Prinzip H3) beginnt einen neuen Teil, dazu gehört der ganze Text bis zur nächsten Überschrift. Teile nie zusammenlegen, auch wenn sie kurz sind (z. B. „Praktični savjeti“). Nur falls ein einzelner Abschnitt für einen Lauf zu lang wird (über ca. 600 Wörter), an einer Absatzgrenze teilen und als 05a, 05b nummerieren.
* Den Text am schnellsten per JavaScript in das Textfeld setzen (`textarea[aria-label="Speech block text"]`, fokussieren, alles markieren, `document.execCommand('insertText', ...)`), statt ihn zu tippen.

## Ablauf pro Teil

1. Text von Teil N in den Sprechblock setzen.
2. **Run** klicken und warten, bis wieder „Run“ statt „Stop“ erscheint (ca. 1,5 bis 2 Minuten). Lange Wartezeiten mit kurzen Wait Schritten überbrücken, kein JavaScript das länger als 40 Sekunden läuft.
3. Die Wiedergabe startet automatisch: sofort **Pause** klicken.
4. Länge notieren (rechts im Player).
5. **Download** klicken (Downloads nur, wenn Pavo sie in diesem Gespräch freigegeben hat; einmal Ja für alle Teile eines Buches reicht).
6. Erst danach den nächsten Teil einsetzen.

## Nummerierung (wichtig)

Jede Audiodatei muss eindeutig mit ihrer Reihenfolge nummeriert sein, damit Pavo sofort sieht, was zuerst kommt:

* Dateiname: `01_<Buchtitel>_Audio.wav`, `02_<Buchtitel>_Audio.wav`, `03_…` (zweistellig, beginnend bei 01), Buchtitel ohne Sonderzeichen, z. B. `01_Kako_mislis_tako_stvaras_Audio.wav`.
* AI Studio vergibt beim Download eigene Namen. Deshalb nach dem Download umbenennen:
  * Ist Pavos Download Ordner (oder der Buchordner) über die Desktop App verbunden, die Dateien dort in der Download Reihenfolge (älteste zuerst) direkt umbenennen und in den Buchordner verschieben.
  * Ist kein Ordner verbunden, Pavo bitten, den Download Ordner über „+“ → „Ordner hinzufügen“ zu verbinden, oder ihm die genaue Zuordnung nennen (Teil 1 = älteste Datei usw.).
* In der Abschlussmeldung immer eine nummerierte Tabelle liefern: Nummer, Überschrift des Teils, Länge.

## Abschluss

* Tabelle mit allen Teilen (Nummer, Inhalt, Länge) und Gesamtdauer.
* Pavo bitten, reinzuhören, besonders bei Jahreszahlen, fremdsprachigen Titeln und Markern. Claude kann das Audio selbst nicht anhören.
* Bei Fehlern nur den betroffenen Teil neu erzeugen, mit derselben Nummer.

## Grenzen

* Kostenlos bleiben: keine bezahlten Funktionen, Abos oder API Keys einrichten, ohne vorher ausdrücklich zu fragen.
* Nichts in Pavos Konto löschen oder Einstellungen ändern außer den oben genannten Feldern im Playground.