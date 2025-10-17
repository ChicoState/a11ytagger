import base64
import hashlib
import time
import os
from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache

from server.accessibility.validators import validate_pdf_file
from server.accessibility.extractor import extract_accessibility_info


def hello_world(request):
    return render(request, "server/index.html")


class PDFUploadView(View):
    def get(self, request):
        return render(request, "server/upload.html")

    def post(self, request):
        pdf_file = request.FILES.get("pdf_file")
        if not pdf_file:
            return render(request, "server/upload.html", {"error": "No file uploaded"})

        pdf_data = pdf_file.read()
        pdf_id = base64.urlsafe_b64encode(pdf_file.name.encode()).decode()[:16]

        cache.set(f"pdf_{pdf_id}", pdf_data, timeout=3600)

        return redirect("pdf_viewer", pdf_id=pdf_id)


class PDFViewerView(View):
    def get(self, request, pdf_id):
        pdf_data = cache.get(f"pdf_{pdf_id}")
        if not pdf_data:
            return redirect("pdf_upload")

        pdf_base64 = base64.b64encode(pdf_data).decode()
        pdf_data_url = f"data:application/pdf;base64,{pdf_base64}"

        return render(request, "server/viewer.html", {"pdf_data_url": pdf_data_url})


class PDFAccessibilityUploadView(View):
    def get(self, request):
        return render(request, "server/accessibility_upload.html")

    def post(self, request):
        pdf_file = request.FILES.get("pdf_file")
        if not pdf_file:
            return render(request, "server/accessibility_upload.html", {
                "error_type": "missing_file",
                "error_message": "No file uploaded"
            })

        temp_path = f"/tmp/{pdf_file.name}"
        with open(temp_path, "wb") as f:
            for chunk in pdf_file.chunks():
                f.write(chunk)

        validation = validate_pdf_file(temp_path)
        
        if validation.is_encrypted:
            os.remove(temp_path)
            return render(request, "server/accessibility_upload.html", {
                "error_type": "encrypted",
                "error_message": validation.errors[0] if validation.errors else "PDF is encrypted",
                "warnings": validation.warnings
            })
        
        if not validation.is_valid_pdf:
            os.remove(temp_path)
            return render(request, "server/accessibility_upload.html", {
                "error_type": "invalid_pdf",
                "error_message": validation.errors[0] if validation.errors else "Invalid PDF",
                "warnings": validation.warnings
            })
        
        if not validation.can_proceed:
            os.remove(temp_path)
            return render(request, "server/accessibility_upload.html", {
                "error_type": validation.status,
                "error_message": validation.errors[0] if validation.errors else "Validation failed",
                "warnings": validation.warnings
            })

        result = extract_accessibility_info(temp_path, pdf_file.name)

        os.remove(temp_path)

        cache_key = f"pdf_extraction:{hashlib.md5(pdf_file.name.encode()).hexdigest()[:8]}:{int(time.time())}"
        result.cache_key = cache_key
        cache.set(cache_key, result, timeout=3600)

        if result.timed_out:
            return render(request, "server/accessibility_upload.html", {
                "error_type": "timeout",
                "error_message": "PDF is too complex for processing. Please try a smaller document.",
                "warnings": validation.warnings
            })

        return redirect("extraction_results", cache_key=cache_key)


class ExtractionResultsView(View):
    def get(self, request, cache_key):
        result = cache.get(cache_key)

        if not result:
            return render(request, "server/extraction_error.html", {
                "error_type": "cache_miss",
                "error_message": "Results not found or expired. PDFs are retained for 1 hour."
            }, status=404)

        view_mode = request.GET.get("view", "simple")

        return render(request, "server/extraction_results.html", {
            "result": result,
            "view_mode": view_mode
        })
