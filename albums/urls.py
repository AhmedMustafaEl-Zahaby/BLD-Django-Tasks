from django.urls import path 
from .views import * 
urlpatterns = [
    path('' , AlbumView.as_view()),
    path('<int:id>' , AlbumDetailView.as_view())
]