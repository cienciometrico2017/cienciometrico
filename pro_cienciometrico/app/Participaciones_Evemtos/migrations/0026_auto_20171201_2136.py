# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Participaciones_Evemtos', '0025_auto_20171201_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participaciones_eventos',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
