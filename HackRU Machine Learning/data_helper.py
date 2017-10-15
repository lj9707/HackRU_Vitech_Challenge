from enum import Enum
import pickle
from itertools import chain
from random import shuffle

from pymongo import MongoClient

client = MongoClient()
db = client['vitech']


col = db['new_final']

print('Loading data...')
positives = col.find({'accidental':'Y'})
print(str(positives.count())  + ' positives found')
negatives = col.find({'accidental':'N'}).limit(220000)
results = [x for x in chain(positives, negatives)]
shuffle(results)
print('Data loaded')

testing_data = results

training_data = results

class MARITAL_STATUS(Enum):
    SINGLE = 0
    MARRIED = 1

class SEX(Enum):
    MALE = 0
    FEMALE = 1

class DENTAL(Enum):
    NO = 0
    YES = 1

class ACCIDENTAL(Enum):
    NO = 0
    YES = 1

class INSURANCE_PRODUCT(Enum):
    ACCIDENTAL = 0
    DENTAL = 1


class INSURANCE_COVERAGE(Enum):
    SINGLE = 0
    FAMILY = 1

class INSURANCE_PLAN(Enum):
    GOLD = 0
    SILVER = 1
    REGULAR = 2

class PROMOCODE(Enum):
    FREESPOUSE = 0
    FREEZE = 1
    FREEMONTH = 2
    FINCON = 3


class STATE(Enum):
    NOVA_SCOTIA = 0
    NORTHWEST_TERRITORY = 0.25
    NUNAVUT_TERRITORY = 0.5
    ALBERTA = 0.75
    BRITISH_COLUMBIA = 1
    ONTARIO = 1.25
    QUEBEC = 1.5
    SASKATCHEWAN = 1.75
    YUKON = 2
    PRINCE_EDWARD_ISLAND = 2.25
    MANITOBA = 2.5
    NEW_BRUNSWICK = 2.75
    NEWFOUNDLAND = 3


testing_set_size = 15000

last_index = testing_set_size


def process_batch(data, start, end):

    batch_x = []
    batch_y = []
    for i in range(start, end):
        #print(str(i))
        row = data[i]
        x = []
        y = [0,0]

        marital_status = row['marital_status']
        if marital_status == 'S':
            x.append(MARITAL_STATUS.SINGLE.value)
        else:
            x.append(MARITAL_STATUS.MARRIED.value)

        sex = row['sex']
        if sex == 'M':
            x.append(SEX.MALE.value)
        else:
            x.append(SEX.FEMALE.value)

        x.append(float(row['longitude'])/40)
        x.append(float(row['latitude'])/40)

        date_added = row['date_added']
        x.append(int(date_added.strftime("%s"))/31536000/30)


        birth_date = row['birth_date']
        x.append(int(birth_date.strftime("%s"))/31536000/30)


        insurance_coverage = row['insurance_coverage']
        if insurance_coverage == 'Family':
            x.append(INSURANCE_COVERAGE.FAMILY.value)
        else:
            x.append(INSURANCE_COVERAGE.SINGLE.value)

        x.append(int(row['insurance_premium'])/20)

        insurance_plan = row['insurance_plan']
        if insurance_plan == 'Silver':
            x.append(INSURANCE_PLAN.SILVER.value)
        elif insurance_plan =='Gold':
            x.append(INSURANCE_PLAN.GOLD.value)
        else:
            x.append(INSURANCE_PLAN.REGULAR.value)

        policy_start_date = row['policy_start_date']
        x.append(int(policy_start_date.strftime("%s"))/31536000/30)

        state = row['state']

        if state == 'Nova Scotia':
            x.append(STATE.NOVA_SCOTIA.value)
        elif state == 'Northwest Territory':
            x.append(STATE.NORTHWEST_TERRITORY.value)
        elif state == 'Nunavut Territory':
            x.append(STATE.NUNAVUT_TERRITORY.value)
        elif state == 'Alberta':
            x.append(STATE.ALBERTA.value)
        elif state == 'British Columbia':
            x.append(STATE.BRITISH_COLUMBIA.value)
        elif state == 'Ontario':
            x.append(STATE.ONTARIO.value)
        elif state == 'Quebec':
            x.append(STATE.QUEBEC.value)
        elif state == 'Saskatchewan':
            x.append(STATE.SASKATCHEWAN.value)
        elif state == 'Yukon':
            x.append(STATE.YUKON.value)
        elif state == 'Prince Edward Island':
            x.append(STATE.PRINCE_EDWARD_ISLAND.value)
        elif state == 'Manitoba':
            x.append(STATE.MANITOBA.value)
        elif state == 'New Brunswick':
            x.append(STATE.NEW_BRUNSWICK.value)
        else:
            x.append(STATE.NEWFOUNDLAND.value)


        if len(x) != 11:
            raise Exception('Wrong x size')

        if row['accidental'] == 'Y':
            y[1] = 1
        else:
            y[0] = 1

        batch_x.append(x)
        batch_y.append(y)

    return (batch_x, batch_y)


print('Processing test set...')
test_set = process_batch(testing_data, 0, testing_set_size)
print('Test set processed\nSaving test set to file...')
pickle.dump( test_set, open( "test_set.p", "wb" ) )
print('Done')



# Inputs:
# -marital_status
# -sex
# -longitude
# -latitude
# -date_added
# -dental_flag
# -accidental
# -birth_date
# -insurance_product
# -insurance_coverage
# -insurance_premium
# -insurance_plan
# -policy_start
#
# Output:
# -promocode
def next_train_batch(size):
    global last_index

    batch =  process_batch(training_data, last_index, last_index+size)
    last_index = last_index+size

    return batch


def get_test_data():
    return test_set