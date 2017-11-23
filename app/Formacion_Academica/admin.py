# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from app.Formacion_Academica.models import formacion_academica

admin.site.register(formacion_academica)