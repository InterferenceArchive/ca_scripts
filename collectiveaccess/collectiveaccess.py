import requests
from urlparse import urlparse, urljoin
from urllib import urlencode
import json
import os

class CollectiveAccess(object):
	"""creates a session for collective access actions"""
	def __init__(self, base, user, passw, header={'content-type':'application/json'}):
		super(CollectiveAccess, self).__init__()
		self.base = base
		self.user = user
		self.passw = passw
		self.header = header
		self.sesh = requests.session()
		self.sesh.auth = (self.user, self.passw)

	def get_entities(self, q=None):
		query = '*' if q is None else q
		path = _build_api_uri(endpoint='find', table='ca_entities', q={'q':query})
		print self.base
		target = os.path.join(self.base, path)
		print target
		return self.sesh.get(target, headers=self.header)

	def get_objects(self, q=None):
		query = '*' if q is None else q
		path = _build_api_uri(endpoint='find', table='ca_objects', q={'q':query})
		target = os.path.join(self.base, path)
		return self.sesh.get(target, headers=self.header)

	def get_entity(self, entity_id):
		path = _build_api_uri(endpoint='item', table='ca_entities', identifier='id', item=entity_id)
		target = os.path.join(self.base, path)
		return self.sesh.get(target, headers=self.header)

	def get_object(self, object_id):
		path = _build_api_uri(endpoint='item', table='ca_objects', identifier='id', item=object_id)
		target = os.path.join(self.base, path)
		return self.sesh.get(target, headers=self.header)

	def create_entity(self, data):
		path = _build_api_uri(endpoint='item', table='ca_entities')
		target = os.path.join(self.base, path)
		return self.sesh.put(target, data=data, headers=self.header)
	
	def create_object(self, data):
		path = _build_api_uri(endpoint='item', table="ca_objects")
		target = os.path.join(self.base, path)
		return self.sesh.put(target, data=data, headers=self.header)

	def update_entity(self, entity_id, data):
		path = _build_api_uri(endpoint='item', table='ca_entities', identifier='id', item=entity_id)
		target = os.path.join(self.base, path)
		return self.sesh.put(target, data=data, headers=self.header)

	def update_object(self, object_id, data):
		path = _build_api_uri(endpoint='item', table='ca_objects', identifier='id', item=object_id)
		target = os.path.join(self.base, path)
		return self.sesh.put(target, data=data, headers=self.header)

	def delete_entity(self, entity_id):
		path = _build_api_uri(endpoint='item', table='ca_entities', identifier='id', item=entity_id)
		target = os.path.join(self.base, path)
		return self.sesh.delete(target, headers=self.header)

	def delete_object(self, object_id):
		path = _build_api_uri(endpoint='item', table='ca_entities', identifier='id', item=object_id)
		target = os.path.join(self.base, path)
		return self.sesh.delete(target, headers=self.header)


# helper methods

def _build_api_uri(**kwargs):

	path = (kwargs.pop('endpoint', ''), 
			kwargs.pop('table', ''),
			kwargs.pop('identifier', ''),
			kwargs.pop('item', ''))

	path_items = [p for p in path if p != '']

	query = urlencode(kwargs.pop('q', {}))

	# join them
	url_path = '/'.join(path_items)

	if query != '':
		return url_path + '?' + query
	else:
		return url_path 

