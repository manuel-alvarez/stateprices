__author__ = 'mnu'

import logging

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from google.appengine.api import users

from .forms import SourceForm
from .models import Source

logger = logging.getLogger('django')


class SourcesView(TemplateView):
    template_name = 'sources/templates/sources_list.html'

    def get_context_data(self, **kwargs):
        context = super(SourcesView, self).get_context_data(**kwargs)
        context['sources'] = Source.query().order(-Source.created)
        context['title'] = 'List of sources'

        if users.get_current_user():
            url = users.create_logout_url(self.request.get_full_path())
            url_link_text = 'Logout'
        else:
            url = users.create_login_url(self.request.get_full_path())
            url_link_text = 'Login'
        additional_context = {
            'url': url,
            'url_link_text': url_link_text,
            'source_save_url': reverse('save_source'),
            'form': SourceForm(),
        }
        context.update(additional_context)

        return context


class SourceSaveView(View):
    form_class = SourceForm

    def get(self, request):
        return HttpResponseRedirect(reverse('sources'))

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # TODO: Do things that have to do with source object form values
            logger.info('TODO: Do things that have to do with source object form values')
            source = Source(
                name=request.POST.get('name'),
                api_key_name=request.POST.get('api_key_name'),
                api_source=request.POST.get('api_source')
            )
            source.put()
            return HttpResponseRedirect(reverse('sources'))

        return HttpResponseRedirect(reverse('home'))
