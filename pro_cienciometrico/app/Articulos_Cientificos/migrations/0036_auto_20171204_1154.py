# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos_Cientificos', '0035_auto_20171204_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos_cientificos',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
