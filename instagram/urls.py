
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('sign-up', views.sign_up)
]
