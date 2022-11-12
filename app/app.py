from flask import Flask
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from secret import *

app = Flask(__name__)
app.secret_key = app_secret_key

app.config["MONGO_URI"] = "mongodb://levch:ubuntu@mongodb:27017/pismo"
app.config['MONGODB_SETTINGS'] = {
    'db': 'pismo',
    'host': 'mongodb://levch:ubuntu@mongodb:27017'
}

mongo = PyMongo(app)
db = MongoEngine(app)

@app.route('/api', methods=['GET'])
def hello():
    return 'This is Pismo contest API! If you see this message, it means that the API is up and running'