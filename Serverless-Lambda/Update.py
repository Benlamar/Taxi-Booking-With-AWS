import json
from Database import Customer, Taxi


def lambda_handler(event, context):
    # TODO implement
    # data = json.loads(event['body'])
    user = event['pathParameters']['user']
    print(user, '<------')
    if user == 'customers':
        customer_col = Customer()
        try:
            data = []
            for customer in customer_col.find():
                data.append({'id': customer['id'], 'name': customer['name'],
                             'location': customer['location'], 'status': customer['status'],
                             'timestamp': str(customer['timestamp'])})
            res = {"statusCode": 200, "msg": data}

        except:
            res = {"statusCode": 404, "msg": "Data not found"}

    if user == 'taxis':
        taxi_col = Taxi()
        try:
            data = []
            for taxi in taxi_col.find():
                data.append({'id': taxi['id'], 'name': taxi['name'], 'status': taxi['status'],
                             'type': taxi['type'],
                             'location': taxi['location'], 'timestamp': str(taxi['timestamp'])})
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
