# API for essays
from flask import jsonify
from services import EssayService

from app import *


# Получить Сочинение по id
@app.route('/api/essay/<id>', methods=['GET'])
def getById(id):
    work = EssayService.getEssayById(id)
    return jsonify(work)

# Получить список Сочинений Участника за всё время
@app.route('/api/essay/by/<user_id>', methods=['GET'])
def getByUserId(user_id):
    return ''

# Загрузить Сочинение
@app.route('/api/essay/submit', methods=['POST'])
def saveEssay():
    
    return ''

# Получить Сочинение Участника активного Конкурса
@app.route('/api/essay/active', methods=['GET'])
def getCurrent(id):
    return ''

# Получить рейтинг работ за Конкурс
@app.route('/api/essay/raiting', methods=['GET'])
def getRaiting(id):
    return ''
