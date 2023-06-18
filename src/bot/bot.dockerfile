FROM python:3.11-slim

# Install curl and nc
# RUN apt-get update; apt-get install -y curl; apt-get install -y netcat

COPY ./requirements.txt /bot/

WORKDIR /bot

RUN pip install -r requirements.txt

COPY ./app /bot/app

ENTRYPOINT sleep 15;PYTHONPATH=/bot python ./app/run_bot.py