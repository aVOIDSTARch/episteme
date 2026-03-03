#!/usr/bin/env python3
"""
Scrape code-guide sources from the list in sources_config.py.
Writes raw scraped content to public/<source_group>/ and a report to scrape-report-<timestamp>.md.
Usage: from language-style-guides/scripts: python scrape_guides.py
       or from repo root: python episteme-framework/language-style-guides/scripts/scrape_guides.py
"""
import os
import sys
from datetime import datetime, timezone
from typing import Optional

import requests
from bs4 import BeautifulSoup

# Allow running from script dir or repo root
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from sources_config import SOURCES, Source

# Scrapers by parser_key
from scrapers import google_styleguide, peps_python, dart_dev, android_kotlin

PARSERS = {
    "google_styleguide": google_styleguide,
    "peps_python": peps_python,
    "dart_dev": dart_dev,
    "android_kotlin": android_kotlin,
}

# Output: framework-relative
FRAMEWORK_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIRS = {
    "google_styleguide": os.path.join(FRAMEWORK_ROOT, "public", "google"),
    "peps_python": os.path.join(FRAMEWORK_ROOT, "public", "peps"),
    "dart_dev": os.path.join(FRAMEWORK_ROOT, "public", "dart"),
    "android_kotlin": os.path.join(FRAMEWORK_ROOT, "public", "android"),
}

USER_AGENT = "EpistemeCodeGuideScraper/1.0 (file-based library; no crawler)"


def fetch(url: str) -> tuple[Optional[BeautifulSoup], Optional[str]]:
    """Fetch URL and return (soup, error)."""
    try:
        r = requests.get(url, timeout=30, headers={"User-Agent": USER_AGENT})
        r.raise_for_status()
        r.encoding = r.apparent_encoding or "utf-8"
        return BeautifulSoup(r.text, "html.parser"), None
    except requests.RequestException as e:
        return None, str(e)
    except Exception as e:
        return None, str(e)


def scrape_one(source: Source) -> tuple[bool, int, Optional[str]]:
    """
    Scrape one source. Returns (success, byte_count, error_message).
    """
    parser_mod = PARSERS.get(source.parser_key)
    if not parser_mod or not hasattr(parser_mod, "extract"):
        return False, 0, f"Unknown parser: {source.parser_key}"
    soup, err = fetch(source.url)
    if err:
        return False, 0, err
    content, extract_err = parser_mod.extract(soup, source.url)
    if extract_err:
        return False, 0, extract_err
    if not content or len(content.strip()) < 50:
        return False, 0, "Extracted content too short or empty"
    # Write file
    out_dir = OUTPUT_DIRS.get(source.parser_key, os.path.join(FRAMEWORK_ROOT, "public", "other"))
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, source.slug + ".md")
    header = f"""# Scraped: {source.slug}
**Source:** {source.url}
**Fetched:** {datetime.now(timezone.utc).isoformat()}

---

"""
    body = header + content
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(body)
    return True, len(body.encode("utf-8")), None


def main() -> None:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    report_path = os.path.join(FRAMEWORK_ROOT, "scrape-report-" + timestamp + ".md")
    report_lines = [
        "# Scrape report",
        "",
        f"**Run:** {datetime.now(timezone.utc).isoformat()}",
        f"**Sources:** {len(SOURCES)}",
        "",
        "| Slug | URL | Status | Bytes | Note |",
        "|------|-----|--------|-------|------|",
    ]
    ok = 0
    fail = 0
    for source in SOURCES:
        success, size, err = scrape_one(source)
        if success:
            ok += 1
            report_lines.append(f"| {source.slug} | {source.url} | OK | {size} | |")
        else:
            fail += 1
            report_lines.append(f"| {source.slug} | {source.url} | FAIL | 0 | {err or 'unknown'} |")
    report_lines.extend([
        "",
        "---",
        f"**Summary:** {ok} OK, {fail} failed.",
    ])
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    print(f"Report written to {report_path}")
    print(f"OK: {ok}, Failed: {fail}")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
