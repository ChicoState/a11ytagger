# Data Model: PDF Accessibility Extraction

**Feature**: PDF Accessibility Information Extraction & Display  
**Date**: 2025-10-08

## Overview

This feature uses Python dataclasses for in-memory data representation (not Django models). Results are stored in Django's cache framework for 1-hour retention. The model supports future migration to database persistence per FR-013.

## Core Entities

### 1. ImageReference

Represents an image object found in the PDF with its accessibility information.

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class ImageReference:
    """Reference to an image in the PDF with accessibility metadata"""
    
    page_number: int                    # 1-based page number
    alt_text: Optional[str]             # /Alt text from Figure element
    actual_text: Optional[str]          # /ActualText if present
    has_alt_text: bool                  # Quick check for missing alt text
    
    # Optional position data (for future enhancement)
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
```

**Validation Rules**:
- `page_number` must be >= 1
- `has_alt_text` is True if `alt_text` is not None and not empty string
- `alt_text` and `actual_text` are mutually exclusive in practice (use alt_text first)

**Lifecycle**:
- Created during structure tree traversal when `/Figure` element encountered
- Stored in `ExtractionResult.images` list
- Retained in cache for 1 hour
- No persistence to database in MVP

### 2. StructureElement

Represents a single element in the PDF structure tree hierarchy.

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class StructureElement:
    """A node in the PDF structure tree"""
    
    element_type: str                       # H1, P, Figure, Table, etc.
    depth: int                              # Nesting level (0 = root)
    reading_order_index: int                # Pre-order traversal index
    
    # Optional accessibility metadata
    alt_text: Optional[str] = None          # /Alt text (images)
    actual_text: Optional[str] = None       # /ActualText replacement
    title: Optional[str] = None             # /T title
    lang: Optional[str] = None              # /Lang language override
    
    # Tree structure
    children: List['StructureElement'] = field(default_factory=list)
    parent_type: Optional[str] = None       # Parent element type (for context)
```

**Validation Rules**:
- `element_type` should match standard PDF structure types or be mapped via RoleMap
- `depth` must be >= 0 and <= 20 (recursion limit)
- `reading_order_index` is unique within tree (assigned during traversal)
- `children` forms a tree structure (no cycles)

**Relationships**:
- **Parent-Child**: Each element has 0-N children via `children` list
- **Sibling Order**: Order in parent's `children` list defines reading sequence
- **Type Hierarchy**: Standard types (H1-H6, P, L, Table, Figure, etc.)

**State Transitions**:
1. **Created**: During tree traversal when structure element encountered
2. **Populated**: Metadata fields filled from PDF object
3. **Linked**: Added to parent's children list
4. **Indexed**: `reading_order_index` assigned

### 3. ExtractionResult

The complete output of PDF accessibility extraction.

```python
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class ExtractionResult:
    """Complete accessibility extraction result for a PDF"""
    
    # Metadata
    pdf_filename: str
    extraction_timestamp: datetime
    cache_key: str                          # For Django cache storage
    expires_at: datetime                    # 1 hour from extraction
    
    # PDF properties
    page_count: int
    file_size_bytes: int
    pdf_version: str                        # e.g., "1.7"
    
    # Status flags
    success: bool                           # Overall extraction success
    has_structure_tree: bool                # /StructTreeRoot exists
    is_tagged: bool                         # /MarkInfo /Marked = true
    is_encrypted: bool = False              # Password protected
    timed_out: bool = False                 # Exceeded 10-second limit
    
    # Extracted accessibility features
    document_language: Optional[str] = None # /Lang from Root
    document_title: Optional[str] = None    # /Title from DocInfo
    structure_tree: Optional[StructureElement] = None
    images: List[ImageReference] = field(default_factory=list)
    
    # Analysis summary (for simple view)
    total_images: int = 0
    images_with_alt_text: int = 0
    images_without_alt_text: int = 0
    structure_types_found: List[str] = field(default_factory=list)  # Unique types
    max_heading_level: Optional[int] = None  # Highest H level (1-6)
    
    # Errors and warnings
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Compute summary fields after initialization"""
        self.total_images = len(self.images)
        self.images_with_alt_text = sum(1 for img in self.images if img.has_alt_text)
        self.images_without_alt_text = self.total_images - self.images_with_alt_text
        
        if self.structure_tree:
            self.structure_types_found = self._collect_unique_types(self.structure_tree)
            self.max_heading_level = self._find_max_heading_level(self.structure_tree)
    
    def _collect_unique_types(self, element: StructureElement) -> List[str]:
        """Recursively collect unique structure types"""
        types = {element.element_type}
        for child in element.children:
            types.update(self._collect_unique_types(child))
        return sorted(list(types))
    
    def _find_max_heading_level(self, element: StructureElement) -> Optional[int]:
        """Find highest heading level (H1=1, H6=6)"""
        max_level = None
        
        if element.element_type.startswith('H'):
            try:
                level = int(element.element_type[1:]) if len(element.element_type) > 1 else 1
                max_level = level
            except ValueError:
                pass
        
        for child in element.children:
            child_max = self._find_max_heading_level(child)
            if child_max is not None:
                max_level = max(max_level or 0, child_max)
        
        return max_level
```

**Validation Rules**:
- `success` is False if `is_encrypted`, `timed_out`, or critical error occurred
- `has_structure_tree` is False if `/StructTreeRoot` is None
- `is_tagged` requires both `/MarkInfo` and `/Marked = true`
- `expires_at` must be exactly 1 hour after `extraction_timestamp`
- `cache_key` format: `pdf_extraction:{filename}:{timestamp_hash}`

**Lifecycle**:
1. **Created**: After PDF validation passes
2. **Populated**: During extraction process (tree traversal, image collection)
3. **Summarized**: `__post_init__` computes summary fields
4. **Cached**: Stored in Django cache with 1-hour TTL
5. **Retrieved**: Fetched from cache for display
6. **Expired**: Automatically removed after 1 hour

### 4. ValidationResult

Result of pre-flight PDF validation before extraction.

```python
from dataclasses import dataclass
from typing import List
from enum import Enum

class ValidationStatus(Enum):
    VALID = "valid"
    INVALID = "invalid"
    ENCRYPTED = "encrypted"
    WARNING = "warning"

@dataclass
class ValidationResult:
    """Result of PDF pre-flight validation"""
    
    status: ValidationStatus
    can_proceed: bool               # Can extraction proceed?
    
    file_size_bytes: int
    is_valid_pdf: bool
    is_encrypted: bool
    
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
```

**Validation Rules**:
- `can_proceed` is True only if `status` is VALID or WARNING
- `status` is ENCRYPTED if `is_encrypted` is True
- `status` is INVALID if `is_valid_pdf` is False
- Large file warnings added if `file_size_bytes > 10MB`

**Lifecycle**:
1. **Created**: Immediately after file upload
2. **Validated**: PDF opened and checked
3. **Returned**: To view for decision (proceed or reject)
4. **Discarded**: Not cached (ephemeral)

## Entity Relationships

```
ExtractionResult (1)
├── images (0..N) → ImageReference
│   ├── page_number: int
│   ├── alt_text: Optional[str]
│   └── has_alt_text: bool
│
├── structure_tree (0..1) → StructureElement
│   ├── element_type: str
│   ├── depth: int
│   ├── children (0..N) → StructureElement (recursive)
│   └── metadata fields
│
├── errors (0..N) → str
├── warnings (0..N) → str
└── summary fields (computed)
```

## Storage Strategy

### MVP: Django Cache (In-Memory)

```python
from django.core.cache import cache
import hashlib
from datetime import datetime, timedelta

def cache_extraction_result(result: ExtractionResult) -> str:
    """Store extraction result in cache for 1 hour"""
    
    # Generate cache key
    cache_key = f"pdf_extraction:{result.pdf_filename}:{hash(result.extraction_timestamp)}"
    result.cache_key = cache_key
    result.expires_at = result.extraction_timestamp + timedelta(hours=1)
    
    # Store with 1-hour TTL
    cache.set(cache_key, result, timeout=3600)
    
    return cache_key

def retrieve_extraction_result(cache_key: str) -> Optional[ExtractionResult]:
    """Retrieve extraction result from cache"""
    return cache.get(cache_key)
```

**Cache Configuration** (Django settings):
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'pdf-extraction-cache',
        'OPTIONS': {
            'MAX_ENTRIES': 1000,  # Limit cache size
        }
    }
}
```

### Future: Database Persistence (FR-013)

When migrating to persistent storage, convert dataclasses to Django models:

```python
# Future models.py (not implemented in MVP)
from django.db import models
import json

class PDFExtractionResult(models.Model):
    # Metadata
    pdf_filename = models.CharField(max_length=255)
    extraction_timestamp = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=40, null=True)  # Future session support
    
    # PDF properties
    page_count = models.IntegerField()
    file_size_bytes = models.BigIntegerField()
    pdf_version = models.CharField(max_length=10)
    
    # Status
    success = models.BooleanField()
    has_structure_tree = models.BooleanField()
    is_tagged = models.BooleanField()
    
    # Extracted data (JSON fields)
    structure_tree_json = models.JSONField(null=True)
    images_json = models.JSONField(default=list)
    
    # Summary
    total_images = models.IntegerField(default=0)
    images_with_alt_text = models.IntegerField(default=0)
    
    # Errors/warnings
    errors_json = models.JSONField(default=list)
    warnings_json = models.JSONField(default=list)
    
    class Meta:
        indexes = [
            models.Index(fields=['session_key', 'extraction_timestamp']),
        ]
```

## Data Validation

### Input Validation (Upload)

```python
def validate_uploaded_file(file) -> ValidationResult:
    """Validate uploaded PDF file before extraction"""
    
    result = ValidationResult(
        status=ValidationStatus.VALID,
        can_proceed=True,
        file_size_bytes=file.size,
        is_valid_pdf=False,
        is_encrypted=False
    )
    
    # Check file size (soft limit - warn only)
    if file.size > 10 * 1024 * 1024:  # 10MB
        result.warnings.append(f"Large file ({file.size // 1024 // 1024}MB) may take longer to process")
        result.status = ValidationStatus.WARNING
    
    if file.size > 50 * 1024 * 1024:  # 50MB
        result.warnings.append("Very large file - extraction may timeout")
    
    # Try opening PDF
    try:
        pdf = pikepdf.Pdf.open(file)
        result.is_valid_pdf = True
        
        # Check encryption
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
        result.errors.append("PDF is password-protected. Please decrypt before uploading.")
    
    except PdfError as e:
        result.is_valid_pdf = False
        result.status = ValidationStatus.INVALID
        result.can_proceed = False
        result.errors.append(f"Invalid PDF: {str(e)}")
    
    return result
```

### Output Validation (Extraction)

```python
def validate_extraction_result(result: ExtractionResult) -> bool:
    """Validate extraction result before caching"""
    
    # Required fields
    assert result.pdf_filename, "pdf_filename is required"
    assert result.extraction_timestamp, "extraction_timestamp is required"
    assert result.page_count >= 0, "page_count must be non-negative"
    assert result.file_size_bytes >= 0, "file_size_bytes must be non-negative"
    
    # Summary consistency
    assert result.total_images == len(result.images), "total_images mismatch"
    assert result.images_with_alt_text <= result.total_images, "images_with_alt_text cannot exceed total"
    
    # Status consistency
    if result.is_encrypted:
        assert not result.success, "Encrypted PDFs should not succeed"
    
    if result.timed_out:
        assert not result.success, "Timed out extractions should not succeed"
    
    return True
```

## Migration Path (Future)

To support session-based persistence per FR-013:

1. **Add Session Model**: Create `PDFExtractionSession` model
2. **Convert Dataclasses**: Serialize dataclasses to JSON for storage
3. **Update Cache Logic**: Store session reference in cache, data in DB
4. **Add Cleanup Task**: Celery task to purge old sessions
5. **File Storage**: Store large PDFs on disk instead of memory

**Migration steps** (not implemented in MVP):
```python
# 1. Create migration
python manage.py makemigrations

# 2. Update cache_extraction_result to also save to DB
def cache_extraction_result_with_persistence(result: ExtractionResult, session_key: str):
    # Cache for fast access
    cache_key = cache_extraction_result(result)
    
    # Also persist to DB
    PDFExtractionResult.objects.create(
        pdf_filename=result.pdf_filename,
        session_key=session_key,
        structure_tree_json=dataclass_to_dict(result.structure_tree),
        images_json=[dataclass_to_dict(img) for img in result.images],
        # ... other fields
    )
    
    return cache_key
```
