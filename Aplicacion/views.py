#Llamamos todas las librerias que usaremos
from django.shortcuts import render,redirect
from .Formularios.registerform import NewUserForm
from .Formularios.loginform import LoginForm
from django.http import HttpResponseRedirect
from .models import Productos,Proveedores
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Productos as prod
from .Formularios.agregarProducto import agregarProductos as addProd
from .models import Proveedores as prov


#formulario para agregar un producto
# def Add_Productos(request):
#     if request.method == "POST":
#         formulario = addProd(request.POST)
#         if formulario.is_valid():
#             nuevoReg = Productos()
#             nuevoReg.nombre = formulario.data['nombre']
#             nuevoReg.stock = formulario.data['stock']
#             nuevoReg.fk_prov = formulario.data['fk_prov']
#             nuevoReg.save()
#             return HttpResponseRedirect('proveedores.html')
#     else:
#         formulario = addProd()
#         return render(request,"productos.html", {'form':formulario})

#funcion de registrar un usuario
def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario = NewUserForm()
        return render(request, 'Reg_user.html', {'form': formulario})


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
    if request.method == "POST":
        formulario = addProd(request.POST)
        if formulario.is_valid():
            nuevoReg = Productos()
            nuevoReg.nombre = formulario.cleaned_data['nombre']
            nuevoReg.stock = formulario.cleaned_data['stock']
            proveedor_id = formulario.cleaned_data['fk_prov']
            proveedor = Proveedores.objects.get(id=proveedor_id)
            nuevoReg.fk_prov = proveedor
            nuevoReg.save()
            return HttpResponseRedirect("/productos")
    else:
        formulario = addProd()
        productosObj = prod.objects.all()
        proveedoresObj = prov.objects.all()
        return render(request, "productos.html",{"productosT": productosObj,
                                             "proveedoresT": proveedoresObj,
                                             "form":formulario})
    return HttpResponseRedirect("/proveedores")