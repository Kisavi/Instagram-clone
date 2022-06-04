from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from decouple import config


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            subject = 'Welcome to The Stargram'
            message = f'Hello {username}! We are glad that you have joined our platform. Let us make memories worthwhile.'
            from_email = config('EMAIL_HOST_USER')
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


def loginpage(request):
    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'main/home.html')


def profile(request):
    return render(request, 'main/profile.html')
