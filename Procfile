release: DJANGO_SETTINGS_MODULE="cbwg.settings.production" python manage.py migrate
web: DJANGO_SETTINGS_MODULE="cbwg.settings.production" gunicorn cbwg.wsgi --log-file -
