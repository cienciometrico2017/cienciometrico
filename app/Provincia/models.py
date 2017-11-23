# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.Pais.models import pais

# Create your models here.
class provincia (models.Model):
    Nombre=models.CharField(max_length=15)
    pais=models.ForeignKey(pais,null=True ,blank=True ,on_delete=models.CASCADE)

    def __unicode__(self): return '{}'.format(self.Nombre)