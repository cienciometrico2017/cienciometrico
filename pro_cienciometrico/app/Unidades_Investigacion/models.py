# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Universidad.models import universidad
class unidaddes_investigacion (models.Model):
    Nombre=models.CharField(max_length=30)
    Director=models.CharField(max_length=30)
    universidad=models.ForeignKey(universidad,null=True ,blank=True ,on_delete=models.CASCADE)