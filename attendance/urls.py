from django.conf.urls import url
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^$', root, name='root'),

    url(r'lecture/(\d+)', lecture, name='lecture'),
]
