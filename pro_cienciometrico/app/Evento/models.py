# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class evento(models.Model):
    Nombre=models.CharField(max_length=300)
    Lugar=models.CharField(max_length=100)
    Fecha=models.CharField(max_length=50)

    def __str__(self): return '{}'.format(self.Nombre)


