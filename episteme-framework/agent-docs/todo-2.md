# TODO-2: Remaining work (increment)

**Source:** [TODO-MIND-MACHINE-BASE.md](TODO-MIND-MACHINE-BASE.md). Sections 1–2 are complete. This doc lists what is left to do.

---

## Done (no action)

- **§1 Agent interface:** Bootstrap, Cursor rules, LIBRARY-MAP, meta-agent as default — all done.
- **§2 Structures:** Root README, ai-docs refs removed, .episteme-project refactored out; _docs and leading-underscore convention OK.
- **§3.2, 3.3, 3.5:** Tracking sample, code guides, skills — OK.
- **§4.2:** list-topics.sh — OK.
- **§5.2–5.4:** Per-section READMEs, discoverability of code guides and skills — OK.
- **§6.1:** Placeholder for “your repo” in meta-agent — OK.
- **§3.1:** Ideas sample — `ideas-engine/sample/` + getting-started.md + README added.
- **§3.4:** Code guide sources — `language-style-guides/code-guide-sources.md` added.
- **§6.2:** Overrides + secrets — `agent-docs/OVERRIDES.md` + repo root `SECRETS.md` added.
- **§6.3:** New project one-pager — `agent-docs/NEW-PROJECT.md` added.
- **§5.1:** Top-level index — `episteme-framework/INDEX.md` added.

---

## Remaining (by priority)

### 1. Functions and automation

| ID   | Item | Action |
|------|------|--------|
| 4.4  | **Load-context helper** | Generate a doc or list of exact file paths for a “minimal context set” (e.g. meta-agent + skills tree + project schema). Add a short blurb on why this is the exemplar. |
| 4.1  | **Menu skill(s)** | Skill or skill collection that implements the menu as discussed. Include: specify a file by path and insert each item in the file as an idea (blank lines as separators). |
| 4.5  | **Integrity / sync (skills)** | Implement or stub SKILL_INTEGRITY_CHECK and SKILL_STANDARD_SYNC (recompute hash, compare to stored; compare local skill-standard to website). |
| 4.3  | **Scrape / merge scripts** | Do **last**. Add scripts (or stubs + README) under language-style-guides for scrape_guides and merge so the fork can refresh or merge code guides. |

### 2. Optional

| ID   | Item | Action |
|------|------|--------|
| 5.5  | **Manifest or INDEX** | Optional: single list of all _*.md, SKILL.md, code-guide-*.ai for programmatic “list all library assets.” (Skills map already exists: SKILLS_TREE + LIBRARY-MAP.) |

---

## File checklist (remaining)

| File or folder | Location | Action |
|----------------|----------|--------|
| ~~code-guide-sources.md~~ | language-style-guides/ | Done. |
| ~~INDEX.md~~ | episteme-framework/ | Done. |
| ~~Override/config doc~~ | agent-docs/OVERRIDES.md | Done. |
| ~~SECRETS.md~~ | Repo root | Done. |
| ~~“New project” one-pager~~ | agent-docs/NEW-PROJECT.md | Done. |
| Load-context doc | agent-docs | Create: minimal context set + exemplar blurb. |
| Scrape/merge scripts or README | language-style-guides | Add last: scripts or stubs + “how to scrape/merge.” |

---

## Summary

- **Immediate (done):** 3.1, 3.4, 6.2, 6.3, 5.1.
- **Next:** 4.4 (load-context), 4.1 (menu skill), 4.5 (integrity/sync).
- **Last:** 4.3 (scrape/merge).
- **Optional:** 5.5 (programmatic INDEX).

After these are done, update §7 Summary and §8 File checklist in [TODO-MIND-MACHINE-BASE.md](TODO-MIND-MACHINE-BASE.md) to match.
