from app import *
from objects.essay import Essay;

def getEssayById(id):
    return Essay.objects.get(_id = id)

def saveEssay(data):
    #TODO: проверить пользователя
    work = Essay(login=login, name=name, theme=current_theme, title=title, work=work).save()