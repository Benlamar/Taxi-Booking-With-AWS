import json
from Database import Customer, Taxi, Booking
from datetime import datetime


customer_col = Customer()
taxi_col = Taxi()
booking_col = Booking()

def deletePendingTaxi(pending_taxi):
    for taxi in pending_taxi:
        Taxi.update_one({'id':taxi['taxi_id']}, {'$set':{'status':'Available'}})
        Booking.delete_one({'taxi_id':taxi['taxi_id'], 'customer':taxi['customer']})
    return "Deleted"

def updateLocation(taxi_id, customer,location):
    current_location = list(map(lambda x:x/100000,location))
    taxi_col.update_one({'id':taxi_id}, 
                    {'$set':{'timestamp':datetime.now(), 
                    'location':{'type':'Point','coordinates':current_location}}})
        
    customer_col.update_one({'name':customer}, 
                    {'$set':{'location':{'type':'Point','coordinates':current_location}}})

    booking_col.update_one({'customer':customer, 'taxi_id':taxi_id}, 
                    {'$set':{'source':{'type':'Point','coordinates':current_location}}})

    booking_col.update_one({'customer':customer, 'taxi_id':taxi_id}, 
                    {'$set':{'taxi_location':{'type':'Point','coordinates':current_location}}})
    return "Updating"

def lambda_handler(event, context):
    # TODO implement
    data = json.loads(event['body'])
    booking_id = data['booking_id']

    book = list(booking_col.find({'booking_id':booking_id, 'status':'Accepted'}))
    data = book[0]
    data.pop('_id')
        
    start = list(map(lambda x:int(x*100000),data['source']['coordinates']))
    stop = list(map(lambda x:int(x*100000),data['destination']['coordinates']))
        
    while True:
        if start[0] > stop[0]:
            start[0] -= 1
        elif start[0] < stop[0]:
            start[0] += 1
        if start[1] > stop[1]:
            start[1] -= 1
        elif start[1] < stop[1]:
            start[1] += 1
        update_res = updateLocation(data['taxi_id'], data['customer'], start)
        print(update_res)
        if start[0] == stop[0] and start[1] == stop[1]:
            break
        print('travelling ... ')
            
    print("Done")
    customer_col.update_one({'name':data['customer']}, {'$set':{'status':'Available'}})
    taxi_col.update_one({'id':data['taxi_id']}, {'$set':{'status':'Available'}})
    booking_col.update_one({'booking_id':data['booking_id']}, {'$set':{'status':'Completed'}})
    print('Passed')
    res = {'statusCode':200,'msg':"You have completed your journey"}
    
    return {
        'statusCode': res['statusCode'],
        'body': json.dumps(res['msg']),
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
    }
