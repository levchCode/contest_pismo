from app import *
from flask import request
from services import ContestService
# Получить Конкурс по id
@app.route('/api/contests/<id>', methods=['GET'])
def getContestById(id):
    return ''

# Получить актуальный Конкурс
@app.route('/api/contests/active', methods=['GET'])
def getActive():
    return ''

# Получить все Конкурсы
@app.route('/api/contests/', methods=['GET'])
def getContests():
    return ''

# Создать Конкурс
@app.route('/api/contests/create', methods=['POST'])
def saveContest():
    return ContestService.createContest(request.json)

# Редактировать Конкурс
@app.route('/api/contests/update/<id>', methods=['PATCH'])
def updateContest(id):
    return ''