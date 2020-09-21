from app import *


@app.errorhandler(404)
def page_not_found(e):
    return render_template('p404.html')
