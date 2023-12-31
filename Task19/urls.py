"""
URL configuration for Task19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Aplicacion import views as app

urlpatterns = [
    path('admin/', admin.site.urls),

    #Agregamos las URLs de nuestra view
path('', app.index,name="home"),
path('registro/',app.reg_user, name="registro"),
path('login/',app.iniciar_sesion,name="login"),
path('logout/', app.cerrar_sesion, name='logout'),
path('proveedores/', app.proveedores, name='proveedores'),
path('productos/', app.productos, name='productos'),
# path('addProductos/', app.Add_Productos, name='addProductos')

]

