# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Otras_investigaciones', '0019_auto_20171129_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otras_investigaciones',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
