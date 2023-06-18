FROM python:3.11-slim

# Install curl and nc
# RUN apt-get update; apt-get install -y curl; apt-get install -y netcat

COPY ./requirements.txt /web/

WORKDIR /web

RUN pip install -r requirements.txt

COPY . /web
