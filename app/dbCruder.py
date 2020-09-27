from werkzeug.security import generate_password_hash, check_password_hash
from secret import DB_link, DB_name
from app import *
from objects.users import User


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
        user = User.objects.get(login=login, password=password)
        return {"name": user['name'], 
                "login": user['login'], 
                "email": user['email'], 
                "password": user['password']}
    except:
        return False
