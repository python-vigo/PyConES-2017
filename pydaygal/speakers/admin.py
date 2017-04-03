# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pydaygal.speakers.models import Speaker

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'biography', 'photo', 'track', 'presentations']
    search_fields = ('name',)
