from flask import Flask, json, render_template, request, url_for, redirect, session
import os
from db_functions import *

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60*60
app.secret_key = "S1h7D2jT0"

@app.route("/")
def index():
    logged = False
    if session.get('logged_user'):
        info = get_user(session.get('logged_user'))[1]
        logged = True
    else:
        info = ''

    current_state = check_date()

    return render_template('index.html', login_info=info, logged=logged, state=current_state)

@app.route("/takepart")
def takepart():
    logged = False
    if session.get('logged_user'):
        info = get_user(session.get('logged_user'))[1]
        logged = True
    else:
        info = ''

    tasks = get_tasks()

    return render_template('takepart.html', login_info=info, logged=logged, tasks=tasks)

@app.route("/register", methods=["GET", "POST"])
def reg():
    if request.method == "POST":
        register(request.form['nickname'], request.form['pwd'], request.form['email'])
        return redirect(url_for('log_in'))
    else:
        return render_template('register.html')

@app.route("/login", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        user = request.form.get('nickname')
        pwd = request.form.get('pwd')
        _id = login(user, pwd)
        if _id != 0:
            session['logged_user'] = _id
            return redirect(url_for('index'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route("/logout", methods=["GET"])
def log_out():
    session['logged_user'] = False
    return redirect(url_for('index'))

@app.route("/top")
def top():
    top = get_submitions()
    return render_template('top.html', top=top)

@app.route("/submission")
def subm():
    if session.get('logged_user'):
        _id = request.args.get('id')
        user_id = session.get('logged_user')
        work, comments, disable_form = get_sub(_id, user_id)
        return render_template('submission.html', work=work[0], comments=comments, disable=disable_form)
    else:
        return redirect(url_for('log_in'))

@app.route("/submit", methods=["GET", "POST"])
def sub():
    if request.method == "POST":
        if session.get('logged_user'):
            task_id = request.form.get('task_id')
            answer = request.form.get('answer')
            user_id = session.get('logged_user')
            done = not request.form.get('done')
            s_id = submit(user_id, task_id, answer, done)
            return redirect(url_for('subm') + "?id=" + str(s_id))
        else:
            return redirect(url_for('log_in'))
    else:
        if session.get('logged_user'):
            t_id = request.args.get('task_id')
            task = get_task(t_id)
            user = get_user(session.get('logged_user'))[1]

            return render_template('submit.html', task=task, user=user)
        else:
            return redirect(url_for('log_in'))

@app.route("/comment", methods=["POST"])
def leave_comment():
    sub_id = request.form.get('sub_id')
    user_id = session.get('logged_user')
    g_s = request.form.get('grammar')
    v_s = request.form.get('vocab')
    tr_s = request.form.get('topic')
    text = request.form.get('comment')
    comment(sub_id, user_id, g_s, v_s, tr_s, text)
    return redirect(url_for('subm') + "?id=" + sub_id)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)