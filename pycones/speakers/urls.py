# -*- coding: utf-8 -*-
from django.conf.urls import url

from pycones.speakers.views import EditSpeaker, SpeakersListView, SpeakersDetailsView

urlpatterns = [
    url(r'^$', SpeakersListView.as_view(), name="list"),
    url(r'^$edit/', EditSpeaker.as_view(), name="edit"),
    url(r'^(?P<slug>.+)/$', SpeakersDetailsView.as_view(), name="speaker"),
]
