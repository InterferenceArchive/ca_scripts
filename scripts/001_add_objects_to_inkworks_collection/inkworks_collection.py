from ... import collectiveaccess as ca
import json
import argparse


'''
script to relate all ingested Inkworks Press objects
to the Inkworks Press Collection (collection_id = )

relations defined as
	"item_type_id":"435",
    "object_id":"<OBJECT_ID>",
    "relationship_type_id":"100",
    "idno":"<IDNO>",

RUN WITH: `python -m ca_scripts.scripts.001_add_objects_to_inkworks_collection.inkworks_collection -u <USER> -p <PASSWORD>` outside of this folder
'''

# 0) Create a collection in Collective Access (could do it with API, also)

# 1) Prepare Client

parser = argparse.ArgumentParser(description='Script for batch editing IA Collective Access content')
parser.add_argument('-u', '--user', help='Collective Access Username', required=True)
parser.add_argument('-p', '--password', help='Collective Access Password', required=False)

args = vars(parser.parse_args())

_USER = args['user'] 
_PASS = args['password']
_SITE = 'https://catalog.interferencearchive.org/admin'

client = ca.CollectiveAccess(_SITE, _USER, _PASS)

# 2) Use inkworks collection.json to update sample of which is:

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

path_to_json = './ca_scripts/scripts/001_add_objects_to_inkworks_collection/inkworks_collection.json'

data = json.loads(open(path_to_json, 'r').read())


# 3) Send data by update

res = client.update_collection(39, data)

print "sending data, please wait..."

print res

