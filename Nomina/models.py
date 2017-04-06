from django.db import models
from empleados.models import Empleado


class Tipo(models.Model):
    tipo = models.CharField(max_length=5, choices=(
        ('IN', 'Ingreso'),
        ('DE', 'Deduccion'),
    ))
    nombre = models.CharField(max_length=150)
    depende_salario = models.BooleanField()
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    defecto = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)


class Pago(models.Model):
    empleado = models.ForeignKey(Empleado)
    fecha = models.DateTimeField(auto_now_add=True)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def pago_neto_empleado(self):
        salario_neto = self.sueldo
        for transaccion in self.transaccion_set.all():
            if transaccion.tipo.tipo == 'IN':
                if transaccion.tipo.depende_salario:
                    salario_neto += salario_neto*transaccion.tipo.porcentaje
                else:
                    salario_neto += transaccion.tipo.monto
            elif transaccion.tipo.tipo == 'DE':
                if transaccion.tipo.depende_salario:
                    salario_neto -= salario_neto*transaccion.tipo.porcentaje
                else:
                    salario_neto -= transaccion.tipo.monto
        return salario_neto


class Transaccion(models.Model):
    pago = models.ForeignKey(Pago, default=None)
    tipo = models.ForeignKey(Tipo, null=True)
    tipo_trans = models.CharField(max_length=150)
    estado = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)


class AsientoContable(models.Model):
    descripcion = models.CharField(max_length=200)
    id_db = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
