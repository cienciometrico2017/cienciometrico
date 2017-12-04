# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Carrera.models import carrera

class investigador(models.Model):
    cedula=models.CharField(max_length=12,primary_key=True)
    Nombres=models.CharField(max_length=30)
    Apellidos=models.CharField(max_length=30)
    Direccion=models.TextField(100),
    Telefono=models.CharField(max_length=12)
    Email=models.EmailField()
    Genero=models.CharField(max_length=10)
    Ciudadania=models.CharField(max_length=30)

    Usuario=models.CharField(max_length=10)
    Password=models.CharField(max_length=30)
    carrera=models.ManyToManyField(carrera)

    def __str__(self): return '{}'.format(self.Nombres)
