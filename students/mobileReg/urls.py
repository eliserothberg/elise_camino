from django.conf.urls import url
from django.conf.urls import include
from django.views.decorators import csrf
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib import auth
from django.contrib import admindocs
from django.contrib.auth import views as auth_views
from students.forms import LoginForm
from students.forms import SMSVerification
from students.forms import addClassForm
from . import views
import django_twilio

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^message/$', views.message, name='message'),
    url(r'^foobar/$', views.message, name='message'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^classes/$', views.classes, name='classes'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}), 
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    # url(r'^ajax_send_pin/$', views.ajax_send_pin, name='ajax_send_pin'),

    # url(r'^foo/$',django_twilio.views.message, name='message'),
    
]