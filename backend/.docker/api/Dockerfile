FROM golang:latest

RUN apt-get update
RUN apt-get -y install locales-all

ENV LANG ja_JP.UTF-8

RUN apt -y update
RUN apt install -y default-mysql-client-core

WORKDIR /workspace/src
RUN go mod init audio-api
RUN go get -u github.com/gin-gonic/gin

