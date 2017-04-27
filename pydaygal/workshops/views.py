# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404

from pydaygal.workshops.forms import WorkshopForm
from pydaygal.workshops.models import Workshop


class WorkshopsListView(View):
    """List of workshops."""

    @staticmethod
    def get(request):
        workshops = Workshop.objects.requested_objects(request)
        return render(request, "workshops/list.html", {"workshops": workshops})


class WorkshopsDetailsView(View):
    """Detail of a workshop"""

    @staticmethod
    def get(request, slug):
        workshop = get_object_or_404(Post, slug=slug)
        return render(request, "workshops/details.html", {"workshop": workshop})


class EditWorkshop(LoginRequiredMixin, View):
    """View for edit the workshop information."""

    def get_login_url(self):
        return reverse("workshops:sign-in")

    def get(self, request):
        try:
            form = WorkshopForm(instance=request.user)
        except ObjectDoesNotExist:
            raise Http404
        data = {
            "form": form,
            "presentations": self.get_presentations(request),
        }
        return render(request, "workshops/edit.html", data)

    def post(self, request):
        try:
            form = WorkshopForm(request.POST, request.FILES,
                               instance=request.user_speaker_profile)
        except ObjectDoesNotExist:
            raise Http404
        data = {
            "form": form,
            "presentations": self.get_presentations(request),
        }
        if form.is_valid():
            form.save()
            messages.success(request, _("Datos actualizados correctamente"))
            return redirect(reverse("workshops:edit"))
        return render(request, "workshops/edit.html", data)
