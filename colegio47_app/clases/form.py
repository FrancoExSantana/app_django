from django.forms import ModelForm
from .models import Materia

class materiaform(ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre']
