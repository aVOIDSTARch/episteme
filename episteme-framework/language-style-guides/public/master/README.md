# Master code style files

**Source:** Core list from [aVOIDSTARch/ai-code-style-guide · ai-guides/guides-collection](https://github.com/aVOIDSTARch/ai-code-style-guide/tree/main/ai-guides/guides-collection). Extended with legacy and other widely used languages (same `code-guide-<topic>.ai` naming).

**Purpose:** Combined and pruned style guides per language/topic. Content from all site folders (google, goat-styles, kristories, project-rules, react-styleguidist, react-style-guide) is merged into these `.ai` files, then edited for perfection.

**Layout:** Guides are grouped in subfolders by language family and ecosystem.

---

## Library status

**This library is not complete.** It is started enough to prime the agent (structure, schema, sample guides, and skills are in place). **Users are expected to complete it:** add or fill in `code-guide-<topic>.ai` files for the languages and topics they use, run scrapes and merges as needed, and keep guides in sync with [code-guide-master-file.md](code-guide-master-file.md). Use [code-guide-sources.md](../../code-guide-sources.md) and the scripts in [language-style-guides/scripts/](../../scripts/) to add sources and refresh content.

---

## Folder structure

| Folder | Contents |
|--------|----------|
| **lisp-family** | Common Lisp, Scheme, Clojure, Racket, Emacs Lisp |
| **c-family** | C++, C#, Objective-C |
| **javascript-runtimes** | Node, Deno, Bun |
| **frontend-frameworks** | Angular, React, Vue, Svelte, Preact, Astro, Next.js |
| **typescript-javascript** | TypeScript / JavaScript (ts-js) |
| **jvm-languages** | Java, Kotlin, Scala |
| **systems-languages** | Go, Rust (rs, rust) |
| **scripting-dynamic** | Python, Ruby, Perl, PHP, Lua |
| **legacy** | Ada, BASIC, COBOL, Fortran, Pascal, Visual Basic |
| **markup-and-data** | Markdown, JSON, XML, Web (HTML/CSS) |
| **markup-languages** | HTML, XML, Markdown, AsciiDoc, reStructuredText, LaTeX, XHTML |
| **query-languages** | GraphQL, SQL, Cypher, SPARQL |
| **tooling** | Vim, Shell |
| **mobile-cross-platform** | Dart, Flutter, Swift |
| **functional** | Haskell, Elixir |
| **vendor-platform** | Salesforce Apex |
| **build-tooling** | Vite |
| **data-science** | R |

---

## Files by folder

- **lisp-family:** code-guide-common-lisp.ai, code-guide-scheme.ai, code-guide-clojure.ai, code-guide-racket.ai, code-guide-elisp.ai
- **c-family:** code-guide-c-plus-plus.ai, code-guide-c-sharp.ai, code-guide-objective-c.ai
- **javascript-runtimes:** code-guide-node.ai, code-guide-deno.ai, code-guide-bun.ai
- **frontend-frameworks:** code-guide-angular.ai, code-guide-react.ai, code-guide-vue.ai, code-guide-svelte.ai, code-guide-preact.ai, code-guide-astro.ai, code-guide-next.ai
- **typescript-javascript:** code-guide-ts-js.ai
- **jvm-languages:** code-guide-java.ai, code-guide-kotlin.ai, code-guide-scala.ai
- **systems-languages:** code-guide-go.ai, code-guide-rs.ai, code-guide-rust.ai
- **scripting-dynamic:** code-guide-python.ai, code-guide-ruby.ai, code-guide-perl.ai, code-guide-php.ai, code-guide-lua.ai
- **legacy:** code-guide-ada.ai, code-guide-basic.ai, code-guide-cobol.ai, code-guide-fortran.ai, code-guide-pascal.ai, code-guide-vb.ai
- **markup-and-data:** code-guide-markdown.ai, code-guide-json.ai, code-guide-xml.ai, code-guide-web.ai
- **markup-languages:** code-guide-html.ai, code-guide-xml.ai, code-guide-markdown.ai, code-guide-asciidoc.ai, code-guide-restructuredtext.ai, code-guide-latex.ai, code-guide-xhtml.ai
- **query-languages:** code-guide-graphql.ai, code-guide-sql.ai, code-guide-cypher.ai, code-guide-sparql.ai
- **tooling:** code-guide-vim.ai, code-guide-shell.ai
- **mobile-cross-platform:** code-guide-dart.ai, code-guide-flutter.ai, code-guide-swift.ai
- **functional:** code-guide-haskell.ai, code-guide-elixir.ai
- **vendor-platform:** code-guide-apex.ai
- **build-tooling:** code-guide-vite.ai
- **data-science:** code-guide-r.ai
