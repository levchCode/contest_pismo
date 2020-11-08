from werkzeug.security import generate_password_hash, check_password_hash
from secret import DB_link, DB_name
from app import *
from objects.users import User
from objects.works import Work, Rating
from objects.themes import Theme
import uuid


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
            return {"name": user['name'], 
                    "login": user['login'], 
                    "email": user['email'], 
                    "password": user['password']}
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
                "works": [[work['url'], work['theme'], work['title'], work['status']] for work in works]}
    except:
        return False


def addTheme(login, theme):
    try:
        theme = Theme(login=login, theme=theme).save()
        return True
    except:
        return False

def addWork(login, name, title, work):
    try:
        url = str(uuid.uuid4())
        work = Work(url=url, login=login, name=name, title=title, work=work, status="На рассмотрении", rating=0).save()
        return True
    except:
        return False

def getWork(url):
    try:
        work = Work.objects.get(url=url)
        return {"login": work['login'],
                "name": work['name'],
                "theme": work['theme'],
                "title": work['title'],
                "work": work['work'],
                "status": work['status'],
                "rating": work['rating']}
    except:
        return False

def getWorks(login):
    return Work.objects(login=login)

def getWorks():
    return Work.objects()

def addRating(url, grammar, vocabulary, relevance):

    rating = Rating(login=current_user.login, grammar=grammar, vocabulary=vocabulary, relevance=relevance)
    work = Work.objects.get(url=url)
    work.rating.append(rating)
    work.save()
