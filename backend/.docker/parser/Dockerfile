FROM python:3.7.17
RUN apt-get update
RUN apt-get -y install locales-all

ENV LANG ja_JP.UTF-8

RUN apt -y update
RUN apt install -y default-mysql-client-core build-essential
RUN pip install mutagen numpy pandas "pysen[lint]"

WORKDIR /workspace/src/parser




