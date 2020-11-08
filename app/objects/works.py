from app import *


class Rating(db.EmbeddedDocument):
    login = db.StringField(required=True)
    grammar = db.IntField(required=True)
    vocabulary = db.IntField(required=True)
    relevance = db.IntField(required=True)

class Work(db.Document):
    meta = {'collection': 'Works'}
    url = db.StringField(required=True)
    login = db.StringField(required=True)
    name = db.StringField(required=True)
    theme = db.StringField() #TODO Сделать привязку к сезонной теме. Создать коллекцию под тему, которую сгенерирует нейросеть.
    title = db.StringField(required=True)
    work = db.StringField(required=True)
    status = db.StringField(required=True)
    rating = db.EmbeddedDocumentListField(Rating, default= [])
