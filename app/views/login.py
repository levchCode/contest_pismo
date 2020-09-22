from app import *

from dbCruder import loginUser, addUser
from constants import email_regexp
import re

@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('profile', login = current_user.login))

    if request.method == "POST":

        # Sign in logic
        if request.form['type'] == 'signin':
            result = loginUser(request.form['login'], request.form['password'])

            if result:
                flash('Success', 'success')
                return redirect(url_for('profile', login = request.form['login']))
            else:
                flash('Error', 'danger')
                return redirect(url_for('login'))
        
        elif request.form['type'] == 'signup':
            good_fields = True
            if len(request.form['login']) < 4:
                flash('Длина логина должна быть больше 3ех символов', 'danger')
                good_fields = False

            if len(request.form['password']) < 7:
                flash('Длина пароля должна быть больше 6ти символов', 'danger')
                good_fields = False
                
            if not re.search(email_regexp, request.form['email']):
                flash('Укажите верный email адрес', 'danger')
                good_fields = False

            if good_fields:               
                addUser(request.form['name'], request.form['login'], request.form['email'], request.form['password'])
                return redirect(url_for('profile', login = request.form['login']))
            else:
                return redirect(url_for('login'))
    else:
        return render_template('login.html')
