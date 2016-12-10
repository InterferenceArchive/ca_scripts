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
   "intrinsic_fields":{  
      "type_id":461,
      "access":"1",
      "status":"4"
   },
   "related":{  
      "ca_objects":[  
         {  
            "object_id":982,
            "type_id":100
         },
         {  
            "object_id":983,
            "type_id":100
         },
         {  
            "object_id":984,
            "type_id":100
         },
         {...}
      ]
   }
}
'''

# 3) Send data by update


