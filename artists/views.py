from django.db.models import Count, Q
from django.shortcuts import render
from django.views import View
from .models import Artist
from django.http import JsonResponse
from django.core import serializers
from .forms import *
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

import json

class ArtistView(APIView):
    def get(self, request):
        data = ArtistSerializer(Artist.objects.all() , many = True)
        return Response(data.data)

    def post(self, request):
        try:
            serializer = ArtistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'Message': f'Please Entre Right Data'}, status=status.HTTP_400_BAD_REQUEST)


class ArtistDetailView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            serializer = ArtistSerializer(Artist.objects.get(id=kwargs['pk']))
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        except Artist.DoesNotExist:
            return Response({'Message': 'Artist with that id is not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    def put(self, request, *args, **kwargs):
        try:
            serializer = ArtistSerializer(Artist.objects.get(id=kwargs['pk']), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Artist.DoesNotExist:
            return Response({'Message': 'Artist with that id is not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    def delete(self, request, *args, **kwargs):
        try:
            Artist.objects.get(id=kwargs['pk']).delete()
            return Response({'Message': 'Sucessful Delete'}, status=status.HTTP_200_OK)

        except Artist.DoesNotExist:
            return Response({'Message': 'Artist with that id is not found'}, status=status.HTTP_404_NOT_FOUND)