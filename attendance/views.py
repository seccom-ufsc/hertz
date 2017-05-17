from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from django.urls import reverse

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
            'students': self.object.attendants.all(),
            'form': RegisterAttendanceForm(),
        }

        return super().get_context_data(**context)


class RegisterAttendance(SingleObjectMixin, FormView):
    template_name = 'attendance/lecture.html'
    form_class = RegisterAttendanceForm
    model = Lecture

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('lecture', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        student_id = form.cleaned_data['student_id']

        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return redirect('lecture', self.object.id)

        self.object.attendants.add(student)

        return super().form_valid(form)


class LectureDetail(View):
    def get(self, request, *args, **kwargs):
        view = LectureDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = RegisterAttendance.as_view()
        return view(request, *args, **kwargs)
