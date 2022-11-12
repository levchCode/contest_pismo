from app import *

class Review(db.EmbeddedDocument):
    meta = {'collection': 'Reviews'}
    grammar = db.IntField()
    vocabulary = db.IntField()
    relevance = db.IntField()


class Essay(db.Document):
    meta = {'collection': 'Essays'}
    user = db.StringField(required=True)
    contest = db.StringField(required=True)
    date = db.StringField(required=True)
    title = db.StringField(required=True)
    text = db.StringField(required=True)
    status = db.StringField(required=True, default='Опубликован')
    reviews = db.EmbeddedDocumentListField(Review, default=[])
