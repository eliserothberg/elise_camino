from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from twilio.rest import TwilioRestClient
from twilio import twiml
from django_twilio.client import twilio_client
from django.http import HttpResponse, HttpResponseRedirect
from mobileReg.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf.urls.static import static
import random
from students.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
rand = random.randint(111111,999999)
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.views import login as django_login
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from students.forms import AuthenticationForm
from mobileReg.models import LoginCode
from mobileReg.utils import get_username, get_username_field

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            code = LoginCode.objects.filter(**{
                'user__%s' % get_username_field(): request.POST.get('username')
            })[0]
            code.next = request.GET.get('next')
            code.save()
            code.send_login_code(
                secure=request.is_secure(),
                host=request.get_host(),
            )
            return render(request, 'registration_complete.html')

    return django_login(request, authentication_form=AuthenticationForm)

def login_with_code(request, login_code):
    code = get_object_or_404(LoginCode.objects.select_related('user'), code=login_code)
    return login_with_code_and_username(request, username=get_username(code.user),
                                        login_code=login_code)

def login_with_code_and_username(request, username, login_code):
    code = get_object_or_404(LoginCode, code=login_code)
    login_with_post = getattr(settings, 'NOPASSWORD_POST_REDIRECT', True)

    if request.method == 'POST' or not login_with_post:
        user = authenticate(**{get_username_field(): username, 'code': login_code})
        if user is None:
            raise Http404
        user = auth_login(request, user)
        return redirect(code.next)

    return render(request, 'registration_complete.html')

def logout(request, redirect_to=None):
    auth_logout(request)
    if redirect_to is None:
        return redirect('{0}:login'.format(getattr(settings, 'NOPASSWORD_NAMESPACE', 'nopassword')))
    else:
        return redirect(redirect_to)

def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          form.save()
          return HttpResponseRedirect('/accounts/registration_complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update()
    token['form'] = form
    return render(request, 'index.html', token)

def message(request):
    phone = request.POST.get('phone', "")
    if not phone:
        return HttpResponse("No mobile number", status=403)

    randPIN = "%04d" % rand
    mess = client.messages.create(
                        body="Your number is %s" % randPIN,
                        to=phone,
                        from_=+12138143752,
                    )
    
    return HttpResponse("Message %s sent" % mess.sid, status=200)

def loggedin(request):
    return render(request, 'loggedin.html', 
                  {'user': request.user })

def invalid_login(request):
    return render(request, 'invalid_login.html')

def classes(request):
    return render(request, 'classes.html')

def home(request):
    return render(request, 'home.html')

def your_class(request):
    return render(request, 'your_class.html')

def register(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    else:
        form = AuthenticationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render(request, 'register.html', args)

def registration_complete(request):
    return render(request, 'accounts/registration_complete.html')