# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grado_Competencia', '0022_auto_20171129_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grado_competencia',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
