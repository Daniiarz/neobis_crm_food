FROM python:3.7-alpine
MAINTAINER daniiarz

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /src
RUN mkdir /src/app
# Setting working directory, so we can easily execute commands like manage.py
WORKDIR /src/
COPY ./app /src/app
RUN mkdir /src/requirements
COPY ./requirements /src/requirements
COPY Pipfile Pipfile.lock /src/

RUN apk add --update --no-cache python3 python3-dev postgresql-client postgresql-dev build-base gettext
RUN pip install --upgrade pip
RUN pip install pipenv

RUN pip install -r requirements/production.txt

RUN adduser -D user
USER user

