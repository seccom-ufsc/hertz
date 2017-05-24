from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ValidationError
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from .forms import LectureForm, RegisterAttendanceForm
from .models import Lecture, Student


class LecturesList(ListView):
    model = Lecture
    queryset = Lecture.objects.all()


class LectureDetail(LoginRequiredMixin, DetailView):
    model = Lecture
    slug_field = 'pk'
    context_object_name = 'lecture'
    template_name = 'attendance/lecture.html'

    def get_context_data(self, **kwargs):
        context = {
            'students': self.object.attendants.all(),
            'form': RegisterAttendanceForm(),
        }

        return super().get_context_data(**context)


class RegisterAttendance(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Lecture
    form_class = RegisterAttendanceForm
    template_name = 'attendance/lecture.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        print(f'printei: {self.object}')

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('lecture_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        student_id = form.cleaned_data['student_id']

        student = get_object_or_404(Student, pk=student_id)

        self.object.attendants.add(student)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            students=self.object.attendants.all())


class LectureDetailMux(View):
    def get(self, request, *args, **kwargs):
        view = LectureDetail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = RegisterAttendance.as_view()
        return view(request, *args, **kwargs)


class LectureCreate(LoginRequiredMixin, CreateView):
    model = Lecture
    form_class = LectureForm
    success_url = reverse_lazy('lecture_list')


class LectureUpdate(LoginRequiredMixin, UpdateView):
    model = Lecture
    form_class = LectureForm
    slug_field = 'pk'
    success_url = reverse_lazy('lecture_list')


class LectureDelete(LoginRequiredMixin, DeleteView):
    model = Lecture
    slug_field = 'pk'
    success_url = reverse_lazy('lecture_list')


class StudentDetail(LoginRequiredMixin, DetailView):
    model = Student
    slug_field = 'pk'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = {
            'lectures': self.object.lectures.all(),
        }

        return super().get_context_data(**context)


class StudentList(ListView):
    model = Student
    queryset = Student.objects.all()


@login_required
def remove_attendance(request, student_pk, lecture_pk):
    student = get_object_or_404(Student, pk=int(student_pk))
    lecture = get_object_or_404(Lecture, pk=int(lecture_pk))

    lecture.attendants.remove(student)

    return redirect('student_detail', student.id)

