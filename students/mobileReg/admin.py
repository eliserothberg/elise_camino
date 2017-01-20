from django.contrib import admin

# Register your models here.
from .models import SMSVerification

admin.site.register(SMSVerification)

from .models import Student

admin.site.register(Student)