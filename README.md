# GhostWriter Skills

Optionale Arbeitsabläufe für [GhostWriter](https://github.com/ploeffler/GhostWriter).

| Skill | Aufgabe |
| --- | --- |
| [Buchteaser](skills/buchteaser/SKILL.md) | Einen Teaser planen, aus Einzelclips schneiden und im Buchrepo archivieren |
| [GhostWriter](skills/ghostwriter/SKILL.md) | Wiedereinstieg: verweist auf `START.md` im Repository (kein eigener Ablauf) |
| [Buchgedächtnis](skills/ghostwriter-buchgedaechtnis/SKILL.md) | Fakten und Kontinuität im Buch abgleichen |
| [Lektorat](skills/ghostwriter-lektorat/SKILL.md) | Buchtexte prüfen und redaktionell überarbeiten |
| [Gegenlesen](skills/ghostwriter-gegenlesen/SKILL.md) | Bereiche zum Gegenlesen auschecken und die Rückgabe einchecken |
| [Material](skills/ghostwriter-material/SKILL.md) | Fotos, Dokumente und Rückgaben zum Buch einbringen, aufbereiten und markieren |
| [Anekdoten](skills/ghostwriter-anekdoten/SKILL.md) | Eigene Erlebnisse festhalten und anonymisiert in Abschnitte einbauen |
| [Figurenbild](skills/ghostwriter-figurenbild/SKILL.md) | Figurenbilder gestalten: Bildstil, Prompt aus dem Profil, Varianten mit Prompt ablegen |
| [Kurz und klar](skills/ghostwriter-kurz-und-klar/SKILL.md) | Antwortstil im Chat: Ergebnis zuerst, wenige Punkte, eine Frage als Auswahl (Einstellung, geplant für GhostWriter 1.6) |

Der Buchteaser ist der Pilot zu [GhostWriter #532](https://github.com/ploeffler/GhostWriter/issues/532). Er funktioniert mit vorhandenen Clips und einem verfügbaren Videoeditor. Für die Nutzung die `SKILL.md` im Agenten laden oder als Arbeitsanweisung referenzieren. Der Buchteaser bleibt optional und wird nicht automatisch in Buchrepositorys installiert.

Die allgemeinen Skills werden hier gepflegt. GhostWriter liefert die sechs allgemeinen Skills (Buchgedächtnis, Lektorat, Gegenlesen, Material, Anekdoten, Figurenbild) als Kopien eines geprüften Quellcommits aus. `ghostwriter-skills.yml` im Hauptrepository hält Commit und SHA-256-Prüfsummen fest; `scripts/sync_skills.py` übernimmt eine bewusst gewählte Version aus einem lokalen Klon. Reguläre GhostWriter-Updates verteilen diese Kopien, ohne zur Laufzeit dieses Repository abrufen zu müssen. Änderungen hier allein aktualisieren vorhandene Bücher nicht.

Projektregeln, persönliche Skills und ausführbare Werkzeuge werden im jeweiligen Buch- oder Programmrepo gelesen. Die Links zur Programmdokumentation führen ins GhostWriter-Hauptrepo.

[English](README.en.md)

---

Entwickelt mit Unterstützung von Claude (Anthropic)
Entwickelt mit Unterstützung von Codex (OpenAI)
