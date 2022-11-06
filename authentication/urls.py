from django.urls import path 
from .views import *
from knox import views
urlpatterns = [
    path('register/' , RegeisterView.as_view()),
    path('login/' , LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]