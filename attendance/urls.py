from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^$', LecturesList.as_view(), name='lecture_list'),

    url(r'^lecture/new/$', LectureCreate.as_view(), name='lecture_create'),

    url(r'^lecture/edit/(?P<pk>\d+)$', LectureUpdate.as_view(),
        name='lecture_edit'),


    url(r'^lecture/delete/(?P<pk>\d+)$', LectureDelete.as_view(),
        name='lecture_delete'),

    url(r'^lecture/(?P<pk>\d+)$', LectureDetailMux.as_view(),
        name='lecture_detail'),

    url(r'^student/(\d+)/remove/(\d+)$', remove_attendance,
        name='student_attendance_remove'),

    url(r'^student/(?P<registration>\d+)$', StudentDetail.as_view(),
        name='student_detail'),

    url(r'^student/$', StudentList.as_view(),
        name='student_list'),
]
