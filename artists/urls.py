from django.urls import path
from .views import *
urlpatterns = [
    path('', ArtistView.as_view()),
    path('<int:pk>' , ArtistDetailView.as_view()),
]