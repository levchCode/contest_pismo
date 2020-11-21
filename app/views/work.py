from app import *

from dbCruder import getWork

def checkUserVoted(rating):
    vote = {
        'voted':False
    }
    for i in rating:
        if i['login'] == current_user.login:
            vote['voted'] = True
            vote['rating_grammar'] = i['grammar']
            vote['rating_vocabulary'] = i['vocabulary']
            vote['rating_relevance'] = i['relevance']
            vote['comment'] = i['comment']
            break
    return vote
    

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
    vote = checkUserVoted(work.rating)
    user = getUser(work['login'])
    return render_template('work.html', work=work, user=user, vote=vote)