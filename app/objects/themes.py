from app import *
from datetime import datetime

class Theme(db.Document):
    meta = {'collection': 'Themes'}
    login = db.StringField(unique=True, required=True)
    theme = db.StringField(required=True)

class CurrentTheme(db.Document):
    meta = {'collection': 'CurrentTheme'}
    theme = db.StringField(required=True, default='')
    year = db.StringField(required=True, default = str(datetime.today().year))
    stage_1 = db.DateTimeField(required=True)
    stage_2 = db.DateTimeField(required=True)
    stage_3 = db.DateTimeField(required=True)
    stage_4 = db.DateTimeField(required=True)