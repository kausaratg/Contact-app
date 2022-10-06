from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username', "first_name", "last_name", "email", "password"]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':("Email is Already in Use")})
        return super().validate(attrs)

    def create(self, Validated_data):
        user = User(
            username = Validated_data['username'],
            first_name = Validated_data['first_name'],
            last_name = Validated_data['last_name']
        )
        user.set_password(Validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return User

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'username']