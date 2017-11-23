# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from app.Proyectos.models import proyectos

admin.site.register(proyectos)
