from app import *


@app.route('/rules', methods=['GET', 'POST'])
def rules():
    return render_template('rules.html')
    