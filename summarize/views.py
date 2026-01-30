import pdfplumber

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from users.models import Document
from .services.summarization import summarize_text


class SummarizeDocument(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, doc_id):
        document = get_object_or_404(
            Document,
            id=doc_id,
            uploaded_by=request.user
        )

        if document.summary:
            return Response(
                {
                    "document_id": document.id,
                    "summary": document.summary,
                    "cached": True
                },
                status=status.HTTP_200_OK
            )

        
        if not document.extracted_text:
            extracted_text = ""

            with pdfplumber.open(document.file.path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        extracted_text += page_text + "\n"

            document.extracted_text = extracted_text
            document.save(update_fields=["extracted_text"])

        
        summary = summarize_text(document.extracted_text)
        document.summary = summary
        document.save(update_fields=["summary"])

        return Response(
            {
                "document_id": document.id,
                "summary": summary,
                "used_cached_text": True if document.extracted_text else False
            },
            status=status.HTTP_200_OK
        )


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services.summarization import summarize_text


# @login_required
def summarize_page(request):
    summary = None
    error = None

    if request.method == "POST":
        doc_id = request.POST.get("doc_id")

        try:
            document = Document.objects.get(
                id=doc_id,
                uploaded_by=request.user
            )
        except Document.DoesNotExist:
            error = "Document not found"
            return render(
                request,
                "summarize/summarize.html",
                {"summary": None, "error": error}
            )

        
        if document.summary:
            summary = document.summary

        else:
            
            if not document.extracted_text:
                extracted_text = ""

                with pdfplumber.open(document.file.path) as pdf:
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            extracted_text += page_text + "\n"

                document.extracted_text = extracted_text
                document.save(update_fields=["extracted_text"])

            
            summary = summarize_text(document.extracted_text)
            document.summary = summary
            document.save(update_fields=["summary"])

    return render(
        request,
        "summarize/summarize.html",
        {
            "summary": summary,
            "error": error
        }
    )