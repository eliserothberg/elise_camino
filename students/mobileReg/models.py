from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class SMSVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    pin = models.IntegerField()
    sent = models.BooleanField(default=False)
    phone = PhoneNumberField(null=False, blank=False)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    classes = models.CharField(max_length=200)
    def __str__(self):
        return self.name
        return self.classes