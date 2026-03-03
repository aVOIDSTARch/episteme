# Code guide file format: analysis and usage

**Purpose:** This document summarizes the analysis of the `code-guide-*.ai` format (as applied to C# in `public/master/c-family/code-guide-c-sharp.ai`) for **future agent use** when analyzing and improving code style for a language. It is an AGENT RESOURCE.

**Reference:** Structure is defined in `language-style-guides/public/master/code-guide-master-file.md`. The C# file is the first full transformation example.

---

## 1. Format summary

Each code guide file has four main sections in order:

| Section | Role |
|--------|------|
| **Overview** | Brief description, best use cases, contraindications, ecosystem. Lets the agent decide if the guide is relevant. |
| **Sources** | Table: source name, URL, last accessed. Canonical list for traceability and re-crawl. |
| **Code guide** | **Consensus** (rules shared across sources) first; then **Per-source** (unique or conflicting rules by source). |
| **Notes for the agent** | When to use, caveats, tooling, how to resolve conflicts. |

Raw scraped content may live in an **Appendix** for traceability; the normalized Consensus + Per-source text is what the agent should apply.

---

## 2. What works well (for agent use)

- **Scannable relevance:** Overview (use cases, contraindications) makes it easy to decide “use this guide / skip” without reading the full file.
- **Clear application order:** Consensus first → then Per-source when context is known (e.g. “Google C#” codebase). Reduces ambiguity.
- **Traceability:** Sources table + optional appendix preserve where rules came from; supports re-crawl and “cite source” behavior.
- **Conflict handling:** “(Unique)” and “(Conflicts with …)” in Per-source give the agent an explicit way to prefer one source when the repo states a style (e.g. README says “Google C#”).
- **Actionable agent notes:** “When to use,” “Caveats,” “Tooling,” “Conflicts” tell the agent when and how to apply the guide and what to suggest (e.g. `dotnet format`, EditorConfig).
- **Single-file scope:** One `.ai` file per language/topic keeps context local and easy to load.

---

## 3. Gaps and improvements

- **Single-source consensus:** With only one scraped source (e.g. Google for C#), “Consensus” is effectively “that one source.” The file should state this (e.g. “Derived from the single scraped source (Google); treat as baseline until more sources are merged”). As more sources are merged, consensus should be re-derived and the note updated.
- **Guide quality rating:** Implement a small rating (e.g. 1–5 or star-like) for trustworthiness/completeness of each guide, with concrete metrics and a short synopsis of why it scored that way. Store the score and synopsis at the top of the guide (or in Overview) so agents can weight usage.
- **Appendix size and archive:** Keeping full raw scrapes in-file can make files very large. Prefer archiving raw scrapes in a **scraping archive folder** in a formatted, pruned form that is easy to traverse later; keep only the Sources table and normalized guide in the `.ai` file (or a truncated appendix plus "full scrape in archive").
- **Per-source density (codified):** Per-source subsections must stay concise: only rules that are **unique** or **conflicting**. Do not restate consensus in Per-source. This is a standing convention for all code guides.
- **Tooling links:** Include direct links to linter/formatter config (e.g. EditorConfig, StyleCop docs) for copy-paste or “suggest this config.”
- **Version/date in Overview:** Add “Style guide last updated: YYYY-MM-DD” (or “Sources last merged: …”) to Overview so agents can decide whether to suggest a refresh.
---

## 4. How to use this format to analyze and improve code style (C# and other languages)

**When asked to analyze or improve code style for a language:**

1. **Load the right guide.**
   Resolve language/framework to the corresponding `code-guide-<topic>.ai` (see `public/master/README.md` for layout). Open that file.

2. **Check relevance.**
   Read **Overview**. If the task (e.g. “backend C# service”) matches “Best for” and does not match “Avoid for,” treat the guide as applicable.

3. **Apply consensus first.**
   Use **Code guide → Consensus** as the default set of rules. When suggesting edits (formatting, naming, structure), align with these bullets. Prefer citing the guide: “Per this project’s C# style guide (consensus): ….”

4. **Apply Per-source when context is known.**
   If the repo or user states a style (e.g. “we follow Google C#” or “Microsoft conventions”), use the **Per-source** subsection for that source and prefer it where it conflicts with consensus. Label suggestions: “Per Google C# style guide: ….”

5. **Use Notes for the agent.**
   - **When to use:** Only suggest style changes when the guide is in scope (e.g. editing `.cs` files, or user asked for style).
   - **Caveats:** Do not override existing repo conventions (e.g. “legacy uses 2 spaces”) unless the user asks to modernize; prefer “new code: consensus; existing: match file.”
   - **Tooling:** Suggest enabling `dotnet format`, EditorConfig, or StyleCop when improving style, and point to the Tools line in the guide.
   - **Conflicts:** If sources disagree and the repo does not state a style, apply consensus and optionally note: “Google C# recommends X; we’re applying the shared rule Y.”

6. **Cite sources when useful.**
   For non-obvious or strict rules, cite the **Sources** table (e.g. “Google C# Style Guide”) so the user can look up the original.

7. **Refresh when appropriate.**
   If the **Sources** table shows old “Last accessed” dates or the guide is clearly outdated, suggest re-running the scrape/merge (see `code-guide-master-file.md` §3) rather than inventing rules.

---

## 5. Recommendations for future improvements

- **Merge more sources for C#:** Run crawler/merge for Microsoft and Goat C# so Consensus can be derived from multiple sources and Per-source can list real differences (e.g. Microsoft vs Google on line length or brace placement).
- **Add “Last updated” to Overview:** One line with the date of the last merge or scrape so agents can decide when to suggest a refresh.
- **Optional: separate raw scrapes:** Keep a single “Sources” table and normalized Consensus/Per-source in the `.ai` file; store full raw scrapes in `public/raw/` or similar to limit file size while preserving traceability.
- **Replicate format for other languages:** Use the C# file as the template: transform one well-populated `.ai` per language (e.g. Python, TypeScript/JS, Go) into this structure, then use this analysis doc to drive consistent behavior across languages.

---

## 6. Quick reference: file locations

| Asset | Path |
|-------|------|
| Master design | `language-style-guides/public/master/code-guide-master-file.md` |
| C# guide (transformed) | `language-style-guides/public/master/c-family/code-guide-c-sharp.ai` |
| This analysis | `ai-docs/code-guide-format-analysis.md` |
| Scrape/merge scripts | `language-style-guides/scrape_guides.py`, `merge_google_into_master.py` |

When analyzing or improving code style for a language: **open the corresponding `code-guide-<topic>.ai`, follow §4 above, and use this document for consistent interpretation of the format.**
