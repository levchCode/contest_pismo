from app import *


class User(db.Document):
    meta = {'collection': 'Users'}
    nickname = db.StringField(unique=True, required=True)
    role = db.StringField(required=False, default='contestant') #can be admin
    level = db.StringField(unique=False, required=True)
    email = db.StringField(unique=True, required=True)