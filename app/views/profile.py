from werkzeug.utils import secure_filename
from app import *
import docx2txt
import os

from dbCruder import *


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
                file = request.files['work']
                if file.filename == '':
                    flash('Не выбран файл', 'danger')
                if file and allowed_file(file.filename):
                    
                    extension = file.filename.split('.')[1]
                    if extension == 'txt':
                        work = ""
                        for i in file.stream:
                            work += i.decode('utf-8')

                    elif extension == 'docx':
                        work = docx2txt.process(file)
                        
                    else:
                        flash('Файл должен иметь расширение .txt или .docx', 'danger')
                        return redirect(url_for('profile', login = login))

                    if len(work) > 1000:
                        flash('В предложенной работе более 1000 символов', 'danger')
                        return redirect(url_for('profile', login = login))
                    else:
                        if addWork(login, current_user.name, request.form['title'], work):
                            flash('Работа успешна загружена', 'success')
                        else:
                            flash(f'Нельзя загрузить более двух работ', 'danger')                
                return redirect(url_for('profile', login = login))

        else:
            return redirect(url_for('login'))

    user = getUser(login)
    stage = getCurrentStage()
    if getUser(login):
        return render_template('profile.html', user = user, stage = stage, theme = getCurrentTheme())
    else:
        return make_response(render_template('p404.html'), 404)
    
