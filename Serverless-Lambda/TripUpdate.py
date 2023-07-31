import json
from Database import Customer, Booking

customer_col = Customer()
booking_col = Booking()

def lambda_handler(event, context):
    # TODO implement
    
    customer_id = int(event['pathParameters']['id'])
    # print(type(customer_id))

    customer = list(customer_col.find({'id': customer_id}))
    print(customer)
    customer_name = customer[0]['name']
    try:
        data = []
        for book in booking_col.find({'customer': customer_name, 'status': {'$ne': 'Completed'}}):
            data.append({'name': book['taxi'],
                        'location': book['taxi_location'], 'type': book['type']})
        res = {"statusCode": 200, "msg": data}
    except:
        res = {"statusCode": 404, "msg": "Data not found"}

    return {
        'statusCode': res['statusCode'],
        'body': json.dumps(res['msg']),
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
    }
