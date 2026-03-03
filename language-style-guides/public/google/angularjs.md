<!-- Processed: content merged or already in master; see google/PROCESSED.md -->

# Content from https://google.github.io/styleguide/angularjs-google-style.html

# An AngularJS Style Guide for Closure Users at Google

This is the external version of a document for Google engineers. It describes a recommended style for AngularJS apps that use Closure. This guide supplements the Google JavaScript Style Guide.

## 1 Angular Language Rules

- **Manage dependencies** with Closure's goog.require and goog.provide; choose a namespace.
- **Modules**: Main application module in root client directory; never alter a module other than where it is defined.
- **Modules reference other modules** using the Angular Module's "name" property (e.g. `my.submoduleA.name`).
- **Use a common externs file** for JS compiler type safety with Angular types.
- **JSCompiler flags**: Use JSCompiler; add ANGULAR_COMPILER_FLAGS_FULL; use @export with appropriate flags for methods/properties.
- **Controllers and Scopes**: Controllers are classes; methods on MyCtrl.prototype; use 'controller as' style; @export for properties/methods with property renaming.
- **Directives**: All DOM manipulation inside directives; keep directives small; goog.provide a static function returning the directive definition object.
- **Services**: Use module.service for classes; use module.service instead of provider/factory unless you need extra initialization.

## 2 Angular Style Rules

- **Reserve $** for Angular properties and services; do not use $ for your own identifiers.
- **Custom elements**: IE8 may require special support for styling.

## 3 Tips and Best Practices

- Testing: Jasmine + Karma; use inject and module adapters.
- Consider the directory structure doc (controllers in nested subdirs, components in 'components' dir).
- Be aware of scope prototypal inheritance.
- Use @ngInject for dependency injection with minification.

(Full content at source URL above.)
