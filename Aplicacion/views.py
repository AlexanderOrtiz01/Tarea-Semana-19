#Llamamos todas las librerias que usaremos
from django.shortcuts import render,redirect
from .Formularios.registerform import NewUserForm
from .Formularios.loginform import LoginForm
from django.http import HttpResponseRedirect
from .models import Productos,Proveedores
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Productos as prod
from .Formularios import agregarProducto as addProd

from .models import Proveedores as prov


#formulario para agregar un producto
def AgregarMedicoView(request):
    if request.method == "POST":
        formulario = addProd.agregarProductos(request.POST)
        if formulario.is_valid():
            nuevoRe

#funcion de registrar un usuario
def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario = NewUserForm()
        return render(request, 'Reg_user.html', {"form": formulario})


#Pagina principal
def index(request):
    return render(request, 'index.html')



#funcion de logearse
def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        form.fields['username'].widget.attrs.update({'class': 'form-control'})
        form.fields['password'].widget.attrs.update({'class': 'form-control'})

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


#Funcion para cerrar sesion
def cerrar_sesion(request):
    logout(request)
    return redirect('login')


#Decorator para index
# @login_required(login_url='login')
# def index(request):
#     return render(request, 'index.html', {'user':
#     request.user})

#decorator para roles
@login_required(login_url='login')
def index(request):
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff
    
    if es_estudiante or es_admin:
        return render(request, 'index.html', {'user':
        request.user, 'es_estudiante': es_estudiante,'es_admin':
        es_admin})
    

    #---------view de proveedores-----------------
def proveedores(request):
    proveedoresObj = prov.objects.all()
    return render(request, "proveedores.html",{"proveedoresT":proveedoresObj})

#---------view de productos-----------------
def productos(request):
    productosObj = prod.objects.all()
    proveedoresObj = prov.objects.all()
    return render(request, "productos.html",{"productosT": productosObj,
                                             "proveedoresT": proveedoresObj})