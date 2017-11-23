# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador



class proyectos(models.Model):
 Titulo = models.CharField(max_length=25)
 investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
 Palabras_Clave = models.TextField(40),
 Documento= models.FileField()
 Tipo_Proyecto=models.CharField(max_length=15)