from ..collectiveaccess import CollectiveAccess

'''
script to relate all ingested Inkworks Press objects
to the Inkworks Press Collection (collection_id = )

relations defined as
	"item_type_id":"435",
    "object_id":"<OBJECT_ID>",
    "relationship_type_id":"100",
    "idno":"<IDNO>",
'''

# 1) get the list of OBJECT_IDs and their IDNOs


# 2) Create the JSON (see ../sample_output/prisoner_collection_id_30.json)


'''
{
	"collection_id": {
		"value": "<COLLECTION_ID>"
	},
	"type_id": {
		"value": "461",
		"display_text": {
			"en_US": "Subject Guide"
		}
	},
	"hier_collection_id": {
		"value": "30"
	},
	"related": {
		"ca_objects": [{
			"item_type_id": "435",
			"object_id": "<OBJECT_ID>",
			"relationship_type_id": "100",
			"idno": "<IDNO>",
			"relation_id": "100"
		}, {
			"item_type_id": "435",
			"object_id": "<OBJECT_ID>",
			"relationship_type_id": "100",
			"idno": "<IDNO>",
			"relation_id": "100"
		}]
	}
}
'''

# 3) Send data by update


