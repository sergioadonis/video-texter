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


## Run postgres and redis locally
Install docker and docker-compose to run postgres as your local db and redis in order tu run async tasks.

Run:
```
docker-compose up -d
```

Check if postgres and redis are up:
```
docker-compose ps
``` 

If postgres is up you must migrate database:
```
pipenv run ./manage.py migrate
```

(optional) Install postgresql-client and connect to db:
``` 
psql --user django --host localhost
```
Hit \q in order to quit psql

(optional) Check redis installation
```
docker-compose exec redis redis-cli 
```
Hit QUIT in order to quit redis-cli

## Create a root super user
(optional) Create a root super user in oder to sign-in into the Admin Site:
``` 
pipenv run ./manage.py createsuperuser
```

## Run django dev server
Using django dev server to try locally:
```
pipenv run ./manage.py runserver
```
Open [http://localhost:8000/](http://localhost:8000/) on your browser.

## Run celery
Using celery to execute async tasks
```
pipenv run celery worker -A video_texter -l info
```
