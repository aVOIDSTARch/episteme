# Episteme skills: map

Hierarchy of episteme-native skills. Top-level = orchestration; leaves = single-purpose. Each skill’s `SKILL.md` lists **REQUIRED_SKILLS** (children) when it composes others.

---

## Tree

```
MANAGE_PROJECT ✅  
├── SETUP_NEW_PROJECT ✅  
│   ├── GATHER_PROJECT_DATA ✅  
│   │   ├── GET_USER_INPUT_FOR_NEW_PROJECT ✅  
│   │   ├── CONFIRM_AGENT_OBSERVED_DATA ✅  
│   │   └── RESOLVE_PROJECT_NAME_AND_STACK ✅  
│   ├── WRITE_PROJECT_SCHEMA ✅  
│   └── (optional) SET_UP_ENVIRONMENT ✅  
├── CREATE_PLANNING_DOC ✅  
├── UPDATE_PROGRESS_DOC ✅  
├── CLOSE_PROJECT ✅  
│   ├── WRITE_COMPLETED_REPORT ✅  
│   └── WRITE_AFTER_ACTION ✅  
└── (optional) TRACKING_SYSTEM_COMPLIANCE ✅  

BUILD_LANG_GUIDES_COLLECTION ✅  
├── NAVIGATE_TO_LANG_GUIDE ✅  
├── CONFIRM_LANG_GUIDE_MATCH ✅  
├── APPLY_CODE_GUIDE_TO_CONTEXT ✅  
│   ├── APPLY_CONSENSUS_RULES ✅  
│   └── APPLY_PER_SOURCE_RULES_IF_KNOWN ✅  
├── TRANSFORM_RAW_GUIDE_TO_MASTER_FORMAT ✅  
├── SCORE_OR_RESCORE_GUIDE_QUALITY ✅  
└── (scripts) scrape_guides / merge_google / clean_and_report

MANAGE_IDEAS ✅  
├── LIST_IDEAS_TOPICS ✅  
├── SHOW_IDEAS_TOPIC_ENTRIES ✅  
├── ADD_IDEA ✅  
│   ├── MATCH_OR_CREATE_TOPIC ✅  
│   ├── APPEND_VERBATIM_AND_INTERPRETATION ✅  
│   └── CONFIRM_ADD ✅  
├── SYNTHESIZE_TOPIC_TO_PROJECT_IDEAS ✅  
└── (optional) SUGGEST_TOPIC_MERGE_OR_SPLIT

META_AGENT_NAVIGATION ✅  
├── SHOW_MENU ✅  
├── HANDLE_INCOMPLETES ✅  
├── HANDLE_DO_MORE ✅  
├── HANDLE_WHATS_NEXT ✅  
└── HANDLE_IDEAS_SUBMENU  →  MANAGE_IDEAS ✅  

MANAGE_SKILLS ✅  
├── CREATE_OR_VALIDATE_SKILL ✅  
│   ├── READ_SKILL_DEFINITION_AND_STANDARD ✅  
│   ├── GATHER_SKILL_METADATA ✅  
│   └── WRITE_OR_VALIDATE_SKILL_FOLDER ✅  
├── IMPORTED_SKILL_META_DOC ✅  
│   ├── ASSESS_SKILL_RISK ✅  
│   └── WRITE_META_DOC ✅  
├── EPISTEME_SKILL_SCAFFOLD ✅  
├── (future) SKILL_INTEGRITY_CHECK ✅  
└── (future) SKILL_STANDARD_SYNC ✅  

EPISTEME_DESIGN ✅  
├── READ_DOCS_DESIGN_LANGUAGE ✅  
└── CREATE_OR_VALIDATE_UNDERSCORE_DOC ✅  

ONBOARD_AGENT_TO_EPISTEME ✅  
├── INTRO_TO_EPISTEME ✅  
└── ORIENT_TO_CURRENT_PROJECT ✅  
```

---

## Legend

| Symbol / term | Meaning |
|--------------|---------|
| **✅** | Skill has a `SKILL.md` in this folder. |
| **(optional)** | May be skipped in some flows; parent skill can run without it. |
| **(future)** | Planned; not yet implemented. |
| **(scripts)** | Done by scripts or external tools, not a SKILL.md. |
| **→** | Delegates to another skill (e.g. submenu). |

---

## Flat list (name and purpose)

| Skill | Purpose |
|-------|---------|
| MANAGE_PROJECT | Full project lifecycle: start, plan, progress, close, optional compliance. |
| SETUP_NEW_PROJECT | Create project schema and optionally env; may lead to planning doc. |
| GATHER_PROJECT_DATA | Collect required/optional schema fields from user and context. |
| GET_USER_INPUT_FOR_NEW_PROJECT | Elicit user-supplied fields (name, summary, owner, type, stack, deployment, constraints). |
| CONFIRM_AGENT_OBSERVED_DATA | Present inferred dev env / agents; user confirms or corrects. |
| RESOLVE_PROJECT_NAME_AND_STACK | Suggest name/slug or stack from description; user picks or edits. |
| WRITE_PROJECT_SCHEMA | Write schema file to 01-project-schemas per _project-schema. |
| SET_UP_ENVIRONMENT | Set up runtimes, tooling (Node, pnpm, etc.); deferrable from SETUP_NEW_PROJECT. |
| CREATE_PLANNING_DOC | Create 002 planning doc from schema + discussion; phased plan, addenda. |
| UPDATE_PROGRESS_DOC | Update 003 progress: stages completed, commits, tests, what to do next. |
| CLOSE_PROJECT | Move to completed folder; write 004 completed report. |
| WRITE_COMPLETED_REPORT | Fill completed report from plan + progress + outcomes. |
| WRITE_AFTER_ACTION | From completed report + plan: improvements, related projects, new SKILLs. |
| TRACKING_SYSTEM_COMPLIANCE | Check 001–005 docs vs _docs; report compliance. |
| BUILD_LANG_GUIDES_COLLECTION | Ensure language guides exist, transformed, scored; orchestrate navigate/apply/transform. |
| NAVIGATE_TO_LANG_GUIDE | Resolve language/framework to code-guide-&lt;topic&gt;.ai path (master layout). |
| CONFIRM_LANG_GUIDE_MATCH | Check Overview relevance (use cases, contraindications) for current task. |
| APPLY_CODE_GUIDE_TO_CONTEXT | Apply consensus first; then per-source if repo style known; cite sources. |
| APPLY_CONSENSUS_RULES | Apply Consensus subsection of code guide to edits. |
| APPLY_PER_SOURCE_RULES_IF_KNOWN | If repo states a style (e.g. Google C#), apply that Per-source subsection. |
| TRANSFORM_RAW_GUIDE_TO_MASTER_FORMAT | Turn raw scraped guide into Overview, Sources, Consensus, Per-source, Notes, Appendix. |
| SCORE_OR_RESCORE_GUIDE_QUALITY | Set or update 1–5 (or star) + synopsis at top of Overview. |
| MANAGE_IDEAS | Ideas system: list topics, show entries, add idea, synthesize. |
| LIST_IDEAS_TOPICS | Scan Ideas root; present topic names (from filename or first #). |
| SHOW_IDEAS_TOPIC_ENTRIES | Show Verbatim + interpretation for selected topic file. |
| ADD_IDEA | Match or create topic; append Verbatim + agent interpretation; confirm. |
| MATCH_OR_CREATE_TOPIC | Choose existing topic or propose new topic name; confirm before create. |
| APPEND_VERBATIM_AND_INTERPRETATION | Append one entry to topic file per _idea-file-schema. |
| CONFIRM_ADD | Confirm what was added and where. |
| SYNTHESIZE_TOPIC_TO_PROJECT_IDEAS | Extended thinking: 10–15 project ideas from topic; show inline. |
| META_AGENT_NAVIGATION | /menu and slash commands: incompletes, do-more, whats-next, ideas. |
| SHOW_MENU | Present Projects / Ideas / Something else. |
| HANDLE_INCOMPLETES | Scan completed-projects appendix; menu of incomplete; continue or return. |
| HANDLE_DO_MORE | Menu of projects with enhancement ideas; propose plan or return. |
| HANDLE_WHATS_NEXT | Combined incomplete + enhancement menu; then act or return. |
| MANAGE_SKILLS | Create/validate skill, imported meta-doc, scaffold episteme skill; future integrity/sync. |
| CREATE_OR_VALIDATE_SKILL | Create or validate skill folder vs skill-definition + skill-standard. |
| READ_SKILL_DEFINITION_AND_STANDARD | Load _skill-definition and _skill-standard (and website if needed). |
| GATHER_SKILL_METADATA | Elicit name, description, when to use, instructions (or path to validate). |
| WRITE_OR_VALIDATE_SKILL_FOLDER | Write SKILL.md + folder or produce validation report. |
| IMPORTED_SKILL_META_DOC | Meta-doc for imported skill: location, risk assessment, conversation notes, integrity. |
| ASSESS_SKILL_RISK | Security, trust, dependencies, conflicts; summary; alternatives if needed. |
| WRITE_META_DOC | Write META.md (or equivalent) per _imported-skills. |
| EPISTEME_SKILL_SCAFFOLD | Scaffold episteme-skills/&lt;name&gt;/ with SKILL.md stub. |
| EPISTEME_DESIGN | Create or validate _docs and instance docs per design language. |
| READ_DOCS_DESIGN_LANGUAGE | Load _docs format, naming, template (e.g. _docs-format-and-design-notes). |
| CREATE_OR_VALIDATE_UNDERSCORE_DOC | Create or validate one _doc and/or instance doc. |
| SKILL_INTEGRITY_CHECK | (Future.) Recompute hash; compare to stored; report tampering risk. |
| SKILL_STANDARD_SYNC | (Future.) Compare local skill-standard to website; report drift. |
| ONBOARD_AGENT_TO_EPISTEME | Orchestrate onboarding for a naive agent: explain episteme and, if applicable, orient to the current project. |
| INTRO_TO_EPISTEME | Explain what the episteme framework is and how agents should behave in this repo. |
| ORIENT_TO_CURRENT_PROJECT | Summarize the current project from tracking docs and state what to do next. |
