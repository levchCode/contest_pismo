from app import *
from datetime import datetime
from objects.contest import Contest, Topic

def getContests(active):
    if active:
        data = Contest.objects.get(active = active)
    else:
        data = Contest.objects.all()
    
    return data

def getContestById(_id):
    return Contest.objects.get(pk=_id)

def createContest(data):
    try:
        topics = []
        for t in data['topics']:
            topics.append(Topic(level=t['level'], title=t['title']))

        Contest(
            year = str(datetime.today().year),
            start = data['start'],
            finish = data['finish'],
            topics = topics
        ).save()

        return {
            'status': 1,
            'msg': 'OK'
        }
    except Exception as e:
        return {
            'status': 0,
            'msg': str(e)
        }

def updateContest(_id, data):
    try:
        contest = Contest.objects.get(pk=_id)

        topics = []
        for t in data['topics']:
            topics.append(Topic(level=t['level'], title=t['title']))

        
        contest['year'] = str(datetime.today().year)
        contest['start'] = data['start']
        contest['finish'] = data['finish']
        contest['topics'] = topics
        
        contest.save()

        return {
            'status': 1,
            'msg': 'OK'
        }
    except Exception as e:
        return {
            'status': 0,
            'msg': str(e)
        }