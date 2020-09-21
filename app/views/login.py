from app import *


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')
