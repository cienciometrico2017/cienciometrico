# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Datos_Profecionales', '0019_auto_20171129_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_profecionales',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
