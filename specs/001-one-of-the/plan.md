# Implementation Plan: PDF Accessibility Information Extraction & Display

**Branch**: `001-one-of-the` | **Date**: 2025-10-08 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-one-of-the/spec.md`

## Summary

Build an MVP library for extracting accessibility information from PDFs (alt text, structure tags, reading order) and display results in a dual-view web interface. The extraction component must be independently testable, handle errors gracefully, and support future migration to async processing and persistent storage.

## Technical Context

**Language/Version**: Python 3.13+  
**Primary Dependencies**: Django 5.2+, pikepdf 9.11+, uv for package management  
**Storage**: Django cache framework (in-memory) for 1-hour PDF retention  
**Testing**: Django test framework (`python manage.py test`)  
**Target Platform**: Self-hosted web application (Linux/macOS/Windows with Docker support)  
**Project Type**: Web application (Django monolith)  
**Performance Goals**: <10 second extraction for typical PDFs (1-20 pages, <5MB); abort on timeout  
**Constraints**: Synchronous processing with 10-second timeout; no file size limit but warn on large files; 95% accuracy for standard-compliant PDFs  
**Scale/Scope**: Self-hosted single-user or small team usage; focus on correctness over throughput

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Core Principles Compliance

✅ **I. Class-Based Architecture**
- All views will use Django CBVs (PDFUploadView, ExtractionResultView)
- Template-based rendering for all UI

✅ **II. Component Separation**
- Extraction logic separated into independent library (`server/accessibility/extractor.py`)
- Views handle only HTTP concerns
- Templates handle only presentation
- Business logic isolated in service layer

✅ **III. Accessibility-First**
- Tool itself will follow WCAG 2.1 AA standards
- Extraction focuses on standard PDF accessibility features
- Clear communication of scope and limitations in UI

✅ **IV. Progressive Enhancement**
- Read-only extraction in MVP (no automatic fixes)
- Foundation for future graduated confidence levels

✅ **V. User Control Over Automation**
- Users control what PDFs to analyze
- Dual-view interface (simple/detailed) gives users control over information depth
- No modifications to source PDFs

### Technical Standards Compliance

✅ **Framework**: Django 5.2+ with Python 3.13+  
✅ **Package Management**: uv  
✅ **PDF Library**: pikepdf  
✅ **Task Runner**: Makefile  
✅ **Storage**: Django cache framework  
✅ **Template Structure**: Django templates with inheritance  
✅ **Import Order**: Standard library, Django, pikepdf, local  
✅ **Naming**: snake_case/PascalCase/ALL_CAPS conventions  
✅ **Error Handling**: Return templates with error context

### Workflow Requirements Compliance

✅ **Development Server**: Port 8080 via `make run`  
✅ **Dependencies**: pyproject.toml managed  
✅ **Migrations**: Django migrations (minimal for this feature - cache only)  
✅ **Testing**: Django test framework  
✅ **Documentation**: README updates required

**GATE STATUS**: ✅ PASS - No violations

## Project Structure

### Documentation (this feature)

```
specs/001-one-of-the/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── extraction-api.md
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```
server/
├── accessibility/
│   ├── __init__.py
│   ├── extractor.py      # Core extraction library
│   ├── models.py         # Data classes for extraction results
│   └── validators.py     # PDF validation logic
├── views.py              # CBVs for upload and results display
├── models.py             # Django models (if needed for future persistence)
└── urls.py               # URL routing

templates/server/
├── accessibility_upload.html    # Upload form
├── extraction_results.html      # Results display (dual-view)
└── extraction_error.html        # Error display

tests/
├── unit/
│   ├── test_extractor.py
│   ├── test_validators.py
│   └── test_models.py
├── integration/
│   └── test_extraction_flow.py
└── fixtures/
    └── sample_pdfs/     # Test PDFs with various accessibility features
```

**Structure Decision**: Django single-app monolith. The `server` app contains all extraction logic, views, and templates. Extraction library (`accessibility/`) is a sub-package within the Django app for easy imports while maintaining separation. This aligns with existing project structure where `server` already exists.

## Complexity Tracking

*No violations - Constitution Check passed.*
