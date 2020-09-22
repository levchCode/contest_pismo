from secret import DB_link, DB_name
from app import *
from objects.users import User


def addUser(name, login, email, password):
    user = User(name=name, login=login, email=email, password=password).save()
    login_user(user, remember=True)

def loginUser(login, password):
    user = User.objects.get(login=login, password=password)
    if user:

        login_user(user, remember=True)
        return {"name": user['name'], 
                "login": user['login'], 
                "email": user['email'], 
                "password": user['password']}
    else:
        return False

def updateUser(name, login, email, password):
    user = User.objects.get(login=login).update_one(name=name, login=login, email=email, password=password)
    return bool(user)

def getUser(login):
    user = User.objects.get(login=login, password=password)
    if user:
        return {"name": user['name'], 
                "login": user['login'], 
                "email": user['email'], 
                "password": user['password']}
    else:
        return False
