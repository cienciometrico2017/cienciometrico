# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 20:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Formacion_Academica', '0014_auto_20171129_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formacion_academica',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
