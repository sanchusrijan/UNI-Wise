from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import RegisterView,verifyuser,uploaddocument,Get_My_Documents,DeleteDocument,textextraction

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('verify/',verifyuser.as_view(),name = "getview"),
    path('fileupload/',uploaddocument.as_view(),name = "file_upload"),
    path('getdocuments/',Get_My_Documents.as_view(),name = "file_upload"),
    path("delete/<int:doc_id>/", DeleteDocument.as_view(), name="delete-document"),
    path("extract_text/<int:doc_id>/", textextraction.as_view(), name="text-extraction-document"),
    
    
    
    


]
