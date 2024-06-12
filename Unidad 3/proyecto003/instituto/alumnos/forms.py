from django import forms
from django.forms import ModelForm

from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields= "__all__"
        labels={
            'apellido1': 'apellido Paterno',
            'apellido2': 'apellido Materno',
        }
        widgets = {
            'email' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'ingrese su email'
            }),
            'nombre' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'ingrese su nombre'
            }),
            'apellido1' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'ingrese su primer apellido'
            }),
            'apellido2' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'ingrese su 2do apellido'
            })
        }