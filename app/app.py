from flask import Flask
from flask_pymongo import PyMongo
from secret import *

app = Flask(__name__)
app.secret_key = app_secret_key

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/pismo"
mongo = PyMongo(app)

@app.route('/api', methods=['GET'])
def hello():
    return 'This is Pismo contest API! If you see this message, it means that the API is up and running'