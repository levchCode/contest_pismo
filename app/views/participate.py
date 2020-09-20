from app import *


@app.route('/participate', methods=['GET', 'POST'])
def participate():
    return render_template('participate.html')
    