from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


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
    path("accounts/login/", login_page, name="login"),
    path("accounts/register/", register_page, name="register"),
    path("users/home/", home_page, name="home"),
    path("users/upload/", upload_page, name="upload-page"),
    path("api/users/", include("users.urls")),
    path("summarize/", include("summarize.urls")),
]

