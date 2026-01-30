from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
import pdfplumber
import os

from .serializers import RegisterSerializer,DocumentUploadSerializer,DocumentListSerializer
from .models import Document

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User registered successfully",
                    "email": user.email
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

class verifyuser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({

        "message": "you are authenticated , below are your details",
        "email" : request.user.email,
        "name":request.user.name
        },
        status = status.HTTP_200_OK
        )
        

class uploaddocument(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self,request):

        data = request.data.copy()

        if "title" not in data:
            data["title"] = request.FILES["file"].name

        serializer = DocumentUploadSerializer(data=data)
        if serializer.is_valid():
            document = serializer.save(uploaded_by = request.user)
        
            return Response({
                "message":"File uploaded successfully",
                "title":document.title,
                "id": document.id,
                "Uploaded_by" : document.uploaded_by.email
            },
            status = status.HTTP_202_ACCEPTED
            )
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

class Get_My_Documents(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        
        Documents = Document.objects.filter(uploaded_by = request.user)
        serializer = DocumentListSerializer(Documents,many = True)

        return  Response({
            "message" : "These are the files uploaded by you",
            "files":serializer.data
        },
        status = status.HTTP_200_OK
        )
        
class DeleteDocument(APIView):
    
    permission_classes = [IsAuthenticated]

    def delete(self, request, doc_id):
        document = get_object_or_404(
            Document,
            id=doc_id,
            uploaded_by=request.user   # 🔐 ownership enforced
        )

        document.delete()

        return Response(
            {
                "message": "Document deleted successfully"
            },
            status=status.HTTP_200_OK
        )
        

class textextraction(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, doc_id):
        document = get_object_or_404(
            Document,
            id=doc_id,
            uploaded_by=request.user
        )

        ext = os.path.splitext(document.file.path)[1].lower()
        if ext != ".pdf":
            return Response(
                {"error": "Only PDF files are supported"},
                status=status.HTTP_400_BAD_REQUEST
            )

        extracted_text = ""
        try:
            with pdfplumber.open(document.file.path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        extracted_text += page_text + "\n"
        except Exception:
            return Response(
                {"error": "Invalid or corrupted PDF"},
                status=status.HTTP_400_BAD_REQUEST
            )

        document.extracted_text = extracted_text
        document.save(update_fields=["extracted_text"])

        return Response(
            {
                "message": "text from your pdf has been successfully extracted",
                "document_id": document.id,
                "extracted_text":extracted_text
            },
            status=status.HTTP_201_CREATED
        )

        

from django.contrib.auth.decorators import login_required
from django.shortcuts import render






    