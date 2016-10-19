from requests import get, put
import urlparse
import json
from config import __SITE

class CollectiveAccess(object):
	"""creates a session for collective access actions"""
	def __init__(self, base, user, passw, header={'content-type':'application/json'}):
		super(CAClient, self).__init__()
		self.base = __SITE
		self.user = user
		self.passw = passw
		self.header = header
		self.sesh = requests.session()
		self.sesh.auth = (self.user, self.passw)
		
	def get_entities(self, q=None):
		if not q:
			endpoint = '/find/ca_entities?q=*'
		else:
			enpoint = '/find/ca_entities?q={0}'.format(q)
		targe = urlencode(self.base, endpoint)
		return self.sesh.get(target, headers=self.header)

	def get_objects(self, q=None):
		if not q:
			endpoint = '/find/ca_objects?q=*'
		else:
			enpoint = '/find/ca_objects?q={0}'.format(q)
		target = urlencode(self.base, endpoint)
		return self.sesh.get(target, headers=self.header)

	def get_entity(self, entity_id):
		endpoint = '/item/ca_entities/id/{0}'.format(entity_id)
		target = urlencode(self.base, endpoint)
		return self.sesh.get(target, headers=self.header)

	def get_object(self, object_id):
		endpoint = '/item/ca_objects/id/{0}'.format(object_id)
		target = urlencode(self.base, endpoint)
		return self.sesh.get(target, headers=self.header)

	def create_entity(self, data):
		target = urlencode(self.base, 'item/ca_entities')
		return self.sesh.put(target, data=data, headers=self.header)
	
	def create_object(self, data):
		target = urlencode(self.base, 'item/ca_objects')
		return self.sesh.put(target,data=data, headers=self.header)