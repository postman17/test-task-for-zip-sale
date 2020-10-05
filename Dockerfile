FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev postgresql-client gettext

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --update bash && rm -rf /var/cache/apk/*

RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY requirements.txt /opt/app
# COPY deploy.sh /opt/app
RUN pip3 install -r requirements.txt


CMD python3 ./project/manage.py runserver 0.0.0.0:8000