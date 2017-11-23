# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from app.Datos_Profecionales.models import datos_profecionales

admin.site.register(datos_profecionales)
