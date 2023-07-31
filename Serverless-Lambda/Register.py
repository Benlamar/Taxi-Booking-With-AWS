import json
from Database import Customer, Taxi
from pymongo import GEOSPHERE

customer_col = Customer()
taxi_col = Taxi()


def lambda_handler(event, context):
    # TODO implement
    data = json.loads(event['body'])
    print(data)
    user = event['pathParameters']['user']
    if user == 'customer':
        if customer_col.count_documents({'id': data['id']}):
            res = {'statusCode': 409, 'msg': "customer ID already exist"}
        else:
            try:
                data['status'] = 'Available'
                # print(data)
                customer_col.insert_one(data)
                customer_col.create_index([('location', GEOSPHERE)])
                res = {'statusCode': 200,
                       'msg': "Successful Registration of Customer"}
            except Exception as e:
                print(e)
                res = {'statusCode': 400, 'msg': "Failed Operation"}

    if user == 'taxi':
        if taxi_col.count_documents({'id': data['id']}):
            res = {'statusCode': 409, 'msg': "taxi ID already exist"}
        else:
            try:
                data['status'] = 'Available'
                # print(data)
                taxi_col.insert_one(data)
                taxi_col.create_index([('location', GEOSPHERE)])
                res = {'statusCode': 200,
                       'msg': "Successful Registration of Taxis"}
            except Exception as e:
                print(e)
                res = {'statusCode': 400, 'msg': "Failed Operation"}
    print("res", res['msg'])

    return {
        'statusCode': res['statusCode'],
        'body': json.dumps(res['msg']),
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
    }
