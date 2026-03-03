"""
Source list for code-guide scrapers. Matches code-guide-sources.md.
Each entry: (slug, url, parser_key).
parser_key: 'google_styleguide' | 'peps_python' | 'dart_dev' | 'android_kotlin'
"""
from dataclasses import dataclass
from typing import List

@dataclass
class Source:
    slug: str
    url: str
    parser_key: str

SOURCES: List[Source] = [
    # Google Style Guide (same HTML structure for all)
    Source("google-cpp", "https://google.github.io/styleguide/cppguide.html", "google_styleguide"),
    Source("google-csharp", "https://google.github.io/styleguide/csharp-style.html", "google_styleguide"),
    Source("google-go", "https://google.github.io/styleguide/go/", "google_styleguide"),
    Source("google-java", "https://google.github.io/styleguide/javaguide.html", "google_styleguide"),
    Source("google-javascript", "https://google.github.io/styleguide/jsguide.html", "google_styleguide"),
    Source("google-typescript", "https://google.github.io/styleguide/tsguide.html", "google_styleguide"),
    Source("google-python", "https://google.github.io/styleguide/pyguide.html", "google_styleguide"),
    Source("google-shell", "https://google.github.io/styleguide/shellguide.html", "google_styleguide"),
    Source("google-objc", "https://google.github.io/styleguide/objcguide.html", "google_styleguide"),
    Source("google-r", "https://google.github.io/styleguide/Rguide.html", "google_styleguide"),
    Source("google-markdown", "https://google.github.io/styleguide/docguide/style.html", "google_styleguide"),
    Source("google-htmlcss", "https://google.github.io/styleguide/htmlcssguide.html", "google_styleguide"),
    Source("google-angularjs", "https://google.github.io/styleguide/angularjs-google-style.html", "google_styleguide"),
    # PEP 8
    Source("pep8", "https://peps.python.org/pep-0008/", "peps_python"),
    # Effective Dart
    Source("effective-dart", "https://dart.dev/guides/language/effective-dart", "dart_dev"),
    # Kotlin (Android)
    Source("kotlin-android", "https://developer.android.com/kotlin/style-guide", "android_kotlin"),
]
