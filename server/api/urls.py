from django.urls import path

from server.api.views import MetadataView, ImageListView, ImageDetailView, DownloadView, CleanupView

urlpatterns = [
    path('<str:pdf_id>/accessibility_metadata/', MetadataView.as_view()),
    path('<str:pdf_id>/images/', ImageListView.as_view()),
    path('<str:pdf_id>/images/<int:image_id>/', ImageDetailView.as_view()),
    path('<str:pdf_id>/download/', DownloadView.as_view()),
    path('<str:pdf_id>/cleanup/', CleanupView.as_view()),
]