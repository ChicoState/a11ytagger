import base64
from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache


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
