FROM python:3.8.3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r --no-cache-dir requirements.txt

COPY . .
