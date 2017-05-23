from datetime import date

from django.forms import *

from .models import Lecture


class RegisterAttendanceForm(Form):
    student_id = IntegerField(label='Student ID')
    student_id.widget.attrs.update({
        'class': 'input is-primary',
        'placeholder': 'Student ID',
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
