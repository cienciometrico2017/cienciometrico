# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador
from app.Libro.models import libro
from app.Revista.models import revista
from app.Evento.models import evento

class ponencia (models.Model):
  Anio=models.IntegerField()
  investigador = models.ManyToManyField(investigador)
  Certificado=models.CharField(max_length=5)
  Titulo_Publicacion=models.CharField(max_length=25)
  Tipo_Publicacion=models.CharField(max_length=15)
  Financiamiento=models.CharField(max_length=7)
  Url_publicacion=models.URLField()
  Informe=models.FileField()
  Datos=models.CharField(max_length=25)
  Asistencia=models.CharField(max_length=5)
  evento=models.ForeignKey(evento,null=True,blank=True,on_delete=models.CASCADE)
  libro = models.ForeignKey(libro, null=True, blank=True, on_delete=models.CASCADE)



