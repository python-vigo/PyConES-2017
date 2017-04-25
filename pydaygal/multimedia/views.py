# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect
# from django.utils.translation import ugettext_lazy as _
from django.views.generic import View
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404

from pydaygal.multimedia.models import Foto
from pydaygal.multimedia.models import Video

class MultimediaListView(View):
    """List of photos and videos."""

    @staticmethod
    def get(request):
        photos = Foto.objects.all()
        videos = Video.objects.all()
        return render(request, "pages/multimedia.html", {"photos": photos, "videos":  videos})
