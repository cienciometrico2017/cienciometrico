# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from app.Participaciones_Evemtos.models import participaciones_eventos

admin.site.register(participaciones_eventos)