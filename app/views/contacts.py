from app import *


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    return render_template('contacts.html')
    