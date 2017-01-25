from django.contrib import admin

# Register your models here.
# from .models import SMSVerification

# admin.site.register(SMSVerification)

# from models import UserForm

# admin.site.register(UserForm)

# from .models import Signup

# admin.site.register(Signup)

from models import CustomUser

admin.site.register(CustomUser)
