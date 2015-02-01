__author__ = 'mnu'

from django.conf.urls import *

from sources.views import SourcesView, SourceSaveView

urlpatterns = patterns('',
    url(r'^save/', SourceSaveView.as_view(), name='save_source'),
    url(r'^$', SourcesView.as_view(), name='sources'),
)