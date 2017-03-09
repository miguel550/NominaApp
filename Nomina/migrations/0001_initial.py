# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleados', '0002_auto_20170309_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('IN', 'Ingreso'), ('DE', 'Deduccion')], max_length=5)),
                ('nombre', models.CharField(max_length=150)),
                ('depende_salario', models.BooleanField()),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_trans', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(max_length=50)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Empleado')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nomina.Tipo')),
            ],
        ),
    ]
