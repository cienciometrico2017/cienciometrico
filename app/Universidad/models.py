# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.Pais.models import pais
from app.Zona.models import zona

# Create your models here.
class universidad (models.Model):
 Nombre=models.CharField(max_length=20)
 Rector=models.CharField(max_length=20)
 pais=models.ForeignKey(pais,null=True ,blank=True ,on_delete=models.CASCADE)
 zona=models.ForeignKey(zona,null=True ,blank=True ,on_delete=models.CASCADE)