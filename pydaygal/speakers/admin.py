# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pydaygal.speakers.models import Speaker

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'biography', 'photo', 'track', 'presentation', 'presentation_text', 'presentation_schedule', 'is_workshop', 'url_github', 'url_twitter', 'url_blog', 'url_mail', 'url_github_2', 'url_twitter_2', 'url_blog_2', 'url_mail_2']
    search_fields = ('name',)
