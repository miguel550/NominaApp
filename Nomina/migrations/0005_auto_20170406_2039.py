# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nomina', '0004_auto_20170406_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradacontable',
            name='asiento',
        ),
        migrations.DeleteModel(
            name='EntradaContable',
        ),
    ]