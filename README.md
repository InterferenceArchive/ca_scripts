Collective Access Client
========================

This is a python client for interating with the collective access client for the Interference Archive. 

It is built as a set of bindings for the [Collective Access Web Service API](http://docs.collectiveaccess.org/wiki/Web_Service_API). The Web Service API covers a lot of endpoints and interactions, many of which we probably won't need. Therefore, this is not built to be a general purpose Collective Access API. 

### Endpoints

#### GET

* browse - `/browse/<table_name>`
* find - `/find/<table_name>?q=<your_query>`
* item - `/item/<table_name>/id/<item_id>`
* model (not used)

#### PUT 

* item (create) - '/item/<table_name>' + data
* item (update) - '/item/<table_name>/id/<item_id>' + data

#### DELETE

* item

### Contents

* search entities
* search objects
* search for a specific entity
* search for a specific object
* add an entity to the catalog
* add an object to the catalog
* remove an entity from the catalog
* remove an object from the catalog


### Examples for using the client

*
*
*
