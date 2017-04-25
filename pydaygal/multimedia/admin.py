# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pydaygal.multimedia.models import Foto, Video

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'photographer', 'annotation', 'photo']
    search_fields = ['title']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'annotation', 'url']
    search_fields = ['title']
