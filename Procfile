web: gunicorn progress.asgi --log-file -

celery -A progress.celery worker --pool=threads -l info