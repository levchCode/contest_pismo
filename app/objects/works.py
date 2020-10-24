from app import *


class Work(db.Document):
    meta = {'collection': 'Works'}
    login = db.StringField(unique=True, required=True)
    theme = db.StringField() #TODO Сделать привязку к сезонной теме. Создать коллекцию под тему, которую сгенерирует нейросеть.
    title = db.StringField(required=True)
    work = db.StringField(required=True)
    status = db.StringField(required=True)