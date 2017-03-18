# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models


class SpeakersManager(models.Manager):
    """Manager for speakers. handle speakers pagination."""

    def requested_objects(self, request, page=None, queryset=None):
        if not queryset:
            queryset = self.all()
        speakers_list = queryset.order_by('name')
        paginator = Paginator(speakers_list, 10)
        if page is None:
            page = request.GET.get('page')
        try:
            speakers = paginator.page(page)
        except PageNotAnInteger:
            speakers = paginator.page(1)
        except EmptyPage:
            speakers = paginator.page(paginator.num_pages)
        return speakers
