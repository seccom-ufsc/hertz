from datetime import date

from django.forms import *

from .models import Lecture, Student


def validate_student_exists(registration):
        try:
            student = Student.objects.get(registration=registration)
        except Student.DoesNotExist:
            raise ValidationError(
                'There is no student with this ID',
            )


class RegisterAttendanceForm(Form):
    student_registration = CharField(
        max_length=8, min_length=8,
        label='Registration', validators=[validate_student_exists])

    student_registration.widget.attrs.update({
        'class': 'input is-primary',
        'placeholder': 'Registration',
        # 'size':5, 'maxlength':5
    })


_lecture_attrs = {
    'class': 'input is-primary',
}


class LectureForm(ModelForm):

    class Meta:
        model = Lecture
        fields = ['title', 'lecturer', 'date', 'time', 'duration']

        widgets = {
            'title': TextInput(attrs={
                'class': 'input is-primary',
                'placeholder': 'Title',
            }),


            'lecturer': TextInput(attrs={
                'class': 'input is-primary',
                'placeholder': 'Lecturer',
            }),

            'date': DateInput(attrs={
                'class': 'input is-primary',
                'placeholder': 'Date (mm/dd/yyyy)',
                'type': 'date',
            }),

            'time': TimeInput(attrs={
                'class': 'input is-primary',
                'placeholder': 'Time (hh:dd)',
                'type': 'time',
            }),

            'duration': TextInput(attrs={
                'class': 'input is-primary',
                'placeholder': 'Duration (mm:ss)',
            }),
        }
