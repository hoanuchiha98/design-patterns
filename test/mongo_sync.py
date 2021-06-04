"""Author: hoannk
   Date created: 04/06/2021
"""
from pymongo import MongoClient, ReadPreference

client = MongoClient('mongodb://u_journey:p_journey@dev.mobio.vn:27018/journey')

db = client.get_default_database()

collection = db.get_collection('journeys')

print(client)
print(collection)

# insert
doc = {
    "name": "[HoanNK] Test 1",
    "definition_file": "/journey-definitions/1b99bdcf-d582-4f49-9715-1b61dfff3924/016465f6-9ec7-4602-b76e-038c2d03b7c3_1615973191.json",
    "id": "016465f6-9ec7-4602-b76e-038c2d03b7c3ghnk",
    "description": None,
    "merchant_id": "1b99bdcf-d582-4f49-9715-1b61dfff3924",
    "master_campaign_id": "d5c5f232-f65d-4198-8c12-54981b28a090",
    "end_time": None,
    "channels": "WEB_PUSH",
    "status": "running",
    "config_receive_report": {
        "receive_report": False,
        "time_send": [
            "end_journey"
        ]
    },
    "finish_day": None,
    "finished_time": None,
    "receive_report": None,
    "state": None,
    "version": None,
    "vouchers": [

    ]
}
for i in range(10000):
    print('case ', i)
    if doc.get('_id', None):
        del doc['_id']
    journey_ins = collection.insert_one(document=doc)
    print('journey_ins: ', journey_ins.inserted_id)
    # update
    doc['state'] = 'validating'
    journey = collection.update_many({'_id': journey_ins.inserted_id}, {"$set": doc})
    # print(doc['_id'])
    journey_find_sec = db.get_collection('journeys', read_preference=ReadPreference.SECONDARY_PREFERRED).find_one(
        {'_id': journey_ins.inserted_id})
    journey_find_pri = db.get_collection('journeys', read_preference=ReadPreference.PRIMARY_PREFERRED).find_one(
        {'_id': journey_ins.inserted_id})
    print('journey_find_pri', journey_find_pri.get('state'), journey_find_pri.get('id'))
    print('journey_find_sec', journey_find_sec.get('state'), journey_find_sec.get('id'))

collection.delete_many({'id': '016465f6-9ec7-4602-b76e-038c2d03b7c3ghnk'})
