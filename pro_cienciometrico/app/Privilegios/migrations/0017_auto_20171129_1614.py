# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Privilegios', '0016_auto_20171129_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privilegios',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
