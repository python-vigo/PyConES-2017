# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

import reversion
from django.apps import AppConfig


class ProposalsConfig(AppConfig):
    name = "pydaygal.proposals"

    def ready(self):
        """Connects signals with their managers."""
        from pydaygal.proposals.models import Proposal

        reversion.register(Proposal)
