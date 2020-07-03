FROM python:3.8.3-slim

#RUN apt-get update && apt-get install pipenv -y

WORKDIR /app

#COPY ./Pipfile* ./
COPY requirements.txt .

#RUN pipenv install --system
RUN pip install -r requirements.txt

COPY . .
