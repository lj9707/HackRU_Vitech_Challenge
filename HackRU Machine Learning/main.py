from db import *
import pymongo
#from neural_net import *
import data_mixer



get_all_records()
#
# print(str(len(records)) + " records retrieved")

# from pymongo import MongoClient
# from bson.code import Code
#
# mapper = Code("""
#     function() {
#                   for (var key in this) { emit(key, null); }
#                }
# """)
# reducer = Code("""
#     function(key, stuff) { return null; }
# """)
#
# distinctThingFields = db.participant.map_reduce(mapper, reducer
#     , out = {'inline' : 1}
#     , full_response = True)
#
#
# print(distinctThingFields)


{'results': [{'_id': '_id', 'value': None},
             {'_id': '_version_', 'value': None},
             {'_id': 'collection_id', 'value': None},
             {'_id': 'id', 'value': None},
             {'_id': 'insurance_coverage', 'value': None},
             {'_id': 'insurance_plan', 'value': None},
             {'_id': 'insurance_premium', 'value': None},
             {'_id': 'insurance_product', 'value': None},
             {'_id': 'participant_id', 'value': None},
             {'_id': 'policy_start_date', 'value': None}],
 'counts': {'emit': 15320000, 'output': 10, 'input': 1532000, 'reduce': 153200}, 'ok': 1.0, 'timeMillis': 44706}


{'counts': {'output': 19, 'emit': 26487593, 'input': 1493700, 'reduce': 282830},
 'results': [{'_id': '_id', 'value': None},
             {'_id': '_version_', 'value': None},
             {'_id': 'accident_flag', 'value': None},
             {'_id': 'address_1', 'value': None},
             {'_id': 'birth_date', 'value': None},
             {'_id': 'city', 'value': None},
             {'_id': 'collection_id', 'value': None},
             {'_id': 'date_added', 'value': None},
             {'_id': 'dental_flag', 'value': None},
             {'_id': 'first_name', 'value': None},
             {'_id': 'id', 'value': None},
             {'_id': 'last_name', 'value': None},
             {'_id': 'latitude', 'value': None},
             {'_id': 'longitude', 'value': None},
             {'_id': 'marital_status', 'value': None},
             {'_id': 'middle_name', 'value': None},
             {'_id': 'postal_code', 'value': None},
             {'_id': 'sex', 'value': None},
             {'_id': 'state', 'value': None}],
 'timeMillis': 76309, 'ok': 1.0}
