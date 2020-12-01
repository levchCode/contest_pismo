from app import *


@app.route('/rating', methods=['GET', 'POST'])
def rating():
    works = getAllWorksByLastTheme()
    if works:
        return render_template('rating.html', works=works)
    else:
        return render_template('rating_empty.html')
    