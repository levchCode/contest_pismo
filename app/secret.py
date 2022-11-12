import os

app_secret_key = os.environ.get('app_secret_key', None)
DB_link = 'mongodb://mongodb:27017'
DB_name = 'pismo'