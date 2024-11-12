from django.contrib import admin
from django.urls import path

from AppEva3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Principal/', views.Home),
    path('IniciarSesion/', views.IniciarSesion),
    path('RegistrarUsuario', views.RegisterUser),
    path('WarframeListado/', views.WarframeListado),
    path('AgregarWarframe/', views.AgregarWarframe),
    path('EliminarWarframe/<int:id>', views.EliminarWarframe),
    path('ModificarDatos/<int:id>', views.ModificarDatosWarframe)
]