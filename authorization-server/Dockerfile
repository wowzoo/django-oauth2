FROM python:3.7.5
LABEL author="wowzoo <wowzoo@gmail.com>"

RUN mkdir -p authorization-server
WORKDIR authorization-server

COPY ./requirements ./requirements
RUN pip install -r requirements/prod.txt

COPY ./auth ./auth
COPY ./users ./users
COPY ./manage.py ./manage.py
COPY ./entrypoint.sh ./entrypoint.sh

ENTRYPOINT ["/authorization-server/entrypoint.sh"]
