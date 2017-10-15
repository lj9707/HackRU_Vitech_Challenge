from pymongo import MongoClient
from dateutil.parser import parse

client = MongoClient()
db = client['vitech']


col_activities = db['activities']
col_policy_info = db['policy_info']
col_participant = db['participants']

col_final = db['new_final']


participants = col_participant.find()

counter = 0


rows = []

for participant in participants:
    policy = col_policy_info.find_one({'participant_id':participant['id']})

    row = {'id':participant['id'],
                       'first_name': participant['first_name'],
                       'last_name' : participant['last_name'],
                       'marital_status':participant['marital_status'],
                       'sex':participant['sex'],
                       'longitude': participant['longitude'],
                       'latitude': participant['latitude'],
                       'date_added': parse(participant['date_added']),
                       'state': participant['state'],
                       'city' : participant['city'],
                       'postal_code':participant['postal_code'],
                       'dental_flag': participant['dental_flag'],
                       'birth_date': parse(participant['birth_date']),
                       'insurance_product': policy['insurance_product'],
                       'insurance_coverage':policy['insurance_coverage'],
                       'insurance_premium': policy['insurance_premium'],
                       'insurance_plan': policy['insurance_plan'],
                       'policy_start_date': parse(policy['policy_start_date']),
                       'accidental': 'N' if not ('accident_flag' in participant) else participant['accident_flag'],
           }

    if 'promo_codes' in policy:
        row['promo_code'] = policy['promo_codes']

        total_targeted_count = 0
        activity_types = ''
        activity_date = None

        activites = col_activities.find({'promocodes':policy['promo_codes']})
        for activity in activites:
            total_targeted_count = total_targeted_count+int(activity['targeted_counts'])
            activity_types = activity_types + activity['activity_type']+', '
            activity_date = parse(activity['activity_date'])

        activity_types = activity_types[:-2]
        row['targeted_count'] = total_targeted_count
        row['activity_type'] = activity_types
        row['activity_date'] = activity_date

    else:
        row['promo_code'] = None
        row['targeted_count'] = None
        row['activity_type'] = None
        row['activity_date'] = None





    rows.append(row)

    if counter % 10000 == 0:
        col_final.insert(rows)
        rows = []

    counter = counter+1
    print(str(counter))




#
# activities = [('FREEZE', '2016-02-15'), ('FREEMONTH', '2016-04-01'), ('FREESPOUSE', '2016-04-01'),('FINCON', '2016-07-01')]
#
# count = 0
#
#
# policies = col_policy_info.find()
#
#
#
#
# ids = []
#
# for policy in policies:
#     ids.append(policy['participant_id'])
#
#
#
# print('participant ids: ' + str(len(set(ids))))
#
#
# participants = col_participant.find({'id': {'$in': ids}})
#
#
# counter = 0
#
# for participant in participants:
#
#     policy = col_policy_info.find_one({'participant_id':participant['id']})
#     activity = col_activities.find_one({'promocodes': policy['promo_codes']})
#
#     row = {'id':participant['id'],
#                    'first_name': participant['first_name'],
#                    'last_name' : participant['last_name'],
#                    'marital_status':participant['marital_status'],
#                    'sex':participant['sex'],
#                    'longitude': participant['longitude'],
#                    'latitude': participant['latitude'],
#                    'date_added': participant['date_added'],
#                    'state': participant['state'],
#                    'city' : participant['city'],
#                    'dental_flag': participant['dental_flag'],
#                    'birth_date': participant['birth_date'],
#                    'insurance_product': policy['insurance_product'],
#                    'insurance_coverage':policy['insurance_coverage'],
#                    'insurance_premium': policy['insurance_premium'],
#                    'insurance_plan': policy['insurance_plan'],
#                    'policy_start_date': policy['policy_start_date'],
#                    'accidental': 'N' if not ('accident_flag' in participant) else participant['accident_flag'],
#                    'promocode': activity['promocodes'],
#                    'activity_start_date': activity['activity_date']
#                    }
#
#     col_final.insert(row)
#     counter = counter+1
#     print(str(counter))
#
# print(str(participants.count()))
#
#
# for participant in participants:
#     policy = col_policy_info.find({'participant_id':})
#
# for activity in activities:
#
#     policies = col_policy_info.find({'promo_codes':activity[0]})
#
#     print(activity[0])
#
#
#
#
#
#     for policy in policies:
#         participant = col_participant.find({'id':policy['participant_id']})
#         count = count+1
#         print(str(count))
#
#         if(participant.count()==0):
#             continue
#
#         row = {'id':participant['id'],
#                'first_name': participant['first_name'],
#                'last_name' : participant['last_name'],
#                'marital_status':participant['marital_status'],
#                'sex':participant['sex'],
#                'longitude': participant['longitude'],
#                'latitude': participant['latitude'],
#                'date_added': participant['date_added'],
#                'state': participant['state'],
#                'dental_flag': participant['dental_flag'],
#                'birth_date': participant['birth_date'],
#                'insurance_product': policy['insurance_product'],
#                'insurance_coverage':policy['insurance_coverage'],
#                'insurance_premium': policy['insurance_premium'],
#                'insurance_plan': policy['insurance_plan'],
#                'policy_start_date': policy['policy_start_date'],
#                'promocode': activity[0],
#                'activity_start_date': activity[1]
#                }
#
#         print('Inserting...')
#
#         col_final.insert(row)