from app import *

class Review(db.EmbeddedDocument):
    meta = {'collection': 'Reviews'}
    judge = db.StringField(required=True)
    grammar = db.IntField()
    vocabulary = db.IntField()
    relevance = db.IntField()
    comment = db.StringField(default='')


class Essay(db.Document):
    meta = {'collection': 'Essays'}
    user = db.StringField(required=True)
    contest = db.StringField(required=True)
    active = db.IntField(required=True)
    date = db.StringField(required=True)
    title = db.StringField(required=True)
    text = db.StringField(required=True)
    reviews = db.EmbeddedDocumentListField(Review, default=[])
