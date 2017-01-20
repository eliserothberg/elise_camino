from django.shortcuts import render
from django.views.decorators import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from django.template.loader import get_template
from django.http import HttpResponse
from twilio.rest import TwilioRestClient
from django.conf import settings
from twilio import twiml
from django.http import HttpResponse
from models import SMSVerification, Student
from students.forms import addClassForm
from django.forms import ModelForm
from django.conf.urls.static import static

def index(request):
    return render(request, 'index.html')

def classes(request):
  if request.method == 'POST':
  
    form = addClassForm(request.POST)
    if form.is_valid():
      classes = request.POST.get('classes', '')
      classes_obj = addClassForm(classes = classes)
      classes_obj.save()
      
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
 