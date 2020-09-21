from flask import Flask, json, render_template, request, url_for, redirect, session
import os
import re
from db_functions import *

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60*60
app.secret_key = "S1h7D2jT0"
email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

@app.route("/", methods=["GET"])
def index():
    logged = False
    submitted = False
    work = []
    user_id = session.get('logged_user')
    if user_id != 0 and user_id != None:
        info = get_user(user_id)[1]
        submitted, work = check_if_submitted(user_id)
        logged = True
    else:
        info = ''

    current_state = check_date()
    
    return render_template('index.html', login_info=info, logged=logged, state=current_state, work=work, submitted=submitted)

@app.route("/takepart", methods=["GET"])
def takepart():
    logged = False

    if session.get('logged_user'):
        info = get_user(session.get('logged_user'))[1]
        logged = True
        state = check_date()[3]
        if state != 1:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('log_in'))

    tasks = get_tasks()

    return render_template('takepart.html', login_info=info, logged=logged, tasks=tasks)

@app.route("/register", methods=["GET", "POST"])
def reg():
    if request.method == "POST":
        if len(request.form['nickname']) > 3 and len(request.form['pwd']) > 6 and re.search(email_regex,request.form['email']):
            register(request.form['nickname'], request.form['pwd'], request.form['email'])
        else:
            return redirect(url_for('index'))
        return redirect(url_for('log_in'))
    else:
        return render_template('register.html')

@app.route("/login", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        if len(request.form['nickname']) > 0 and len(request.form['pwd']) > 0:
            user = request.form.get('nickname')
            pwd = request.form.get('pwd')
            _id = login(user, pwd)
            if _id != 0:
                session['logged_user'] = _id
                return redirect(url_for('index'))
            else:
                return render_template('login.html')
        else:
            return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route("/logout", methods=["GET"])
def log_out():
    session['logged_user'] = False
    return redirect(url_for('index'))

@app.route("/top", methods=["GET"])
def top():
    state = check_date()[3]
    if state == 1:
        return redirect(url_for('index'))
    top = get_submitions()
    return render_template('top.html', top=top)

@app.route("/submission", methods=["GET"])
def subm():
    user_id = session.get('logged_user')
    if user_id != 0:
        _id = request.args.get('id')
        work, comments, enable_form = get_sub(_id, user_id)
        return render_template('submission.html', work=work[0], comments=comments, enable=enable_form)
    else:
        return redirect(url_for('log_in'))

@app.route("/submit", methods=["GET", "POST"])
def sub():
    state = check_date()[3]
    if state != 1:
        return redirect(url_for("index"))
    else:
        user_id = session.get('logged_user')
        if user_id:
            if request.method == "POST":
                task_id = request.form.get('task_id')
                answer = request.form.get('answer')
                done = request.form.get('notdone')
                s_id = submit(user_id, task_id, answer, done)
                return redirect(url_for('subm') + "?id=" + str(s_id))
            else:
                t_id = request.args.get('task_id')
                task = get_task(t_id)
                user = get_user(session.get('logged_user'))[1]
                return render_template('submit.html', task=task, user=user)
        else:
            return redirect(url_for('log_in'))

@app.route("/comment", methods=["POST"])
def leave_comment():
    state = check_date()[3]
    if state != 2:
        return redirect(url_for("index"))
    else:
        user_id = session.get('logged_user')
        if user_id:
            sub_id = request.form.get('sub_id')
            g_s = request.form.get('grammar')
            v_s = request.form.get('vocab')
            tr_s = request.form.get('topic')
            text = request.form.get('comment')
            comment(sub_id, user_id, g_s, v_s, tr_s, text)
            return redirect(url_for('subm') + "?id=" + sub_id)
        else:
            return redirect(url_for('log_in'))

@app.route("/rules", methods=["GET"])
def rules():
    return render_template('rules.html')

@app.route("/results", methods=["GET"])
def r():
    state = check_date()[3]
    if state == 3:
        r_1, r_2, r_3 = get_results()
        return render_template('results.html', nom_1=r_1, nom_2=r_2, nom_3=r_3)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)