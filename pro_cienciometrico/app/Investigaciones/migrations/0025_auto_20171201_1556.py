# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investigaciones', '0024_auto_20171201_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigaciones',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
