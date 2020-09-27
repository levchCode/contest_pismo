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
            login = request.form['login']
            password = request.form['password']
            result = loginUser(login, password)

            if result:
                flash(f'Добро пожаловать, {login}', 'success')
                return redirect(url_for('profile', login = login))
            else:
                flash('Такого пользователя не существует', 'danger')
        
        elif request.form['type'] == 'signup':
            good_fields = True
            name = request.form['name']
            login = request.form['login']
            password = request.form['password']
            email = request.form['email']

            if len(login) < 4:
                flash('Длина логина должна быть больше 3ех символов', 'danger')
                good_fields = False

            if len(password) < 7:
                flash('Длина пароля должна быть больше 6ти символов', 'danger')
                good_fields = False
                
            if not re.search(email_regexp, email):
                flash('Укажите верный email адрес', 'danger')
                good_fields = False

            if good_fields:               
                result = addUser(name, login, email, password)
                print((result))
                if result:
                    flash(f'Добро пожаловать, {login}', 'success')
                    return redirect(url_for('profile', login = login))
                else:
                    flash('Логин или почта уже используются в системе', 'danger')

        return render_template('login.html')

    else:
        return render_template('login.html')
