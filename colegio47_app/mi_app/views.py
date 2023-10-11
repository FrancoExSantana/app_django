from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

def homepage(request):
    return render(request,'homepage.html')

def materias(request):
    return render(request,'materias.html')

def calendario(request):
    return render(request,'calendario.html')

def inscripciones(request):
    return render(request,'inscripciones')


                   
    