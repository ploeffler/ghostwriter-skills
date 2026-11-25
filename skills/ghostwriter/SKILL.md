---
name: ghostwriter
description: Wiedereinstieg in ein GhostWriter-Repository (Buch oder Bibliothek). Verweist auf START.md, Abschnitt 0, im Repository, das den ganzen Ablauf enthält (Repository und Schreibzugriff prüfen, Git-Benutzer, Darstellungsmodus, Bücherregal bzw. Projektübersicht, Fehler ans Hauptrepository melden). Bei jedem ersten Aufruf eines GhostWriter-Buch- oder Bibliotheks-Repositorys verwenden; gibt es einen persönlichen Skill für dieses Repository, gilt er zusätzlich. Nicht für Programmarbeit am Hauptrepository.
---

# GhostWriter: Wiedereinstieg

Dieser Skill enthält bewusst **keinen eigenen Ablauf** (GhostWriter #569). Der Ablauf steht im Repository und gilt dort immer:

1. `CLAUDE.md` bzw. `AGENTS.md` und `START.md`, Abschnitt 0 (Wiedereinstieg), im ausgewählten Buch- oder Bibliotheksrepository lesen und befolgen: Repository und Zugang feststellen, Schreibzugriff prüfen, Git-Benutzer, Darstellungsmodus, erste Ansicht, Kurzbefehle, Fehler ans Hauptrepository melden.
2. Gibt es `assistant.yml`, zusätzlich den persönlichen Skill unter `.claude/skills/<skill>/SKILL.md` lesen (Name in `assistant.yml` → `skill`). Er lebt nur im Repository.
3. Zu Beginn einer Aufgabe in einem Satz nennen, welcher Skill verwendet wird; den spezifischeren nehmen (persönlicher Skill vor diesem).
4. Gezielte Aufträge: Lektorat (`ghostwriter-lektorat`), Buchgedächtnis (`ghostwriter-buchgedaechtnis`), Gegenlesen (`ghostwriter-gegenlesen`), Material (`ghostwriter-material`).

**Ohne Zugriff auf das Repository** (kein Klon, kein GitHub-Werkzeug): nichts erfinden und nicht aus dem Gedächtnis arbeiten. Sag, was fehlt, und biete den Weg über **Auschecken** und **Einchecken** an (Skill `ghostwriter-gegenlesen`): Ein Bereich des Buchs wird als Datei ausgegeben, extern bearbeitet und als Rückgabe wieder eingebracht.

---

<p align="right"><sub>Entwickelt mit Unterstützung von Claude (Anthropic) · <a href="https://claude.ai">claude.ai</a><br>Entwickelt mit Unterstützung von Codex (OpenAI)</sub>&nbsp;&nbsp;<picture><source media="(prefers-color-scheme: dark)" srcset="https://github.com/ploeffler/GhostWriter/raw/refs/heads/main/assets/logo-dark.svg"><img src="https://github.com/ploeffler/GhostWriter/raw/refs/heads/main/assets/logo.svg" alt="GhostWriter" height="22" align="absmiddle"></picture></p>
