release: python manage.py migrate
web: gunicorn progress.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=progress.settings -v2

celery: celery -A progress.celery worker --pool=threads -l info
