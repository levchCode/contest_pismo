from app import *
from objects.users import User

def getAllUsers():
    users = User.objects.users.all()
    return users

def addUser(data):
    try:
        user = User(
            nickname = data['nickname'],
            role = ['role'],
            email = ['email']
        ).save()
    except Exception as e:
        return {
            'status': 0,
            'msg': str(e)
        }