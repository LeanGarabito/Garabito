from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Auto
from django.urls import reverse_lazy

def Inicio(request):
    return render(request,"autos/inicio.html")

    
class CrearAuto(CreateView):
    model = Auto
    template_name = 'autos/crear_auto.html'
    success_url = ''
    fields = ['nombre' 'marca' 'modelo' 'kilometros' 'año' 'precio' 'imagen']
    
# Class EditarAuto(request):
#     ...
    
# Class EliminarAuto(request):
#     ...
    
# Class VerAuto(request):
#     ...
    
# Class ListaAuto(request):
#     ...    