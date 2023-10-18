from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nombre',
        max_length=30,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre',
            'data-toggle': 'tooltip',
            'title': 'Ingrese su nombre'
        })
    )
    last_name = forms.CharField(
        label='Apellido',
        max_length=30,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su apellido',
            'data-toggle': 'tooltip',
            'title': 'Ingrese su apellido'
        })
    )
    username = forms.CharField(
        label='Usuario',
        max_length=150,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese un nombre de usuario',
            'data-toggle': 'tooltip',
            'title': 'Ingrese un nombre de usuario, debe ser de 150 caracteres o menos, utilice solo letras, números y @/./+/-/_'
        })
    )
    email = forms.EmailField(
        label='Correo Electronico',
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su correo electrónico',
            'data-toggle': 'tooltip',
            'title': 'Ingrese su correo electrónico'
        })
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese una contraseña',
            'data-toggle': 'tooltip',
            'title': 'Ingrese una contraseña. Recuerde que sea distinta a su otra información, contenga al menos 8 caracteres, no resulte demasiado común y no esté compuesta enteramente de números'
        })
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme su contraseña',
            'data-toggle': 'tooltip',
            'title': 'Confirme su contraseña'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
