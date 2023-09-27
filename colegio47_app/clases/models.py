from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Materia(models.Model):
    nomnbre = models.CharField(max_length=20)
    maestro = models.ForeignKey(User, on_delete=models.CASCADE)

    
