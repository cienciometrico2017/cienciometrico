# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Carrera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investigador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=11)),
                ('Nombres', models.CharField(max_length=20)),
                ('Apellidos', models.CharField(max_length=20)),
                ('Telefono', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Genero', models.CharField(max_length=10)),
                ('Ciudadania', models.CharField(max_length=20)),
                ('Usuario', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=20)),
                ('carrera', models.ManyToManyField(to='Carrera.carrera')),
            ],
        ),
    ]