from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mongoengine import MongoEngine, Document
from secret import *



app = Flask(__name__)
app.secret_key = app_secret_key
app.config['MONGODB_SETTINGS'] = {
    'db': DB_name,
    'host': DB_link
}

db = MongoEngine(app)
login_manager = LoginManager(app)

from dbCruder import *