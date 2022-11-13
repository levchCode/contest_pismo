# API for essays
from flask import request, jsonify
from services import EssayService

from app import *


# Получить Сочинение по id
@app.route('/api/essay/<id>', methods=['GET'])
def getById(id):
    return jsonify(EssayService.getEssayById(id))

# Получить список Сочинений Участника за всё время
@app.route('/api/essay/by/<user_id>', methods=['GET'])
def getByUserId(user_id):
    return jsonify(EssayService.getEssayByUserId(user_id))

# Загрузить Сочинение
@app.route('/api/essay/submit', methods=['POST'])
def saveEssay():
    return EssayService.saveEssay()

# Оставить отзыв
@app.route('/api/essay/review/<id>', methods=['POST'])
def reviewEssay(id):
    return EssayService.addReview(_id=id, data=request.json)

# Получить Сочинение Участника активного Конкурса
@app.route('/api/essay/active/<user_id>', methods=['GET'])
def getCurrent(user_id):
    return jsonify(EssayService.getActiveEssay(user_id=user_id))

# Получить рейтинг работ за Конкурс
@app.route('/api/essay/raiting/<contest_id>', methods=['GET'])
def getRaiting(contest_id):
    return jsonify(EssayService.getRaiting(contest_id=contest_id))
