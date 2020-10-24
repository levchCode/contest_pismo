from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mongoengine import MongoEngine, Document
import secret



app = Flask(__name__)
app.secret_key = secret.app_secret_key
app.config['MONGODB_SETTINGS'] = {
    'db': secret.DB_name,
    'host': secret.DB_link
}

db = MongoEngine(app)
login_manager = LoginManager(app)

from dbCruder import *