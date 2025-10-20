# a11ytagger Constitution

<!--
SYNC IMPACT REPORT (2025-10-08)

Version Change: 1.0.0 → 1.0.1
Change Type: PATCH (clarification of PDF/UA scope and timeline)

Modified Principles:
- III. Accessibility-First - Clarified that PDF/UA is a long-term goal, not MVP requirement

Changes:
- Updated principle III to reflect progressive approach to PDF/UA compliance
- Clarified that tool accessibility (WCAG) remains mandatory
- Removed implication of immediate full PDF/UA support

Templates Requiring Updates:
✅ plan-template.md - No changes needed
✅ spec-template.md - No changes needed
✅ tasks-template.md - No changes needed

Follow-up TODOs:
- Establish lint/type checking tools and add to Governance section
- Consider adding performance benchmarks for PDF processing
-->

## Core Principles

### I. Class-Based Architecture

All Django views MUST be implemented as class-based views (CBVs). This ensures consistent structure, reusability through mixins, and clear separation of HTTP method handling. Template-based rendering MUST be used for all user-facing pages. No function-based views except for the most trivial cases (explicitly justified).

**Rationale**: CBVs provide better code organization, inheritance, and maintainability as the application grows. They enforce a consistent pattern across all features.

### II. Component Separation

PDF processing logic, accessibility analysis, and UI concerns MUST be cleanly separated. Each accessibility tool (image tagging, reading order, etc.) MUST be implemented as an independent, testable component with a well-defined interface. Business logic MUST NOT be embedded in views or templates.

**Rationale**: Clean separation enables independent development, testing, and extension of accessibility tools. It allows tools to be added or modified without affecting the core application structure.

### III. Accessibility-First

The tool itself MUST be accessible (WCAG 2.1 AA minimum). Features SHOULD work toward PDF/UA compliance as a long-term goal, building capability incrementally. Each accessibility tool MUST clearly communicate its scope and limitations. Automatic fixes MUST be designed with user review and correction in mind. Never sacrifice accessibility for convenience.

**Rationale**: As an accessibility tool, this project must embody the standards it helps users achieve. Full PDF/UA support is a journey, not a sprint—the tool will build toward comprehensive compliance over time while being transparent about current capabilities.

### IV. Progressive Enhancement

Automatic accessibility fixes MUST be implemented with graduated confidence levels. High-confidence fixes MAY be applied automatically with clear notification. Medium and low-confidence fixes MUST require user review and approval. Users MUST always have visibility into what was changed and why.

**Rationale**: Automatic processes make mistakes. Users need control over their documents and must be able to verify and correct automated decisions to ensure quality and compliance.

### V. User Control Over Automation

All automatic processes MUST be transparent and reversible. Users MUST be able to see what changes will be made before they are applied. The UI MUST provide clear feedback about automatic vs. manual changes. Users MUST be able to override or reject any automatic suggestion.

**Rationale**: Trust is built through transparency. Users need to understand and control the tool's actions, especially when their documents' compliance depends on the accuracy of those actions.

## Technical Standards

**Framework**: Django 5.2+ with Python 3.13+

**Package Management**: uv for all dependency management and virtual environment handling

**PDF Library**: pikepdf for all PDF manipulation and accessibility tagging

**Task Runner**: Makefile serves as the task runner interface. All common operations (install, run, test, migrate) MUST be accessible via make targets.

**Storage**: Django's cache framework for temporary PDF storage during processing. Future storage requirements MUST use Django's storage abstraction.

**Template Structure**: Django templates with template inheritance. All pages extend from base.html. Components MUST be reusable template fragments.

**Import Order**: Standard library, Django, third-party (pikepdf), local. Two blank lines between top-level definitions.

**Naming**: snake_case for functions/variables, PascalCase for classes, ALL_CAPS for constants.

**Error Handling**: Return rendered templates with error context rather than raising exceptions. All user-facing errors MUST be actionable and clear.

## Workflow Requirements

**Development Server**: MUST run on port 8080 via `make run`

**Dependencies**: All dependency changes MUST be reflected in pyproject.toml. Use `make install` to sync.

**Migrations**: Database schema changes MUST use Django migrations. Run `make makemigrations` then `make migrate`.

**Testing**: Tests MUST be runnable via Django's test framework. Test command MUST be documented if custom configuration is added.

**Commit Policy**: Changes MUST NOT be committed without explicit user request. Lint and type checking SHOULD be run before commit (tools to be established).

**Documentation**: README.md MUST be kept current with setup and usage instructions. Makefile targets MUST have help text.

## Governance

**Constitution Authority**: This constitution supersedes all other development practices and conventions. When conflicts arise, constitution principles take precedence.

**Amendment Process**: Amendments require clear justification, documentation of impact, version bump according to semantic versioning, and update of all dependent templates and documentation.

**Versioning Policy**:
- MAJOR: Breaking changes to core principles, removal of principles, fundamental architecture shifts
- MINOR: New principles added, expanded guidance, new constraints or standards
- PATCH: Clarifications, wording improvements, typo fixes, non-semantic refinements

**Complexity Justification**: Any violation of core principles MUST be documented in plan.md Complexity Tracking section with justification and explanation of why simpler alternatives are insufficient.

**Compliance Review**: All features MUST pass Constitution Check gate before implementation begins. The check MUST be re-verified after design phase.

**Runtime Guidance**: Use AGENTS.md for runtime development guidance and code style conventions.

**Version**: 1.0.1 | **Ratified**: 2025-10-08 | **Last Amended**: 2025-10-08
