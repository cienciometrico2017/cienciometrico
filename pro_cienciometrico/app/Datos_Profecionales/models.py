# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class datos_profecionales(models.Model):
    Nombre_Profecion=models.CharField(max_length=100)
    Grado_Cientifico=models.CharField(max_length=15)
    Categoria=models.CharField(max_length=10)
    investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self): return '{}'.format(self.Nombre_Profecion)
