from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from empleados.models import Empleado
from .models import Tipo, Transaccion, Pago, AsientoContable
import zeep
from zeep.plugins import HistoryPlugin
from zeep.helpers import serialize_object
import json
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
        'monto',
        'porcentaje',
        'defecto',
        'activo',
    ]

    success_url = '/tipos/'


class PreviewPagos(ListView):
    model = Empleado
    context_object_name = 'all_empleados'
    template_name = 'preview_pago_list.html'

    def get_context_data(self, **kwargs):
        context = super(PreviewPagos, self).get_context_data(**kwargs)
        context['all_tipos'] = Tipo.objects.filter(activo=True)
        return context


class ListaTransacciones(ListView):
    model = Transaccion
    context_object_name = 'all_trans'

    def get_context_data(self, **kwargs):
        context = super(ListaTransacciones, self).get_context_data(**kwargs)
        return context


class ListaAsientos(ListView):
    model = AsientoContable
    context_object_name = 'all_asientos'


class TipoParticular(DetailView):
    model = Tipo
    context_object_name = 'tipo'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TipoParticular, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        return context


@csrf_exempt
def pagar(request):
    if request.method == "POST":
        data = json.loads(request.body)
        total = 0
        for pago in data['data']:
            p = Pago()
            empleado = Empleado.objects.get(pk=pago['empleado_pk'])
            p.empleado = empleado
            p.sueldo = empleado.salario
            total += p.sueldo
            p.save()
            tipos = [d['nombre'] for d in pago['tipos'] if d['use']]
            tipos = Tipo.objects.filter(nombre__in=tipos)
            for tipo in tipos:
                if tipo.depende_salario:
                    monto = empleado.salario*tipo.porcentaje
                else:
                    monto = tipo.monto
                p.transaccion_set.create(tipo=tipo, monto=monto, estado='R', tipo_trans=tipo.nombre)
        history = HistoryPlugin()
        client = zeep.Client('https://contabilidad.ngrok.io/Contabilidad/Contabilidad?wsdl', plugins=[history])
        entrada = dict(cuentaContable=70, tipoMovimiento="CR", monto=total)
        entrada2 = dict(cuentaContable=71, tipoMovimiento="DB", monto=total)
        entradaCont = dict(auxiliar=2,
                           descripcion='Nomina',
                           entradasContables=[{'entradaContable': [entrada, entrada2]}])
        ret = serialize_object(client.service.crearAsiento(entradaCont))
        AsientoContable.objects.create(descripcion=ret['descripcion'],
                                       id_db=ret['idAsiento'])
        return JsonResponse(ret)