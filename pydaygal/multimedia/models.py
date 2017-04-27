# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.templatetags.static import static
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from pydaygal.multimedia.managers import PhotosManager
from pydaygal.multimedia.managers import VideosManager

@python_2_unicode_compatible
class Photo(models.Model):
    title = models.CharField(max_length=150, default="",  blank=True)
    photographer = models.CharField(max_length=100, default="",  blank=True)
    annotation = models.TextField(default="", blank=True)
    photo = models.ImageField(
        upload_to="fotos",
        blank=True
    )
    objects = PhotosManager()

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Video(models.Model):
    title = models.CharField(max_length=150, blank=True, null=False)
    url = models.CharField(max_length=250, blank=True, null=False)
    annotation = models.TextField(default="", blank=True)
    speaker = models.CharField(max_length=150, blank=True, null=False)

    objects =  VideosManager()

    def __str__(self):
        return self.title


