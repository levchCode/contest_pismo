from app import *
from flask import request, jsonify
from services import ContestService

# Получить Конкурс по id
@app.route('/api/contests/<id>', methods=['GET'])
def getContestById(id):
    return jsonify(ContestService.getContestById(_id=id))

# Получить актуальный Конкурс
@app.route('/api/contests/last', methods=['GET'])
def getActive():
    return jsonify(ContestService.getContests(last = 1))

# Получить все Конкурсы
@app.route('/api/contests/', methods=['GET'])
def getContests():
    return jsonify(ContestService.getContests(active=None))

# Создать Конкурс
@app.route('/api/contests/create', methods=['POST'])
def saveContest():
    return ContestService.createContest(request.json)

# Редактировать Конкурс
@app.route('/api/contests/update/<id>', methods=['PATCH'])
def updateContest(id):
    return jsonify(ContestService.updateContest(_id=id, data=request.json))