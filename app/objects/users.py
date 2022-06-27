from app import *


class User(db.Document):
    meta = {'collection': 'Users'}
    name = db.StringField(required=True)
    nickname = db.StringField(unique=True, required=True)
    role = db.StringField(required=True, default='User') # Can be 'User' (no contest), 'Contestant' (contest is underway)