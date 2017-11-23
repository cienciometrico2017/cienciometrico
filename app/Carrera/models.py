# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.Facultad.models import facultad

class carrera (models.Model):
    Nombre=models.CharField(max_length=30)
    Director=models.CharField(max_length=30)
    facultad=models.ForeignKey(facultad,null=True ,blank=True,on_delete=models.CASCADE)