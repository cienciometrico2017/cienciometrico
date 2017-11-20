# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.Provincia.models import provincia
# Create your models here.
class canton (models.Model):
    Nombre=models.CharField(max_length=15)
    provincia=models.ForeignKey(provincia,null=True ,blank=True ,on_delete=models.CASCADE)