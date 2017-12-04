# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos_Cientificos', '0021_auto_20171201_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulos_cientificos',
            old_name='SSN',
            new_name='ISSN',
        ),
        migrations.AlterField(
            model_name='articulos_cientificos',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
