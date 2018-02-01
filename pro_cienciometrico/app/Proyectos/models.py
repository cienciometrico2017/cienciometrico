# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador



class proyectos(models.Model):
 Titulo = models.CharField(max_length=100)
 Palabras_Clave = models.TextField(300),
 Documento= models.FileField()
 Tipo_Proyecto=models.CharField(max_length=50)
 investigador = models.ManyToManyField(investigador)

 def __str__(self): return '{}'.format(self.Titulo)