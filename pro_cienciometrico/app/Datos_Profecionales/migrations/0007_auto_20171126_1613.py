# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Datos_Profecionales', '0006_auto_20171126_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_profecionales',
            name='Grado_Cientifico',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='datos_profecionales',
            name='Nombre_Profecion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='datos_profecionales',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]