from django.contrib import admin
from .models import Lecture, Student

admin.site.register((Lecture, Student))
