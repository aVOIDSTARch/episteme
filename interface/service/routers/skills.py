"""Domain router for episteme skills (my-skills/episteme-skills/)."""

import re
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from cloak.auth import verify_token
from cloak.models import TokenClaims
from helpers import FRAMEWORK_ROOT, is_hidden, list_dir, read_file_contents
import helpers
from schemas import FileContent, FileNode, SearchResult, SkillDetail, SkillSummary

router = APIRouter(prefix="/api/v1/framework/skills", tags=["skills"])

SKILLS_DIR = "my-skills/episteme-skills"
SKILLS_INDEX = "my-skills/000-my-skills-index.md"
SKILL_DEFINITION_DIR = "my-skills/skill-definition"


def _skills_root():
    return helpers.FRAMEWORK_ROOT / "my-skills" / "episteme-skills"


def _parse_skill_md(content: str) -> dict:
    """Parse a SKILL.md file into sections keyed by ## headings."""
    sections = {}
    current_key = None
    current_lines = []

    for line in content.splitlines():
        match = re.match(r"^##\s+(.+)$", line)
        if match:
            if current_key is not None:
                sections[current_key] = "\n".join(current_lines).strip()
            current_key = match.group(1).strip().lower()
            current_lines = []
        else:
            current_lines.append(line)

    if current_key is not None:
        sections[current_key] = "\n".join(current_lines).strip()

    return sections


def _list_skill_folders() -> List[str]:
    """Return sorted list of skill folder names (uppercase dirs with SKILL.md)."""
    root = _skills_root()
    if not root.exists():
        return []
    folders = []
    for child in sorted(root.iterdir(), key=lambda c: c.name):
        if child.is_dir() and not is_hidden(child) and (child / "SKILL.md").exists():
            folders.append(child.name)
    return folders


@router.get(
    "/",
    response_model=List[SkillSummary],
    operation_id="episteme_list_skills",
    summary="List all skills",
    description="Returns all skills with name, trigger, and tags parsed from SKILL.md.",
)
def list_skills(_token: TokenClaims = Depends(verify_token)):
    results = []
    for folder_name in _list_skill_folders():
        skill_path = f"{SKILLS_DIR}/{folder_name}/SKILL.md"
        try:
            content = read_file_contents(skill_path)
            sections = _parse_skill_md(content)
            results.append(SkillSummary(
                name=sections.get("name", folder_name),
                folder=folder_name,
                tags=None,
                trigger=sections.get("when to use"),
            ))
        except Exception:
            results.append(SkillSummary(name=folder_name, folder=folder_name))
    return results


@router.get(
    "/search",
    response_model=List[SearchResult],
    operation_id="episteme_search_skills",
    summary="Search skills",
    description="Search skills by name, content, or trigger description.",
)
def search_skills(
    query: str = Query(..., min_length=1, description="Search query"),
    limit: int = Query(20, description="Max results"),
    _token: TokenClaims = Depends(verify_token),
):
    q = query.lower()
    candidates: List[SearchResult] = []
    for folder_name in _list_skill_folders():
        skill_path = f"{SKILLS_DIR}/{folder_name}/SKILL.md"
        score = 0
        snippet = None
        if q in folder_name.lower():
            score += 10
        try:
            content = read_file_contents(skill_path)
            if q in content.lower():
                score += 20
                idx = content.lower().find(q)
                if idx >= 0:
                    snippet = content[max(0, idx - 40): min(len(content), idx + 120)].replace("\n", " ")
        except Exception:
            pass
        if score > 0:
            candidates.append(SearchResult(
                path=skill_path, name=folder_name, type="file",
                snippet=snippet, score=float(score),
            ))
    candidates.sort(key=lambda r: r.score, reverse=True)
    return candidates[:limit]


@router.get(
    "/definition",
    response_model=FileContent,
    operation_id="episteme_skill_definition",
    summary="Get skill definition standard",
    description="Returns the skill-definition standard document.",
)
def get_skill_definition(_token: TokenClaims = Depends(verify_token)):
    def_index = f"{SKILL_DEFINITION_DIR}/_skill-definition.md"
    try:
        content = read_file_contents(def_index)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Skill definition not found")
    full_path = helpers.FRAMEWORK_ROOT / def_index
    return FileContent(
        path=def_index, content=content, type="file",
        size=full_path.stat().st_size, metadata=None,
    )


@router.get(
    "/index",
    response_model=FileContent,
    operation_id="episteme_skills_index",
    summary="Get skills index",
    description="Returns the master skills index file (000-my-skills-index.md).",
)
def get_skills_index(_token: TokenClaims = Depends(verify_token)):
    try:
        content = read_file_contents(SKILLS_INDEX)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Skills index not found")
    full_path = helpers.FRAMEWORK_ROOT / SKILLS_INDEX
    return FileContent(
        path=SKILLS_INDEX, content=content, type="file",
        size=full_path.stat().st_size, metadata=None,
    )


@router.get(
    "/{skill_name}",
    response_model=SkillDetail,
    operation_id="episteme_get_skill",
    summary="Get a specific skill",
    description="Returns full SKILL.md content with parsed sections for a skill.",
)
def get_skill(skill_name: str, _token: TokenClaims = Depends(verify_token)):
    skill_path = f"{SKILLS_DIR}/{skill_name}/SKILL.md"
    try:
        content = read_file_contents(skill_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Skill not found: {skill_name}")
    sections = _parse_skill_md(content)
    # Body is everything after the first heading
    lines = content.splitlines()
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("## "):
            body_start = i
            break
    body = "\n".join(lines[body_start:]).strip()
    return SkillDetail(
        name=sections.get("name", skill_name),
        folder=skill_name,
        metadata=sections,
        body=body,
        raw=content,
    )


@router.get(
    "/{skill_name}/tree",
    response_model=List[FileNode],
    operation_id="episteme_skill_tree",
    summary="List files in a skill folder",
    description="Returns all files in a specific skill's directory.",
)
def get_skill_tree(skill_name: str, _token: TokenClaims = Depends(verify_token)):
    skill_dir = f"{SKILLS_DIR}/{skill_name}"
    try:
        return list_dir(skill_dir)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Skill not found: {skill_name}")
