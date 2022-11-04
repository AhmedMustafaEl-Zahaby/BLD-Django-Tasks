from django.db.models import Count, Q
from django.shortcuts import render
from django.views import View
from .models import Artist
from django.http import JsonResponse
from django.core import serializers
from .forms import *
from rest_framework import generics
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
import json

class ArtistView(APIView):
    def get(self, request):
        data = ArtistSerializer(Artist.objects.all() , many = True)
        return Response(data.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)