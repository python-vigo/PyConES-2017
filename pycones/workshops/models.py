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

from pycones.workshops.managers import WorkshopsManager
from pycones.utils.files import UploadToDir


@python_2_unicode_compatible
class Workshop(TimeStampedModel):
    """Workshop"""
    name = models.CharField(
        verbose_name=_("Nombre"),
        max_length=100,
        help_text=_(
            "Tal como quieres que apareza en el programa de la conferencia.")
    )
    content = MarkupField(
        verbose_name=_("Contenido del workshop"),
        blank=True,
        default="",
        default_markup_type='markdown',
        help_text=_("Unas palabras sobre el workshop. Edita usando "
                    "<a href='http://warpedvisions.org/projects/"
                    "markdown-cheat-sheet/target='_blank'>"
                    "Markdown</a>.")
    )
    photo = models.ImageField(
        verbose_name=_("Imagen"),
        upload_to="workshops",
        blank=True,
        null=True
    )
    track = models.IntegerField(default=3)
    speaker = models.TextField(default="", blank=True)


    objects = WorkshopsManager()

    class Meta:
        verbose_name = _('workshop')
        verbose_name_plural = _('workshops')

    @property
    def photo_url(self):
        try:
            return self.photo.url
        except ValueError:
            return static("img/default-avatar.png")

    def __str__(self):
        if self:
            return self.name
        else:
            return "?"

    def get_api_id(self):
        return "S{:05d}".format(self.pk)

    def save(self, **kwargs):
        if not self.name:
            self.name = self.__str__(self)
        return super(Workshop, self).save(**kwargs)
