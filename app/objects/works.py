from app import *
from datetime import datetime

class Rating(db.EmbeddedDocument):
    login = db.StringField()
    name = db.StringField()
    grammar = db.IntField()
    vocabulary = db.IntField()
    relevance = db.IntField()
    comment = db.StringField()

class Work(db.Document):
    meta = {'collection': 'Works'}
    url = db.StringField(required=True)
    login = db.StringField(required=True)
    name = db.StringField(required=True)
    theme = db.StringField(required=True)
    title = db.StringField(required=True)
    work = db.StringField(required=True)
    status = db.StringField(required=True, default='На рассмотрении')
    rating = db.EmbeddedDocumentListField(Rating, default=[])
    voices = db.IntField(default=0)
    year = db.StringField(default = str(datetime.today().year))
