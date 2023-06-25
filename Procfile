web: gunicorn progress.wsgi --log-file -
web: daphne progress.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker

celery: celery -A progress.celery worker --pool=threads -l info
