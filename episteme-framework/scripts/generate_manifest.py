#!/usr/bin/env python3
"""
Generate MANIFEST.md: programmatic list of all _*.md, SKILL.md, code-guide-*.ai
in the episteme-framework. Run from repo root or from episteme-framework/.
Output: episteme-framework/MANIFEST.md
"""
from pathlib import Path

# Framework root = parent of scripts/
FRAMEWORK_ROOT = Path(__file__).resolve().parent.parent

def main():
    root = FRAMEWORK_ROOT
    underscore_md = sorted(p.relative_to(root) for p in root.rglob("_*.md"))
    skill_md = sorted(p.relative_to(root) for p in root.rglob("SKILL.md"))
    code_guides = sorted(p.relative_to(root) for p in root.rglob("code-guide-*.ai"))

    lines = [
        "# Library assets manifest",
        "",
        "**Purpose:** Programmatic list of schema docs (_*.md), skills (SKILL.md), and code guides (code-guide-*.ai). Regenerate with: `python episteme-framework/scripts/generate_manifest.py` from repo root.",
        "",
        "---",
        "",
        "## Leading-underscore docs (_*.md)",
        "",
    ]
    for p in underscore_md:
        lines.append(f"- {p.as_posix()}")
    lines.extend([
        "",
        "## Skill definitions (SKILL.md)",
        "",
    ])
    for p in skill_md:
        lines.append(f"- {p.as_posix()}")
    lines.extend([
        "",
        "## Code guides (code-guide-*.ai)",
        "",
    ])
    for p in code_guides:
        lines.append(f"- {p.as_posix()}")
    lines.extend([
        "",
        "---",
        f"*Generated: {len(underscore_md)} _*.md, {len(skill_md)} SKILL.md, {len(code_guides)} code-guide-*.ai*",
    ])

    out = root / "MANIFEST.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(underscore_md)} _*.md, {len(skill_md)} SKILL.md, {len(code_guides)} code-guide-*.ai)")


if __name__ == "__main__":
    main()
