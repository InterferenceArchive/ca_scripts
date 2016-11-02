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

### Methods (what you can do with the client once it's connected)

#### get_entities()
Allows you to search over all entities in your Collective Access site (without a query string, it returns everything):

	client.get_entities(q="SF Mime Troupe")

Returns

	...

#### get_objects()
Allows you to search over all objects in your Collective Access site (without a query string, it returns everything):

	client.get_objects(q="LA Free Press")


Returns

	...


#### get_entity() 
Given an entity ID of an entity already in the catalog returns details about that entity:

	client.get_entity(10)

Returns

	...

#### get_object()
Given an object ID of an object already in the catalog returns details about that object:

	client.get_object(655)

Returns

	...

#### create_entity()
Send it a dictionary of data for creating a new entity and it encodes to json and creates an entity in the catalog:
	
	data = {''}
	client.create_entity(data)

Returns

	...

#### create_object()
Send it a dictionary of data for creating a new object and it encodes to json and creates an object in the catalog:
	
	data = {''}
	client.create_object(data)

Returns

	...

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

	....



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



