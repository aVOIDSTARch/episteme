#!/usr/bin/env python3
"""
Crawl style-guide URLs from each code-guide-*.ai in master/, append scraped content
as new sections (one per source) with timestamp. Resumable via scrape.md state.
Uses stdlib only (urllib, html.parser, re) - no pip install required.
"""
from __future__ import annotations

import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
from datetime import datetime, timezone
import time

MASTER_DIR = Path(__file__).resolve().parent / "public" / "master"
DELAY_SECONDS = 1.0  # Be polite between requests
SCRAPE_MD = Path(__file__).resolve().parent / "scrape.md"
REQUEST_TIMEOUT = 30
REQUEST_HEADERS = {"User-Agent": "EpistemeStyleGuideCrawler/1.0 (resumable scrape)"}
def extract_links_from_section(content: str) -> list[tuple[str, str]]:
    """Parse 'Style guide sources' section; return list of (title, url)."""
    links = []
    in_section = False
    link_re = re.compile(r"^\s*-\s*\[([^\]]+)\]\((https?://[^)\s]+)\)", re.I)
    for line in content.splitlines():
        if "Style guide sources" in line and "##" in line:
            in_section = True
            continue
        if in_section and line.strip().startswith("---"):
            break
        if in_section:
            m = link_re.match(line)
            if m:
                title, url = m.groups()
                links.append((title, url.rstrip(".)")))
    return links


def already_crawled(content: str, url: str) -> bool:
    """True if this URL already has a 'Crawled:' block in the file."""
    return url in content and "Crawled:" in content


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = False
        self.text_parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "header", "footer"):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "header", "footer"):
            self.skip = False
        if tag in ("p", "div", "li", "br", "h1", "h2", "h3", "h4", "h5", "h6", "tr"):
            self.text_parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.text_parts.append(data)

    def get_text(self) -> str:
        s = "".join(self.text_parts)
        return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", s)).strip()


def fetch_and_extract_text(url: str) -> str:
    req = Request(url, headers=REQUEST_HEADERS)
    with urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
        raw = resp.read()
        try:
            charset = resp.headers.get_content_charset() or "utf-8"
            html = raw.decode(charset, errors="replace")
        except Exception:
            html = raw.decode("utf-8", errors="replace")
    parser = TextExtractor()
    parser.feed(html)
    return parser.get_text()


def append_scraped_section(filepath: Path, title: str, url: str, text: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    block = f"\n\n---\n\n## Source: {title}\n\n**URL:** {url}  \n**Crawled:** {now}\n\n```\n{text[:500000]}\n```\n"
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(block)


def load_state() -> dict:
    if not SCRAPE_MD.exists():
        return {"completed": [], "last_file": None, "last_url_index": None, "errors": []}
    state = {"completed": [], "last_file": None, "last_url_index": None, "errors": []}
    with open(SCRAPE_MD, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("- DONE:"):
                state["completed"].append(line.replace("- DONE:", "").strip())
            elif line.startswith("LAST_FILE:"):
                state["last_file"] = line.replace("LAST_FILE:", "").strip()
            elif line.startswith("LAST_URL_INDEX:"):
                try:
                    state["last_url_index"] = int(line.split(":")[1].strip())
                except ValueError:
                    pass
            elif line.startswith("ERROR:"):
                state["errors"].append(line.replace("ERROR:", "").strip())
    return state


def save_state(completed: list[str], last_file: str | None, last_url_index: int | None, errors: list[str]) -> None:
    with open(SCRAPE_MD, "w", encoding="utf-8") as f:
        f.write(f"# Scrape progress\n\nLast updated: {datetime.now(timezone.utc).isoformat()}\n\n")
        f.write("## Completed (file + URL)\n\n")
        for c in completed:
            f.write(f"- DONE: {c}\n")
        f.write("\n## Resume here\n\n")
        f.write(f"LAST_FILE: {last_file or ''}\n")
        f.write(f"LAST_URL_INDEX: {last_url_index if last_url_index is not None else ''}\n")
        if errors:
            f.write("\n## Errors\n\n")
            for e in errors[-50:]:
                f.write(f"- ERROR: {e}\n")


def main() -> None:
    os.chdir(Path(__file__).resolve().parent)
    state = load_state()
    completed_set = set(state["completed"])
    errors = list(state.get("errors") or [])
    ai_files = sorted(MASTER_DIR.rglob("code-guide-*.ai"))
    if not ai_files:
        print("No code-guide-*.ai files found under", MASTER_DIR, file=sys.stderr)
        sys.exit(1)

    started_after_last = not (state.get("last_file") or "").strip()
    for filepath in ai_files:
        rel = filepath.relative_to(MASTER_DIR)
        if not started_after_last:
            if str(rel) != (state.get("last_file") or "").strip():
                continue
            started_after_last = True
        content = filepath.read_text(encoding="utf-8")
        links = extract_links_from_section(content)
        start_idx = 0
        if str(rel) == state["last_file"] and state.get("last_url_index") is not None:
            start_idx = state["last_url_index"] + 1
        for i, (title, url) in enumerate(links):
            if i < start_idx:
                continue
            key = f"{rel} | {url}"
            if key in completed_set:
                continue
            if already_crawled(content, url):
                completed_set.add(key)
                continue
            time.sleep(DELAY_SECONDS)
            try:
                text = fetch_and_extract_text(url)
                append_scraped_section(filepath, title, url, text)
                content = filepath.read_text(encoding="utf-8")
                completed_set.add(key)
                state["completed"] = list(completed_set)
                state["last_file"] = str(rel)
                state["last_url_index"] = i
                save_state(state["completed"], state["last_file"], state["last_url_index"], errors)
                print(f"OK {rel} | {url[:60]}...")
            except (HTTPError, URLError, TimeoutError, Exception) as e:
                err_msg = f"{rel} | {url} | {e!r}"
                errors.append(err_msg)
                save_state(state["completed"], state["last_file"], state["last_url_index"], errors)
                print(f"SKIP {err_msg}", file=sys.stderr)
        state["last_url_index"] = None
    save_state(state["completed"], None, None, errors)
    print("Done.")


if __name__ == "__main__":
    main()
