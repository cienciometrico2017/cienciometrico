# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos_Cientificos', '0028_auto_20171203_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos_cientificos',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
