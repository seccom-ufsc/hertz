import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hertz.settings")

import django

django.setup()

from django.contrib.auth.models import User

from attendance.models import Lecture, Student
from datetime import date, time, timedelta

User.objects.create_superuser('admin', '', 'adminadmin')

lectures = [
    {
        'title': 'Big data ou Big Brother',
        'lecturer': 'Castlevânia',
        'date': date(2016, 10, 5),
        'time': time(15, 10),
        'duration': timedelta(seconds=45 * 60),
    },
    {
        'title': 'Foca Robô',
        'lecturer': 'Professor 1',
        'date': date(2016, 10, 5),
        'time': time(16, 00),
        'duration': timedelta(seconds=60 * 60),
    },
    {
        'title': 'A Terra é Plana',
        'lecturer': 'Professor 2',
        'date': date(2016, 10, 6),
        'time': time(11, 00),
        'duration': timedelta(seconds=30 * 60),
    }
]


students = [
    {
        'name': 'Student 1'
    },
    {
        'name': 'Student 2'
    },
    {
        'name': 'Student 3'
    },

]

for lecture in lectures:
    Lecture(**lecture).save()

for student in students:
    Student(**student).save()
