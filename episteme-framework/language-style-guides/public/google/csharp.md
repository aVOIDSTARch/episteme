<!-- Processed: content merged or already in master; see google/PROCESSED.md -->

# Content from https://google.github.io/styleguide/csharp-style.html

# C# at Google Style Guide

This style guide is for C# code developed internally at Google, and is the default style for C# code at Google. It makes stylistic choices that conform to other languages at Google, such as Google C++ style and Google Java style.

## Formatting guidelines

### Naming rules

Naming rules follow [Microsoft's C# naming guidelines](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/naming-guidelines). Where Microsoft's naming guidelines are unspecified (e.g. private and local variables), rules are taken from the [CoreFX C# coding guidelines](https://github.com/dotnet/runtime/blob/HEAD/docs/coding-guidelines/coding-style.md)

Rule summary:

#### Code

- Names of interfaces start with `I`, e.g. `IInterface`.
- For casing, a "word" is anything written without internal spaces, including acronyms. For example, `MyRpc` instead of `MyRPC`.
- Naming convention is unaffected by modifiers such as const, static, readonly, etc.
- Names of private, protected, internal and protected internal fields and properties: `_camelCase`.
- Names of local variables, parameters: `camelCase`.
- Names of classes, methods, enumerations, public fields, public properties, namespaces: `PascalCase`.

#### Files

- In general, prefer one core class per file.
- Where possible the file name should be the same as the name of the main class in the file, e.g. `MyClass.cs`.
- Filenames and directory names are `PascalCase`, e.g. `MyFile.cs`.

(Full content from source; see URL above for complete guide.)
