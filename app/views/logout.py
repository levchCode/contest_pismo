from flask_login import login_required
from app import *

@app.route('/logout')
@login_required
def logout():
    flash(f'До скорых встреч, {current_user.login}', 'success')
    logout_user()
    return redirect(url_for('login'))