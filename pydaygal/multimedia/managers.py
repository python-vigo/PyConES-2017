# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models


class PhotosManager(models.Manager):
    """Manager for photos. handle photos pagination."""

    def requested_objects(self, request, page=None, queryset=None):
        if not queryset:
            queryset = self.all()
        photos_list = queryset.order_by('title')
        paginator = Paginator(photos_list, 10)
        if page is None:
            page = request.GET.get('page')
        try:
            photos = paginator.page(page)
        except PageNotAnInteger:
            photos = paginator.page(1)
        except EmptyPage:
            photos = paginator.page(paginator.num_pages)
        return photos


class VideosManager(models.Manager):
    """Manager for videos. handle videos pagination."""

    def requested_objects(self, request, page=None, queryset=None):
        if not queryset:
            queryset = self.all()
        videos_list = queryset.order_by('title')
        paginator = Paginator(videos_list, 10)
        if page is None:
            page = request.GET.get('page')
        try:
            videos = paginator.page(page)
        except PageNotAnInteger:
            videos = paginator.page(1)
        except EmptyPage:
            videos = paginator.page(paginator.num_pages)
        return videos
