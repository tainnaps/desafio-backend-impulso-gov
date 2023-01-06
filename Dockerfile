FROM python:3.11.1

WORKDIR /app

COPY ./dev-requirements.txt /app

COPY ./requirements.txt /app

RUN pip install -r dev-requirements.txt
