from django.shortcuts import render
from django.views import View
from .models import Album
from django.http import JsonResponse
from django.core import serializers
from .form import *
from rest_framework import generics , mixins, pagination, permissions
from .serializers import *
import json

class AlbumView(generics.GenericAPIView,
                    mixins.ListModelMixin,):
    queryset = Album.objects.filter(propriet = True)
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        return self.list(request)

class AlbumDetailView(View):
    def get(self , request , id):
        data = serializers.serialize('json' , Album.objects.get(id = id))
        return JsonResponse(json.loads(data) , safe=False)


    def post(self , request , id):
        try:
            form = AlbumForm(data = json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.error , status=422)

        except :
            return JsonResponse({"Message": "Unknown Format"} , status=500)


    def put(self , request , id):
        try:
            form = AlbumForm(data = json.loads(request.body) , instance=Album.objects.get(id = id))
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.error , status=422)
        
        except :
            return JsonResponse({"Message": "Record does not exist"} , status=500)
    

    def delete(self, request , id):
        Album.objects.filter(id = id).delete()
        data = serializers.serialize('json', Album.objects.all())
        return JsonResponse(json.loads(data) , safe=False)


