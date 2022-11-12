from app import *

class Topic(db.EmbeddedDocument):
    meta = {'collection': 'Topics'}
    level = db.StringField(required=True)
    title = db.StringField(required=True)

class Contest(db.Document):
    meta = {'collection': 'Contests'}
    year = db.IntField(required=True)
    start = db.StringField(required=True)
    finish = db.StringField(required=True)
    topics = db.EmbeddedDocumentListField(Topic, default=[])