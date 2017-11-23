# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Investigador.models import investigador

class intereses_formativos (models.Model):
    Tematica_Interes=models.CharField(max_length=30)
    Descripcion=models.TextField(70)
    investigador=models.ForeignKey( investigador,null=True,blank=True,on_delete=models.CASCADE)
