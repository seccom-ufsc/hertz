from django.db import models


class Student(models.Model):
    registration = models.CharField(max_length=8, unique=True, db_index=True)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        cls = self.__class__.__name__
        return f'<{cls}: registration={self.registration}, name={self.name}>'


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
        cls = self.__class__.__name__
        return f'<{cls}: id={self.id}, title={self.title}>'
