FROM python:3.7.5
LABEL author="wowzoo <wowzoo@gmail.com>"

RUN mkdir -p application-server
WORKDIR application-server

COPY ./requirements ./requirements
RUN pip install -r requirements/prod.txt

COPY ./proxy ./proxy
COPY ./users ./users
COPY ./manage.py ./manage.py
COPY ./entrypoint.sh ./entrypoint.sh

ENTRYPOINT ["/application-server/entrypoint.sh"]
