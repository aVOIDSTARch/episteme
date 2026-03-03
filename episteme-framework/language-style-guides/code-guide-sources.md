# Code guide sources

**Purpose:** List of style-guide URLs used for scraping and merging into the master code-guide-*.ai files. For maintainers: when adding or refreshing a language guide, use these (or add new rows) and run the scrape/merge workflow.

**Note:** The master guide library is not complete; it is started enough to prime the agent. Users are expected to complete it (add sources, run scrapes/merges, fill or add code-guide-*.ai files). See [public/master/README.md](public/master/README.md) (§ Library status).

---

## Primary sources

| Source | URL | Notes |
|--------|-----|------|
| **Google Style Guide (index)** | https://google.github.io/styleguide/ | Main index; we scrape per-language pages. |
| **Google C++** | https://google.github.io/styleguide/cppguide.html | |
| **Google C#** | https://google.github.io/styleguide/csharp-style.html | |
| **Google Go** | https://google.github.io/styleguide/go/ | Overview + guide/decisions/best-practices subpages. |
| **Google Java** | https://google.github.io/styleguide/javaguide.html | |
| **Google JavaScript** | https://google.github.io/styleguide/jsguide.html | |
| **Google TypeScript** | https://google.github.io/styleguide/tsguide.html | |
| **Google Python** | https://google.github.io/styleguide/pyguide.html | |
| **Google Shell** | https://google.github.io/styleguide/shellguide.html | |
| **Google Objective-C** | https://google.github.io/styleguide/objcguide.html | |
| **Google R** | https://google.github.io/styleguide/Rguide.html | |
| **Google Markdown** | https://google.github.io/styleguide/docguide/style.html | |
| **Google HTML/CSS** | https://google.github.io/styleguide/htmlcssguide.html | |
| **Google AngularJS** | https://google.github.io/styleguide/angularjs-google-style.html | |
| **PEP 8 (Python)** | https://peps.python.org/pep-0008/ | Canonical Python style; often used alongside Google. |
| **Effective Dart** | https://dart.dev/guides/language/effective-dart | Dart/Flutter. |
| **Kotlin (Android)** | https://developer.android.com/kotlin/style-guide | When targeting Android. |

---

## Scraped content in this repo

- **scripts/** — Scrapers and runner: [scripts/README.md](scripts/README.md). Run `python scrape_guides.py` from scripts/ (use venv + requirements-scrape.txt). Report: `scrape-report-<timestamp>.md` in this folder.
- **public/google/** — Fetched from Google style guide; one .md per topic. See [public/google/README.md](public/google/README.md) and PROCESSED.md for merge status.
- **public/peps/**, **public/dart/**, **public/android/** — Scraped from PEP 8, Effective Dart, Android Kotlin style guide (one .md per run).
- **public/master/** — Merged, normalized code-guide-*.ai files. Schema: [public/master/code-guide-master-file.md](public/master/code-guide-master-file.md).

---

## Adding a new source

1. Add a row to the table above (or a new “Other sources” table) with the URL and scope.
2. If scraping: add the target URL to the scrape script’s list and run; raw output can go under `public/<source-name>/` or into the master file’s appendix until merged.
3. Merge into the right code-guide-&lt;topic&gt;.ai per the master format; update the guide’s Sources table and Consensus/Per-source sections.
