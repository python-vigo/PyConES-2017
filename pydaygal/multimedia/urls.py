# -*- coding: utf-8 -*-
from django.conf.urls import url
from pydaygal.multimedia.views import MultimediaListView

urlpatterns = [
    url(r'multimedia', MultimediaListView.as_view(), name="multimedia"),
]
