from app import *
from views import index, participate, about, rules, contacts, support, profile, login, logout, p404


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, port=port)
