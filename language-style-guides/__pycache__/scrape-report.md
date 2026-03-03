# Scrape report

Generated after cleaning scraped content: trim line whitespace, collapse 3+ blank lines to 2, trim each source block. Content is left as plain text (no reformatting of rules/code) so sources remain traceable.

- **Successfully scraped:** 61 files (all `code-guide-*.ai` under `public/master/` that have at least one scraped source).
- **Failed / could not access:** 6 URLs (see below; fix links or retry).
- **Low-value / index pages:** 3 files contain at least one source that is a listing page or very short; consider replacing those links with direct style-guide URLs.

---

## Successfully scraped files

Files that have at least one scraped source block (and were cleaned):

- `build-tooling/code-guide-vite.ai`
- `c-family/code-guide-c-plus-plus.ai`
- `c-family/code-guide-c-sharp.ai`
- `c-family/code-guide-objective-c.ai`
- `data-science/code-guide-r.ai`
- `frontend-frameworks/code-guide-angular.ai`
- `frontend-frameworks/code-guide-astro.ai`
- `frontend-frameworks/code-guide-next.ai`
- `frontend-frameworks/code-guide-preact.ai`
- `frontend-frameworks/code-guide-react.ai`
- `frontend-frameworks/code-guide-svelte.ai`
- `frontend-frameworks/code-guide-vue.ai`
- `functional/code-guide-elixir.ai`
- `functional/code-guide-haskell.ai`
- `javascript-runtimes/code-guide-bun.ai`
- `javascript-runtimes/code-guide-deno.ai`
- `javascript-runtimes/code-guide-node.ai`
- `jvm-languages/code-guide-java.ai`
- `jvm-languages/code-guide-kotlin.ai`
- `jvm-languages/code-guide-scala.ai`
- `legacy/code-guide-ada.ai`
- `legacy/code-guide-basic.ai`
- `legacy/code-guide-cobol.ai`
- `legacy/code-guide-fortran.ai`
- `legacy/code-guide-pascal.ai`
- `legacy/code-guide-vb.ai`
- `lisp-family/code-guide-clojure.ai`
- `lisp-family/code-guide-common-lisp.ai`
- `lisp-family/code-guide-elisp.ai`
- `lisp-family/code-guide-racket.ai`
- `lisp-family/code-guide-scheme.ai`
- `markup-and-data/code-guide-json.ai`
- `markup-and-data/code-guide-markdown.ai`
- `markup-and-data/code-guide-web.ai`
- `markup-and-data/code-guide-xml.ai`
- `markup-languages/code-guide-asciidoc.ai`
- `markup-languages/code-guide-html.ai`
- `markup-languages/code-guide-latex.ai`
- `markup-languages/code-guide-markdown.ai`
- `markup-languages/code-guide-restructuredtext.ai`
- `markup-languages/code-guide-xhtml.ai`
- `markup-languages/code-guide-xml.ai`
- `mobile-cross-platform/code-guide-dart.ai`
- `mobile-cross-platform/code-guide-flutter.ai`
- `mobile-cross-platform/code-guide-swift.ai`
- `query-languages/code-guide-cypher.ai`
- `query-languages/code-guide-graphql.ai`
- `query-languages/code-guide-sparql.ai`
- `query-languages/code-guide-sql.ai`
- `scripting-dynamic/code-guide-lua.ai`
- `scripting-dynamic/code-guide-perl.ai`
- `scripting-dynamic/code-guide-php.ai`
- `scripting-dynamic/code-guide-python.ai`
- `scripting-dynamic/code-guide-ruby.ai`
- `systems-languages/code-guide-go.ai`
- `systems-languages/code-guide-rs.ai`
- `systems-languages/code-guide-rust.ai`
- `tooling/code-guide-shell.ai`
- `tooling/code-guide-vim.ai`
- `typescript-javascript/code-guide-ts-js.ai`
- `vendor-platform/code-guide-apex.ai`

Total: 61 files. (Files with at least one scraped source block.)

---

## Failed or could not access

URLs that returned HTTP errors or could not be fetched. Fix links or retry.

- **frontend-frameworks/code-guide-svelte.ai | https://svelte.dev/docs/component-format**  
  Reason: `<HTTPError 404: 'Not Found'>`

- **functional/code-guide-elixir.ai | https://hexdocs.pm/elixir/style-guide.html**  
  Reason: `<HTTPError 404: ''>`

- **legacy/code-guide-ada.ai | https://www.adaic.org/resources/add_content/docs/styleguide/html/**  
  Reason: `<HTTPError 404: 'Not Found'>`

- **legacy/code-guide-ada.ai | https://www.adaic.org/resources/add_content/standards/95style/style.pdf**  
  Reason: `<HTTPError 404: 'Not Found'>`

- **query-languages/code-guide-cypher.ai | https://neo4j.com/developer/cypher/guide-cypher-best-practices/**  
  Reason: `<HTTPError 404: 'Not Found'>`

- **query-languages/code-guide-cypher.ai | https://neo4j.com/docs/cypher-manual/current/style-guide/**  
  Reason: `<HTTPError 404: 'Not Found'>`

---

## Low-value / index pages (scraped but likely off-topic or listing only)

These URLs were successfully fetched but are index/listing pages or very short content. Consider replacing with direct style-guide links.

- **functional/code-guide-elixir.ai**
  - https://hexdocs.pm/credo/

- **legacy/code-guide-ada.ai**
  - https://github.com/Kristories/awesome-guidelines

- **query-languages/code-guide-cypher.ai**
  - https://github.com/Kristories/awesome-guidelines
