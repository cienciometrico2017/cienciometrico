# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class revista(models.Model):

 Nombre = models.CharField(max_length=100)
 investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
 ISSN=models.CharField(max_length=20)
 Base_Indexada=models.CharField(max_length=50)
 Cuartil_Pertenece=models.CharField(max_length=50)
 Factor_Inpacto=models.IntegerField()
 Url=models.URLField()
 Archivo = models.FileField()

 def __str__(self): return '{}'.format(self.Nombre)

