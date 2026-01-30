"""
URL configuration for UNI_Wise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# ------------------
# Page views
# ------------------

def login_page(request):
    return render(request, "registration/login.html")

def register_page(request):
    return render(request, "registration/register.html")

def home_page(request):
    return render(request, "home.html")

def upload_page(request):
    return render(request, "users/upload.html")


urlpatterns = [
    path("admin/", admin.site.urls),

    # -------- PAGES (HTML) --------
    path("accounts/login/", login_page, name="login"),
    path("accounts/register/", register_page, name="register"),
    path("users/home/", home_page, name="home"),
    path("users/upload/", upload_page, name="upload-page"),

    # -------- APIs (JSON) --------
    path("api/users/", include("users.urls")),
    path("summarize/", include("summarize.urls")),
]
