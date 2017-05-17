from django.conf.urls import url
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^$', LecturesListView.as_view(), name='root'),

    url(r'lecture/(?P<pk>\d+)', LectureDetail.as_view(), name='lecture'),
]
