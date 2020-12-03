from app import *

from dbCruder import *
    

@app.route('/work/<url>', methods=['GET', 'POST'])
def work(url):

    if request.method == "POST":
        if current_user.is_authenticated:
            if request.form['type'] == 'rating':
                try:
                    grammar = request.form['grammar']
                    vocabulary = request.form['vocabulary']
                    relevance = request.form['relevance']
                    comment = request.form['comment']
                    rating = addRating(url, grammar, vocabulary, relevance, comment)
                    if rating:
                        flash('Работа оценена', 'success')
                    else:
                        flash('Вы уже оценили работу', 'danger')
                except:
                    flash('Поставьте оценку за все критерии', 'danger')

    work = getWork(url)
    return(render_template('work.html', work=work))