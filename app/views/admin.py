from app import *
from dbCruder import *
from datetime import datetime


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    elif current_user.role =='User':
        return redirect(url_for('profile', login = current_user.login))

    elif current_user.role =='Admin':
        if request.method == "POST" and current_user.is_authenticated:
            stage_1 = datetime.strptime(request.form['stage_1'], '%Y-%m-%dT%H:%M')
            stage_2 = datetime.strptime(request.form['stage_2'], '%Y-%m-%dT%H:%M')
            stage_3 = datetime.strptime(request.form['stage_3'], '%Y-%m-%dT%H:%M')
            stage_4 = datetime.strptime(request.form['stage_4'], '%Y-%m-%dT%H:%M')

            addCurrentTheme(stage_1, stage_2, stage_3, stage_4)
        return render_template('admin.html', themes=getAllCurrentThemes()) 
    