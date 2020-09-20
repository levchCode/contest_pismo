from app import *


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
    