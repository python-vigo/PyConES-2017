# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pycones.workshops.models import Workshop


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['speaker', 'name',
                    'content', 'photo', 'track']
    search_fields = ('name',)
