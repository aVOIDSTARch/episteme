"""
PEP pages (peps.python.org). Sphinx-generated; main content in .document or .body.
"""
from bs4 import BeautifulSoup
from typing import Optional, Tuple


def extract(soup: BeautifulSoup, url: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract main content from a PEP page.
    peps.python.org uses Sphinx; content is typically in div.document or div.body or main.
    """
    for selector in (
        "div.document",
        "div.body",
        "main",
        "article",
        "div#pep-content",
        "div.content",
        "#content .document",
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
