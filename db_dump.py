import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hertz.settings')

import django
django.setup()

from attendance.models import Lecture, Student

backup_dir = os.path.abspath(sys.argv[1])

if os.path.exists(backup_dir):
    print('Directory already exists!')
    exit(1)

os.mkdir(backup_dir)

with open(os.path.join(backup_dir, 'lecture.csv'), 'w') as f:
    for lecture in Lecture.objects.all():
        entry = (f'"{lecture.id}","{lecture.title}","{lecture.lecturer}",'
                 f'"{lecture.date}","{lecture.time}","{lecture.duration}"')
        print(entry)
        f.write(entry + '\n')


with open(os.path.join(backup_dir, 'student.csv'), 'w') as f:
    for student in Student.objects.all():
        entry = (f'"{student.id}","{student.registration}","{student.name}"')
        print(entry)
        f.write(entry + '\n')

with open(os.path.join(backup_dir, 'attendance.csv'), 'w') as f:
    for lecture in Lecture.objects.all():
        for student in lecture.attendants.all():
            entry = f'"{lecture.id}","{student.registration}"'
            print(entry)
            f.write(entry + '\n')
