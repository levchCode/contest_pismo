from app import *
from datetime import datetime
from objects.contest import Contest, Topic

def createContest(data):
    try:
        topics = []
        for t in data['topics']:
            topics.append(Topic(level=t['level'], title=t['title']))

        contest = Contest(
            year = str(datetime.today().year),
            start = data['start'],
            finish = data['finish'],
            topics = topics
        )

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
