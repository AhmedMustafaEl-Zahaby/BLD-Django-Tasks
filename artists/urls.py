from django.urls import path
from .views import *
urlpatterns = [
    path('', ArtistView.as_view()),
    path('<int:id>' , ArtistDetailView.as_view()),
]