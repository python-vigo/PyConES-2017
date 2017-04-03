# -*- coding: utf-8 -*-
from django.conf.urls import url

from pydaygal.workshops.views import EditWorkshop, WorkshopsListView, WorkshopsDetailsView

urlpatterns = [
    url(r'^$', WorkshopsListView.as_view(), name="list"),
    url(r'^$edit/', EditWorkshop.as_view(), name="edit"),
    url(r'^(?P<slug>.+)/$', WorkshopsDetailsView.as_view(), name="workshop"),
]
