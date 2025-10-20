# API Contract: PDF Accessibility Extraction

**Feature**: PDF Accessibility Information Extraction & Display  
**Date**: 2025-10-08  
**Type**: Web Application (Django Views)

## Overview

This feature exposes two primary user interactions through Django class-based views:
1. PDF upload and validation
2. Extraction results display (dual-view: simple/detailed)

Since this is a Django web application (not a REST API), the "contract" is defined by:
- URL routes
- Form submissions
- Template contexts
- Cache keys

## URL Routes

```python
# server/urls.py
from django.urls import path
from server.views import PDFAccessibilityUploadView, ExtractionResultsView

urlpatterns = [
    # Upload page
    path('accessibility/upload/', 
         PDFAccessibilityUploadView.as_view(), 
         name='pdf_accessibility_upload'),
    
    # Results page
    path('accessibility/results/<str:cache_key>/', 
         ExtractionResultsView.as_view(), 
         name='extraction_results'),
]
```

## View Contracts

### 1. PDFAccessibilityUploadView

**Purpose**: Handle PDF file upload, validation, and extraction trigger.

**HTTP Methods**:
- `GET`: Display upload form
- `POST`: Accept PDF upload, validate, extract, redirect to results

**Request (GET)**:
```
GET /accessibility/upload/
Accept: text/html
```

**Response (GET)**:
```html
HTTP/1.1 200 OK
Content-Type: text/html

<!-- Template: server/accessibility_upload.html -->
<form method="post" enctype="multipart/form-data">
    <input type="file" name="pdf_file" accept="application/pdf" required>
    <button type="submit">Analyze PDF</button>
</form>
```

**Request (POST)**:
```
POST /accessibility/upload/
Content-Type: multipart/form-data
Cookie: csrftoken=...

------WebKitFormBoundary
Content-Disposition: form-data; name="pdf_file"; filename="document.pdf"
Content-Type: application/pdf

[PDF binary data]
------WebKitFormBoundary--
```

**Response (POST - Success)**:
```
HTTP/1.1 302 Found
Location: /accessibility/results/{cache_key}/
```

**Response (POST - Validation Error)**:
```html
HTTP/1.1 200 OK
Content-Type: text/html

<!-- Template: server/accessibility_upload.html with error context -->
<div class="error">
    <strong>Error:</strong> PDF is encrypted. Please decrypt before uploading.
</div>
```

**Response (POST - Timeout)**:
```html
HTTP/1.1 200 OK
Content-Type: text/html

<div class="error">
    <strong>Timeout:</strong> PDF is too complex for processing.
    Please try a smaller document.
</div>
```

**Template Context (GET)**:
```python
{
    'form': PDFUploadForm(),  # Django form
}
```

**Template Context (POST - Error)**:
```python
{
    'form': PDFUploadForm(),
    'error_type': 'encrypted' | 'invalid_pdf' | 'timeout' | 'unknown',
    'error_message': str,  # User-friendly message
    'warnings': List[str],  # Optional warnings (large file, etc.)
}
```

**Business Logic**:
1. Validate uploaded file is PDF
2. Check file size (warn if > 10MB, very large if > 50MB)
3. Detect encryption → reject with error
4. Run extraction with 10-second timeout
5. Cache result with 1-hour TTL
6. Redirect to results view with cache key

### 2. ExtractionResultsView

**Purpose**: Display extraction results in simple or detailed view.

**HTTP Methods**:
- `GET`: Display results (with optional view mode parameter)

**Request (GET - Simple View)**:
```
GET /accessibility/results/{cache_key}/
Accept: text/html
```

**Request (GET - Detailed View)**:
```
GET /accessibility/results/{cache_key}/?view=detailed
Accept: text/html
```

**Response (GET - Success)**:
```html
HTTP/1.1 200 OK
Content-Type: text/html

<!-- Template: server/extraction_results.html -->
<div class="results">
    <h1>Accessibility Analysis: document.pdf</h1>
    
    <!-- View toggle -->
    <div class="view-toggle">
        <button data-view="simple" class="active">Simple View</button>
        <button data-view="detailed">Detailed View</button>
    </div>
    
    <!-- Simple view content -->
    <div class="simple-view">
        <div class="summary-card">
            <h2>Summary</h2>
            <p>Total Images: 5</p>
            <p>Images with Alt Text: 3</p>
            <p class="warning">Images Missing Alt Text: 2</p>
        </div>
        
        <div class="summary-card">
            <h2>Document Structure</h2>
            <p>Has Structure Tags: Yes</p>
            <p>Structure Types Found: H1, H2, P, L, Figure</p>
        </div>
    </div>
    
    <!-- Detailed view content (hidden by default) -->
    <div class="detailed-view" style="display:none;">
        <!-- Full structure tree, image list with positions, etc. -->
    </div>
</div>
```

**Response (GET - Cache Miss)**:
```html
HTTP/1.1 404 Not Found
Content-Type: text/html

<div class="error">
    <h1>Results Not Found</h1>
    <p>Extraction results have expired or were not found.</p>
    <a href="/accessibility/upload/">Upload a new PDF</a>
</div>
```

**Template Context (Simple View)**:
```python
{
    'result': ExtractionResult,  # Full extraction result
    'view_mode': 'simple',
    
    # Simple view data
    'summary': {
        'filename': str,
        'page_count': int,
        'file_size_mb': float,
        'total_images': int,
        'images_with_alt': int,
        'images_without_alt': int,
        'has_structure': bool,
        'is_tagged': bool,
        'structure_types': List[str],  # Unique types found
        'document_language': Optional[str],
        'document_title': Optional[str],
    },
    
    # Warnings/errors
    'warnings': List[str],
    'errors': List[str],
}
```

**Template Context (Detailed View)**:
```python
{
    'result': ExtractionResult,
    'view_mode': 'detailed',
    
    # Detailed view data
    'images': List[ImageReference],  # All images with full metadata
    'structure_tree': StructureElement,  # Full tree hierarchy
    'structure_tree_json': str,  # JSON for JavaScript tree rendering
    
    # Same summary as simple view
    'summary': {...},
    'warnings': List[str],
    'errors': List[str],
}
```

## Data Formats

### Cache Key Format

```python
cache_key = f"pdf_extraction:{filename_hash}:{timestamp_hash}"

# Example:
"pdf_extraction:a3f5c1d8:2025100812345"
```

**Components**:
- Prefix: `pdf_extraction:`
- Filename hash: First 8 chars of SHA256(filename)
- Timestamp hash: Unix timestamp in seconds

**Properties**:
- Unique per upload
- URL-safe (alphanumeric + underscores)
- Predictable length (~40 chars)

### Template Data Structures

**Simple Summary View** (rendered from ExtractionResult):
```html
<div class="summary-stats">
    <div class="stat">
        <span class="label">Total Images:</span>
        <span class="value">{{ summary.total_images }}</span>
    </div>
    <div class="stat {{ 'warning' if summary.images_without_alt > 0 }}">
        <span class="label">Images with Alt Text:</span>
        <span class="value">{{ summary.images_with_alt }} / {{ summary.total_images }}</span>
    </div>
    <div class="stat">
        <span class="label">Structure Tags:</span>
        <span class="value">{{ 'Yes' if summary.has_structure else 'No' }}</span>
    </div>
    <div class="stat">
        <span class="label">Tagged PDF:</span>
        <span class="value">{{ 'Yes' if summary.is_tagged else 'No' }}</span>
    </div>
</div>

<div class="structure-types">
    <h3>Structure Types Found:</h3>
    <ul>
        {% for type in summary.structure_types %}
        <li>{{ type }}</li>
        {% endfor %}
    </ul>
</div>
```

**Detailed View - Images List**:
```html
<div class="images-detail">
    <h3>Images ({{ images|length }})</h3>
    <table>
        <thead>
            <tr>
                <th>Page</th>
                <th>Alt Text</th>
                <th>Actual Text</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% for image in images %}
            <tr class="{{ 'missing-alt' if not image.has_alt_text }}">
                <td>{{ image.page_number }}</td>
                <td>{{ image.alt_text|default:"(none)" }}</td>
                <td>{{ image.actual_text|default:"—" }}</td>
                <td>
                    {% if image.has_alt_text %}
                    <span class="badge success">Has Alt Text</span>
                    {% else %}
                    <span class="badge warning">Missing Alt Text</span>
                    {% endif %}
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
```

**Detailed View - Structure Tree** (rendered as nested list):
```html
<div class="structure-tree">
    <h3>Document Structure</h3>
    <div class="tree-container">
        <!-- Recursive template include -->
        {% include "server/partials/structure_node.html" with node=structure_tree depth=0 %}
    </div>
</div>

<!-- server/partials/structure_node.html -->
<div class="structure-node" style="margin-left: {{ depth * 20 }}px;">
    <div class="node-header">
        <span class="node-type">{{ node.element_type }}</span>
        {% if node.alt_text %}
        <span class="node-alt">Alt: "{{ node.alt_text }}"</span>
        {% endif %}
        {% if node.title %}
        <span class="node-title">Title: "{{ node.title }}"</span>
        {% endif %}
    </div>
    
    {% for child in node.children %}
        {% include "server/partials/structure_node.html" with node=child depth=depth|add:1 %}
    {% endfor %}
</div>
```

## Error Handling Contract

### Error Types and Messages

| Error Type | HTTP Status | User Message | Template |
|------------|-------------|--------------|----------|
| `encrypted` | 200 (form error) | "PDF is encrypted. Please decrypt before uploading." | `accessibility_upload.html` |
| `invalid_pdf` | 200 (form error) | "File is not a valid PDF." | `accessibility_upload.html` |
| `timeout` | 200 (form error) | "PDF is too complex for processing. Please try a smaller document." | `accessibility_upload.html` |
| `cache_miss` | 404 | "Results not found or expired." | `extraction_error.html` |
| `unknown` | 500 | "An unexpected error occurred." | `extraction_error.html` |

**Error Context Structure**:
```python
{
    'error_type': str,  # One of above types
    'error_message': str,  # User-friendly message
    'error_details': Optional[str],  # Technical details (for debug mode)
    'can_retry': bool,  # Show "Try Again" button
    'suggestions': List[str],  # Actionable suggestions for user
}
```

**Example Error Context**:
```python
{
    'error_type': 'encrypted',
    'error_message': 'PDF is encrypted. Please decrypt before uploading.',
    'error_details': 'pikepdf.PasswordError: Document is encrypted',
    'can_retry': True,
    'suggestions': [
        'Open the PDF in Adobe Acrobat or similar tool',
        'Use "Save As" to create an unencrypted copy',
        'Try uploading the unencrypted version'
    ]
}
```

## Cache Contract

### Storage

**Backend**: Django LocMemCache (in-memory)  
**Timeout**: 3600 seconds (1 hour)  
**Max Entries**: 1000 results

### Cache Operations

**Set**:
```python
from django.core.cache import cache

cache_key = generate_cache_key(filename, timestamp)
cache.set(cache_key, extraction_result, timeout=3600)
```

**Get**:
```python
result = cache.get(cache_key)
if result is None:
    # Cache miss - expired or never existed
    return render(request, 'extraction_error.html', {'error_type': 'cache_miss'})
```

**Delete** (manual cleanup, not used in MVP):
```python
cache.delete(cache_key)
```

## Performance Contract

### Response Time Targets

| Operation | Target | Timeout | Notes |
|-----------|--------|---------|-------|
| Upload form (GET) | < 100ms | N/A | Static page |
| File upload + extraction (POST) | < 10s | 10s | Abort on timeout |
| Results display (GET) | < 200ms | N/A | Cache lookup + render |

### Extraction Performance

**Target**: < 10 seconds for typical PDFs (1-20 pages, < 5MB)

**Timeout Behavior**:
- Hard timeout at 10 seconds
- Process killed via `signal.alarm()` (Unix) or threading (Windows)
- Partial results discarded
- User sees timeout error with retry option

**Large File Warnings**:
- **> 10MB**: Warning banner "Large file may take longer"
- **> 50MB**: Strong warning "Very large file - may timeout"
- **> 100 pages**: Warning "Many pages - may timeout"

## Security Considerations

### File Upload Security

1. **File Type Validation**: Check magic bytes (PDF signature `%PDF-`)
2. **Size Limit**: Soft warning only (no hard limit per requirements)
3. **CSRF Protection**: Django CSRF token required on POST
4. **Filename Sanitization**: Hash filenames for cache keys
5. **Malicious PDF Protection**: Timeout prevents infinite loops; validation catches malformed PDFs

### Cache Security

1. **Cache Key Uniqueness**: Hash-based keys prevent collisions
2. **TTL Enforcement**: 1-hour expiration prevents unbounded growth
3. **No Sensitive Data**: PDFs not stored in cache (only extraction results)
4. **Session Isolation**: Future enhancement (FR-013) will add session binding

## Testing Contract

### Test Fixtures

Upload endpoints must handle these test cases:

1. **Valid tagged PDF** → 302 redirect to results
2. **Valid untagged PDF** → 302 redirect to results (with "no tags" message)
3. **Encrypted PDF** → 200 with error form
4. **Invalid PDF** → 200 with error form
5. **Timeout PDF** (mock slow extraction) → 200 with timeout error
6. **Large PDF (> 10MB)** → 302 with warning in results
7. **Cache miss** (expired results) → 404 error page

### Example Test (Django)

```python
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile

class PDFAccessibilityUploadViewTest(TestCase):
    def test_upload_encrypted_pdf_shows_error(self):
        client = Client()
        
        # Create encrypted PDF fixture
        with open('tests/fixtures/encrypted.pdf', 'rb') as f:
            pdf_file = SimpleUploadedFile('encrypted.pdf', f.read(), content_type='application/pdf')
        
        response = client.post('/accessibility/upload/', {'pdf_file': pdf_file})
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'encrypted')
        self.assertContains(response, 'Please decrypt')
    
    def test_upload_valid_pdf_redirects_to_results(self):
        client = Client()
        
        with open('tests/fixtures/tagged.pdf', 'rb') as f:
            pdf_file = SimpleUploadedFile('tagged.pdf', f.read(), content_type='application/pdf')
        
        response = client.post('/accessibility/upload/', {'pdf_file': pdf_file})
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accessibility/results/'))
```

## Future API Considerations (FR-013, FR-016)

When migrating to async processing and persistent storage:

**Async Job Submission**:
```python
# POST /api/extraction/submit
{
    "session_id": "uuid",
    "pdf_url": "https://..."  # Or file upload
}

# Response
{
    "job_id": "uuid",
    "status": "queued",
    "estimated_completion": "2025-10-08T12:35:00Z"
}
```

**Job Status Polling**:
```python
# GET /api/extraction/status/{job_id}
{
    "job_id": "uuid",
    "status": "processing" | "completed" | "failed",
    "progress_percent": 45,
    "result_url": "/api/extraction/results/{job_id}"  # When completed
}
```

**Results Retrieval**:
```python
# GET /api/extraction/results/{job_id}
{
    "success": true,
    "result": {
        "pdf_filename": "document.pdf",
        "total_images": 5,
        "images_with_alt_text": 3,
        # ... full ExtractionResult as JSON
    }
}
```
