from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from flask import Flask, render_template, request, flash, redirect, url_for, make_response
from flask_mongoengine import MongoEngine, Document
from secret import *


UPLOAD_FOLDER = 'app/static/works'
ALLOWED_EXTENSIONS = {'txt', 'doc', 'docx'}

app = Flask(__name__)
app.secret_key = app_secret_key
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MONGODB_SETTINGS'] = {
    'db': DB_name,
    'host': DB_link
}

db = MongoEngine(app)
login_manager = LoginManager(app)

from dbCruder import *