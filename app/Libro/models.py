# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class libro(models.Model):
    Titulo=models.CharField(max_length=30)
    investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
    Editorial=models.CharField(max_length=15)
    ISBN=models.CharField(max_length=15)
    Resumen= models.DateField()
    Ubicacion=models.CharField(max_length=15)
    Url=models.URLField()
