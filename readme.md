### Steps to install: ###
- Create `./app/secret.py`, that must contain `app_secret_key="test"`
- Run in CMD/Terminal `pip install virtualenv`
- Create virtualenv with:
	- Windows -> `virtualenv venv --python=python`
	- Linux ->`virtualenv venv --python=python3`
- Activate virtualenv: 
	- Windows:
		1) `cd .\venv\Scripts\` 
		2) ` .\activate`
		
		If you see exception:
		1) Run as administrator PowerShell
		2) Run `Set-ExecutionPolicy RemoteSigned`
		3) Type `A`
		4) Try again

	- Linux:
		1) `source env/bin/activate`
- Run `pip install -r requirements.txt`
- Run:
	- Windows -> `python app/main.py`
	- Linux ->`python3 app/main.py`
------------

### Run with Docker: ###

- Install Docker
- Run `docker build -t server . -f server.dockerfile`
- Run `docker run -d -p 5000:5000 server `
------------
### Run with Docker-compose: ###
- Install Docker
- Run `docker-compose up`
- Open `http://localhost:5000/`
------------