from app import *
from datetime import datetime

class Theme(db.Document):
    meta = {'collection': 'Themes'}
    login = db.StringField(unique=True, required=True)
    theme = db.StringField(required=True)

class CurrentTheme(db.Document):
    meta = {'collection': 'CurrentTheme'}
    theme = db.StringField(required=True)
    year = db.StringField(default = str(datetime.today().year))
    start = db.DateTimeField()
    end = db.DateTimeField()