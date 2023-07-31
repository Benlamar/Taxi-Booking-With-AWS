import json
from Database import Customer, Booking, Taxi
from pymongo import GEOSPHERE

customer_col = Customer()
booking_col = Booking()
taxi_col = Taxi()


def findNearestTaxi(location, type):
    data = []
    if type == "Any":
        query = {'location': {"$near": location}, "status": {"$eq": "Available"}}
    else:
        query = {'location': {"$near": location},
             "type": type, "status": {"$eq": "Available"}}
    for taxi in taxi_col.find(query).limit(3):
        data.append({'id': taxi['id'], 'name': taxi['name'],
                    'type': taxi['type'], 'status': taxi['status'],
                     'location': taxi['location'], 'timestamp': str(taxi['timestamp'])})
    return data


def setNotification(customerData, taxiData):
    try:
        customer_col.update_one({"id": customerData['id']}, {
                                "$set": {"status": "Requesting"}})
        for taxi in range(len(taxiData)):
            taxi_col.update_one({"id": taxiData[taxi]['id']}, {
                                "$set": {"status": "Pending"}})
            booking_col.insert_one({
                "booking_id": "Booking_"+taxiData[taxi]['name'],
                "taxi_id": taxiData[taxi]['id'],
                "taxi": taxiData[taxi]['name'],
                "customer": customerData["name"],
                "status": "Pending",
                "type": taxiData[taxi]["type"],
                "timestamp": customerData["timestamp"],
                "source": customerData["location"],
                "destination": customerData["destination"],
                "taxi_location": taxiData[taxi]["location"]})
        booking_col.create_index([("destination", GEOSPHERE)])
        return True
    except Exception as e:
        print(e)
        return False


def lambda_handler(event, context):
    # TODO implement
    data = json.loads(event['body'])
    print(data)
    taxi_list = findNearestTaxi(data['location'], data['type'])
    print("-->", taxi_list)
    notification_res = setNotification(data, taxi_list)
    if notification_res:
        res = {"statusCode": 200, "msg": taxi_list}
    else:
        res = {"statusCode": 400, "msg": 'Error: cannot request taxi'}

    return {
        'statusCode': res['statusCode'],
        'body': json.dumps(res['msg']),
        'headers': {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
    }
