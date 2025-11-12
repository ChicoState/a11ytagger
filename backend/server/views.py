import base64
import os
from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache

from server.accessibility.validators import validate_pdf_file


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

        temp_path = f"/tmp/{pdf_file.name}_{pdf_id}"
        with open(temp_path, "wb") as f:
            f.write(pdf_data)
        
        cache.set(f"pdf_temp_path_{pdf_id}", temp_path, timeout=3600)

        validation = validate_pdf_file(temp_path)
        if not validation.can_proceed:
            os.remove(temp_path)
            return render(request, "server/upload.html", {
                "error": validation.errors[0] if validation.errors else "Invalid PDF",
                "warnings": validation.warnings
            })

        return redirect("pdf_viewer", pdf_id=pdf_id)


class PDFViewerView(View):
    def get(self, request, pdf_id):
        temp_path = cache.get(f"pdf_temp_path_{pdf_id}")
        if not temp_path or not os.path.exists(temp_path):
            return redirect("pdf_upload")

        with open(temp_path, "rb") as f:
            pdf_data = f.read()
        
        pdf_base64 = base64.b64encode(pdf_data).decode()
        pdf_data_url = f"data:application/pdf;base64,{pdf_base64}"

        return render(request, "server/viewer.html", {
            "pdf_data_url": pdf_data_url,
            "pdf_id": pdf_id
        })


class AboutView(View):
    def get(self, request):
        return render(request, "server/about.html")


class FAQView(View):
    def get(self, request):
        return render(request, "server/faq.html")

