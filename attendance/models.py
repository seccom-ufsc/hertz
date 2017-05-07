from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '<{}: id={}, name={}>'.format(
            self.__class__.__name__, self.id, self.name)


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    lecturer = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()

    attendant = models.ManyToManyField(
        Student, related_name='lectures', blank=True)

    def __str__(self):
        return '<{}: id={}, title={}>'.format(
            self.__class__.__name__, self.id, self.title)
