FROM python:3.7.5
MAINTAINER wowzoo <wowzoo@gmail.com>

RUN mkdir -p resource-server
WORKDIR resource-server

COPY ./requirements ./requirements
RUN pip install -r requirements/prod.txt

COPY ./api ./api
COPY ./unicorns ./unicorns
COPY ./recipes ./recipes
COPY ./manage.py ./manage.py
COPY ./entrypoint.sh ./entrypoint.sh

EXPOSE 8088

ENTRYPOINT ["/resource-server/entrypoint.sh"]
