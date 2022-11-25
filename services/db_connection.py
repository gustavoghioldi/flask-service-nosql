import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb+srv://barba:bgUW3Yh86nqr0sTO@cluster0.nucqsgs.mongodb.net/?retryWrites=true&w=majority")

class DBConnection:
    def __init__(self):
        self.db = client.stock

    def insert(self, article:dict)->str:
        return self.db.articles.insert_one(article).inserted_id

    def read(self, uid:str=None):
        if uid:
            return self.db.articles.find_one({"_id":ObjectId(uid)})
        else:
            cur = self.db.articles.find()
            ret = []
            for i in cur:
                i["_id"] = str(i["_id"])
                ret.append(i)
            return ret

    def update(self, uid):
        pass

    def search(self, parameter, value):
        pass