from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CloudUser, CloudFile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CloudUser
        fields = ['id', 'username', 'full_name', 'email', 'password']
    
    def create(self, validated_data):
        user = CloudUser(
            username=validated_data['username'],
            full_name=validated_data['full_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные данные для входа.")

class CloudFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudFile
        fields = '__all__'
        read_only_fields = ['upload_date', 'last_download_date']
