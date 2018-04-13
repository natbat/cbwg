release: python manage.py migrate
web: DJANGO_SETTINGS_MODULE="cbwg.settings.dev" gunicorn cbwg.wsgi --log-file -
