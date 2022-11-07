from django.shortcuts import render
from rest_framework import generics , status
from .models import *
from .serializers import *
from rest_framework import permissions
from .permission import *
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication

class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly , Vaild_request]
    # authentication_classes = [TokenAuthentication,]

