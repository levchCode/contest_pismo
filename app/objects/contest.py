from app import *


class Contest(db.Document):
    meta = {'collection': 'Contest'}
    year = db.IntField(required=True)
    # themes = [{'level': Intermediate, 'theme': 'That'}]