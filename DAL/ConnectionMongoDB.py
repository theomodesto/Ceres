from pymongo import MongoClient
def Connection(Collection):
    client = MongoClient('localhost',27017)
    #client = MongoClient("")

    #DATABASE
    db = client.test
    db = client['Ceres']

    #COLLECTION
    collection = db[Collection]
    return collection
