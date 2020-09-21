from app import *


@app.route('/support', methods=['GET', 'POST'])
def support():
    return render_template('support.html')
    