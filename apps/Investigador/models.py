# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Carrera.models import carrera

class investigador(models.Model):
    cedula=models.CharField(max_length=11)
    Nombres=models.CharField(max_length=20)
    Apellidos=models.CharField(max_length=20)
    Direccion=models.TextField(50),
    Telefono=models.IntegerField()
    Email=models.EmailField()
    Genero=models.CharField(max_length=10)
    Ciudadania=models.CharField(max_length=20)

    Usuario=models.CharField(max_length=10)
    Password=models.CharField(max_length=20)
    carrera=models.ManyToManyField(carrera)
