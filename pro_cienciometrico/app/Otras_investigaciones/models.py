# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class otras_investigaciones(models.Model):
 Titulo = models.CharField(max_length=100)
 Palabras_Clave = models.TextField(300),
 Resumen = models.FileField()
 Fecha = models.DateField()
 Editor = models.CharField(max_length=50)
 Estado_Investigacion=models.CharField(max_length=40)
 Url = models.URLField()
 investigador = models.ManyToManyField(investigador)
 def __str__(self): return '{}'.format(self.Titulo)