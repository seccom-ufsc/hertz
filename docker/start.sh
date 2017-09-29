#! /bin/bash

./manage.py makemigrations attendance
./manage.py migrate
gunicorn -w 4 -b 0.0.0.0:8000 hertz.wsgi:application
