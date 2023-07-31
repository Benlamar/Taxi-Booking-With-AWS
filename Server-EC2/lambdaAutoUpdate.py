import random
import datetime
import pymongo
import asyncio

client = pymongo.MongoClient("...")

db = client.TaxisandCustomers
taxis = db.taxis

def random_location():
    x_lad = random.uniform(28.55195, 28.75195)
    y_long = random.uniform(77.13149, 77.33149)
    return [round(x_lad,5), round(y_long,5)]


async def generatelocation(event, context):
    for obj in taxis.find():
        taxis.update_one({'id':obj['id'],'status': 'Available'},
            {'$set': {'location': {'type': 'Point', 'coordinates': [1,1]}}})
        print(obj)
    return "Success"

def lambda_handler(event, context):
    result = asyncio.run(generatelocation(event, context))
    print(result)



## Layers to add
# Pymongo
# bson
# pythondns

#increase time out