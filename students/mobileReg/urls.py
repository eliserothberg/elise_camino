from django.conf.urls import include, url
from django.views.decorators import csrf
from django.contrib import admin
from django.contrib import auth
# from django.contrib.auth import views as auth_views
from students.forms import CustomUserChangeForm, CustomUserCreationForm
# from students import views as student_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'^invalid_login/$', views.invalid_login, name='invalid_login'),
    url(r'^classes/$', views.classes, name='classes'),
    url(r'^message/$', views.message, name='message'),
    url(r'^classes/message/$', views.message, name='message'),

    url(r'^accounts/registration_complete/$', views.registration_complete, name='registration_complete'),
    # url(r'^login/$', student_views.login, name='login'), 
    url(r'^loggedin/$', views.login, name='loggedin'),
    url(r'^classes/your_class/$', views.your_class, name='your_class'),
    url(r'^logout/$', views.logout,  {'next_page': '/index'}),
  ]