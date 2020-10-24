from app import *


class Theme(db.Document):
    meta = {'collection': 'Themes'}
    login = db.StringField(unique=True, required=True)
    theme = db.StringField(required=True)