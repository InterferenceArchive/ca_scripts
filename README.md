Collective Access Client
========================

This is a python client for interating with the collective access client. 

It is built as a set of bindings for the [Collective Access Web Service API](http://docs.collectiveaccess.org/wiki/Web_Service_API). The Web Service API covers a lot of endpoints and interactions, many of which we probably won't need. Therefore, this is not built to be a general purpose Collective Access API. 

Below are a list of methods and how to use the script in general.

Since it is not a complete set of bindings for the API, it does not seem to make a lot of sense to make it an installable package through [pip](https://pip.pypa.io/en/stable/). Should it evolve it into something more, that might be more preferable.

Other, more full-fledged API clients/service wrappers may be found for [Ruby](https://github.com/CollectiveAccessProject/collectiveaccess) and [PHP](https://github.com/skeidel/ca-service-wrapper)

### Contents

* search entities
* search objects
* search for a specific entity
* search for a specific object
* add an entity to the catalog
* add an object to the catalog
* remove an entity from the catalog
* remove an object from the catalog

### Using

Clone the script locally with: 

    
The script is standalone so you can move it whereever you might need it. It only requires an additional install of [Requests](http://docs.python-requests.org/en/master/) to run:

	pip install requests

If you store the script in the same directory with whatever code you want to access it, just import it and be sure to enter the url where you CA **admin** page is at (that is, the Providence homepage, not Pawtucket) along with your login credentials as in this example:

	import collectiveaccess

	client = collectiveaccess.CollectiveAccess('https://myCAcatalog.org/admin_home', 'myusername', 'mypass')

### Methods (what you can do with the client once it's connected) and their response objects (as [Python dictionaries](https://docs.python.org/2/tutorial/datastructures.html#dictionaries))

#### get_entities()
Allows you to search over all entities in your Collective Access site (without a query string, it returns everything):

	client.get_entities(q="SF Mime Troupe")

Returns

	{u'ok': True,
 		u'results': [
 			{u'display_label': u'SF Mime Troupe',
   			 u'entity_id': 2353,
   		     u'id': 2353,
   		     u'idno': u'inkworks_ent_240'}]
   	}

#### get_objects()
Allows you to search over all objects in your Collective Access site (without a query string, it returns everything):

	client.get_objects(q="LA Free Press")


Returns

	{u'ok': True,
 	 u'results': [
 	 	{
 	 		u'display_label': u'LA Free Press',
   		 	u'id': 841,
   		 	u'idno': u'2016.040.9',
   		 	u'object_id': 841},
  		{
  			u'display_label': 
  		 	u'Libertad Para Las Prisoneras Politicas! Free Angela Y. Davis 25th Anniversary',
   		 	u'id': 311,
   			u'idno': u'IA.ITM.272',
   			u'object_id': 311}
   		]
   	}


#### get_entity() 
Given an entity ID of an entity already in the catalog returns details about that entity:

	client.get_entity(110)

Returns

	{u'access': {u'display_text': {u'en_US': u'accessible to public'},
  u'value': u'1'},
 u'ca_entities.agentDates': [{u'en_US': {u'agentDateType': u'activity'}}],
 u'ca_entities.culture': [{u'en_US': []}],
 u'deleted': {u'value': u'0'},
 u'entity_id': {u'value': u'110'},
 u'hier_entity_id': {u'value': u'110'},
 u'hier_left': {u'value': u'1.00000000000000000000'},
 u'hier_right': {u'value': u'101.00000000000000000000'},
 u'idno': [],
 u'idno_sort': [],
 u'lifespan': [],
 u'ok': True,
 u'preferred_labels': {u'en_US': [u'World Council of Churches']},
 u'rank': {u'value': u'0'},
 u'related': {u'ca_objects': [{u'_key': u'relation_id',
    u'direction': u'rtol',
    u'idno': u'IA.ITM.105',
    u'item_type_id': u'435',
    u'label': u'Cabora Bassa and the Struggle for Southern Africa',
    u'labels': {u'1': u'Cabora Bassa and the Struggle for Southern Africa'},
    u'locale_id': u'1',
    u'name': u'Cabora Bassa and the Struggle for Southern Africa',
    u'object_id': u'18',
    u'relation_id': u'90',
    u'relationship_type_code': u'author',
    u'relationship_type_id': u'167',
    u'relationship_typename': u'author',
    u'row_id': u'110'}]},
 u'status': {u'display_text': {u'en_US': u'editing in progress'},
  u'value': u'1'},
 u'type_id': {u'display_text': {u'en_US': u'Organization'}, u'value': u'81'}}

#### get_object()
Given an object ID of an object already in the catalog returns details about that object:

	client.get_object(655)

Returns

	{u'access': {u'display_text': {u'en_US': u'accessible to public'},
  u'value': u'1'},
 u'acl_inherit_from_ca_collections': {u'value': u'0'},
 u'acl_inherit_from_parent': {u'value': u'0'},
 u'ca_objects.dateSet': [{u'en_US': {u'dateSet': u'June 21 - September 20 2010'}}],
 u'ca_objects.description_text': [{u'en_US': []}],
 u'ca_objects.enumeration_chronology': [{u'en_US': {u'enumeration_chronology': u'Summer 2010'}}],
 u'ca_objects.holdings': [{u'en_US': {u'holdings': u'1 copy'}}],
 u'ca_objects.materials_techniques': [{u'en_US': {u'materials_techniques': u'Photocopy'}}],
 u'ca_objects.measurements_field': [{u'en_US': {u'measurements_field': u'Halfsize'}}],
 u'ca_objects.media_views': [{u'none': {u'Media_view_image_desc': u'-',
    u'media_views': u'Front'}}],
 u'ca_objects.notes': [{u'en_US': []}],
 u'ca_objects.subject_terms': [{u'en_US': {u'subject_terms': u'poetry '}},
  {u'en_US': {u'subject_terms': u'prose'}},
  {u'en_US': {u'subject_terms': u'Political writings'}},
  {u'en_US': {u'subject_terms': u'news'}},
  {u'en_US': []}],
 u'ca_objects.titleType': [{u'none': {u'titleType': u'published'}}],
 u'deleted': {u'value': u'0'},
 u'extent': {u'value': u'0'},
 u'extent_units': [],
 u'hier_left': {u'value': u'1.00000000000000000000'},
 u'hier_object_id': {u'value': u'655'},
 u'hier_right': {u'value': u'4294967296.00000000000000000000'},
 u'idno': {u'value': u'IA.ITM.612'},
 u'idno_sort': [],
 u'lot_id': {u'value': u'211'},
 u'object_id': {u'value': u'655'},
 u'ok': True,
 u'preferred_labels': {u'en_US': [u'Armistice (issue six)']},
 u'rank': {u'value': u'0'},
 u'related': {u'ca_list_items': [{u'_key': u'relation_id',
    u'direction': u'ltor',
    u'is_enabled': u'1',
    u'item_id': u'331',
    u'item_type_id': u'2',
    u'label': u'zine',
    u'labels': {u'1': u'zine'},
    u'locale_id': u'1',
    u'name_singular': u'zine',
    u'relation_id': u'830',
    u'relationship_type_code': u'format',
    u'relationship_type_id': u'195',
    u'relationship_typename': u'format',
    u'row_id': u'655'}],
  u'ca_object_lots': [{u'_key': u'lot_id',
    u'idno_stub': u'2014.040',
    u'item_type_id': u'60',
    u'label': u'Tom Quigley',
    u'labels': {u'1': u'Tom Quigley'},
    u'locale_id': u'1',
    u'lot_id': u'211',
    u'name': u'Tom Quigley',
    u'row_id': u'655'}],
  u'ca_object_representations': [{u'_key': u'relation_id',
    u'item_type_id': u'463',
    u'label': u'Cover Image',
    u'labels': {u'1': u'Cover Image'},
    u'locale_id': u'1',
    u'name': u'Cover Image',
    u'relation_id': u'145',
    u'representation_id': u'144',
    u'row_id': u'655'}]},
 u'representations': {u'144': {u'access': u'1',
   u'dimensions': {u'original': u'2104p x 3224p; 8 bpp; SRGB; 72ppi; 567.68kb',
    u'preview170': u'2104p x 3224p; 8 bpp; SRGB; 72ppi; 567.68kb'},
   u'info': {u'original': {u'EXTENSION': u'jpg',
     u'FILENAME': u'ca_object_representations_media_144_original.jpg',
     u'HASH': u'1',
     u'HEIGHT': 3224,
     u'MAGIC': 72014,
     u'MD5': u'7391f33be393b01671f49b152ceb3c97',
     u'MIMETYPE': u'image/jpeg',
     u'PROPERTIES': {u'bitdepth': 8,
      u'colorspace': u'SRGB',
      u'faces': [],
      u'filesize': 581304,
      u'height': 3224,
      u'mimetype': u'image/jpeg',
      u'resolution': {u'x': 72, u'y': 72},
      u'typename': u'JPEG',
      u'version': u'original',
      u'width': 2104},
     u'VOLUME': u'images',
     u'WIDTH': 2104},
    u'original_filename': u'interference catalog_5.jpg',
    u'preview170': {u'EXTENSION': u'jpg',
     u'FILENAME': u'ca_object_representations_media_144_preview170.jpg',
     u'HASH': u'1',
     u'HEIGHT': 170,
     u'MAGIC': 55199,
     u'MD5': u'3ac303db7520801302536591570ed3be',
     u'MIMETYPE': u'image/jpeg',
     u'PROPERTIES': {u'bitdepth': 8,
      u'colorspace': u'SRGB',
      u'faces': [],
      u'filesize': 78711,
      u'height': 170,
      u'mimetype': u'image/jpeg',
      u'quality': u'75',
      u'resolution': {u'x': 72, u'y': 72},
      u'typename': u'JPEG',
      u'version': u'preview170',
      u'width': 111},
     u'VOLUME': u'images',
     u'WIDTH': 111}},
   u'is_primary': u'1',
   u'label': u'Cover Image',
   u'locale_id': u'1',
   u'md5': u'7391f33be393b01671f49b152ceb3c97',
   u'mimetype': u'image/jpeg',
   u'name': u'English',
   u'num_multifiles': 0,
   u'original_filename': u'interference catalog_5.jpg',
   u'paths': {u'original': u'/srv/publicca/web/admin/media/ia_collectiveaccess/images/1/72014_ca_object_representations_media_144_original.jpg',
    u'preview170': u'/srv/publicca/web/admin/media/ia_collectiveaccess/images/1/55199_ca_object_representations_media_144_preview170.jpg'},
   u'rank': u'144',
   u'representation_id': u'144',
   u'status': u'4',
   u'tags': [],
   u'type_id': u'463',
   u'urls': {u'original': u'http://catalog.interferencearchive.org/admin/media/ia_collectiveaccess/images/1/72014_ca_object_representations_media_144_original.jpg',
    u'preview170': u'http://catalog.interferencearchive.org/admin/media/ia_collectiveaccess/images/1/55199_ca_object_representations_media_144_preview170.jpg'}}},
 u'status': {u'display_text': {u'en_US': u'completed'}, u'value': u'4'},
 u'type_id': {u'display_text': {u'en_US': u'Item'}, u'value': u'435'}}

#### create_entity()
Send it a dictionary of data for creating a new entity and it encodes to json and creates an entity in the catalog:
	
	data = {"preferred_labels": [
				{"locale": "en_US", 
			     "middlename": "", 
			     "surname": "TEST Accion Latina TEST", 
			     "forename": ""}], 
			"intrinsic_fields": {
				"idno": "test", 
				"type_id": 81}
			}
	
	client.create_entity(data)

Returns

	{"ok":true,"entity_id":<####>}.

#### create_object()
Send it a dictionary of data for creating a new object and it encodes to json and creates an object in the catalog:
	
	data = {
        "attributes": {
            "notes": [], 
            "dateSet": [
                {
                    "locale": "en_US", 
                    "dateSet": "1972"
                }
            ], 
            "measurements_field": [
                {
                    "locale": "en_US", 
                    "measurements_field": "45x26"
                }
            ], 
            "rightsSet": []
        }, 
        "preferred_labels": [
            {
                "locale": "en_US", 
                "name": "Red Boogie Benefit Concert for Berkeley Legal Defense and Blue Fairyland Nursery School"
            }
        ], 
        "related": {
            "ca_list_items": [
                {
                    "item_id": 329, 
                    "type_id": 195, 
                    "list_id": 57
                }
            ], 
            "ca_entities": [
                {
                    "entity_id": "2156", 
                    "type_id": 202
                }
            ], 
            "ca_object_lots": [
                {
                    "lot_id": 305, 
                    "type_id": 60
                }
            ]
        }, 
        "intrinsic_fields": {
            "idno": "IA.ITM.829", 
            "type_id": 435
        }
    }
	
	client.create_object(data)

Returns

	{"ok":true,"object_id":<####>}

#### update_entity()
Provide updated dictionary data for an entity (see `get_entity()`) and entity ID for entity to update and it will modify that record in the catalog:
	
	data = {}
	client.update_entity(10, data)

Returns:

	...


#### update_object()
Provide updated dictionary data for an object (see `get_object()`) and object ID for object to update and it will modify that record in the catalog:
	
	data = {}
	client.update_object(655, data)

Returns:

	....


#### delete_object() & delete_entity()
Provide ID for object or entity and it [soft deletes](http://docs.collectiveaccess.org/wiki/Web_Service_API#Deleting_records) this record in the catalog. It will still be in the catalog, but will not show up in search results:

	client.delete_object(655)

Returns:

	{u'deleted': u'2797', u'ok': True}



### Endpoints Reference

#### GET

* browse - `/browse/<table_name>`
* find - `/find/<table_name>?q=<your_query>`
* item - `/item/<table_name>/id/<item_id>`
* model (not used)

#### PUT 

* item (create) - '/item/<table_name>' + data
* item (update) - '/item/<table_name>/id/<item_id>' + data

#### DELETE

* item - '/item/<table_name>/id/<item_id>'



