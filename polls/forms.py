from django import forms
from .import models

class Trader(forms.ModelForm):
    nombre: forms.CharField(widget=forms.TextInput(),required=True)
    descripcion: forms.CharField(widget=forms.TextInput(),required=True)
