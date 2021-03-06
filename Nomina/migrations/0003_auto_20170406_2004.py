# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nomina', '0002_auto_20170406_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradacontable',
            name='transaccion',
        ),
        migrations.AddField(
            model_name='pago',
            name='sueldo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Nomina.Tipo'),
        ),
    ]
