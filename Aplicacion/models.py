from django.db import models


#Modelos creados:

#Modelo de proveedores
class Proveedores(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=8)
    def __str__(self):
        return self.nombre

#Modelo de productos
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    fk_prov=models.ForeignKey(Proveedores,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
