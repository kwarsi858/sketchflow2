from pymongo import MongoClient


def users(table):
    client = MongoClient('localhost',27017)
    db = client['sketchflow']
    collection = db[table]
    return collection



