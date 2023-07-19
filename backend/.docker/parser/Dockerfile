FROM python:latest
RUN apt-get update
RUN apt-get -y install locales-all

ENV LANG ja_JP.UTF-8

RUN apt -y update
RUN apt install -y default-mysql-client-core

RUN pip install mutagen numpy pandas

WORKDIR /workspace/src/parser




