# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class participaciones_eventos(models.Model):

    Titulo = models.CharField(max_length=25)
    Nivel_Autoria=models.CharField(max_length=15)
    investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
    Palabras_Clave = models.TextField(max_length=40)
    Resumen = models.FileField()
    Fecha = models.DateField()
    Nombre_Evento=models.CharField(max_length=20)
    Nivel=models.IntegerField()
    Lugar_Evento=models.CharField(max_length=20)