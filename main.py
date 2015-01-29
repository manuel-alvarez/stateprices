import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'stateprices.settings'

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher

# Log errors.
#import logging
#def log_exception(*args, **kwds):
#    logging.exception('Exception in request:')
#
#django.dispatch.dispatcher.connect(
#   log_exception, django.core.signals.got_request_exception)

# Unregister the rollback event handler.
# django.dispatch.dispatcher.disconnect(
#     django.db._rollback_on_exception,
#     django.core.signals.got_request_exception)
# Fix Django disconnect
django.dispatch.Signal.disconnect(
    django.core.signals.got_request_exception,
    django.db._rollback_on_exception)

# def main():
# Create a Django application for WSGI.
app = django.core.handlers.wsgi.WSGIHandler()

# Run the WSGI CGI handler with that application.
util.run_wsgi_app(app)

# if __name__ == '__main__':
#   main()
