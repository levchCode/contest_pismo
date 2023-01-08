from app import *


class User(db.Document):
    meta = {'collection': 'Users'}
    nickname = db.StringField(unique=True, required=True)
    role = db.StringField(required=False, default='contestant')
    level = db.StringField(unique=False, required=True)
    email = db.StringField(unique=True, required=True)
    hash = db.StringField(unique=True, required=True)
    token = db.StringField(unique=True, required=True)