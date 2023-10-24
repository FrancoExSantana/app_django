from django.urls import path
from . import views

urlpatterns = [
    path('materia/', views.submit_data, name= 'materia'),
]