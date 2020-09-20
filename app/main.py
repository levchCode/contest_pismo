from secret import app_secret_key
from app import app
from views import index, participate, about, rules, contacts, support, profile, login, p404


if __name__ == "__main__":
	app.secret_key = app_secret_key
	app.run(debug=True)
