# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Revista', '0032_auto_20171203_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revista',
            name='Numero_Revista',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='revista',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
