from app import *


class User(UserMixin, db.Document):
    meta = {'collection': DB_collection_users}
    name = db.StringField(required=True)
    login = db.StringField(unique=True, required=True)
    email = db.StringField(unique=True, required=True)
    password = db.StringField()