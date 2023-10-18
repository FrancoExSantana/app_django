from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name= 'inicio'),
    path('inscripciones/', views.inscripciones, name='inscripciones'),
    path('calendario/', views.calendario, name='calendario'),
    path('materias/', views.materias, name='materias'),     
    ]