"""
Google Style Guide (google.github.io/styleguide/*).
Single-page HTML; main content is typically in a devsite or content wrapper.
"""
from bs4 import BeautifulSoup
from typing import Optional, Tuple


def extract(soup: BeautifulSoup, url: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract main prose from a Google style guide page.
    Tries: devsite-content, devsite-article-body, main, article, then body.
    """
    # Google's devsite layout: content often in devsite-article-body or devsite-content
    for selector in (
        "div#devsite-article-body",
        "div.devsite-article-body",
        "div#devsite-content",
        "main",
        "article",
        "div.content",
        "div#content",
    ):
        el = soup.select_one(selector)
        if el:
            text = _element_to_text(el)
            if text and len(text.strip()) > 200:
                return text.strip(), None
    # Fallback: body, but strip nav/footer by removing script/style and common nav IDs
    body = soup.find("body")
    if body:
        for tag in body.find_all(["script", "style", "nav", "header", "footer"]):
            tag.decompose()
        for sel in ["#devsite-header", ".devsite-nav", ".devsite-footer", ".navigation"]:
            for t in body.select(sel):
                t.decompose()
        text = _element_to_text(body)
        if text and len(text.strip()) > 100:
            return text.strip(), None
    return None, "Could not find main content container"


def _element_to_text(el) -> str:
    """Get readable text; normalize whitespace."""
    text = el.get_text(separator="\n", strip=True)
    return "\n\n".join(p for p in text.split("\n") if p.strip())
