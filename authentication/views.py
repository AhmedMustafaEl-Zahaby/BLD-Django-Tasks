from django.shortcuts import render
from rest_framework import generics , mixins
from rest_framework.views import APIView 
from .serializers import *
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.serializers import ValidationError
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken


class RegeisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AutenticationSerializer
    def create(self, request, *args, **kwargs):
        serializer = AutenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model_serializer = AutenticationSerializer(data=serializer.data)
        model_serializer.is_valid(raise_exception=True)
        [username, email, password, bio] = [model_serializer.data['username'], model_serializer.data['email'], model_serializer.data['password'],model_serializer.data['bio']]
        user = User.objects.create_user(username=username, email=email, password=password, bio=bio)
        _, token = AuthToken.objects.create(user)
        return Response({
            "token" : token,
            "user" : {
                "id" : user.id,
                "username" : user.username,
                "email" : user.email,
                "bio" : user.bio
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']      
        _, token = AuthToken.objects.create(user)
        return Response({
            "token" : token,
            "user" : {
                "id" : user.id,
                "username" : user.username,
                "email" : user.email,
                "bio" : user.bio
            }
        }, status=status.HTTP_200_OK)
