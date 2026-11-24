# GhostWriter Skills

Optional workflows for [GhostWriter](https://github.com/ploeffler/GhostWriter).

| Skill | Task |
| --- | --- |
| [Book teaser](skills/buchteaser/SKILL.md) | Plan and edit a teaser from existing clips and archive the production in the book repository |
| [GhostWriter](skills/ghostwriter/SKILL.md) | Start and work with GhostWriter books and libraries |
| [Story memory](skills/ghostwriter-buchgedaechtnis/SKILL.md) | Compare facts and continuity in a book |
| [Editorial review](skills/ghostwriter-lektorat/SKILL.md) | Review and edit book text |
| [YouTube upload](skills/youtube-upload/SKILL.md) | Upload videos such as book teasers for free via the YouTube Data API |

The book teaser is the pilot for [GhostWriter #532](https://github.com/ploeffler/GhostWriter/issues/532). It works with existing clips and an available video editor. Load its SKILL.md explicitly as an agent skill or workflow instruction; it is not installed into books automatically.

The general skills are maintained here. GhostWriter distributes copies of the three general skills pinned to a reviewed source commit. The main repository records the commit and SHA-256 digests in `ghostwriter-skills.yml`; `scripts/sync_skills.py` imports a deliberately selected version from a local clone. Normal GhostWriter updates distribute these copies without runtime access to this repository. Changes here alone do not update existing books.

Read project rules, personal skills and executable tools from the selected book or program repository. Program documentation links point to the GhostWriter main repository. Personal skills remain in their book repositories.

[Deutsch](README.md)

---

Developed with support from Claude (Anthropic)
Developed with support from Codex (OpenAI)
