from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from students.forms import CustomUserCreationForm
from twilio.rest import TwilioRestClient
from twilio import twiml
from django_twilio.client import twilio_client
from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls.static import static
import random
from students.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
rand = random.randint(111111,999999)


def index(request):
    phone_number = request.POST.get('phone_number', '')
    name = request.POST.get('name', '')
    pin = request.POST.get('pin', '')
    class_name = request.POST.get('class_name', '')
    user = auth.authenticate(phone_number=phone_number, pin=pin)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid_login/')

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

def your_class(request):
    return render(request, 'your_class.html')

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

def login(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/classes')
        else:
          form = CustomUserCreationForm()
        args = {}
        args.update(csrf(request))
    
    args['form'] = form
    
    return render(request, 'index.html')

# def login(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/classes')
#     else:
#         form = CustomUserCreationForm()
#     args = {}
#     args.update(csrf(request))
    
#     args['form'] = form
    
#     return render(request, 'index.html', args)

def registration_complete(request):
    return render(request, 'accounts/registration_complete.html')