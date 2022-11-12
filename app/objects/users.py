from app import *


class User(db.Document):
    meta = {'collection': 'Users'}
    nickname = db.StringField(unique=True, required=True)
    role = db.StringField(required=True, default='contestant') #can be admin
    level = db.StringField(unique=True, required=True)