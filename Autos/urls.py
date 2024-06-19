from django.contrib import admin
from django.urls import path
from Autos import views 



urlpatterns = [
    path('inicio/',views.Inicio, name='Inicio'),
    path('autos/crear/', views.CrearAuto.as_view(), name='crear_autos')
]
