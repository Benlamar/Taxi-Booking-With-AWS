import json
import pymongo
from bson.son import SON

# mongo db server endpoint
client = pymongo.MongoClient("") 

aggregator_db = client['TaxisandCustomers']
taxis = aggregator_db['taxis']
customers = aggregator_db['customers']
booking = aggregator_db['booking']

def deleteTaxi():
    try:
        taxis.delete_many({})
        return True
    except:
        return False


def deleteCustomer():
    try:
        customers.delete_many({})
        return True
    except:
        return False


def deleteBooking():
    try:
        booking.delete_many({})
        return True
    except:
        return False
    
def lambda_handler(event, context):
    # TODO implement
    # print(event)
    user = event['pathParameters']['user']
    if user == 'taxis':
        if deleteTaxi():
            res = {'status':200, 'msg':'Successful'}
        else:
            res ={'status':400, 'msg':'Error: can not delete taxis'}
    elif user == 'customers':
        if deleteCustomer():
            res = {'status':200, 'msg':'Successful'}
        else:
            res ={'status':400, 'msg':'Error: can not delete customers'}
    elif user == 'booking':
        if deleteBooking():
            res = {'status':200, 'msg':'Successful'}
        else:
            res ={'status':400, 'msg':'Error: can not delete Booking'}
    else:
        res = {'status':400, 'msg':'wrong resource'}
    
    return {
        'statusCode': res['status'],
        'body': json.dumps(res['msg']),
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
    }
