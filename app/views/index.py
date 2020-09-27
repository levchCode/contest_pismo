from app import *


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    