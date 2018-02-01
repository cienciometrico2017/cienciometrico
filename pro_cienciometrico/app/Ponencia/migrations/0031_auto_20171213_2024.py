# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ponencia', '0030_auto_20171209_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='ponencia',
            name='PalabrasClave',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ponencia',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
