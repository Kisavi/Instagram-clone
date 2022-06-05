from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up),
    path('profile', views.profile, name='profile'),
]
