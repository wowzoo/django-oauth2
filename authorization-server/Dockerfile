FROM python:3.7.5
MAINTAINER wowzoo <wowzoo@gmail.com>

RUN mkdir -p authorization-server
WORKDIR authorization-server

COPY ./requirements ./requirements
RUN pip install -r requirements/prod.txt

COPY ./authorization ./authorization
COPY ./core ./core
COPY ./manage.py ./manage.py
COPY ./entrypoint.sh ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/authorization-server/entrypoint.sh"]

