'''# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, translator

from pycones.speakers.models import Speaker

class SpeakerTranslationOptions(TranslationOptions):
    fallback_languages = {'default': ('gl', 'es', 'ca', 'en')}

translator.register(Speaker, SpeakerTranslationOptions)
'''
