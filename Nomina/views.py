from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Tipo, Transaccion
# Create your views here.


class ListaTipo(ListView):
    model = Tipo
    context_object_name = 'all_tipo'


class CrearTipo(CreateView):
    model = Tipo
    fields = [
        'tipo',
        'nombre',
        'depende_salario',
        'activo',
    ]

    success_url = '/tipos/'