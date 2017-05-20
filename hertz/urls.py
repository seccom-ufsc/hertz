from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/?$', auth_views.login, dict(template_name='login.html'),
        name='login'),

    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'', include('attendance.urls')),
]
