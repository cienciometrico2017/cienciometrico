# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class intereses_formativos (models.Model):
    Tematica_Interes=models.CharField(max_length=50)
    Descripcion=models.TextField(100)
    investigador=models.ForeignKey( investigador,null=True,blank=True,on_delete=models.CASCADE)
    PalabrasClave = models.CharField(max_length=300)

    def __str__(self): return '{}'.format(self.Tematica_Interes)
