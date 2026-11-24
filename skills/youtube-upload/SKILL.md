---
name: youtube-upload
description: Lade GhostWriter-Videos wie Buchteaser über die kostenlose YouTube Data API hoch. Verwende diesen Skill für die einmalige Google-Cloud-Einrichtung, Titel, Beschreibung, Tags, Sichtbarkeit und den Upload mit yt_upload.py.
---

# Video auf YouTube hochladen

Kostenloser Weg über die YouTube Data API v3, ohne Bezahldienst. Das Skript [`yt_upload.py`](yt_upload.py) läuft auf dem Rechner des Nutzers.

## Einmalige Einrichtung

1. In der [Google Cloud Console](https://console.cloud.google.com) ein Projekt anlegen, z. B. „GhostWriter Upload“.
2. Unter „APIs & Dienste“ → Bibliothek die **YouTube Data API v3** aktivieren.
3. OAuth-Zustimmungsbildschirm: Typ „Extern“, App-Name eintragen, die eigene Google-Adresse als **Testnutzer** hinzufügen.
4. Anmeldedaten → „OAuth-Client-ID“ → Typ **Desktop-App** → JSON herunterladen und als `client_secret.json` in den Upload-Ordner legen.
5. `pip install google-api-python-client google-auth-oauthlib`

Hinweise:

- Kontingent: 10.000 Einheiten pro Tag, ein Upload kostet etwa 1.600. Das reicht für rund sechs Uploads pro Tag.
- Bei ungeprüften Projekten setzt YouTube hochgeladene Videos auf **privat**, bis Google das Projekt geprüft hat. Danach lässt sich die Sichtbarkeit in YouTube Studio ändern.
- `client_secret.json` und `token.json` nie in ein Repo übernehmen. In Buchrepos beide Dateien in `.gitignore` eintragen.

## Ablauf pro Video

1. **Video und Zweck klären.** Welches Buch, welcher Abschnitt, welche Zielgruppe. Bei Buchteasern den finalen Export aus `marketing/teaser/` oder dem bestehenden Projektpfad verwenden.
2. **Texte entwerfen.** Titel (höchstens 100 Zeichen), Beschreibung (höchstens 5.000 Zeichen) und Tags aus belegtem Buchmaterial ableiten. Die Erzählstimme und Spoilergrenze des Buchs beachten. Die Beschreibung als `beschreibung.txt` neben das Video legen.
3. **Freigabe einholen.** Titel, Beschreibung, Tags und Sichtbarkeit (privat, nicht gelistet, öffentlich) dem Nutzer vorlegen und erst nach Bestätigung hochladen. Standard ist privat. Die Veröffentlichung als eigene Aktion behandeln.
4. **Hochladen.** Im Upload-Ordner ausführen, über eine Shell auf dem Rechner des Nutzers oder als kopierfertiger Befehl:

   ```
   python yt_upload.py "teaser.mp4" --title "…" --description-file beschreibung.txt --tags "GhostWriter,…" --privacy private
   ```

   Beim ersten Lauf öffnet sich die Google-Anmeldung. Danach wird `token.json` wiederverwendet.
5. **Ergebnis festhalten.** Den Link melden. Auf Auftrag Link, Datum und Sichtbarkeit in der Teaser-Übersicht des Buchrepos ergänzen.

## Fehler

- `quotaExceeded`: Tageskontingent aufgebraucht, am nächsten Tag erneut versuchen.
- `access_denied` bei der Anmeldung: Die Google-Adresse fehlt als Testnutzer (Einrichtung, Schritt 3).
- `invalid_grant`: `token.json` löschen und neu anmelden.
- Video bleibt trotz `--privacy public` privat: Das Projekt ist noch nicht von Google geprüft.
