from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.conf import settings


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    auth_provider = models.CharField(max_length=200, default=email)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email


class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/")
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title