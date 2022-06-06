from .models import Image, Profile, Follow, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadForm, ProfileForm, CommentForm, RegisterForm
from django.urls.base import reverse
from django.http.response import Http404

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

def index(request):
    images = Image.images()
    users = User.objects.exclude(id=request.user.id)
    context = {
        "users": users,
        "images": images[::1]
    }
    return render(request, 'index.html', context)


def loginpage(request):
    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'main/home.html')


def profile(request,username):
    current_user = request.user
    user = User.objects.get(username=current_user.username)
    user_select = User.objects.get(username=username)
    if user_select == user:
        return redirect('instagram:profile', username=request.user.username)

    posts = Post.objects.filter(user = user_select.id)

    ctx = {
        "posts":posts,
        "profile":profile,
        'user':user,
        }
    return render(request, 'main/profile.html',ctx)


def saved(request):
    return render(request, 'main/saved.html')


def post(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return redirect('index')
    else:
        form = UploadForm()
    return render(request, 'post_image.html', {"form": form})
