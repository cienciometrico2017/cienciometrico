# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investigador', '0004_auto_20171129_1702'),
        ('Revista', '0015_auto_20171129_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revista',
            name='investigador',
        ),
        migrations.AddField(
            model_name='revista',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]