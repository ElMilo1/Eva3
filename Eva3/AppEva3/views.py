from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from AppEva3.models import Warframe, UserData, BuildResume, Weapon
from AppEva3.forms import WarframeForm, User, WeaponForm, BuildResumeForm

# Create your views here.

def Home(request):
    return render(request, 'index.html')

# Warframe
def WarframeListado(request):
    listado = Warframe.objects.all()
    data = {'listado': listado}
    return render(request, 'ListadosWarframe.html', data)

def AgregarWarframe(request):
    form = WarframeForm()
    if request.method == 'POST':
        form = WarframeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/WarframeListado/")
    else:
        form = WarframeForm()
    data = {'form' : form}
    return render(request, 'FormularioWarframe.html', data)

def EliminarWarframe(request, id):
    listado = Warframe.objects.get(id = id)
    listado.delete()
    return redirect('../WarframeListado/')

def ModificarDatosWarframe(request, id):
    listado = Warframe.objects.get(id = id)
    form = WarframeForm(instance = listado)
    if request.method == 'POST':
        form = WarframeForm(request.POST, instance = listado)
        if form.is_valid():
            form.save()
            return redirect("/WarframeListado/")
    else:
        form = WarframeForm(instance = listado)
        
    data = {'form' : form}
    return render(request, 'FormularioWarframe.html', data)

#Weapon
def WeaponListado(request):
    listado = Weapon.objects.all()
    data = {'Weapon': listado}
    return render(request, 'ListadoWeapons.html',data)

def AgregarWeapon(request):
    form = WeaponForm
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            form.save()
        return Home(request)
    data = {'form' : form}
    return render(request,'AgregarWeapons.html',data)

def BorrarWeapon(request,id):
    x = Weapon.objects.get(id=id)
    x.delete()
    return redirect('../WeaponListado/')

def EditarWeapon(request,id):
    EWeapon = Weapon.objects.get(id=id)
    form = WeaponForm
    if request.method == 'POST':
        form = WeaponForm(request.POST, instance=EWeapon)
        if form.is_valid():
            form.save()
        return Home(request)
    else:
        form = WeaponForm(instance=EWeapon)
    data = {'form':form}
    return render(request,'AgregarWeapons.html',data)

#Build
def AgregarBuild(request):
    if request.method == 'POST':
        form = BuildResumeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/VerBuilds/')  # Es mejor usar redirect que llamar a Home(request)
            except Exception as e:
                print(f"Error al guardar: {e}")  # Para debugging
    else:
        form = BuildResumeForm()  # Instancia vacía del formulario para GET
    
    return render(request, 'AgregarBuild.html', {'form': form})

#User
def IniciarSesion(request):
    form = User()
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            username = form.cleaned_data['UserName']
            password = form.cleaned_data['Password']
            
            user = UserData.objects.get(UserName = username)
            
            if check_password(password, user.Password):
                auth_user = authenticate(request, username = username, password=password)
                if auth_user is not None:
                    login(request, auth_user)
                    messages.success(request, 'Has iniciado sesión')
                    return redirect('/Principal/')
    else:
        form = User()
        
    data = {'form' : form}
    return render(request, 'IniciarSesion.html', data)

def RegisterUser(request):
    form = User()
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/IniciarSesion/')
    else:
        form = User()
        
    data = {'form' : form}
    return render(request, 'RegistroUsuario.html', data)

#Builds
def ListadoBuilds(request):
    listadoB = BuildResume.objects.all()
    data = {'ListadoB': listadoB}
    return render(request, 'Builds.html', data)