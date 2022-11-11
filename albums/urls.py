from django.urls import path 
from .views import * 
urlpatterns = [
    path('' , AlbumView.as_view()),
    path('filter/' , AlbumDetailView.as_view())
]