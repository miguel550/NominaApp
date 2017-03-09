from django.db import models


class Empleado(models.Model):
    cedula = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=150)
    segundo_nombre = models.CharField(max_length=150)
    primer_apellido = models.CharField(max_length=150)
    segundo_apellido = models.CharField(max_length=150)
    salario = models.DecimalField(decimal_places=2, max_digits=10)
