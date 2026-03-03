"""
Dart dev docs (dart.dev). Docs layout: main content in main, .content, or article.
"""
from bs4 import BeautifulSoup
from typing import Optional, Tuple


def extract(soup: BeautifulSoup, url: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract main content from dart.dev guide pages.
    """
    for selector in (
        "main",
        "main article",
        "article",
        "[role='main']",
        "div.content",
        "div.main-content",
        ".site-content",
    ):
        el = soup.select_one(selector)
        if el:
            text = _element_to_text(el)
            if text and len(text.strip()) > 200:
                return text.strip(), None
    body = soup.find("body")
    if body:
        for tag in body.find_all(["script", "style", "nav", "header", "footer"]):
            tag.decompose()
        text = _element_to_text(body)
        if text and len(text.strip()) > 100:
            return text.strip(), None
    return None, "Could not find main content container"


def _element_to_text(el) -> str:
    """Readable text; normalize whitespace."""
    text = el.get_text(separator="\n", strip=True)
    return "\n\n".join(p for p in text.split("\n") if p.strip())
