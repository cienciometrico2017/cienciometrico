# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.Investigador.models import investigador
from app.Pais.models import pais
from app.Revista.models import revista


# Create your models here.


class articulos_cientificos (models.Model):
    Nombre=models.CharField(max_length=300)
    Estado=models.CharField(max_length=30)
    Anio=models.IntegerField()
    ISSN=models.CharField(max_length=60)
    Base_Datos=models.CharField(max_length=50)
    Url=models.CharField(max_length=300)
    Fecha_Publicacion=models.CharField(max_length=30)
    investigador = models.ManyToManyField(investigador)
    pais = models.ForeignKey(pais, null=True, blank=True, on_delete=models.CASCADE)
    ciudad=models.CharField(max_length=50)
    revista = models.ForeignKey(revista, null=True, blank=True, on_delete=models.CASCADE)
    Resumen=models.FileField()
    PalabrasClave=models.CharField(max_length=300)





    def __str__(self): return '{}'.format(self.Nombre)


