from app import *

from dbCruder import getUser

@app.route('/profile/<login>', methods = ['GET', 'POST'])
def profile(login):
    if request.method == "POST":
        if current_user.is_authenticated:
            if request.form['type'] == 'theme': 
                theme = request.form['theme']

                if len(theme) < 3 and len(theme) > 100:
                    flash(f'Нельзя предложить тему больше двух раз', 'danger')

                result = addTheme(current_user.login, theme)

                if result:
                    flash(f'Тема успешно предложена', 'success')
                else:
                    flash(f'Нельзя предложить тему больше двух раз', 'danger')

                return redirect(url_for('profile', login = login))


            # elif request.form['type'] == 'work':
            #     try:
            #         file = request.files['work']
            #         for i in file.stream:
            #             print(i.decode('ascii'))
            #     except:
            #         file = request.form['work']
            #         print(file)

        else:
            return redirect(url_for('login'))

    user = getUser(login)
    if getUser(login):
        return render_template('profile.html', user=user)
    else:
        return make_response(render_template('p404.html'), 404)
    