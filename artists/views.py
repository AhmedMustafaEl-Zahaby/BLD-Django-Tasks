from django.db.models import Count, Q
from django.shortcuts import render
from django.views import View
from .models import Artist
from django.http import JsonResponse
from django.core import serializers
from .forms import *
import json


class ArtistView(View):
    def get(self , request):
        data = serializers.serialize('json', 
        Artist.objects.filter(Q(Album__propriet=True)).annotate(count = Count('Album')).order_by('-count'))
        return JsonResponse(json.loads(data) , safe=False)


    def post(self , request):
        try:
            form = ArtistForm(data = json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.error , status=422)

        except :
            return JsonResponse({"Message": "Unknown Format"} , status=500)



class ArtistDetailView(View):
    def get(self , request , id):
        data = serializers.serialize('json' , Artist.objects.filter(id = id))
        return JsonResponse(json.loads(data) , safe=False)


    def post(self , request , id):
        try:
            form = ArtistForm(data = json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.error , status=422)

        except :
            return JsonResponse({"Message": "Unknown Format"} , status=500)


    def put(self , request , id):
        try:
            form = ArtistForm(data = json.loads(request.body) , instance=Artist.objects.get(id = id))
            print(form.instance)
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.error , status=422)
        
        except :
            return JsonResponse({"Message": "Record does not exist"} , status=500)
    

    def delete(self, request , id):
        Artist.objects.filter(id = id).delete()
        data = serializers.serialize('json',
        Artist.objects.filter(Q(Album__propriet=True)).annotate(count = Count('Album')).order_by('-count'))
        return JsonResponse(json.loads(data) , safe=False)



