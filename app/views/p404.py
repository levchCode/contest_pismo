from app import *


@app.errorhandler(404)
def p404(e):
    return render_template('p404.html')
