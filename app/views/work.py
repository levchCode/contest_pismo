from app import *

from dbCruder import getWork

@app.route('/work/<url>', methods=['GET', 'POST'])
def work(url):

    if request.method == "POST":
        if current_user.is_authenticated:
            if request.form['type'] == 'rating':
                grammar = request.form['grammar']
                vocabulary = request.form['vocabulary']
                relevance = request.form['relevance']

                rating = addRating(url, grammar, vocabulary, relevance)

    work = getWork(url)
    user = getUser(work['login'])
    return render_template('work.html', work=work, user=user)