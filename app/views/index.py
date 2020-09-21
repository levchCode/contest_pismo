from app import *


@login_manager.user_loader
def load_user(user):
    return User.get(user)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    