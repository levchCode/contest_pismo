from app import *


@app.route('/rating', methods=['GET', 'POST'])
def rating():
    works = getAllWorks()
    return render_template('rating.html', works=works)
    