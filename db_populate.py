import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hertz.settings')

import django
django.setup()

from django.contrib.auth.models import User

from attendance.models import Lecture, Student

try:
    User.objects.create_superuser(
        os.environ['HERTZ_ADMIN_LOGIN'], '', os.environ['HERTZ_ADMIN_PASSWORD'],
    )
except Exception as e:
    print(e)

if len(sys.argv) < 2:
    print('Must tell which file to import!')
    exit(1)


for line in open(sys.argv[1]):
    name, registration = line.strip().split(',')

    student = Student(
        registration=registration.strip().zfill(8),
        name=name.strip().strip('"'),
    )

    student.save()

    print(student)
