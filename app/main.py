from app import *
import os
from views import index, participate, about, rules, contacts, support, profile, login, logout, p404, work, rating


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host="0.0.0.0", port=port)
