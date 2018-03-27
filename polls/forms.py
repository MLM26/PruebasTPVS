from django import forms

class Info(forms.Form):
    nombre: forms.CharField(widget=forms.TextInput(),required=True)
    descripcion: forms.CharField(widget=forms.TextInput(),required=True)
