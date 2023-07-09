from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from django.contrib.auth import logout
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import status  
import json
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate,login
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from functools import wraps


# from .serializers import CustomModelSerializer
from django.contrib.auth import get_user_model
User=get_user_model()


# Create your views here.
class Get_Response:
    def get_response(self, user):
        serializer = UserSerializer(user, context=self.get_serializer_context())
        token = AuthToken.objects.create(user)[1]
        return Response({
            "user": serializer.data,
            "token": token
        })
    
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = request.data
        user1 = data.get('username')
        if User.objects.filter(username=user1).exists():
              return Response({"response_message":"Please create a different user, as the provided username already exists."}, status=status.HTTP_400_BAD_REQUEST) 
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
            })
    
class LoginAPI(Get_Response,generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthTokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer =self.get_serializer(data=request.data) #self.get_serializer
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return self.get_response(user)
    
    
    
class LogoutAPI(Get_Response,generics.GenericAPIView):
    permission_classes=(permissions.AllowAny,)
    serializer_class = AuthTokenSerializer
    def post(self,request,format=None):
        logout(request)
        return Response('User Logged out successfully')  
    