from pymongo import MongoClient

# paste your mongodb atlas server endpoint here
url = "..."

client = MongoClient(url)
database = client["TaxisandCustomers"]


def Customer():
    collection = database['customers']
    return collection


def Taxi():
    collection = database['taxis']
    return collection


def Booking():
    collection = database['booking']
    return collection
