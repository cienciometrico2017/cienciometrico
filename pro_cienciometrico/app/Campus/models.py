# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Universidad.models import universidad
from app.Provincia.models import provincia
class campus (models.Model):
 Nombre=models.CharField(max_length=30)
 provincia=models.ForeignKey(provincia,null=True ,blank=True ,on_delete=models.CASCADE)
 universidad=models.ForeignKey(universidad,null=True ,blank=True ,on_delete=models.CASCADE)
