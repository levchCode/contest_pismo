from app import *


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')
    