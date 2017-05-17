from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import RegisterAttendanceForm
from .models import Lecture, Student


class LecturesListView(ListView):
    model = Lecture
    queryset = Lecture.objects.all()
    template_name = 'attendance/root.html'


class LectureDetailView(DetailView):
    model = Lecture
    slug_field = 'pk'
    context_object_name = 'lecture'
    template_name = 'attendance/lecture.html'

    def get_context_data(self, **kwargs):
        context = {
            'students': self.object.attendants.all()
        }

        return super().get_context_data(**context)

# class RegisterAttendanceView(FormView):
#     pass

# @login_required
# def lecture(request, lecture_id):
#     lecture = get_object_or_404(Lecture, pk=lecture_id)

#     print(request.POST)

#     if request.method == 'POST':
#         form = RegisterAttendanceForm(request.POST)

#         if form.is_valid():
#             student_id = form.cleaned_data.get('student_id')

#             # try:
#             #     student = Student.objects.get(pk=int(student_id))
#             # except ValueError:

#             try:
#                 student = Student.objects.get(pk=student_id)
#             except Student.DoesNotExist:
#                 form.add_error(
#                     'student_id',
#                     ValidationError(
#                         'Student not found',
#                         code='student_not_found',
#                     )
#                 )

#             # return redirect('lecture', lecture_id)

    # else:
    #     form = RegisterAttendanceForm()

    #     students = lecture.attendants.all()

    #     context = {
    #         'lecture': lecture,
    #         'students': students,
    #         'form': form,
    #     }

    #     return render(request, 'attendance/lecture.html', context)
