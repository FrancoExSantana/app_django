from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name= 'inicio'),
    path('about/', views.about, name='inscripciones'),
    ]