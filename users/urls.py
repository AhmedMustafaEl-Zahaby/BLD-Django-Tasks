from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', UserView.as_view()),
]