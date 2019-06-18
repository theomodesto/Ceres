from pymongo import MongoClient
def Connection(Collection):
    #client = MongoClient('localhost',27017)
    client = MongoClient("mongodb://Ceres:Ceres1234@ceres-shard-00-00-vol56.mongodb.net:27017,ceres-shard-00-01-vol56.mongodb.net:27017,ceres-shard-00-02-vol56.mongodb.net:27017/test?ssl=true&replicaSet=Ceres-shard-0&authSource=admin&retryWrites=true&w=majority")

    #DATABASE
    db = client.test
    db = client['Ceres']

    #COLLECTION
    collection = db[Collection]
    return collection