# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Revista', '0023_auto_20171201_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revista',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
