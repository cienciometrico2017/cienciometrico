# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Revista', '0018_auto_20171129_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revista',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
