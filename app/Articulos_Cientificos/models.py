# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.Investigador.models import investigador
from app.Provincia.models import provincia

# Create your models here.


class articulos_cientificos (models.Model):
    Nombre=models.CharField(max_length=20)
    Numero=models.IntegerField()
    Estado=models.CharField(max_length=15)
    Anio=models.IntegerField()
    SSN=models.CharField(max_length=15)
    Base_Datos=models.CharField(max_length=20)
    provincia=models.ForeignKey(provincia, null=True, blank=True, on_delete=models.CASCADE)
    Url=models.URLField()
    Fecha_Publicacion=models.DateField()
    investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)



