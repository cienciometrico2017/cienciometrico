# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from app.Articulos_Cientificos.models import articulos_cientificos

admin.site.register(articulos_cientificos)