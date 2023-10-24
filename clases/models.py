from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Materia(models.Model):
    nombre = models.CharField(max_length=20)
    maestro = models.ForeignKey(User, on_delete=models.CASCADE)