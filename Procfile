release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn digital_retail.wsgi --preload --log-file -