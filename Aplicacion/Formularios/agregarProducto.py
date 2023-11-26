from django import forms

class agregarProductos(forms.Form):
    nombre=forms.CharField(max_length=100)
    stock=forms.CharField(max_length=6)