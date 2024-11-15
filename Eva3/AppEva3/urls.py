from django.contrib import admin
from django.urls import path

from AppEva3 import views

urlpatterns = [
    path('home/', views.Home), #Ejecutar despues de principal/Iniciar sesion
    path('Principal/', views.IniciarSesion), #Hacer pagina principal previo a home
    path('RegistrarUsuario/', views.RegisterUser), #Ejecutar desde principal
    path('WarframeListado/', views.WarframeListado), #listo
    path('AgregarWarframe/', views.AgregarWarframe), #Listo
    path('EliminarWarframe/<int:id>', views.EliminarWarframe), #Listo
    path('ModificarDatos/<int:id>', views.ModificarDatosWarframe), #Listo
    path('WeaponListado/',views.WeaponListado), #Funcional
    path('AgregarWeapon/',views.AgregarWeapon), #Por probar
    path('AgregarBuild/',views.AgregarBuild)
]