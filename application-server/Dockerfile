FROM python:3.7.5
MAINTAINER wowzoo <wowzoo@gmail.com>

RUN mkdir -p application-server
WORKDIR application-server

COPY ./requirements ./requirements
RUN pip install -r requirements/prod.txt

COPY ./authentication ./authentication
COPY ./users ./users
COPY ./manage.py ./manage.py
COPY ./entrypoint.sh ./entrypoint.sh

EXPOSE 8087

ENTRYPOINT ["/application-server/entrypoint.sh"]
