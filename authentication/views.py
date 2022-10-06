from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView
from authentication.serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework.views import APIView 
from django.contrib.auth import authenticate
import jwt

# Create your views here.
class RegisterView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(GenericAPIView):
    permission_classes = ()
    serializer_class = LoginSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token':user.auth_token.key})
        return Response({"error": "wrong credentials"}, status=status.HTTP_400_BAD_REQUEST)