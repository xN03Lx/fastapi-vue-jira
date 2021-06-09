FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./app /app

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

