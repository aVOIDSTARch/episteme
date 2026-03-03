#!/usr/bin/env python3
"""
Clean scraped content in code-guide-*.ai: trim whitespace, collapse blank lines.
Produce scrape-report.md with: success list, failed/trash list with reasons.
"""
import re
from pathlib import Path

MASTER_DIR = Path(__file__).resolve().parent / "public" / "master"
SCRAPE_MD = Path(__file__).resolve().parent / "scrape.md"
REPORT_MD = Path(__file__).resolve().parent / "scrape-report.md"

# Min chars (after trim) to consider content "substantive" (else flag as low-value)
MIN_SUBSTANTIVE_CHARS = 300


def is_low_value_url(url: str, content_len: int) -> bool:
    """True if URL is an index/listing page or content is very short."""
    if content_len < MIN_SUBSTANTIVE_CHARS:
        return True
    # Repo index (README only, no specific file)
    if "github.com/Kristories/awesome-guidelines" in url and "/blob/" not in url and "/tree/" not in url:
        return True
    # Project Rules site index (no specific guide path)
    if "projectrules.ai" in url and url.rstrip("/").endswith("projectrules.ai"):
        return True
    return False


def clean_block(text: str) -> str:
    """Collapse whitespace, trim lines, max 2 consecutive newlines."""
    lines = [line.rstrip() for line in text.splitlines()]
    out = []
    prev_blank = False
    for line in lines:
        is_blank = not line.strip()
        if is_blank:
            if not prev_blank:
                out.append("")
            prev_blank = True
        else:
            out.append(line)
            prev_blank = False
    return "\n".join(out).strip()


def process_ai_file(filepath: Path) -> tuple[bool, list[str]]:
    """
    Rewrite file with cleaned source blocks. Return (has_any_content, list of low_value_urls).
    """
    raw = filepath.read_text(encoding="utf-8")
    low_value = []
    parts = re.split(r"\n(?=## Source: )", raw)
    if len(parts) <= 1:
        return False, []
    header = parts[0].rstrip()
    new_parts = [header]
    for block in parts[1:]:
        # Find ```\n ... \n``` (first code block after Crawled:)
        idx = block.find("\n```\n")
        if idx == -1:
            new_parts.append(block)
            continue
        end_idx = block.find("\n```", idx + 5)
        if end_idx == -1:
            new_parts.append(block)
            continue
        head = block[:idx]
        content = block[idx + 5 : end_idx]
        tail = block[end_idx:]
        # Parse URL from head ( **URL:** ... )
        url = ""
        for line in head.splitlines():
            if line.strip().startswith("**URL:**"):
                url = line.strip().replace("**URL:**", "").strip().rstrip()
                break
        content_cleaned = clean_block(content)
        if is_low_value_url(url, len(content_cleaned)):
            low_value.append(url)
        new_parts.append(head + "\n```\n" + content_cleaned + tail)
    filepath.write_text("\n\n---\n\n".join(new_parts) + "\n", encoding="utf-8")
    has_content = len(parts) > 1
    return has_content, low_value


def parse_scrape_md() -> tuple[set[str], list[tuple[str, str]]]:
    """Return (set of completed file paths from DONE, list of (file | url, reason) for errors)."""
    completed_files = set()
    errors = []
    if not SCRAPE_MD.exists():
        return completed_files, errors
    in_errors = False
    for line in SCRAPE_MD.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s == "## Errors":
            in_errors = True
            continue
        if in_errors and s.startswith("- ERROR:"):
            rest = s.replace("- ERROR:", "").strip()
            if " | " in rest:
                file_url, reason = rest.rsplit(" | ", 1)
                errors.append((file_url, reason))
        elif not in_errors and s.startswith("- DONE:"):
            rest = s.replace("- DONE:", "").strip()
            if " | " in rest:
                completed_files.add(rest.split(" | ")[0].strip())
    return completed_files, errors


def main():
    # 1. Parse scrape.md for errors and completed files
    completed_files, error_list = parse_scrape_md()
    all_ai = sorted(MASTER_DIR.rglob("code-guide-*.ai"))
    success_files = set()
    low_value_by_file = {}
    # 2. Clean each .ai file and note which have substantive content / low-value sources
    for filepath in all_ai:
        rel = filepath.relative_to(MASTER_DIR)
        if not filepath.read_text().count("## Source:"):
            continue
        has_content, low_value = process_ai_file(filepath)
        success_files.add(str(rel))
        if low_value:
            low_value_by_file[str(rel)] = low_value
    # 3. Build report
    failed_unique = []
    for file_url, reason in error_list:
        failed_unique.append((file_url, reason))
    # Dedupe by file+url
    failed_dedup = list({(f, r) for f, r in failed_unique})
    lines = [
        "# Scrape report",
        "",
        "Generated after cleaning scraped content (trim whitespace, collapse blank lines).",
        "",
        "---",
        "",
        "## Successfully scraped files",
        "",
        "Files that have at least one scraped source block (and were cleaned):",
        "",
    ]
    for f in sorted(success_files):
        lines.append(f"- `{f}`")
    lines.append("")
    lines.append(f"Total: {len(success_files)} files. (Files with at least one scraped source block.)")
    lines.extend([
        "",
        "---",
        "",
        "## Failed or could not access",
        "",
        "URLs that returned HTTP errors or could not be fetched. Fix links or retry.",
        "",
    ])
    for file_url, reason in sorted(failed_dedup, key=lambda x: x[0]):
        lines.append(f"- **{file_url}**  ")
        lines.append(f"  Reason: `{reason}`")
        lines.append("")
    lines.extend([
        "---",
        "",
        "## Low-value / index pages (scraped but likely off-topic or listing only)",
        "",
        "These URLs were successfully fetched but are index/listing pages or very short content. Consider replacing with direct style-guide links.",
        "",
    ])
    for rel in sorted(low_value_by_file):
        lines.append(f"- **{rel}**")
        for url in low_value_by_file[rel][:10]:
            lines.append(f"  - {url}")
        if len(low_value_by_file[rel]) > 10:
            lines.append(f"  - ... and {len(low_value_by_file[rel]) - 10} more")
        lines.append("")
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote", REPORT_MD)
    print("Success files:", len(success_files))
    print("Failed entries:", len(failed_dedup))
    print("Files with low-value sources:", len(low_value_by_file))


if __name__ == "__main__":
    main()
