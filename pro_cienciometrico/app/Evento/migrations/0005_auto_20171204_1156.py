# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evento', '0004_auto_20171204_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='Lugar',
            field=models.CharField(max_length=100),
        ),
    ]
