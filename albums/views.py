from django.shortcuts import render
from django.views import View
from .models import Album
from django.http import JsonResponse
from django.core import serializers
from .form import *
from rest_framework import generics , mixins, pagination, permissions, status
from .serializers import *
from rest_framework.response import Response
from filters import *
import json
import sys

class AlbumView(generics.GenericAPIView,
                    mixins.ListModelMixin,):
    queryset = Album.objects.filter(propriet = True)
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = AlbumFilter

    def get(self, request):
        return self.list(request)

    def perform_create(self, serializer):
        serializer.save(artist = self.request.user.artist)
    

    def perform_create(self, serializer):
        serializer.save(artist = self.request.user.artist)
    
    def post(self , request):
        print(self.request.user.artist)
        if not hasattr(request.user , 'artist'):
            return Response(status = status.HTTP_403_FORBIDDEN , data = {"Message": "You should be an artist"})
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AlbumDetailView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_class = AlbumFilter

    def get(self, request, *args, **kwargs):
        params =  request.query_params
        gte, lte, icontains = 0, sys.maxsize, ''
        if 'cost__gte' in params:
            if params['cost__gte']:
                try:
                    data = int(params['cost__gte'])
                    gte = data
                    print(gte)
                except:
                    return Response(data={"cost__gte": ["Enter a number"]}, status=status.HTTP_400_BAD_REQUEST)

        if 'cost__lte' in params:
            if params['cost__lte']:
                try:
                    data = int(params['cost__lte'])
                    lte = data
                except:
                    return Response(data={"cost__lte": ["Enter a number"]}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'name__icontains' in params:
            if params['name__icontains']:
                icontains = params['name__icontains']
        
        # print(gte , lte , icontains)
        data = Album.objects.filter(cost__gte=gte, cost__lte=lte, name__icontains=icontains)
        serializer = AlbumSerializer(data, many=True)

        if 'limit' not in params:
            return Response(serializer.data)
        
        return self.get_paginated_response(self.paginate_queryset(serializer.data))


