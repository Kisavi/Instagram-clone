from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


def loginpage(request):
    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'main/home.html')
