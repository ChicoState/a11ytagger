import base64
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
        cache.set(f"pdf_filename_{pdf_id}", pdf_file.name, timeout=3600)

        temp_path = f"/tmp/{pdf_file.name}_{pdf_id}"
        with open(temp_path, "wb") as f:
            f.write(pdf_data)

        validation = validate_pdf_file(temp_path)
        if not validation.can_proceed:
            os.remove(temp_path)
            return render(request, "server/upload.html", {
                "error": validation.errors[0] if validation.errors else "Invalid PDF",
                "warnings": validation.warnings
            })

        result = extract_accessibility_info(temp_path, pdf_file.name)
        os.remove(temp_path)

        cache.set(f"pdf_extraction_{pdf_id}", result, timeout=3600)

        return redirect("pdf_viewer", pdf_id=pdf_id)


class PDFViewerView(View):
    def get(self, request, pdf_id):
        pdf_data = cache.get(f"pdf_{pdf_id}")
        if not pdf_data:
            return redirect("pdf_upload")

        pdf_base64 = base64.b64encode(pdf_data).decode()
        pdf_data_url = f"data:application/pdf;base64,{pdf_base64}"

        extraction_result = cache.get(f"pdf_extraction_{pdf_id}")

        return render(request, "server/viewer.html", {
            "pdf_data_url": pdf_data_url,
            "pdf_id": pdf_id,
            "extraction_result": extraction_result
        })



