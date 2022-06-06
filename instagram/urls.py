from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up),
    path('profile/<str:username>', views.profile, name='profile'),
    path('saved', views.saved, name='saved'),
    path('post', views.new_post, name='post'),
]
