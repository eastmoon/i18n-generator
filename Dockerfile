FROM python:slim

COPY requirements.txt requirements.txt

RUN \
    apt-get update -y && \
    apt-get install -y \
        curl \
        git

RUN \
    pip install -r requirements.txt

WORKDIR /app
