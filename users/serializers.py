from rest_framework import serializers
from .models import User, Document


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ['email', 'name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )


class DocumentUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ["title", "file"]


class DocumentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ["id", "title", "file", "uploaded_at"]