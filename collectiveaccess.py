import requests
from urlparse import urlparse, urljoin
from urllib import urlencode
import json
import os, sys

_SCRIPT = 'service.php' #only script, currently, for CA API.

class CollectiveAccess(object):
	"""creates a session for collective access actions
	   and provides a set of methods for doing basic
	   interactions:
	   GET, PUT (create and update), and DELETE objects and entities"""
	def __init__(self, base, user, passw, header={'content-type':'application/json'}):
		super(CollectiveAccess, self).__init__()
		self.base = base
		self.user = user
		self.passw = passw
		self.header = header
		self.sesh = requests.Session()
		try:
			self.sesh.auth = (self.user, self.passw)
		except Exception as e:
			sys.exit("Error creating login session. Check your credentials and try again: {0}".format(e))	

	def _request_get(self, target, headers=None):
		res = self.sesh.get(target, headers=self.header)
		if res.status_code == 200:
			return json.loads(res.text)
		else:
			print "Request failed with status code: {0}".format(res.status_code)

	def _request_put(self, target, identifier=None, data=None):
		res = self.sesh.get(target, headers=self.header)
		if res.status_code == 200:
			return json.loads(res.text)
		else:
			print "Request failed with status code: {0}".format(res.status_code)

	#get many	
	def get_entities(self, q=None):
		query = '*' if q is None else q
		path = _build_api_uri(endpoint='find', table='ca_entities', q={'q':query})
		target = os.path.join(self.base, path)
		print target
		return self._request_get(target, headers=self.header)

	def get_objects(self, q=None):
		query = '*' if q is None else q
		path = _build_api_uri(endpoint='find', table='ca_objects', q={'q':query})
		target = os.path.join(self.base, path)
		return self._request_get(target, headers=self.header)

	#get one
	def get_entity(self, entity_id):
		path = _build_api_uri(endpoint='item', table='ca_entities', identifier='id', item=entity_id)
		target = os.path.join(self.base, path)
		return self.sesh.get(target, headers=self.header)

	def get_object(self, object_id):
		path = _build_api_uri(endpoint='item', table='ca_objects', identifier='id', item=object_id)
		target = os.path.join(self.base, path)
		return self.sesh.get(target, headers=self.header)

	#create one
	def create_entity(self, data):
		path = _build_api_uri(endpoint='item', table='ca_entities')
		data = json.dumps(data)
		target = os.path.join(self.base, path)
		return self.sesh.put(target, data=data, headers=self.header)
	
	def create_object(self, data):
		path = _build_api_uri(endpoint='item', table="ca_objects")
		data = json.dumps(data)
		target = os.path.join(self.base, path)
		return self.sesh.put(target, data=data, headers=self.header)

	#update one
	def update_entity(self, entity_id, data):
		path = _build_api_uri(endpoint='item', table='ca_entities', identifier='id', item=entity_id)
		data = json.dumps(data)
		target = os.path.join(self.base, path)
		return self.sesh.put(target, data=data, headers=self.header)

	def update_object(self, object_id, data):
		path = _build_api_uri(endpoint='item', table='ca_objects', identifier='id', item=object_id)
		data = json.dumps(data)
		target = os.path.join(self.base, path)
		return self.sesh.put(target, data=data, headers=self.header)

	#delete one
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
			str(kwargs.pop('item', '')))

	path_items = [p for p in path if p != '']

	query = urlencode(kwargs.pop('q', {}))

	# join them
	url_path = os.path.join(_SCRIPT, '/'.join(path_items))

	if query != '':
		return url_path + '?' + query
	else:
		return url_path 



