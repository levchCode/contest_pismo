from app import *


@app.route('/profile/<login>', methods = ['GET', 'POST'])
def profile(login):

    # -- TODO -- #
    # If user in DB: render page
    # Else render p404
    return render_template('profile.html')
    