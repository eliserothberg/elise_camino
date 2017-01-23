from django.shortcuts import render
from django.views.decorators import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from twilio.rest import TwilioRestClient
from django.conf import settings
from twilio import twiml
from models import SMSVerification, Student
from students.forms import addClassForm
from django.forms import ModelForm
from django.conf.urls.static import static
from django_twilio.client import twilio_client
from django.conf.urls.static import static
import random
from students.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
rand = random.randint(111111,999999)

def index(request):
    return render(request, 'index.html')

# def SMSVerification(request):
#     form = PostForm(request.POST)
#     if form.is_valid():
#         form = form_class(data=request.POST)
#         phone = form.cleaned_data['sendTo']
    
#     return render(request, 'index.html', {
#         'form': form,
#     })

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

def classes(request):
  if request.method == 'POST':
  
    form = addClassForm(request.POST)
    if form.is_valid():
      classes = request.POST.get('classes', '')
      #__init__() got an unexpected keyword argument 'classes'
      classes_obj = addClassForm(classes = classes, user_id = user)
      classes_obj.save()
      if form.is_valid():
          form.save()
      
      return HttpResponseRedirect(reverse('classes'))
  else:
    form = addClassForm()


  return render(request, 'classes.html', {
    'form': form,
    })
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          form.save()
          return HttpResponseRedirect('/accounts/register/complete')
    else:
        form = UserCreationForm()
    token = {}
    token.update()
    token['form'] = form
    return render(request, 'accounts/register.html', token)

def registration_complete(request):
    return render(request, 'accounts/registration_complete.html')
 