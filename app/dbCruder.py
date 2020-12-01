from werkzeug.security import generate_password_hash, check_password_hash
from secret import DB_link, DB_name
from app import *
from objects.users import User
from objects.works import Work, Rating
from objects.themes import CurrentTheme, Theme
import uuid
from datetime import datetime


def addUser(name, login, email, password):
    try:
        password = generate_password_hash(password)
        user = User(name=name, login=login, email=email, password=password).save()
        login_user(user, remember=True)
        return True

    except:
        return False

def loginUser(login, password):
    try:
        user = User.objects.get(login=login)

        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            return user
    except:
        return False

def updateUser(name, login, email, password):
    try:
        user = User.objects.get(login=login).update_one(name=name, login=login, email=email, password=password)
        return True

    except:
        return False

def getUser(login):
    try:
        user = User.objects.get(login=login)
        works = Work.objects(login=login)
        return {"name": user['name'], 
                "login": user['login'], 
                "email": user['email'], 
                "password": user['password'],
                "works": [[work['url'], work['theme'], work['title'], work['status'], work['year']] for work in works]}
    except:
        return False

def addCurrentTheme(theme, start, end):
    last_theme = CurrentTheme.objects.order_by('-id').first()
    current_time = datetime.now()
    print(current_time > last_theme['end'])
    if current_time > last_theme['end']:
        Theme.drop_collection()
    theme = CurrentTheme(theme=theme, start=start, end=end).save()
    return True

def getCurrentStage():
    all_themes = CurrentTheme.objects.order_by('-id')
    current_theme = None
    stage = ""
    current_time = datetime.now()

    for i in all_themes:
        if i['start'] <= current_time and i['end'] >= current_time :
            second_stage_time = datetime.fromtimestamp( datetime.timestamp(i['start']) + (datetime.timestamp(i['end']) - datetime.timestamp(i['start']) ) // 3)
            third_stage_time = datetime.fromtimestamp( datetime.timestamp(i['start']) + (datetime.timestamp(i['end']) - datetime.timestamp(i['start']) ) // 1.5)
            if current_time < second_stage_time:
                stage = "Suggestion"
            elif current_time < third_stage_time:
                stage = "Loading"
            else:
                stage = "Assessment"
    return stage

def addTheme(login, theme):
    try:
        theme = Theme(login=login, theme=theme).save()
        return True
    except:
        return False

def addWork(login, name, title, work):
    current_theme = CurrentTheme.objects.order_by('-id').first()['theme']
    for i in getWorksByLogin(login):
        if i['theme'] == current_theme:
            return False
    else:
        url = str(uuid.uuid4())
        work = Work(url=url, login=login, name=name, theme=current_theme, title=title, work=work).save()
        return True

def getWork(url):
    try:
        work = Work.objects.get(url=url)
        return work
    except:
        return False

def getCanVote():

    current_theme = CurrentTheme.objects.order_by('-id').first()['theme']
    try:
        last_work = Work.objects.order_by('-id').get(login=current_user.login)
    except:
        last_work = None

    if last_work and last_work['theme'] == current_theme:
        return True
    else:
        return False

def getWorksByLogin(login):
    return Work.objects(login=login)

def getAllWorksByLastTheme():
    last_theme = CurrentTheme.objects.order_by('-id').first()
    current_time = datetime.now()
    if current_time <= last_theme['end']:
        return Work.objects(theme=last_theme['theme']).order_by('-voices')
    else:
        return None

def getAllThemes():
    return CurrentTheme.objects.order_by('id')

def addRating(url, grammar, vocabulary, relevance, comment):
    work = Work.objects.get(url=url)
    for i in work.rating:
        if i['login'] == current_user.login:
            return False
    
    last_work = Work.objects.order_by('-id').get(login=current_user.login)
    current_theme = CurrentTheme.objects.order_by('-id').first()['theme']
    if last_work['theme'] == current_theme:
        last_work['voices'] += 1
        last_work.save()

    rating = Rating(login=current_user.login,name=current_user.name, grammar=grammar, vocabulary=vocabulary, relevance=relevance, comment=comment)
    work.rating.append(rating)
    work.save()
    return True
  