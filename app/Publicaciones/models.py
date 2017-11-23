# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from  app.Investigador.models import investigador
class publicaciones(models.Model):
 Titulo = models.CharField(max_length=25)
 Nivel_Autoria=models.IntegerField()
 investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
 Palabras_Clave = models.TextField(40),
 Resumen = models.FileField()
 Fecha = models.DateField()
 Editorial = models.CharField(max_length=20)
 DB_Indexada=models.CharField(max_length=20)
 Url=models.URLField()