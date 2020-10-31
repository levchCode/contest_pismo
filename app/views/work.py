from app import *

from dbCruder import getWork

@app.route('/work/<url>', methods=['GET', 'POST'])
def work(url):
    
    work = getWork(url)
    user = getUser(work['login'])
    return render_template('work.html', work=work, user=user)