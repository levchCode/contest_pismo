from flask import Flask, redirect, url_for, session, request
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from authlib.integrations.flask_client import OAuth
from secret import *
#from services.UserService import *

# decorator for routes that should be accessible only by logged in users
from auth_token_decorator import token_required

app = Flask(__name__)

# Session config
app.secret_key = 'sxekrxetniy_klxuc'
#app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# oAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'email'},
)

app.config["MONGO_URI"] = "mongodb://root:root@mongodb:27017/pismo?authSource=admin"
app.config['MONGODB_SETTINGS'] = {
    'db': 'pismo',
    'host': 'mongodb://root:root@mongodb:27017/pismo?authSource=admin'
}

mongo = PyMongo(app)
db = MongoEngine(app)

@app.route('/api', methods=['GET'])
def hello():
    return '1 This is Pismo contest API! If you see this message, it means that the API is up and running'

@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

#этот эндпоинт не нужен, просто я через него получал токен для себя
@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/')

#@app.route('/users')
#@token_required
#def users(): 
#    users = getAllUsers()
#    return users

@app.route('/token_test')
@token_required
def notoken(userid):
    return 'token is fine'