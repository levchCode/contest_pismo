from secret import DB_link, DB_name
from flask_pymongo import pymongo
from objects.user import User


# DB connection
client = pymongo.MongoClient(DB_link)
db = client.get_database(DB_name)

def addUser(user):
    try:
        result = db.Users.insert_one({"_id": user._id, "name": user.name, "password": user.password})
        return bool(result)
    except pymongo.errors.OperationFailure:
        return False

def updateUser(user):
    try:
        result = db.Users.update_one({"_id": user._id}, {"$set":{"name": user.name, "password": user.password}})
        print(result.modified_count)
        return result.modified_count
    except pymongo.errors.OperationFailure:
        return False

def getUser(_id):
    try:
        result = db.Users.find_one({"_id": _id})
        if result:
            return User(result['_id'], result['name'], result['password'])
        else:
            return False
    except pymongo.errors.OperationFailure:
        return False