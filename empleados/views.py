from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.


class CrearEmpleado(FormView):
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('lista-empleados')

    def form_valid(self, form):
        Empleado(**form.cleaned_data).save()
        return super(CrearEmpleado, self).form_valid(form)


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
