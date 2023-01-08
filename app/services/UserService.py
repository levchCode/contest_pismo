from app import *
from objects.users import User
import bcrypt
from uuid import uuid4

def get_hashed_password(plain_password):
    return bcrypt.hashpw(plain_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)

def getAllUsers():
    return User.objects.users.all()

def addUser(data):
    try:
        user = User(
            nickname = data['nickname'],
            role = data['role'],
            email = data['email'],
            hash = get_hashed_password(data['password']),
            level = data['level'],
            token = uuid4()
        )
        user.save()
        return {
            'status': 1,
            'msg': 'Успешная регистрация',
            'token': user.token
        }
    except Exception as e:
        return {
            'status': 0,
            'msg': str(e)
        }

def loginUser(data):
    try:
        user = User.objects.get(email = data.login)

        if check_password(data.password, user.hash):
            return {
                'status': 1,
                'token': uuid4()
            }
        else:
           return {
                'status': 0,
                'msg': 'Неверное имя пользователя или пароль'
            } 
    except Exception as e:
        return {
            'status': 0,
            'msg': str(e)
        }