from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name= 'home'),
    path('homepage/', views, name= 'clases'),
    path('about/', views.about, name='inscripciones'),
    path('carreras/', views.index, name='carreras'),
    ]
    
