__author__ = 'mnu'

from google.appengine.ext import ndb

from stateprices import settings

class Source(ndb.Model):
    name = ndb.StringProperty(indexed=True, required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    api_key_name = ndb.StringProperty(indexed=False)
    api_source = ndb.StringProperty(indexed=False)
    fields_map = ndb.JsonProperty(indexed=False)

    @property
    def sample_source(self):
        params = {
            'operation': settings.SP_DEFAULT_OPERATION,
            'position': settings.SP_DEFAULT_ADDRESS,
            'distance': settings.SP_DEFAULT_DISTANCE,
            'api_key': getattr(settings, self.api_key_name),
        }
        return self.api_source % params
