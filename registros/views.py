from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CustomUserCreationForm, CareerForm
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
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'signup.html', data, {
                    'error': 'El usuario creado ya existe'
                })

        return render(request, 'signup.html', data, {
            'error': 'Las contraseñas no coinciden'
        })

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
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else: 
            login(request, user)
            return redirect('inicio')

def career_form(request):
    if request.method == 'POST':
        form = CareerForm(request.POST)
        if form.is_valid():
            career = form.cleaned_data['career']
            if career == 'Analista De Sistemas':
                subjects = ['Subject 1', 'Subject 2', 'Subject 3']
            elif career == 'career2':
                subjects = ['Subject 4', 'Subject 5', 'Subject 6']
            elif career == 'career3':
                subjects = ['Subject 7', 'Subject 8', 'Subject 9']
            else:
                subjects = ['Subject 10', 'Subject 11', 'Subject 12']
            return render(request, 'subject_list.html', {'subjects': subjects})
    else:
        form = CareerForm()
    return render(request, 'inscription.html', {'form': form})

