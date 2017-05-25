import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hertz.settings")

import django

django.setup()

from django.contrib.auth.models import User

from attendance.models import Lecture, Student
from datetime import date, time, timedelta

from faker import Factory

import random

try:
    User.objects.create_superuser('admin', '', 'adminadmin')
except Exception as e:
    print(e)

fake = Factory.create('pt_BR')


for _ in range(10):
    lecture = Lecture(
        title=fake.sentence(nb_words=6, variable_nb_words=True),
        lecturer=f'{fake.first_name()} {fake.last_name()}',
        date=fake.date_object(),
        time=fake.time_object(),
        duration=timedelta(seconds=60 * random.randint(30, 60)),
    )

    print(lecture)

    lecture.save()

for line in open('seccom2016-estudante.csv'):
    registration, name = line.strip().split(',')

    student = Student(
        registration=registration.zfill(8),
        name=name.strip('"'),
    )

    student.save()

    print(student)

