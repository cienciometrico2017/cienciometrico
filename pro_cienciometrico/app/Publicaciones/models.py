# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from  app.Investigador.models import investigador
class publicaciones(models.Model):
 Titulo = models.CharField(max_length=100)
 Nivel_Autoria=models.IntegerField()
 investigador = models.ManyToManyField(investigador)
 Palabras_Clave = models.TextField(300),
 Resumen = models.FileField()
 Fecha = models.DateField()
 Editorial = models.CharField(max_length=50)
 DB_Indexada=models.CharField(max_length=50)
 Url=models.URLField()

 def __str__(self): return '{}'.format(self.Titulo)