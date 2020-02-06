from flask import Flask, json, render_template, request
import os

from db_functions import *

app = Flask(__name__, static_url_path='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60*60

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register")
def reg():
    return render_template('register.html')

@app.route("/login")
def log_in():
    return render_template('login.html')

@app.route("/top")
def top():
    top = get_submitions()
    return render_template('top.html', top=top)

@app.route("/submission")
def subm():
    _id = request.args.get('id')
    work, comments = get_sub(_id)
    return render_template('submission.html', work=work[0], comments=comments)

@app.route("/submit")
def sub():
    return render_template('success.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)