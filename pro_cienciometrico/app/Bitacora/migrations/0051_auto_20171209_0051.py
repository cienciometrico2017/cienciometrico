# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bitacora', '0050_auto_20171209_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitacora',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]