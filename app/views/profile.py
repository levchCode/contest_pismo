from app import *


@app.route('/profile/<id>', methods = ['GET', 'POST'])
def profile(id):

    # -- TODO -- #
    # If user in DB: render page
    # Else render p404
    return render_template('profile.html')
    