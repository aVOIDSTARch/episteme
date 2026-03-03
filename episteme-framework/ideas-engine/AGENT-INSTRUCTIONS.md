# Agent instructions: Ideas System

**Purpose:** Step-by-step instructions for agents implementing `/ideas` and `/add-idea`. Use with [README.md](README.md) and [_idea-file-schema.md](_idea-file-schema.md).

---

## Resolving the Ideas root

1. If the user or project sets `IDEAS_ROOT`, use that directory.
2. Otherwise use `~/ideas/` (user home + `ideas`).
3. If the directory does not exist, offer to create it (and optionally add a first topic from `template-topic.md`).

---

## `/ideas` — implementation

1. **Scan** the Ideas root for all `*.md` files. Ignore non-markdown files and optional internal files (e.g. `README.md` in that folder if present).
2. **Build menu:** List topic names. Derive each name from the first `# ` heading in the file, or from the filename (strip `.md`, replace `-` with spaces, title-case if desired).
3. **On user selection:** Open that topic file and display each idea entry (Verbatim + Claude/Agent interpretation). Preserve order (top to bottom = oldest to newest unless schema says otherwise).
4. **Offer actions:**
   - **Synthesize** — Use extended thinking to generate 10–15 project ideas that combine or build on the ideas in this topic. Present the list inline (numbered, short titles + one-line description). Then offer “Return to topic list” or “Return to prompt”.
   - **Return to topic list** — Go back to the list of topics.
   - **Return to prompt** — Exit to normal chat.
5. Use menus (e.g. `AskUserQuestion` or equivalent) when available; always include “Return to prompt”.

---

## `/add-idea <text>` — implementation

1. **Capture text:** Everything after `/add-idea` is the raw idea text. Trim leading/trailing whitespace but do not alter the wording (it becomes **Verbatim**).
2. **Match or create topic:**
   - If there are existing topic files, infer the best-matching topic from filename/heading and content (e.g. keywords). Propose that topic.
   - If none fits, propose a new topic name (slug form: `lowercase-with-hyphens.md`). **Confirm with the user** before creating a new file.
3. **Append entry** to the chosen topic file:
   - Add a separator `---` if the file already has content.
   - Add a level-2 heading (e.g. `## Entry N` where N = next sequential number, or a short slug).
   - Add `**Verbatim:** "<exact text>"` (escape internal quotes if needed).
   - Add `**Claude:**` (or `**Agent:**`) followed by your interpretation: implications, connections to other ideas in that file, and optionally to other topics.
   - Optionally add `id: N` and `created_at: <ISO 8601>` on the next line.
4. **Confirm:** Tell the user which file was updated and show the new entry (or a one-line summary). Ask if they want to add another or return to prompt.

---

## Topic merge/split (occasional)

- **Not every session.** Periodically (e.g. when the user asks, or when you notice many similar topics), suggest:
  - **Merge:** Two or more topics that have grown similar could be combined into one file. Propose which; get approval; create merged file and optionally move/archive old files.
  - **Split:** A topic that has become very broad could be split into two files. Propose which entries go where; get approval; create new files and optionally archive the old one.
- Never rewrite or delete existing entries; only reorganize by creating new files and (if desired) archiving.

---

## When Ideas root is missing or empty

- If `~/ideas/` (or `IDEAS_ROOT`) does not exist: offer to create it and add a first topic (e.g. “general” or a topic name the user provides), using the structure in [template-topic.md](template-topic.md).
- If the directory exists but has no `*.md` files: offer to create the first topic from `/add-idea` text, or suggest the user run `/add-idea` with their first idea.
