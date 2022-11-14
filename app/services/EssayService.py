from app import *
from objects.essay import Essay, Review;
from datetime import datetime

def getEssayById(id):
    return Essay.objects.get(_id = id)

def getEssayByUserId(user_id):
    return Essay.objects.get(user = user_id)

def getActiveEssay(user_id):
    return Essay.objects.get(user = user_id, active = 1)

def getRaiting(contest_id):
    return Essay.objects.get(contest=contest_id)

def addReview(_id, data):
    #TODO: проверка на админа
    try:
        essay = Essay.objects.get(pk=_id)

        essay.reviews.append(Review(
            user = data['user'],
            grammar = data['grammar'],
            vocabulary = data['vocabulary'],
            relevance = data['relevance'],
            comment = data['comment']
        ))
        essay.save()

        return {
            'status': 1,
            'msg': 'OK'
        }
    except Exception as e:
        return {
            'status': 0,
            'msg': str(e)
        }


def saveEssay(data):
    #TODO: проверить пользователя и можно загрузить только одно сочинение
    try:
       
        essay = Essay(
            user = data['user'],
            contest = data['contest'],
            active = 1,
            date = str(datetime.today()),
            title =  data['title'],
            text = data['text'],
            reviews = []
        ).save()

        return {
            'status': 1,
            'url': '/work/' + str(essay.id),
            'msg': 'OK'
        }
    except Exception as e:
        return {
            'status': 0,
            'msg': str(e)
        }