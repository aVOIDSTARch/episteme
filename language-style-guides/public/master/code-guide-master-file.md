# Code guide master file design (AGENT RESOURCE)

**Purpose:** Defines the target structure and conventions for every `code-guide-<topic>.ai` in this folder. Use when creating, editing, or validating a language/topic code guide so guides stay consistent and agents can parse and apply them reliably.

**Audience:** Agents and humans that generate or maintain code-style guidance.

---

## 1. Document structure (sections in order)

Each code guide must contain the following sections, in this order. Use level-2 headings (`##`) for these main sections; subsections use `###` and `####` as shown below.

### 1.1 Language / topic overview (top of document)

**What to include:**

- **Brief description** of the language or topic (1–3 sentences).
- **Best use cases:** When to choose this language/tool (e.g. “systems code”, “frontend UI”, “data pipelines”).
- **Contraindications:** When *not* to use it (e.g. “avoid for real-time safety-critical systems”, “not for large monoliths”).
- **General data:** Typical ecosystem (runtime, package manager, version), link to official docs or spec if one exists.
- **Style guide last updated:** One line with date of last merge or scrape (e.g. `Style guide last updated: YYYY-MM-DD` or `Sources last merged: …`) so agents can decide whether to suggest a refresh.
- **Guide quality rating (required):** A small rating (e.g. 1–5 or star-like) for trustworthiness/completeness, with concrete metrics and a short synopsis of why it scored that way. Store at the top of the Overview so agents can weight usage. Re-score when sources are added or conflicts resolved.

Keep this section short and scannable. The agent uses it to decide whether the guide is relevant to the current task.

**Example (conceptual):**

```markdown
## Overview

Python is a dynamic, interpreted language with a large standard library and ecosystem. Best for: scripting, tooling, data science, backend services, and rapid prototyping. Avoid for: low-latency or memory-constrained systems, heavy numeric kernels (prefer compiled). Ecosystem: CPython/pypa, pip/venv, 3.x. [Official docs](https://docs.python.org/). Style guide last updated: YYYY-MM-DD.
```

---

### 1.2 Sources and access

**What to include:**

- A **list of sources** used to build this guide.
- For each source: **name**, **site URL**, and **date last accessed** (or “Crawled:” timestamp if you keep scrape metadata).

This supports traceability and re-crawl; agents can use it to refresh or verify content.

**Format:**

```markdown
## Sources

| Source | URL | Last accessed |
|--------|-----|----------------|
| Google Python Style Guide | https://google.github.io/styleguide/pyguide.html | 2026-03-03 |
| PEP 8 | https://peps.python.org/pep-0008/ | 2026-03-03 |
| … | … | … |
```

Raw scraped blocks (e.g. `## Source: …` with **URL:** and **Crawled:**) can live in an appendix or in a separate **scraping archive folder** (formatted, pruned, easy to traverse). Prefer archiving full raw scrapes in that archive and keeping only the Sources table plus normalized guide in the `.ai` file (or a truncated appendix plus “full scrape in archive”); the table is the canonical summary for agents.

---

### 1.3 Code guide (consensus first, then per-source)

**What to include:**

1. **Subsection: Guidelines common across sources**  
   Rules that appear in a reasonable majority of the scraped guides. Prefer one bullet or short paragraph per guideline. No duplication of the same rule.

2. **Subsections per source: Unique or conflicting guidelines**  
   One subsection per source (or per notable source) that either:
   - Adds rules not in the consensus, or  
   - Contradicts the consensus or another source.

   **Per-source density (codified):** Per-source subsections must stay concise. Include **only** rules that are unique to that source or that conflict with consensus or another source. Do not restate consensus in Per-source. For each rule, **indicate the source** and, if relevant, **that it conflicts** with [source X] or “majority”.

**Why this order:** Agents can apply “consensus” first for safe, general advice; then consider source-specific or conflicting rules when the context (e.g. “Google-style codebase”) is known.

**Format (conceptual):**

```markdown
## Code guide

### Consensus (majority of sources)

- Use 4 spaces for indentation.
- Max line length 100 characters; wrap at natural boundaries.
- Names: snake_case for functions/variables, PascalCase for classes.
- …

### Per-source: unique or conflicting

#### Google Python Style Guide

- Type annotations required for public APIs. (Unique.)
- Prefer `from x import y` only when y is not too generic. (Conflicts with [PEP 8] “no strong opinion”.)

#### PEP 8

- …
```

---

### 1.4 Notes for the agent

**What to include:**

- **When to use this guide:** e.g. “Use when the user asks for Python style”, “Use when editing files under `frontend/`”.
- **Caveats:** e.g. “Legacy codebase uses 2 spaces; prefer consensus 4 for new code.”
- **Tooling:** Linters, formatters, or configs that enforce this guide (e.g. Black, Ruff, pylint). Include **direct links** to linter/formatter config (e.g. EditorConfig, StyleCop docs) for copy-paste or “suggest this config.”
- **Conflicts:** How to behave when sources disagree (e.g. “Prefer Google when repo has a Google-style README; otherwise consensus.”).

Keep this section actionable so the agent can decide when and how to apply the guide without guessing.

---

## 2. Conventions for agents

- **File naming:** `code-guide-<topic>.ai` under the appropriate subfolder (see `README.md` in this directory). Topic matches the language or framework (e.g. `code-guide-python.ai`, `code-guide-ts-js.ai`).
- **Scraped content:** Raw `## Source: …` blocks with **URL:** and **Crawled:** may remain in the file or in a scraping archive folder. The **Sources** table (section 1.2) is the canonical list; consensus and per-source subsections (1.3) are the normalized, usable guide. Prefer a formatted, pruned archive for full raw scrapes to keep `.ai` files manageable.
- **Single-source disclaimer:** When only one source has been scraped, state in Consensus that it is “derived from the single scraped source (e.g. [name]); treat as baseline until more sources are merged.” Re-derive consensus when additional sources are merged.
- **Per-source density:** Per-source subsections contain only **unique** or **conflicting** rules; do not restate consensus there.
- **Conflicts:** Always label conflicting rules with the source and “(Conflicts with …)” or “(Unique)” so the agent can choose by context.
- **Updates:** When re-scraping or merging (e.g. from `public/google/` or crawl), add new content under 1.2 and 1.3; then refresh consensus and per-source subsections so they stay accurate. Update “Style guide last updated” (or “Sources last merged”) in Overview.

---

## 3. Relationship to other assets

| Asset | Role |
|-------|------|
| **code-guide-master-file.md** (this file) | Design and structure for every `code-guide-*.ai`; AGENT RESOURCE for how to format and maintain guides. |
| **README.md** (this directory) | Folder layout and list of code-guide files. |
| **Scrape/merge** | Populate raw source content; scripts and state: `scrape_guides.py`, `merge_google_into_master.py`, `scrape.md`, `scrape-report.md`. Cleaning and merging produce the blocks that feed sections 1.2 and 1.3. |
| **code-guide-sources.md** (repo root) | List of style-guide sites to crawl; used by scrape workflow. |
| **code-guide-format-analysis.md** (ai-docs) | Analysis and usage notes for agents: how to apply this format when analyzing or improving code style; recommendations and quick reference. |

When in doubt: **this document defines the target shape of each code guide; scrape/merge and manual editing fill and refine the content.** For usage and interpretation, see `ai-docs/code-guide-format-analysis.md`.
