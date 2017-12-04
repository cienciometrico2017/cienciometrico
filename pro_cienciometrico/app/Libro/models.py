# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class libro(models.Model):
    Titulo=models.CharField(max_length=200)
    Editorial=models.CharField(max_length=50)
    ISBN=models.CharField(max_length=50)
    Resumen=models.FileField()
    Ubicacion=models.CharField(max_length=50)
    Url=models.URLField()
    Anio=models.CharField(max_length=5)
    investigador = models.ManyToManyField(investigador)

    def __str__(self): return '{}'.format(self.Titulo)


