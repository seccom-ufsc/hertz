from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/?$', login, dict(template_name='login.html'), name='login'),

    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

    url(r'', include('attendance.urls')),
]
