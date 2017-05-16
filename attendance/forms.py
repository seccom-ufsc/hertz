from django import forms


class RegisterAttendanceForm(forms.Form):
    student_id = forms.IntegerField()
