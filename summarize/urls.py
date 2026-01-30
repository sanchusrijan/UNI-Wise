from django.urls import path
from .views import SummarizeDocument
from .views import summarize_page

urlpatterns = [
    path(
        "summarizedocument/<int:doc_id>/",
        SummarizeDocument.as_view(),
        name="summarize_document"
    ),
    path("web/", summarize_page, name="summarize-page")
]