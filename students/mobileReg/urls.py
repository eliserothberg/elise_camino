from django.conf.urls import include, url
from django.views.decorators import csrf
from django.contrib import admin
from django.contrib import auth
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/message/$', views.message, name='message'),
    url(r'^admin/', include(admin.site.urls)),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'^invalid_login/$', views.invalid_login, name='invalid_login'),
    url(r'^classes/$', views.classes, name='classes'),
    url(r'^message/$', views.message, name='message'),
    url(r'^classes/message/$', views.message, name='message'),
    url(r'^accounts/registration_complete/$', views.registration_complete, name='registration_complete'),
    url(r'^home/$', views.home, name='home'), 
    url(r'^home/message/$', views.message, name='message'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^loggedin/$', views.login, name='loggedin'),
    url(r'^your_class/$', views.your_class, name='your_class'),
    # url(r'^logout/$', views.logout,  {'next_page': '/index'}),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^accounts/', include('nopassword.urls', namespace='nopassword')),
    url(r'^login-code/(?P<login_code>[a-zA-Z0-9]+)/$', views.login_with_code, name='login_with_code'),
    url(r'^login-code/(?P<username>[a-zA-Z0-9_@\.\+-]+)/(?P<login_code>[a-zA-Z0-9]+)/$', views.login_with_code_and_username, name='login_with_code_and_username'),
]