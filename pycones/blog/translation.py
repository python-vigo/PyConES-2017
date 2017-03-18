# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, translator

from pycones.blog.models import Post


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'content')
    fallback_languages = {'default': ('gl', 'es', 'ca', 'en')}


translator.register(Post, PostTranslationOptions)
