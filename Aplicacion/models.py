from django.db import models
from django.contrib.auth.models import Group


#Modelos creados:

#Modelo de proveedores
class Proveedores(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=8)
    #Retorna el nombre cuando el modelo se llama a traves de una llave foranea
    def __str__(self):
        return self.nombre

#Modelo de productos
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    fk_prov=models.ForeignKey(Proveedores,on_delete=models.CASCADE)
    
  
    



#Grupos
#Grupo Cajero
Group.objects.get_or_create(name='Cajero')
#Grupo Estudiante
Group.objects.get_or_create(name='Estudiante')
