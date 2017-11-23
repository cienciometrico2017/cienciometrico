# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class revista(models.Model):

 Nombre = models.CharField(max_length=30)
 investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
 ISSN=models.CharField(max_length=15)
 Base_Indexada=models.CharField(max_length=20)
 Cuartil_Pertenece=models.CharField(max_length=20)
 Factor_Inpacto=models.IntegerField()
 Url=models.URLField()
 Archivo = models.DateField()

