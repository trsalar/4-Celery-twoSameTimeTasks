web: gunicorn progress.wsgi --log-file -

celery -A progress.celery worker --pool=threads -l info