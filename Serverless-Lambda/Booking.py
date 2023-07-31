import json
from Database import Booking, Taxi, Customer

booking_col = Booking()
taxi_col = Taxi()
customer_col = Customer()

def lambda_handler(event, context):
    # TODO implement
    data = json.loads(event['body'])
    print(data)
    booking_id = data

    booking_col.update_one({'booking_id':booking_id['booking_id'], 'status':{'$ne':'Completed'}}, {'$set':{'status':'Accepted'}})
    book = list(booking_col.find({'booking_id':booking_id['booking_id']}))
    customer_name = book[0]['customer']
    taxi_id=book[0]['taxi_id']

    taxi_col.update_one({'id':taxi_id}, 
                {'$set':{
                    'location':{'type':'Point','coordinates':book[0]['source']['coordinates']}, 'status':'Accepted'}})
        
    customer_col.update_one({'name':customer_name}, {'$set':{'status':'Accepted'}})
    pending = booking_col.find({'booking_id':{"$ne":booking_id['booking_id']}, 'status':{'$ne':'Completed'}})
    for taxi in pending:
        taxi_col.update_one({'id':taxi['taxi_id']}, {'$set':{'status':'Available'}})
        booking_col.delete_one({'taxi_id':taxi['taxi_id'], 'customer':taxi['customer']})
                
    res = {"statusCode":200,"msg":"Trip request accepted"}

    return {
        'statusCode': res['statusCode'],
        'body': json.dumps(res['msg']),
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
    }