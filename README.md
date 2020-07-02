# video-texter

Web app to transcribe/translate youtube videos


## Install dependencies
This is a python project so you have to instal python3 and pipenv to isolate dependencies and environment stuff.

Run:
```
PIPENV_VENV_IN_PROJECT=1 pipenv install
```

Local .env:
```
cp .env-example .env
```


## Run db locally
Install docker and docker-compose to run postgres as your local db.

Run:
```
docker-compose up -d
```

Check if postgres (db process) is up:
```
docker-compose ps
``` 

Migrations:
```
pipenv run ./manage.py migrate
```

(optional) Create a root super user in oder to sign-in into the Admin Site:
``` 
pipenv run ./manage.py createsuperuser
```

(optional) Install postgresql-client and connect to db:
``` 
psql --user django --host localhost
```

## Run dev server
Using django dev server to try locally:
```
pipenv run ./manage.py runserver
```
Open [http://localhost:8000/](http://localhost:8000/) on your browser.
