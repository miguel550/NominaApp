from django.db import models
from empleados.models import Empleado

# Create your models here.


class Tipo(models.Model):
    tipo = models.CharField(max_length=5, choices=(
        ('IN', 'Ingreso'),
        ('DE','Deduccion'),
    ))
    nombre = models.CharField(max_length=150)
    depende_salario = models.BooleanField()
    activo = models.BooleanField()


class Transaccion(models.Model):
    empleado = models.ForeignKey(Empleado)
    tipo = models.ForeignKey(Tipo)
    tipo_trans = models.CharField(max_length=150)
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(decimal_places=2, max_digits=10)
    estado = models.CharField(max_length=50)