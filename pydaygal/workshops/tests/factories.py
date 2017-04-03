# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

import factory

from pydaygal.workshops.tests.factories import WorkshopFactory


class WorkshopFactory(factory.django.DjangoModelFactory):

    workshop = factory.SubFactory(WorkshopFactory)

    class Meta:
        model = "workshops.Workshop"
