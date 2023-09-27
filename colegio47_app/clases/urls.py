from django.urls import path
from . import views

urlpatterns = [
    path('materia/', views.create_materia, name= 'materia'),
]