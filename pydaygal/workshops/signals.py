# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

from django.contrib.auth.models import Group

from pydaygal.workshops import WORKSHOPS_GROUP_NAME
from pydaygal.workshops.models import Workshop


def register_workshops_handler(sender, **kwargs):
    """Handle profiles when the workshop is added to a group."""

    action = kwargs.get("action")
    instance = kwargs.get("instance")
    if instance and action in ("post_add", "post_remove"):
        if WORKSHOPS_GROUP_NAME in instance.groups.values_list("name", flat=True):
            if not Workshop.objects.filter(workshop=instance).exists():
                Workshop.objects.create(workshop=instance)
        else:
            if Workshop.objects.filter(workshop=instance).exists():
                Workshop.objects.filter(workshop=instance).delete()


def create_workshops_group(sender, **kwargs):
    """Creates workshops group."""

    if not Group.objects.filter(name=WORKSHOPS_GROUP_NAME).exists():
        Group.objects.create(name=WORKSHOPS_GROUP_NAME)
