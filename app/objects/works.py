from app import *

class Review(db.EmbeddedDocument):
    meta = {'collection': 'Reviews'}
    grammar = db.IntField()
    vocabulary = db.IntField()
    relevance = db.IntField()


class Essay(db.Document):
    meta = {'collection': 'Essays'}
    login = db.StringField(required=True)
    name = db.StringField(required=True)
    # Link of contests
    text = db.StringField(required=True)
    status = db.StringField(required=True, default='Опубликован')
    review = db.EmbeddedDocumentListField(Rating, default=[])
