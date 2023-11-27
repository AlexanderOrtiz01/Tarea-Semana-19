from django import forms
from ..models import Proveedores

class agregarProductos(forms.Form):
    nombre=forms.CharField(max_length=100)
    stock=forms.CharField(max_length=100)
    fk_prov=forms.CharField(max_length=100)