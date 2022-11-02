from django.db.models import Count, Q
from django.shortcuts import render
from django.views import View
from .models import Artist
from django.http import JsonResponse
from django.core import serializers
import json
class ArtistView(View):
    def get(self , request):
        data = serializers.serialize('json', 
        Artist.objects.filter(Q(Album__propriet=True)).annotate(count = Count('Album')).order_by('-count'))
        return JsonResponse(json.loads(data) , safe=False)



