from django.contrib import admin
from django.urls import path

from AppEva3 import views

urlpatterns = [
    path('', views.Home), #Ejecutar despues de principal/Iniciar sesion
    path('WarframeListado/', views.WarframeListado), #listo
    path('AgregarWarframe/', views.AgregarWarframe), #Listo
    path('EliminarWarframe/<int:id>', views.EliminarWarframe), #Listo
    path('ModificarDatos/<int:id>', views.ModificarDatosWarframe), #Listo
    path('WeaponListado/',views.WeaponListado), #Funcional
    path('AgregarWeapon/',views.AgregarWeapon), #Por probar
    path('AgregarBuild/',views.AgregarBuild),
    path('VerBuilds/', views.ListadoBuilds)
]