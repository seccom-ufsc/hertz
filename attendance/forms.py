from django import forms


class RegisterAttendanceForm(forms.Form):
    student_id = forms.IntegerField(label='Student ID')
    student_id.widget.attrs.update({
        'class': 'input is-primary',
        'placeholder': 'Student ID',
    })
