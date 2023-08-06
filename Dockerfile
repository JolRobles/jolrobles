# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

# Installing PostgreSQL development libraries
RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "jolrobles.wsgi:application", "--bind", "0.0.0.0:8000" ]