# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class revista(models.Model):

 Nombre = models.CharField(max_length=200)
 investigador = models.ManyToManyField(investigador)
 ISSN=models.CharField(max_length=50)
 Base_Indexada=models.CharField(max_length=50)
 Cuartil_Pertenece=models.CharField(max_length=50)
 Factor_Inpacto=models.CharField(max_length=50)
 Url=models.URLField()
 Archivo = models.FileField()
 Numero_Revista=models.CharField(max_length=100)

 def __str__(self): return '{}'.format(self.Nombre)

