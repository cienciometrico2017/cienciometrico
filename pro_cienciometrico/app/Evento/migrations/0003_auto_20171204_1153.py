# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evento', '0002_auto_20171126_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='Fecha',
            field=models.CharField(max_length=50),
        ),
    ]
