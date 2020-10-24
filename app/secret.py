import os


app_secret_key = os.environ.get('app_secret_key', None)
DB_link = os.environ.get('DB_link', None)
DB_name = os.environ.get('DB_name', None)