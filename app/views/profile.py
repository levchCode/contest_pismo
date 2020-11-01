from werkzeug.utils import secure_filename
from app import *
import os

from dbCruder import getUser


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/profile/<login>', methods = ['GET', 'POST'])
def profile(login):
    if request.method == "POST":
        if current_user.is_authenticated:
            if request.form['type'] == 'theme': 
                theme = request.form['theme']

                if len(theme) < 3 and len(theme) > 100:
                    flash(f'Тема должна быть от 3 до 100 символов', 'danger')

                result = addTheme(current_user.login, theme)

                if result:
                    flash(f'Тема успешно предложена', 'success')
                else:
                    flash(f'Тему можно предложить только один раз', 'danger')

                return redirect(url_for('profile', login = login))


            elif request.form['type'] == 'work':
                # try:
                file = request.files['work']
                if file.filename == '':
                    flash('No selected file')
                if file and allowed_file(file.filename):

                    work = ""
                    for i in file.stream:
                        work += i.decode('utf-8')
                    addWork(login, request.form['title'], work)

                # except:
                #     work = request.form['work']
                #     addWork(login, request.form['title'], work)
                
                return redirect(url_for('profile', login = login))

        else:
            return redirect(url_for('login'))

    user = getUser(login)
    if getUser(login):
        return render_template('profile.html', user = user)
    else:
        return make_response(render_template('p404.html'), 404)
    
