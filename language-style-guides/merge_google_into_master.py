#!/usr/bin/env python3
"""
Merge content from language-style-guides/public/google/*.md into the
corresponding code-guide-*.ai files under public/master/. Skip if that
Google URL already exists as a ## Source in the .ai file. Mark Google
files as processed in google/PROCESSED.md.
"""
import re
from pathlib import Path
from datetime import datetime, timezone

GOOGLE_DIR = Path(__file__).resolve().parent / "public" / "google"
MASTER_DIR = Path(__file__).resolve().parent / "public" / "master"

# (google .md basename without .md, master path relative to master/, Google source URL fragment)
GOOGLE_TO_MASTER = [
    ("python", "scripting-dynamic/code-guide-python.ai", "pyguide.html"),
    ("cpp", "c-family/code-guide-c-plus-plus.ai", "cppguide.html"),
    ("csharp", "c-family/code-guide-c-sharp.ai", "csharp-style.html"),
    ("java", "jvm-languages/code-guide-java.ai", "javaguide.html"),
    ("javascript", "typescript-javascript/code-guide-ts-js.ai", "jsguide.html"),
    ("typescript", "typescript-javascript/code-guide-ts-js.ai", "tsguide.html"),
    ("shell", "tooling/code-guide-shell.ai", "shellguide.html"),
    ("r", "data-science/code-guide-r.ai", "Rguide.html"),
    ("markdown", "markup-and-data/code-guide-markdown.ai", "docguide/style.html"),
    ("htmlcss", "markup-and-data/code-guide-web.ai", "htmlcssguide.html"),
    ("objective-c", "c-family/code-guide-objective-c.ai", "objcguide.html"),
    ("angularjs", "frontend-frameworks/code-guide-angular.ai", "angularjs-google-style.html"),
    ("go", "systems-languages/code-guide-go.ai", "google.github.io/styleguide/go"),
]


def already_has_google_source(ai_content: str, url_fragment: str) -> bool:
    """True if .ai file already has a ## Source block with this Google URL."""
    return url_fragment in ai_content and "**Crawled:**" in ai_content


def strip_google_md_header(text: str, source_url: str) -> str:
    """Remove first line like 'Content from ...' or 'styleguide | ...' and excessive leading newlines."""
    lines = text.strip().splitlines()
    while lines and (
        lines[0].startswith("Content from ") or
        "styleguide" in lines[0].lower() and "|" in lines[0] or
        not lines[0].strip()
    ):
        lines.pop(0)
    return "\n".join(lines).strip()


def main():
    processed = []
    for google_basename, master_rel, url_fragment in GOOGLE_TO_MASTER:
        google_path = GOOGLE_DIR / f"{google_basename}.md"
        master_path = MASTER_DIR / master_rel
        if not google_path.exists():
            processed.append((google_basename, "skip", "file not found"))
            continue
        if not master_path.exists():
            processed.append((google_basename, "skip", f"master {master_rel} not found"))
            continue
        ai_content = master_path.read_text(encoding="utf-8")
        if already_has_google_source(ai_content, url_fragment):
            processed.append((google_basename, "already_present", master_rel))
            # Still mark as processed
            continue
        body = google_path.read_text(encoding="utf-8")
        body = strip_google_md_header(body, url_fragment)
        # Build canonical Google URL
        if url_fragment.startswith("http"):
            full_url = url_fragment
        else:
            full_url = f"https://google.github.io/styleguide/{url_fragment}"
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        title = f"Google {google_basename.replace('-', ' ').title()} Style Guide (merged from google/)"
        block = f"\n\n---\n\n## Source: {title}\n\n**URL:** {full_url}  \n**Crawled:** {now} (merged from public/google/{google_basename}.md)\n\n```\n{body[:500000]}\n```\n"
        master_path.write_text(ai_content + block, encoding="utf-8")
        processed.append((google_basename, "merged", master_rel))
    # Write PROCESSED.md in google folder
    lines = [
        "# Processed: Google style files",
        "",
        "These files have been merged into the corresponding `public/master/` code-guide-*.ai files or were already present there.",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        "| Google file | Status | Master file |",
        "|-------------|--------|-------------|",
    ]
    for name, status, detail in processed:
        lines.append(f"| {name}.md | {status} | {detail} |")
    (GOOGLE_DIR / "PROCESSED.md").write_text("\n".join(lines), encoding="utf-8")
    # Prepend "Processed" note to each Google .md so it's visible when opening the file
    processed_note = "<!-- Processed: content merged or already in master; see google/PROCESSED.md -->\n\n"
    for google_basename, _, _ in GOOGLE_TO_MASTER:
        p = GOOGLE_DIR / f"{google_basename}.md"
        if p.exists() and not p.read_text(encoding="utf-8").strip().startswith("<!-- Processed:"):
            p.write_text(processed_note + p.read_text(encoding="utf-8"), encoding="utf-8")
    print("Processed:", processed)
    print("Wrote", GOOGLE_DIR / "PROCESSED.md")


if __name__ == "__main__":
    main()
