from pymongo import MongoClient
def Connection(Collection):
    client = MongoClient('localhost',27017)
    #DATABASE
    db = client['Ceres']
    #COLLECTION
    collection = db[Collection]
    return collection