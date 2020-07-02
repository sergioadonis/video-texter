FROM python:3.8.2

RUN apt-get update && apt-get install pipenv -y

WORKDIR /app

COPY ./Pipfile* ./

RUN pipenv install --system

COPY . .


