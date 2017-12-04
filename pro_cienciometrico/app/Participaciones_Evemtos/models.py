# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class participaciones_eventos(models.Model):

    Titulo = models.CharField(max_length=100)
    Nivel_Autoria=models.CharField(max_length=50)
    Palabras_Clave = models.TextField(max_length=200)
    Resumen = models.FileField()
    Fecha = models.DateField()
    Nombre_Evento=models.CharField(max_length=50)
    Nivel=models.IntegerField()
    Lugar_Evento=models.CharField(max_length=50)
    investigador = models.ManyToManyField(investigador)

    def __str__(self): return '{}'.format(self.Titulo)