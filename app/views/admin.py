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
            theme = request.form['theme']
            start = datetime.strptime(request.form['start'], '%Y-%m-%dT%H:%M')
            end = datetime.strptime(request.form['end'], '%Y-%m-%dT%H:%M')

            addCurrentTheme(theme, start, end)
        return render_template('admin.html', themes=getAllThemes()) 
    