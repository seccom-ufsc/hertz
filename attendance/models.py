from django.db import models


class Student(models.Model):
    registration = models.CharField(max_length=8, unique=True, db_index=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '<{}: registration={}, name={}>'.format(
            self.__class__.__name__, self.registration, self.name)


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    lecturer = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()

    attendants = models.ManyToManyField(
        Student, related_name='lectures', blank=True)

    class Meta:
        ordering = ('date', 'time')

    def __str__(self):
        return '<{}: id={}, title={}>'.format(
            self.__class__.__name__, self.id, self.title)
