from pymongo import MongoClient

class Database:
    def __init__(self, database, collection):
        self.database = self._createDB(database)
        self.collection = self._createCollection(collection)

    def _createDB(self, dbname):
        # paste your mongodb atlas server endpoint here
        mongo_connect = MongoClient("...")
        db = mongo_connect[dbname]
        return db

    def _createCollection(self, collection_name):
        coll = self.database[collection_name]
        return coll

    def getCollection(self):
        return self.collection
        
    def getDatabase(self):
        return self.database

