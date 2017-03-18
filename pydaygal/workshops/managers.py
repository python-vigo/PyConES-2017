# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models


class WorkshopsManager(models.Manager):
    """Manager for workshops. handle workshops pagination."""

    def requested_objects(self, request, page=None, queryset=None):
        if not queryset:
            queryset = self.all()
        workshops_list = queryset.order_by('name')
        paginator = Paginator(workshops_list, 10)
        if page is None:
            page = request.GET.get('page')
        try:
            workshops = paginator.page(page)
        except PageNotAnInteger:
            workshops = paginator.page(1)
        except EmptyPage:
            workshops = paginator.page(paginator.num_pages)
        return workshops
