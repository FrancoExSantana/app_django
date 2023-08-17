from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CustomUserCreationForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'GET':
        return render(request, 'signup.html', data)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homepage')
            except IntegrityError:
                return render(request, 'signup.html', data, {
                    'error': 'El usuario creado ya existe'
                })

        return render(request, 'signup.html', data, {
            'error': 'Las contraseñas no coinciden'
        })


def homepage(request):
    return render(request, 'homepage.html')


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sigin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else: 
            login(request, user)
            return redirect('homepage')