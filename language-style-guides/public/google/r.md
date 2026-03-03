# Content from https://google.github.io/styleguide/Rguide.html

# Google's R Style Guide

R is a high-level programming language used primarily for statistical computing and graphics. The goal of the R Programming Style Guide is to make our R code easier to read, share, and verify.

The Google R Style Guide is a fork of the [Tidyverse Style Guide](https://style.tidyverse.org/) by Hadley Wickham. Google modifications were developed in collaboration with the internal R user community. The rest of this document explains Google's primary differences with the Tidyverse guide, and why these differences exist.

## Syntax

### Naming conventions

Google prefers identifying functions with `BigCamelCase` to clearly distinguish them from other objects.

The names of private functions should begin with a dot. We're moving away from `dot.case` for objects.

### Don't use attach()

The possibilities for creating errors when using `attach()` are numerous.

## Pipes

### Right-hand assignment

We do not support using right-hand assignment.

### Use explicit returns

Do not rely on R's implicit return feature. Use explicit `return()`.

### Qualifying namespaces

Users should explicitly qualify namespaces for all external functions (e.g. `purrr::map()`). Prefer `@importFrom` in Roxygen above the function where the external dependency is used.

## Documentation

All packages should have a package documentation file, in a `packagename-package.R` file.

(Full content at source URL above.)
