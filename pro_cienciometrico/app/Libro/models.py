# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class libro(models.Model):
    Titulo=models.CharField(max_length=100)
    investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
    Editorial=models.CharField(max_length=50)
    ISBN=models.CharField(max_length=20)
    Resumen=models.FileField()
    Ubicacion=models.CharField(max_length=50)
    Url=models.URLField()

    def __str__(self): return '{}'.format(self.Titulo)


