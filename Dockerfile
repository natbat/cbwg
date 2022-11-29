FROM python:3.6.15-slim-buster

RUN mkdir -p /app
WORKDIR /app

COPY . .

ENV PIPENV_VENV_IN_PROJECT=1

RUN pip install pipenv
RUN pipenv sync

RUN pipenv run ./manage.py collectstatic --noinput

EXPOSE 8000

CMD pipenv run gunicorn --bind 0.0.0.0:8000 --timeout 120 --workers 2 cbwg.wsgi
