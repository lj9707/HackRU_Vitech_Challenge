from enum import Enum
import requests
import json
from pymongo import MongoClient

client = MongoClient()
db = client['vitech']

base_url = 'https://v3v10.vitechinc.com/solr/'

class Collection(Enum):
    PARTICIPANT = 'participant',
    ACTIVITIES = 'activities',
    POLICY_INFO = 'policy_info'


def get_records(collection, rows=100, start=0):
    r = requests.get('https://v3v10.vitechinc.com/solr/policy_info/select?indent=on&q=*:*&wt=json&rows=' + str(rows) + '&start='+str(start)).text
    response = json.loads(r)
    return response['response']['docs']

def get_total_number_of_records(collection):
    return int(json.loads(requests.get(base_url + collection.value[0] + '/select?q=*:*&wt=json&rows=1').text)['response']['numFound'])


def get_all_records():
    mongo_collection = db['policy_info']
    records = []
    total_num_records=1482000
    rows_per_query = 100000
    for i in range(int(total_num_records/rows_per_query)+2):
        url = 'https://v3v10.vitechinc.com/solr/policy_info/select?indent=on&q=*:*&wt=json&rows='+str(rows_per_query)+'&start='+str(i*rows_per_query+1)
        v = requests.get(url).text
        response = json.loads(v)
        r = response['response']['docs']
        mongo_collection.insert(r)
        records = records + r
        print(str(int(i*rows_per_query)) + " out of " + str(total_num_records) + " rows retrieved")

    return records

