# Research: PDF Accessibility Extraction with pikepdf

**Feature**: PDF Accessibility Information Extraction & Display  
**Date**: 2025-10-08

## Executive Summary

This feature requires extracting accessibility information from PDFs that lack built-in support in pikepdf. Research confirms that pikepdf provides sufficient low-level access to the PDF structure tree, enabling extraction of alt text, structure tags, and reading order through direct object graph traversal.

## Core Technical Decisions

### Decision 1: Use pikepdf for Direct Structure Tree Traversal

**Decision**: Extract accessibility information by directly traversing the PDF structure tree using pikepdf's object access APIs.

**Rationale**:
- pikepdf provides Pythonic access to all PDF internal objects including `/StructTreeRoot`
- Built on qpdf (industry-standard C++ PDF library) for robust parsing
- MPL 2.0 license (vs PyMuPDF's restrictive AGPL)
- Existing project dependency - no new libraries needed
- Supports both modern XMP and legacy DocInfo metadata

**Alternatives Considered**:
- **PyMuPDF**: AGPL license too restrictive; limited structure tree APIs; primarily focused on rendering
- **PyPDF2/pypdf**: Lacks native structure tree traversal; less mature for accessibility features
- **pdfminer.six**: Focused on text extraction, not structural/accessibility markup
- **Custom PDF parser**: Excessive complexity; reinventing mature qpdf functionality

**Code Pattern**:
```python
# Access structure tree root
struct_tree_root = pdf.Root.get('/StructTreeRoot')

# Recursively traverse structure elements
def traverse_element(elem, depth=0):
    info = {
        'type': str(elem.get('/S')),           # Structure type (H1, P, Figure, etc.)
        'alt_text': str(elem.get('/Alt')),     # Alt text (images)
        'children': []
    }
    
    # Recurse on children (/K key defines reading order)
    children = elem.get('/K')
    if children:
        info['children'] = traverse_element(children, depth + 1)
    
    return info
```

### Decision 2: Three-Layer Architecture (Validator → Extractor → Presenter)

**Decision**: Separate concerns into three components:
1. **Validator** (`validators.py`): PDF file validation and pre-flight checks
2. **Extractor** (`extractor.py`): Core extraction logic for accessibility features
3. **Presenter** (Views + Templates): Django CBVs and templates for UI

**Rationale**:
- Aligns with Constitution Principle II (Component Separation)
- Validator can be tested independently with various malformed PDFs
- Extractor is pure Python with no Django dependencies (reusable)
- Views handle only HTTP concerns (upload, cache management, template rendering)
- Clear boundaries enable future async processing migration

**Component Responsibilities**:

**Validator**:
- Check file is valid PDF
- Detect encryption (`pdf.is_encrypted`)
- Verify structure tree exists
- Emit warnings for large files
- Return validation result object

**Extractor**:
- Traverse structure tree
- Extract alt text from `/Figure` elements
- Extract structure types (headings, paragraphs, lists, tables)
- Determine reading order (pre-order tree traversal)
- Extract metadata (language, title)
- Handle corrupted tags gracefully (partial extraction)
- Return structured extraction result

**Presenter** (Django layer):
- CBVs for upload and results display
- Cache management (1-hour retention)
- Timeout enforcement (10 seconds)
- Error template rendering
- Dual-view toggle (simple/detailed)

### Decision 3: Timeout Strategy Using signal.alarm() (Unix) with Fallback

**Decision**: Implement 10-second timeout using `signal.alarm()` on Unix/Linux/macOS with threading fallback for Windows.

**Rationale**:
- Spec requires 10-second abort for complex PDFs
- `signal.alarm()` is most reliable for CPU-bound operations
- Threading fallback ensures cross-platform compatibility
- Applied around entire extraction operation (open + traverse)

**Implementation**:
```python
import signal
from contextlib import contextmanager

class ExtractionTimeout(Exception):
    pass

@contextmanager
def timeout(seconds):
    def handler(signum, frame):
        raise ExtractionTimeout("Extraction exceeded timeout")
    
    # Unix/Linux/macOS
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

# Usage in extractor
try:
    with timeout(10):
        pdf = pikepdf.Pdf.open(pdf_path)
        result = extract_structure_tree(pdf)
except ExtractionTimeout:
    return {'error': 'timeout', 'message': 'PDF too complex for processing'}
```

**Windows Fallback** (to be implemented if needed):
```python
import threading

def timeout_wrapper(func, args, timeout_sec):
    result = [None]
    exception = [None]
    
    def wrapper():
        try:
            result[0] = func(*args)
        except Exception as e:
            exception[0] = e
    
    thread = threading.Thread(target=wrapper)
    thread.daemon = True
    thread.start()
    thread.join(timeout_sec)
    
    if thread.is_alive():
        raise ExtractionTimeout()
    if exception[0]:
        raise exception[0]
    return result[0]
```

### Decision 4: Error Classification System

**Decision**: Classify errors into specific categories for user-friendly messaging:

| Error Type | Detection | User Message |
|------------|-----------|--------------|
| `encrypted` | `pdf.is_encrypted == True` | "Please decrypt the PDF before uploading" |
| `invalid_pdf` | `PdfError` on open | "File is not a valid PDF" |
| `timeout` | Extraction exceeds 10 seconds | "PDF is too complex for processing" |
| `missing_features` | No `/StructTreeRoot` | "PDF has no accessibility tags" |
| `corrupted_tags` | Exception during traversal | "PDF has malformed accessibility tags" |
| `large_file_warning` | File size > 10MB (soft limit) | "Large file may take longer to process" |

**Rationale**:
- Aligns with FR-006, FR-007, FR-008 (error handling requirements)
- Users get actionable guidance (e.g., "decrypt file" vs generic error)
- System distinguishes between user-fixable (encryption) and inherent issues (no tags)
- Supports partial extraction (continue on corrupted tags, report what succeeded)

**Implementation**:
```python
def classify_error(exception, pdf=None):
    if isinstance(exception, ExtractionTimeout):
        return {'type': 'timeout', 'user_message': 'PDF is too complex...'}
    elif isinstance(exception, PasswordError):
        return {'type': 'encrypted', 'user_message': 'Please decrypt...'}
    elif isinstance(exception, PdfError):
        return {'type': 'invalid_pdf', 'user_message': 'Not a valid PDF...'}
    elif pdf and not pdf.Root.get('/StructTreeRoot'):
        return {'type': 'missing_features', 'user_message': 'No accessibility tags...'}
    else:
        return {'type': 'unknown', 'user_message': 'An error occurred...'}
```

### Decision 5: Extraction Data Model

**Decision**: Use Python dataclasses for extraction results (not Django models for MVP).

**Rationale**:
- Results stored in Django cache (in-memory), not database
- Dataclasses provide type safety and serialization
- Simpler than Django models for non-persistent data
- Easy to serialize to JSON for future API
- Supports future migration to database models (FR-013)

**Data Classes**:

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ImageReference:
    page_number: int
    alt_text: Optional[str]
    actual_text: Optional[str]
    position: Optional[dict] = None  # {x, y, width, height}

@dataclass
class StructureElement:
    element_type: str  # H1, P, Figure, Table, etc.
    depth: int
    alt_text: Optional[str] = None
    actual_text: Optional[str] = None
    title: Optional[str] = None
    lang: Optional[str] = None
    children: List['StructureElement'] = field(default_factory=list)

@dataclass
class ExtractionResult:
    success: bool
    pdf_filename: str
    page_count: int
    file_size_bytes: int
    
    # Extracted features
    has_structure_tree: bool
    is_tagged: bool
    document_language: Optional[str]
    document_title: Optional[str]
    
    images: List[ImageReference] = field(default_factory=list)
    structure_tree: Optional[StructureElement] = None
    
    # Errors and warnings
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
```

## PDF Accessibility Structure Reference

### Relevant PDF Specification Sections

**ISO 32000-1:2008 (PDF 1.7)**:
- Section 14.7: Logical Structure (Tagged PDF)
- Section 14.7.2: Structure Hierarchy
- Section 14.7.3: Structure Types
- Section 14.8: Marked Content
- Section 14.9: Accessibility Support

### Key PDF Objects for Extraction

| Object | Location | Purpose |
|--------|----------|---------|
| `/StructTreeRoot` | `pdf.Root` | Root of structure tree |
| `/MarkInfo` | `pdf.Root` | Tagged PDF marker with `/Marked` boolean |
| `/RoleMap` | `/StructTreeRoot` | Maps custom to standard structure types |
| `/K` | Structure elements | Children array (defines reading order) |
| `/S` | Structure elements | Structure type (H1, P, Figure, etc.) |
| `/Alt` | Structure elements | Alternative text (IMAGE ALT TEXT) |
| `/ActualText` | Structure elements | Replacement text |
| `/Lang` | `pdf.Root` or elements | Language code |
| `/Title` | `pdf.docinfo` | Document title (legacy) |

### Standard Structure Types (Table 323 in PDF Spec)

**Document Level**: Document, Part, Art, Sect, Div  
**Headings**: H, H1, H2, H3, H4, H5, H6  
**Paragraphs**: P  
**Lists**: L (list), LI (list item), Lbl (label), LBody (body)  
**Tables**: Table, TR (row), TH (header), TD (cell), THead, TBody, TFoot  
**Figures**: Figure (contains `/Alt` for image alt text)  
**Inline**: Span, Quote, Note, Reference, BibEntry, Code

### Reading Order Determination

Reading order is determined by **pre-order depth-first traversal** of the structure tree:
1. Visit structure element
2. Process `/K` children left-to-right
3. Recurse on each child
4. Order of children in `/K` array defines reading sequence

## Implementation Notes

### Handling Missing Features vs Corrupted Tags

```python
# Missing: No structure tree at all
if not pdf.Root.get('/StructTreeRoot'):
    return ExtractionResult(
        success=True,  # Success, just no features
        has_structure_tree=False,
        errors=[],
        warnings=['PDF has no accessibility tags']
    )

# Corrupted: Structure tree exists but throws during traversal
try:
    structure = traverse_tree(struct_tree_root)
except Exception as e:
    return ExtractionResult(
        success=True,  # Partial success
        has_structure_tree=True,
        structure_tree=None,  # Failed to extract
        errors=[f'Corrupted accessibility tags: {str(e)}'],
        warnings=[]
    )
```

### Encryption Detection

```python
# Check is_encrypted property
if pdf.is_encrypted:
    return {'error': 'encrypted'}

# Also catch PasswordError on open
try:
    pdf = pikepdf.Pdf.open(path)
except PasswordError:
    return {'error': 'encrypted'}
```

### Large File Warnings

```python
import os

file_size = os.path.getsize(pdf_path)
warnings = []

if file_size > 10 * 1024 * 1024:  # 10MB
    warnings.append(f'Large file ({file_size // 1024 // 1024}MB) may take longer')

if file_size > 50 * 1024 * 1024:  # 50MB
    warnings.append('Very large file - extraction may timeout')
```

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Timeout on large PDFs | User cannot extract | Clear error message; future async processing |
| Proprietary structure types | Incomplete extraction | Use `/RoleMap` to map to standard types; document limitations |
| Deeply nested structures | Stack overflow or timeout | Limit recursion depth to 20 levels |
| Memory exhaustion (huge PDFs) | Process crash | Timeout kills process; warn on large files |
| Cross-platform timeout (Windows) | Feature unavailable on Windows | Implement threading fallback |

## Testing Strategy

### Test Fixtures Required

1. **Valid tagged PDF** - All features present (alt text, headings, reading order)
2. **Untagged PDF** - No structure tree
3. **Partially tagged PDF** - Structure tree but missing alt text on images
4. **Encrypted PDF** - Password protected
5. **Corrupted tags PDF** - Malformed structure tree
6. **Large PDF** - 100+ pages to test timeout
7. **Custom role map PDF** - Non-standard structure types

### Unit Tests

- `test_extract_alt_text()` - Verify alt text extraction from Figure elements
- `test_extract_structure_types()` - Verify H1, P, Table, etc. detection
- `test_reading_order()` - Verify tree traversal order matches expected sequence
- `test_encrypted_detection()` - Verify `is_encrypted` catches password PDFs
- `test_missing_structure_tree()` - Verify graceful handling of untagged PDFs
- `test_corrupted_tags()` - Verify partial extraction on malformed tags
- `test_timeout()` - Mock slow PDF to trigger timeout
- `test_metadata_extraction()` - Verify language and title extraction

### Integration Tests

- Upload → Extract → Display (full flow)
- Error rendering for each error type
- Cache expiration (1 hour)
- View toggle (simple/detailed)

## References

- **pikepdf documentation**: https://pikepdf.readthedocs.io/
- **PDF 1.7 specification**: ISO 32000-1:2008
- **qpdf documentation**: https://qpdf.readthedocs.io/
- **PDF/UA standard**: ISO 14289-1:2014 (future reference for full compliance)
