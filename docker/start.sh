#! /bin/bash

./manage.py makemigrations
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
# gunicorn -w 2 -b 0.0.0.0:8000 hertz.wsgi:application
