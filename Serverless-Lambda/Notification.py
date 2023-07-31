import json
from Database import Booking

booking_col = Booking()


def lambda_handler(event, context):
    # TODO implement
    # data = json.loads(event['body'])
    # print(data)
    id = int(event['pathParameters']['id'])
    notification = {}
    noti = list(booking_col.find(
        {'taxi_id': id, 'status': {'$ne': 'Completed'}}))
    if len(noti) > 0:
        notification = noti[0]
        notification.pop('_id')

    print(notification)
    res = {"statusCode": 200, "msg": notification}

    return {
        'statusCode': res['statusCode'],
        'body': json.dumps(res['msg']),
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
    }
