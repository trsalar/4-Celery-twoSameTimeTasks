web: gunicorn progress.wsgi --log-file -


celery: celery -A progress.celery worker --pool=threads -l info
