FROM python:3.6.6-alpine

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install pipenv && \
 pipenv install --system --deploy && \
 apk --purge del .build-deps
