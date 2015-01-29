from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from stateprices.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^stateprices/', include('stateprices.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^sp-admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^sp-admin/', include(admin.site.urls)),
)
