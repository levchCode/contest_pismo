from google.oauth2 import id_token
from google.auth.transport import requests
from functools import wraps
from flask import request, jsonify 
from secret import *

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'x-access-tokens' in request.headers:
           token = request.headers['x-access-tokens']
 
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
           testik = CLIENT_ID
           idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
           userid = idinfo['sub']
       except:
           return jsonify({'message': 'token is invalid'})
 
       return f(userid, *args, **kwargs)
   return decorator