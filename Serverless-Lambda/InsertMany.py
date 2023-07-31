import json
import pymongo
from bson.son import SON
import datetime

# mongo server endpoint
client = pymongo.MongoClient("") 

aggregator_db = client['TaxisandCustomers']
taxis = aggregator_db['taxis']
customers = aggregator_db['customers']

def registerTaxi(data):
    taxis.delete_many({})
    try:
        taxis.insert_many(data)
        taxis.create_index([('location', pymongo.GEOSPHERE)])
        return True
    except:
        return False

def getTaxiList():
    carlist = []
    for doc in taxis.find():
        carlist.append({'id':doc['id'], 'name':doc['name']})
    return {'status':200, 'msg':carlist}

def registerCustomer(data):
    customers.delete_many({})
    try:
        customers.insert_many(data)
        customers.create_index([('location', pymongo.GEOSPHERE)])
        return True
    except:
        return False

def getCustomerList():
    customerlist = []
    for doc in customers.find():
        customerlist.append(doc['name'])
    return {'status':200, 'msg':customerlist}
    
def lambda_handler(event, context):
    # TODO implement
    # print(event)
    user = event['pathParameters']['user']
    if user == 'taxis':
        data = json.loads(event['body'])
        for item in data:
            item['status'] = 'Available'
            item['timestamp'] = str(datetime.datetime.now())[:-3]
        reg = registerTaxi(data)
        if reg:
            res = getTaxiList()
        else:
            res ={'status':400, 'msg':'Error: can not insert customers'}
    elif user == 'customer':
        data = json.loads(event['body'])
        for item in data:
            item['status'] = 'Available'
            item['timestamp'] = str(datetime.datetime.now())[:-3]
        if registerCustomer(data):
            res = getCustomerList()
        else:
            res ={'status':400, 'msg':'Error: can not insert customers'} 
    else:
        res = {'status':400, 'msg':'wrong resource'}
    
    
    # client.close()
    
    return {
        'statusCode': res['status'],
        'body': json.dumps(res['msg'])
    }
