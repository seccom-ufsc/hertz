from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Lecture, Student


def root(request):
    lectures = Lecture.objects.all()

    return render(request, 'attendance/root.html', {'lectures': lectures})


@login_required
def lecture(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)

    students = lecture.attendants.all()

    context = {
        'lecture': lecture,
        'students': students,
    }

    return render(request, 'attendance/lecture.html', context)
