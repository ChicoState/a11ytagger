# Quickstart: PDF Accessibility Extraction

**Feature**: PDF Accessibility Information Extraction & Display  
**Date**: 2025-10-08

## Overview

This guide helps developers implement and test the PDF accessibility extraction feature. It covers local setup, running the feature, and validating the implementation.

## Prerequisites

- Python 3.13+
- uv package manager
- Django 5.2+ (already in project)
- pikepdf 9.11+ (already in project)
- Make (for task runner)

## Local Development Setup

### 1. Install Dependencies

```bash
# From project root
make install
```

This runs `uv sync --frozen` to install all dependencies including pikepdf.

### 2. Run Migrations

```bash
make migrate
```

Note: This feature uses Django cache (no database models), but migrations may be needed for other parts of the app.

### 3. Start Development Server

```bash
make run
```

Server starts on `http://localhost:8080`

### 4. Access Upload Page

Navigate to: `http://localhost:8080/accessibility/upload/`

## Feature Walkthrough

### Upload a PDF

1. Click "Choose File" and select a PDF
2. Click "Analyze PDF"
3. System validates PDF:
   - ✅ Valid PDF → Extraction starts
   - ❌ Encrypted → Error message shown
   - ❌ Invalid → Error message shown
4. Extraction runs (max 10 seconds)
5. Redirect to results page

### View Results (Simple View)

Default view shows high-level summary:

```
Summary
- Total Images: 5
- Images with Alt Text: 3 (60%)
- Images Missing Alt Text: 2 (40%)

Document Structure
- Has Structure Tags: Yes
- Tagged PDF: Yes
- Structure Types: H1, H2, P, L, Figure
- Document Title: "Example Document"
- Language: en-US
```

### Toggle to Detailed View

Click "Detailed View" button to see:

- Full list of all images with page numbers and alt text
- Complete structure tree hierarchy
- Reading order visualization
- Technical metadata

## Testing the Feature

### Test with Sample PDFs

Create test fixtures in `tests/fixtures/sample_pdfs/`:

1. **tagged.pdf** - PDF with accessibility features
2. **untagged.pdf** - PDF without accessibility features
3. **encrypted.pdf** - Password-protected PDF
4. **large.pdf** - 50+ page PDF (for timeout testing)
5. **corrupted.pdf** - Malformed structure tree

### Run Unit Tests

```bash
# Run all tests
make test

# Run specific test file
uv run python manage.py test server.tests.test_extractor

# Run specific test
uv run python manage.py test server.tests.test_extractor.TestExtractor.test_extract_alt_text
```

### Run Integration Tests

```bash
# Test full upload → extract → display flow
uv run python manage.py test server.tests.test_extraction_flow
```

### Manual Testing Checklist

- [ ] Upload valid tagged PDF → See extraction results
- [ ] Upload untagged PDF → See "no accessibility tags" message
- [ ] Upload encrypted PDF → See encryption error
- [ ] Upload invalid file → See validation error
- [ ] Toggle between simple/detailed views
- [ ] Wait 1 hour → Access expired results → See cache miss error
- [ ] Upload large PDF (>10MB) → See warning banner

## Directory Structure

```
server/
├── accessibility/              # NEW: Extraction library
│   ├── __init__.py
│   ├── extractor.py           # Core extraction logic
│   ├── models.py              # Dataclasses (ImageReference, etc.)
│   └── validators.py          # PDF validation
├── views.py                   # UPDATE: Add CBVs
├── urls.py                    # UPDATE: Add routes
└── models.py                  # No changes (cache only)

templates/server/
├── accessibility_upload.html   # NEW: Upload form
├── extraction_results.html     # NEW: Results display
├── extraction_error.html       # NEW: Error page
└── partials/
    └── structure_node.html     # NEW: Recursive tree node

tests/
├── unit/
│   ├── test_extractor.py      # NEW: Extractor tests
│   ├── test_validators.py     # NEW: Validator tests
│   └── test_models.py         # NEW: Dataclass tests
├── integration/
│   └── test_extraction_flow.py # NEW: End-to-end tests
└── fixtures/
    └── sample_pdfs/           # NEW: Test PDFs
```

## Implementation Steps

### Step 1: Create Extraction Library

**File**: `server/accessibility/__init__.py`

```python
# Empty file to make it a package
```

**File**: `server/accessibility/models.py`

```python
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class ImageReference:
    page_number: int
    alt_text: Optional[str]
    actual_text: Optional[str]
    has_alt_text: bool

@dataclass
class StructureElement:
    element_type: str
    depth: int
    reading_order_index: int
    alt_text: Optional[str] = None
    actual_text: Optional[str] = None
    title: Optional[str] = None
    lang: Optional[str] = None
    children: List['StructureElement'] = field(default_factory=list)
    parent_type: Optional[str] = None

@dataclass
class ExtractionResult:
    pdf_filename: str
    extraction_timestamp: datetime
    cache_key: str
    expires_at: datetime
    page_count: int
    file_size_bytes: int
    pdf_version: str
    success: bool
    has_structure_tree: bool
    is_tagged: bool
    is_encrypted: bool = False
    timed_out: bool = False
    document_language: Optional[str] = None
    document_title: Optional[str] = None
    structure_tree: Optional[StructureElement] = None
    images: List[ImageReference] = field(default_factory=list)
    total_images: int = 0
    images_with_alt_text: int = 0
    images_without_alt_text: int = 0
    structure_types_found: List[str] = field(default_factory=list)
    max_heading_level: Optional[int] = None
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
```

**File**: `server/accessibility/validators.py`

```python
import pikepdf
from pikepdf import PdfError, PasswordError
from dataclasses import dataclass, field
from typing import List
from enum import Enum

class ValidationStatus(Enum):
    VALID = "valid"
    INVALID = "invalid"
    ENCRYPTED = "encrypted"
    WARNING = "warning"

@dataclass
class ValidationResult:
    status: ValidationStatus
    can_proceed: bool
    file_size_bytes: int
    is_valid_pdf: bool
    is_encrypted: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

def validate_pdf_file(file_path):
    """Validate PDF file before extraction"""
    result = ValidationResult(
        status=ValidationStatus.VALID,
        can_proceed=True,
        file_size_bytes=0,
        is_valid_pdf=False,
        is_encrypted=False
    )
    
    # Check file size
    import os
    result.file_size_bytes = os.path.getsize(file_path)
    
    if result.file_size_bytes > 10 * 1024 * 1024:  # 10MB
        result.warnings.append(f"Large file ({result.file_size_bytes // 1024 // 1024}MB) may take longer")
        result.status = ValidationStatus.WARNING
    
    # Try opening PDF
    try:
        pdf = pikepdf.Pdf.open(file_path)
        result.is_valid_pdf = True
        
        if pdf.is_encrypted:
            result.is_encrypted = True
            result.status = ValidationStatus.ENCRYPTED
            result.can_proceed = False
            result.errors.append("PDF is encrypted. Please decrypt before uploading.")
        
        pdf.close()
    
    except PasswordError:
        result.is_encrypted = True
        result.status = ValidationStatus.ENCRYPTED
        result.can_proceed = False
        result.errors.append("PDF is password-protected.")
    
    except PdfError as e:
        result.is_valid_pdf = False
        result.status = ValidationStatus.INVALID
        result.can_proceed = False
        result.errors.append(f"Invalid PDF: {str(e)}")
    
    return result
```

**File**: `server/accessibility/extractor.py`

```python
import pikepdf
from datetime import datetime, timedelta
import signal
from contextlib import contextmanager
from .models import ExtractionResult, ImageReference, StructureElement

class ExtractionTimeout(Exception):
    pass

@contextmanager
def timeout(seconds):
    def handler(signum, frame):
        raise ExtractionTimeout()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

def extract_accessibility_info(pdf_path, filename, timeout_seconds=10):
    """Extract accessibility information from PDF"""
    result = ExtractionResult(
        pdf_filename=filename,
        extraction_timestamp=datetime.now(),
        cache_key="",  # Set by caller
        expires_at=datetime.now() + timedelta(hours=1),
        page_count=0,
        file_size_bytes=0,
        pdf_version="",
        success=False,
        has_structure_tree=False,
        is_tagged=False
    )
    
    try:
        with timeout(timeout_seconds):
            pdf = pikepdf.Pdf.open(pdf_path)
            
            # Basic info
            result.page_count = len(pdf.pages)
            result.pdf_version = pdf.pdf_version
            
            # Check encryption
            if pdf.is_encrypted:
                result.is_encrypted = True
                result.errors.append("PDF is encrypted")
                return result
            
            # Check for structure tree
            struct_tree_root = pdf.Root.get('/StructTreeRoot')
            result.has_structure_tree = struct_tree_root is not None
            
            # Check if marked as tagged
            mark_info = pdf.Root.get('/MarkInfo')
            result.is_tagged = bool(mark_info and mark_info.get('/Marked'))
            
            # Extract metadata
            result.document_language = str(pdf.Root.get('/Lang')) if pdf.Root.get('/Lang') else None
            result.document_title = str(pdf.docinfo.get('/Title')) if pdf.docinfo.get('/Title') else None
            
            # Extract structure tree if present
            if struct_tree_root:
                result.structure_tree = extract_structure_tree(struct_tree_root)
                result.images = extract_images_from_tree(result.structure_tree)
            
            result.success = True
            pdf.close()
    
    except ExtractionTimeout:
        result.timed_out = True
        result.errors.append("Extraction timed out")
    
    except Exception as e:
        result.errors.append(f"Extraction error: {str(e)}")
    
    return result

def extract_structure_tree(struct_tree_root):
    """Recursively extract structure tree"""
    # Implementation from research.md
    # Traverse /K children, extract /S types, /Alt text, etc.
    pass

def extract_images_from_tree(structure_element):
    """Extract all images from structure tree"""
    images = []
    # Recursively find Figure elements with /Alt text
    pass
```

### Step 2: Create Django Views

**File**: `server/views.py` (add these classes)

```python
from django.views import View
from django.shortcuts import render, redirect
from django.core.cache import cache
from server.accessibility.validators import validate_pdf_file
from server.accessibility.extractor import extract_accessibility_info
import hashlib
import time

class PDFAccessibilityUploadView(View):
    def get(self, request):
        return render(request, 'server/accessibility_upload.html')
    
    def post(self, request):
        pdf_file = request.FILES.get('pdf_file')
        if not pdf_file:
            return render(request, 'server/accessibility_upload.html', {
                'error_type': 'invalid',
                'error_message': 'No file uploaded'
            })
        
        # Save temporarily
        temp_path = f'/tmp/{pdf_file.name}'
        with open(temp_path, 'wb') as f:
            for chunk in pdf_file.chunks():
                f.write(chunk)
        
        # Validate
        validation = validate_pdf_file(temp_path)
        if not validation.can_proceed:
            return render(request, 'server/accessibility_upload.html', {
                'error_type': validation.status.value,
                'error_message': validation.errors[0] if validation.errors else 'Validation failed',
                'warnings': validation.warnings
            })
        
        # Extract
        result = extract_accessibility_info(temp_path, pdf_file.name)
        
        # Cache result
        cache_key = f"pdf_extraction:{hashlib.md5(pdf_file.name.encode()).hexdigest()[:8]}:{int(time.time())}"
        result.cache_key = cache_key
        cache.set(cache_key, result, timeout=3600)
        
        return redirect('extraction_results', cache_key=cache_key)

class ExtractionResultsView(View):
    def get(self, request, cache_key):
        result = cache.get(cache_key)
        
        if not result:
            return render(request, 'server/extraction_error.html', {
                'error_type': 'cache_miss',
                'error_message': 'Results not found or expired'
            }, status=404)
        
        view_mode = request.GET.get('view', 'simple')
        
        return render(request, 'server/extraction_results.html', {
            'result': result,
            'view_mode': view_mode
        })
```

### Step 3: Add URL Routes

**File**: `server/urls.py` (add these patterns)

```python
from django.urls import path
from server.views import PDFAccessibilityUploadView, ExtractionResultsView

urlpatterns = [
    # ... existing patterns ...
    path('accessibility/upload/', PDFAccessibilityUploadView.as_view(), name='pdf_accessibility_upload'),
    path('accessibility/results/<str:cache_key>/', ExtractionResultsView.as_view(), name='extraction_results'),
]
```

### Step 4: Create Templates

See contracts/extraction-api.md for full template examples.

## Troubleshooting

### Timeout on Windows

If `signal.alarm()` doesn't work on Windows, implement threading fallback:

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
    return result[0]
```

### Cache Not Working

Verify Django cache settings:

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'pdf-extraction-cache',
    }
}
```

### Large Files Causing Memory Issues

Monitor memory usage:

```bash
# Linux
watch -n 1 'ps aux | grep python'

# macOS
watch -n 1 'ps aux | grep python'
```

If memory exceeds limits, add explicit cleanup:

```python
import gc

# After extraction
pdf.close()
gc.collect()
```

## Next Steps

1. Implement extraction logic (follow research.md patterns)
2. Create test fixtures
3. Write unit tests
4. Write integration tests
5. Create templates
6. Manual testing with real PDFs
7. Performance testing with large PDFs
8. Document any edge cases discovered

## References

- [research.md](research.md) - Technical decisions and pikepdf patterns
- [data-model.md](data-model.md) - Data structure details
- [contracts/extraction-api.md](contracts/extraction-api.md) - View and template contracts
- [Constitution](../../.specify/memory/constitution.md) - Project principles
