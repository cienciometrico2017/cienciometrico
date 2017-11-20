# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class privilegios(models.Model):
    Nombre=models.CharField(max_length=15)
    Descripcion=models.CharField(max_length=50)
    investigador=models.ForeignKey(investigador,null=True ,blank=True,on_delete=models.CASCADE)