from app import *
from objects.essay import Essay, Review
from objects.users import User
from objects.contest import Contest
from datetime import datetime

def getEssayById(id):
    return Essay.objects.get(id = id)

def getEssayByUserId(user_id):
    return Essay.objects.filter(user = user_id)

def getActiveEssay(user_id):
    return Essay.objects.get(user = user_id, active = 1)

def getRaiting(contest_id):
    return Essay.objects.filter(contest = contest_id)

def addReview(_id, data):
    try:
        user = User.objects.get(_id = data['user'])

        if user.token == data['token'] and user.role == 'admin':
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
        else:
            return {
                'status': 0,
                'msg': 'Unauthorized'
            }
    except Exception as e:
        return {
            'status': 0,
            'msg': str(e)
        }


def saveEssay(data):
    #TODO: проверить пользователя и можно загрузить только одно сочинение
    try:
        user = User.objects.get(_id = data['user'])
        thisYearEssay = Essay.objects.get(user = data['user'], contest = data['contest'])

        if user.token == data['token'] and thisYearEssay is not None:
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
                'essayId': str(essay.id),
                'url': '/work/' + str(essay.id),
                'msg': 'OK'
            }
        else:
            return {
                'status': 0,
                'msg': 'Unauthorized or too many essays submitted'
            }
    except Exception as e:
        return {
            'status': 0,
            'msg': str(e)
        }