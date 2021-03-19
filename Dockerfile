FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev postgresql-client gettext

RUN apk add uwsgi

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --update bash && rm -rf /var/cache/apk/*

RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY requirements.txt /opt/app

RUN pip3 install -r requirements.txt

WORKDIR /opt/app/checker

# prod
#CMD gunicorn -b unix:/opt/app/tmp/gunicorn.sock project.wsgi:application

# for develop
CMD python3 manage.py runserver 0.0.0.0:8000