### Steps to install: ###
- Create `./app/secret.py`, that must contain 
```
app_secret_key="test"
DB_link = "Atlas URL"
DB_name = "test"
```
LETS USE PIPENV

- Run in CMD/Terminal `pip install pipenv`
- pipenv shell
- pipenv install ()


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
- Open `http://localhost:5000/`
------------

### Run with Docker-compose: ###
- Install Docker
- Run `docker-compose up --build`
- NOTE --build flag may be removed if there is no need to rebuild container
- Open `http://localhost:5000/`
------------

### Run only DB container

`docker-compose up -d mongo`

To run all in containers - change .env file connection string to:
`mongodb://mongo:27017`

`server = "gunicorn -b=0.0.0.0:8443 -w=4 bot.app:app"`