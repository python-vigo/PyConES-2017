# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.templatetags.static import static
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _, get_language

from markupfield.fields import MarkupField
from model_utils.models import TimeStampedModel

from pydaygal.speakers.managers import SpeakersManager
from pydaygal.utils.files import UploadToDir


@python_2_unicode_compatible
class Speaker(TimeStampedModel):
    """Speaker"""
    name = models.CharField(
        verbose_name=_("Nombre"),
        max_length=100,
        help_text=_(
            "Tal como quieres que apareza en el programa de la conferencia.")
    )
    biography = MarkupField(
        verbose_name=_("Biografía"),
        blank=True,
        default="",
        default_markup_type='markdown',
        help_text=_("Unas palabras sobre el speaker. Edita usando "
                    "<a href='http://warpedvisions.org/projects/"
                    "markdown-cheat-sheet/target='_blank'>"
                    "Markdown</a>.")
    )
    photo = models.ImageField(
        verbose_name=_("Foto"),
        upload_to="speakers",
        blank=True,
        null=True
    )
    track = models.IntegerField(default=0)
    annotation = models.TextField(default="", blank=True)
    is_keynoter = models.BooleanField(default=False)
    presentations = []

    objects = SpeakersManager()

    class Meta:
        verbose_name = _('speaker')
        verbose_name_plural = _('speakers')

    @property
    def photo_url(self):
        try:
            return self.photo.url
        except ValueError:
            return static("img/default-avatar.png")

    @property
    def all_presentations(self):
        if self.presentations:
            for p in self.presentations.all():
                presentations.append(p)
            for p in self.copresentations.all():
                presentations.append(p)
        return presentations

    def __str__(self):
        if self:
            return self.name
        else:
            return "?"

    def has_biography(self):
        return bool(self.biography.raw)

    def get_api_id(self):
        return "S{:05d}".format(self.pk)

    def save(self, **kwargs):
        """Save user full name by default for user."""
        if not self.name:
            self.name = self.__str__(self)
        return super(Speaker, self).save(**kwargs)
