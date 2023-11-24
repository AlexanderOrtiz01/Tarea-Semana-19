from django.contrib import admin
from .models import Proveedores, Productos


#Se registran los modelos personalizados
admin.site.register(Proveedores)
admin.site.register(Productos)
