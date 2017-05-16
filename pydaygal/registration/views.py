from django.shortcuts import render

from django.views.generic.base import RedirectView

class RegistrationRedirectView(RedirectView):
    pattern_name = 'reg'

    def get_redirect_url(self, *args, **kwargs):
            return super(RegistrationRedirectView, self).get_redirect_url(*args, **kwargs)
