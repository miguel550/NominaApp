from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Empleado
# Create your views here.


class CrearEmpleado(CreateView):
    model = Empleado
    fields = ['cedula',
              'primer_nombre',
              'segundo_nombre',
              'primer_apellido',
              'segundo_apellido',
              'salario']
    success_url = reverse_lazy('lista-empleados')


class ListaEmpleados(ListView):
    model = Empleado
    context_object_name = 'all_empleados'


class EmpleadoParticular(DetailView):
    model = Empleado
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EmpleadoParticular, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        return context
