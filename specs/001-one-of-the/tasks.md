# Tasks: PDF Accessibility Information Extraction & Display

**Input**: Design documents from `/specs/001-one-of-the/`  
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/extraction-api.md, research.md, quickstart.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, etc.)
- Include exact file paths in descriptions

## Path Conventions
Django single-app monolith - all code in `server/` app at repository root.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure needed by all user stories

- [x] T001 [P] Create accessibility package directory structure: `server/accessibility/__init__.py`
- [x] T002 [P] Create test directory structure: `tests/unit/`, `tests/integration/`, `tests/fixtures/sample_pdfs/`
- [x] T003 [P] Create templates directory: `templates/server/partials/`
- [x] T004 Verify pikepdf dependency in pyproject.toml (should already exist from project setup)

**Checkpoint**: Basic project structure in place

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 [P] Create dataclass models in `server/accessibility/models.py`: ImageReference, StructureElement, ExtractionResult, ValidationResult
- [ ] T006 [P] Create PDF validation logic in `server/accessibility/validators.py`: validate_pdf_file(), ValidationStatus enum, encryption detection, file size warnings
- [ ] T007 Create timeout context manager in `server/accessibility/extractor.py`: timeout() context manager using signal.alarm() for Unix/Linux/macOS
- [ ] T008 Create core extraction scaffolding in `server/accessibility/extractor.py`: extract_accessibility_info() function signature, error handling structure
- [ ] T009 [P] Add URL routes to `server/urls.py`: /accessibility/upload/, /accessibility/results/<cache_key>/
- [ ] T010 Configure Django cache settings in `a11ytagger/settings.py` if not already configured: LocMemCache with 1-hour TTL

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View Existing Accessibility Tags (Priority: P1) 🎯 MVP

**Goal**: Users can upload a PDF and see what accessibility features exist (alt text, structure tags, reading order)

**Independent Test**: Upload a PDF with known accessibility features and verify extracted information matches expected results

### Implementation for User Story 1

- [ ] T011 [US1] Implement structure tree extraction in `server/accessibility/extractor.py`: extract_structure_tree() function to traverse /StructTreeRoot and /K children
- [ ] T012 [US1] Implement structure element traversal in `server/accessibility/extractor.py`: traverse_element() recursive function to build StructureElement tree
- [ ] T013 [US1] Implement image alt text extraction in `server/accessibility/extractor.py`: extract_images_from_tree() to find Figure elements with /Alt text
- [ ] T014 [US1] Implement metadata extraction in `server/accessibility/extractor.py`: get_metadata() to extract /Lang and /Title from pdf.Root and pdf.docinfo
- [ ] T015 [US1] Implement reading order indexing in `server/accessibility/extractor.py`: assign reading_order_index during pre-order traversal
- [ ] T016 [US1] Complete extract_accessibility_info() in `server/accessibility/extractor.py`: integrate all extraction functions, handle timeouts, populate ExtractionResult
- [ ] T017 [US1] Create PDFAccessibilityUploadView in `server/views.py`: CBV with get() and post() methods
- [ ] T018 [US1] Implement file upload handling in PDFAccessibilityUploadView.post(): save temp file, call validator, handle validation errors
- [ ] T019 [US1] Implement extraction trigger in PDFAccessibilityUploadView.post(): call extract_accessibility_info() with timeout, cache result, redirect to results
- [ ] T020 [US1] Create cache key generation logic in PDFAccessibilityUploadView.post(): hash-based cache key with format "pdf_extraction:{hash}:{timestamp}"
- [ ] T021 [US1] Create ExtractionResultsView in `server/views.py`: CBV with get() method to retrieve from cache
- [ ] T022 [US1] Implement cache retrieval in ExtractionResultsView.get(): cache.get(cache_key), handle cache miss with 404
- [ ] T023 [P] [US1] Create upload form template in `templates/server/accessibility_upload.html`: file upload form with CSRF, error display area
- [ ] T024 [P] [US1] Create results template in `templates/server/extraction_results.html`: basic structure with simple view container
- [ ] T025 [P] [US1] Create error template in `templates/server/extraction_error.html`: error message display with retry link
- [ ] T026 [US1] Implement simple summary view in `templates/server/extraction_results.html`: display total_images, images_with_alt_text, has_structure_tree, is_tagged, structure_types_found
- [ ] T027 [US1] Add encrypted PDF rejection in PDFAccessibilityUploadView.post(): render error template when validation.is_encrypted
- [ ] T028 [US1] Add timeout error handling in PDFAccessibilityUploadView.post(): render error template when result.timed_out
- [ ] T029 [US1] Add invalid PDF error handling in PDFAccessibilityUploadView.post(): render error template when validation.is_valid_pdf is False

**Checkpoint**: At this point, User Story 1 should be fully functional - users can upload PDFs and see basic accessibility status in simple view

---

## Phase 4: User Story 2 - Understand Missing Accessibility Features (Priority: P2)

**Goal**: Users can identify gaps in accessibility (missing alt text, no structure tags) and toggle between simple/detailed views

**Independent Test**: Upload a PDF with partial accessibility features and verify system correctly identifies and displays missing elements

### Implementation for User Story 2

- [ ] T030 [US2] Implement detailed view toggle in `templates/server/extraction_results.html`: JavaScript toggle buttons for simple/detailed views
- [ ] T031 [US2] Create detailed images list in `templates/server/extraction_results.html`: table showing all images with page number, alt text, and status badges
- [ ] T032 [US2] Create structure tree visualization in `templates/server/extraction_results.html`: container for recursive tree rendering
- [ ] T033 [P] [US2] Create structure node partial template in `templates/server/partials/structure_node.html`: recursive template include for tree hierarchy display
- [ ] T034 [US2] Implement missing features identification in ExtractionResultsView.get(): calculate images_without_alt_text, missing structure tags, add to context
- [ ] T035 [US2] Add warning badges in `templates/server/extraction_results.html`: highlight missing alt text with visual indicators
- [ ] T036 [US2] Add gap summary section in `templates/server/extraction_results.html`: "Issues Found" section listing missing features
- [ ] T037 [US2] Implement view mode parameter handling in ExtractionResultsView.get(): read ?view=simple|detailed query parameter, pass to template
- [ ] T038 [US2] Add CSS styling for view toggle in `templates/server/extraction_results.html`: button active states, view container show/hide
- [ ] T039 [US2] Add detailed metadata display in `templates/server/extraction_results.html`: document title, language, PDF version in detailed view
- [ ] T040 [US2] Implement large file warnings in PDFAccessibilityUploadView.post(): display warnings from validation.warnings in upload template

**Checkpoint**: All user stories should now be independently functional - users can see both simple summaries and detailed breakdowns with missing feature identification

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and production readiness

- [ ] T041 [P] Add WCAG 2.1 AA accessibility attributes to `templates/server/accessibility_upload.html`: ARIA labels, form labels, keyboard navigation
- [ ] T042 [P] Add WCAG 2.1 AA accessibility attributes to `templates/server/extraction_results.html`: semantic HTML, headings hierarchy, alt text for visual indicators
- [ ] T043 [P] Add WCAG 2.1 AA accessibility attributes to `templates/server/extraction_error.html`: clear error announcements, focus management
- [ ] T044 [P] Create test fixture PDFs in `tests/fixtures/sample_pdfs/`: tagged.pdf, untagged.pdf, encrypted.pdf, large.pdf (for various test scenarios)
- [ ] T045 Update README.md with feature documentation: usage instructions, upload page URL, example screenshots
- [ ] T046 Add cache cleanup consideration note in quickstart.md: document 1-hour expiration behavior
- [ ] T047 [P] Add error logging in `server/accessibility/extractor.py`: log extraction errors for debugging (console logging sufficient for MVP)
- [ ] T048 [P] Add error logging in `server/accessibility/validators.py`: log validation failures for debugging

**Checkpoint**: Feature is production-ready with accessibility compliance, documentation, and error logging

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User Story 1 (P1) can start after Foundational
  - User Story 2 (P2) can start after Foundational (builds on US1 templates but is independently testable)
- **Polish (Phase 5)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Enhances US1 templates but is independently testable (adds detailed view to existing simple view)

### Within Each User Story

**User Story 1 execution order**:
1. Core extraction logic (T011-T016) - sequential, builds on each other
2. Views (T017-T022) - sequential, depends on extraction logic
3. Templates (T023-T026) - parallel, no dependencies between templates
4. Error handling (T027-T029) - sequential after views, adds error cases

**User Story 2 execution order**:
1. Template enhancements (T030-T033, T038) - parallel, different template areas
2. View logic updates (T034, T037) - sequential after template structure
3. Display logic (T035-T036, T039-T040) - parallel, different display areas

### Parallel Opportunities

**Phase 1 (Setup)**: All tasks [P] - can run in parallel
- T001, T002, T003 all create different directories

**Phase 2 (Foundational)**: Tasks T005, T006 can run in parallel (different files)
- T005 (models.py) and T006 (validators.py) are independent

**User Story 1**: Parallel opportunities:
- T023, T024, T025 (different template files)

**User Story 2**: Parallel opportunities:
- T030, T031, T032, T033, T038 (template updates in different areas)
- T044, T045, T046, T047, T048 (polish tasks in different files)

---

## Parallel Example: User Story 1 Core Extraction

```bash
# After Foundational phase completes, launch extraction implementation:

# Parallel: Create different template files
Task T023: "Create upload form template in templates/server/accessibility_upload.html"
Task T024: "Create results template in templates/server/extraction_results.html"  
Task T025: "Create error template in templates/server/extraction_error.html"

# Then sequential: Build extraction logic (dependencies)
Task T011: extract_structure_tree()
Task T012: traverse_element() 
Task T013: extract_images_from_tree()
Task T014: get_metadata()
Task T015: reading order indexing
Task T016: integrate all functions in extract_accessibility_info()
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T010) - CRITICAL blocking phase
3. Complete Phase 3: User Story 1 (T011-T029)
4. **STOP and VALIDATE**: Test User Story 1 independently:
   - Upload a tagged PDF → See structure tags and alt text
   - Upload an untagged PDF → See "no accessibility tags" message
   - Upload encrypted PDF → See error
   - Test timeout with large PDF
5. If working, deploy/demo MVP

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (enhanced view)
4. Add Polish tasks → Production-ready

Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (critical path)
2. Once Foundational is done:
   - Developer A: User Story 1 extraction logic (T011-T016)
   - Developer B: User Story 1 views and templates (T017-T026)
   - Developer C: User Story 1 error handling (T027-T029)
3. After US1 complete:
   - Developer A: User Story 2 detailed view (T030-T040)
   - Developer B: Polish and accessibility (T041-T043)
   - Developer C: Documentation and test fixtures (T044-T046)

---

## Notes

- [P] tasks = different files, no dependencies - can run in parallel
- [Story] label maps task to specific user story (US1, US2) for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at checkpoints to validate story independently
- Foundational phase is CRITICAL - blocks all user stories
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Tests are NOT included in this task list (no test tasks requested in specification)

## Task Count Summary

**Total Tasks**: 48

**By Phase**:
- Phase 1 (Setup): 4 tasks
- Phase 2 (Foundational): 6 tasks (BLOCKING)
- Phase 3 (User Story 1 - P1): 19 tasks
- Phase 4 (User Story 2 - P2): 11 tasks
- Phase 5 (Polish): 8 tasks

**Parallel Opportunities**: 18 tasks marked [P] (37.5% of total)

**Critical Path** (minimum for MVP):
- Setup (4) + Foundational (6) + User Story 1 (19) = **29 tasks for MVP**

**Story Independence**:
- ✅ User Story 1 can be tested independently after T029
- ✅ User Story 2 can be tested independently after T040
- ✅ Each story delivers standalone value

**Suggested MVP Scope**: Phase 1 + Phase 2 + Phase 3 (User Story 1 only) = 29 tasks
