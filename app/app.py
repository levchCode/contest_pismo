from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
import os


app = Flask(__name__)
login_manager = LoginManager(app)