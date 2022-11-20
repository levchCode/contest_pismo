from app import *

class Topic(db.EmbeddedDocument):
    meta = {'collection': 'Topics'}
    level = db.StringField(required=True)
    title = db.StringField(required=True)

class Contest(db.Document):
    meta = {'collection': 'Contests'}
    year = db.IntField(required=True)
    start = db.IntField(required=True)
    finish = db.IntField(required=True)
    topics = db.EmbeddedDocumentListField(Topic, default=[])