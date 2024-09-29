release: python manage.py migrate
web: gunicorn APPNAME.wsgi
worker: REMAP_SIGTERM=SIGQUIT celery -A APPNAME worker -c $WEB_CONCURRENCY -l INFO
beat: REMAP_SIGTERM=SIGQUIT celery -A APPNAME beat -l INFO
