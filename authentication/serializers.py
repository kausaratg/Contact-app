from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=55, min_length=8)
    first_name = serializers.CharField(max_length=55, min_length=2)
    last_name = serializers.CharField(max_length=55, min_length=2)
    
    class Meta:
        model=User
        fields = ['username', "first_name", "last_name", "email", "password"]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':("Email is Already in Use")})
        return super().validate(attrs)

    def create(self, Validated_data):
        return User.objects.create_user(**Validated_data)