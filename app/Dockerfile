FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY ./requirements.txt  /requirements.txt
RUN python -m pip install -r requirements.txt

RUN mkdir /app
COPY . /app
WORKDIR /app
