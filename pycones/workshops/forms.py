# -*- coding: utf-8 -*-
from django import forms
from markupfield.widgets import AdminMarkupTextareaWidget

from pycones.workshops.models import Workshop


class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        fields = ['speaker', 'name',
                    'content', 'photo', 'track']
        widgets = {
            "content": AdminMarkupTextareaWidget(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
