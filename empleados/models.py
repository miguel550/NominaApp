from django.db import models


class Empleado(models.Model):
    cedula = models.TextField(max_length=20)
    primer_nombre = models.TextField(max_length=150)
    segundo_nombre = models.TextField(max_length=150)
    primer_apellido = models.TextField(max_length=150)
    segundo_apellido = models.TextField(max_length=150)
    salario = models.DecimalField()
