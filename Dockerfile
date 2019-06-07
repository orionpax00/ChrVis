FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /chrvis

WORKDIR /chrvis

ADD . /chrvis/

RUN pip install -r requirements.txt
