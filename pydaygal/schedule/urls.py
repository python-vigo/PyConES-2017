# -*- coding: utf-8 -*-
from django.conf.urls import url

from pydaygal.schedule.views import ScheduleView

urlpatterns = [
    url(r'^$', ScheduleView.as_view(), name="schedule"),
]
