# Code-guide scrapers

**Purpose:** Fetch style-guide content from the URLs in [code-guide-sources.md](../code-guide-sources.md). Each site has a small parser in `scrapers/` tuned to its HTML structure. Output goes to `public/<source>/` and a timestamped report to `scrape-report-<timestamp>.md` in the language-style-guides folder.

---

## Setup

From this directory (`scripts/`):

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-scrape.txt
```

---

## Run

```bash
python scrape_guides.py
```

- **Sources** are listed in `sources_config.py` (Google, PEP 8, Dart, Android Kotlin).
- **Output:** One `.md` file per source under `../public/<parser_group>/` (e.g. `public/google/google-python.md`, `public/peps/pep8.md`, `public/dart/effective-dart.md`, `public/android/kotlin-android.md`).
- **Report:** `../scrape-report-YYYYMMDD-HHMMSS.md` with status (OK/FAIL), byte count, and any error note.

---

## Parsers (site-specific)

| Parser | Site | Selectors used |
|--------|------|----------------|
| `google_styleguide` | google.github.io/styleguide | devsite-article-body, main, article, body fallback |
| `peps_python` | peps.python.org | div.document, div.body, main |
| `dart_dev` | dart.dev | main, article, [role=main] |
| `android_kotlin` | developer.android.com | article, main, .article-content |

To add a source: add a row to `sources_config.SOURCES` and, if the site needs different HTML handling, add a new module in `scrapers/` and register it in `scrape_guides.PARSERS`.

---

## Merge

Scraped files are raw dumps. To merge into the master code-guide-*.ai format, use the transform/merge workflow described in [code-guide-master-file.md](../public/master/code-guide-master-file.md) and the BUILD_LANG_GUIDES_COLLECTION skills.
