from django import forms
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Archivo

class Trader(forms.ModelForm):
    nombre: forms.CharField(widget=forms.TextInput(),required=True)
    descripcion: forms.CharField(widget=forms.TextInput(),required=True)

class CargarArchivo(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = [
            "nombre",
            "file",
        ]
"""
    nombre: forms.CharField(widget=forms.TextInput(),required=True)
    file = forms.FileField()

class CargarArchivo(CreateView):
    model = Archivo
    fields = [
        "nombre",
        "file"
    ]

"""
