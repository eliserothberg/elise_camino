from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    def _create_user(self, phone_number, name, class_name, 
                    pin, 
                    is_anonymous, is_active, 
                    **extra_fields):
        
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        phone_number = self.normalize_name(phone_number)
        user = self.model(phone_number=phone_number, 
                        name=name, 
                        class_name=class_name,
                        pin=pin,
                        is_anonymous=False,
                        is_active=True,
                        last_login=now,
                        **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, **extra_fields)

    def create_superuser(self, phone_number,  **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, **extra_fields)

class CustomUser(AbstractBaseUser):
#     """
#     Custom user class.
#     """
    phone_number = models.IntegerField(db_index=True, unique=True,)
    name = models.CharField(max_length=50, blank=True)
    pin = models.IntegerField()
    class_name = models.CharField(max_length=250, blank=True)
     
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'pin', 'class_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
            return "/users/%s/" % urlquote(self.phone_number)

    def phone_number_user(self, message, TWILIO_NUMBER=None):
            
        send_phone_number(message, TWILIO_NUMBER, [self.phone_number])