from django import forms

class agregarProveedores(forms.Form):
    nombre=forms.CharField(max_length=100)
    telefono=forms.CharField(max_length=8)