__author__ = 'mnu'

from google.appengine.ext import ndb


class Source(ndb.Model):
    name = ndb.StringProperty(indexed=True, required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    api_key_name = ndb.StringProperty(indexed=False)
    api_source = ndb.StringProperty(indexed=False)
    fields_map = ndb.JsonProperty(indexed=False)
