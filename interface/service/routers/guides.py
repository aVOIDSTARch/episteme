"""Domain router for language style guides (language-style-guides/)."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query

from cloak.auth import verify_token
from cloak.models import TokenClaims
from helpers import is_hidden, read_file_contents
import helpers
from schemas import FileContent, GuideCategorySummary, GuideSummary, SearchResult

router = APIRouter(prefix="/api/v1/framework/guides", tags=["guides"])

GUIDES_DIR = "language-style-guides"
MASTER_DIR = f"{GUIDES_DIR}/public/master"
PERSONALIZED_DIR = f"{GUIDES_DIR}/personalized"


def _master_root():
    return helpers.FRAMEWORK_ROOT / "language-style-guides" / "public" / "master"


def _personalized_root():
    return helpers.FRAMEWORK_ROOT / "language-style-guides" / "personalized"


@router.get(
    "/",
    response_model=List[GuideCategorySummary],
    operation_id="episteme_list_guide_categories",
    summary="List guide categories",
    description="Returns all category folders under the master guides directory with guide counts.",
)
def list_categories(_token=Depends(verify_token)):
    root = _master_root()
    if not root.exists():
        return []
    results = []
    for child in sorted(root.iterdir(), key=lambda c: c.name.lower()):
        if child.is_dir() and not is_hidden(child):
            guide_count = sum(
                1 for f in child.iterdir()
                if f.is_file() and not is_hidden(f)
            )
            results.append(GuideCategorySummary(
                category=child.name, guide_count=guide_count,
            ))
    return results


@router.get(
    "/search",
    response_model=List[SearchResult],
    operation_id="episteme_search_guides",
    summary="Search guides",
    description="Full-text search across all guide files.",
)
def search_guides(
    query: str = Query(..., min_length=1),
    limit: int = Query(20),
    _token=Depends(verify_token),
):
    q = query.lower()
    candidates: List[SearchResult] = []
    root = _master_root()
    if not root.exists():
        return []
    for category_dir in root.iterdir():
        if not category_dir.is_dir() or is_hidden(category_dir):
            continue
        for f in category_dir.iterdir():
            if f.is_dir() or is_hidden(f):
                continue
            rel_path = f"{MASTER_DIR}/{category_dir.name}/{f.name}"
            score = 0
            snippet = None
            if q in f.name.lower():
                score += 10
            if q in category_dir.name.lower():
                score += 5
            try:
                content = f.read_text(encoding="utf-8")
                if q in content.lower():
                    score += 20
                    idx = content.lower().find(q)
                    if idx >= 0:
                        snippet = content[max(0, idx - 40): min(len(content), idx + 120)].replace("\n", " ")
            except (UnicodeDecodeError, OSError):
                pass
            if score > 0:
                candidates.append(SearchResult(
                    path=rel_path, name=f.name, type="file",
                    snippet=snippet, score=float(score),
                ))
    candidates.sort(key=lambda r: r.score, reverse=True)
    return candidates[:limit]


@router.get(
    "/sources",
    response_model=FileContent,
    operation_id="episteme_guide_sources",
    summary="Get guide sources",
    description="Returns code-guide-sources.md documenting where guides originate.",
)
def get_sources(_token=Depends(verify_token)):
    path = f"{GUIDES_DIR}/code-guide-sources.md"
    try:
        content = read_file_contents(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Guide sources not found")
    full = helpers.FRAMEWORK_ROOT / path
    return FileContent(
        path=path, content=content, type="file",
        size=full.stat().st_size, metadata=None,
    )


@router.get(
    "/personalized",
    response_model=List[GuideSummary],
    operation_id="episteme_list_personalized_guides",
    summary="List personalized guides",
    description="Returns personalized style guide entries.",
)
def list_personalized(_token=Depends(verify_token)):
    root = _personalized_root()
    if not root.exists():
        return []
    results = []
    for child in sorted(root.iterdir(), key=lambda c: c.name.lower()):
        if is_hidden(child):
            continue
        if child.is_dir():
            for f in sorted(child.iterdir(), key=lambda c: c.name.lower()):
                if f.is_file() and not is_hidden(f):
                    results.append(GuideSummary(
                        name=f.name,
                        category=child.name,
                        path=f"{PERSONALIZED_DIR}/{child.name}/{f.name}",
                    ))
        elif child.is_file():
            results.append(GuideSummary(
                name=child.name,
                category="personalized",
                path=f"{PERSONALIZED_DIR}/{child.name}",
            ))
    return results


@router.get(
    "/personalized/{name:path}",
    response_model=FileContent,
    operation_id="episteme_get_personalized_guide",
    summary="Read a personalized guide",
    description="Returns the content of a personalized style guide.",
)
def get_personalized_guide(name: str, _token=Depends(verify_token)):
    path = f"{PERSONALIZED_DIR}/{name}"
    try:
        content = read_file_contents(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Personalized guide not found")
    full = helpers.FRAMEWORK_ROOT / path
    return FileContent(
        path=path, content=content, type="file",
        size=full.stat().st_size, metadata=None,
    )


@router.get(
    "/category/{category}",
    response_model=List[GuideSummary],
    operation_id="episteme_list_guides_by_category",
    summary="List guides in a category",
    description="Returns all guide files within a specific category folder.",
)
def list_by_category(category: str, _token=Depends(verify_token)):
    cat_dir = _master_root() / category
    if not cat_dir.exists() or not cat_dir.is_dir():
        raise HTTPException(status_code=404, detail=f"Category not found: {category}")
    results = []
    for f in sorted(cat_dir.iterdir(), key=lambda c: c.name.lower()):
        if f.is_file() and not is_hidden(f):
            results.append(GuideSummary(
                name=f.name,
                category=category,
                path=f"{MASTER_DIR}/{category}/{f.name}",
            ))
    return results


@router.get(
    "/category/{category}/{guide_name:path}",
    response_model=FileContent,
    operation_id="episteme_get_guide",
    summary="Read a specific guide",
    description="Returns the text content of a guide file (.ai files read as plain text).",
)
def get_guide(category: str, guide_name: str, _token=Depends(verify_token)):
    path = f"{MASTER_DIR}/{category}/{guide_name}"
    try:
        content = read_file_contents(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Guide not found")
    full = helpers.FRAMEWORK_ROOT / path
    return FileContent(
        path=path, content=content, type="file",
        size=full.stat().st_size, metadata=None,
    )
