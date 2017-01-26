from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import FieldError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from nopassword.models import LoginCode
from nopassword.utils import get_user_model
from django.conf import settings
from django.template.loader import render_to_string
from twilio.rest import TwilioRestClient
from django.db import models
from .base import NoPasswordBackend

class NoPasswordBackend(ModelBackend):
    def authenticate(self, code=None, **credentials):
        try:
            user = get_user_model().objects.get(**credentials)
            if not self.verify_user(user):
                return None
            if code is None:
                return LoginCode.create_code_for_user(user)
            else:
                timeout = getattr(settings, 'NOPASSWORD_LOGIN_CODE_TIMEOUT', 900)
                timestamp = datetime.now() - timedelta(seconds=timeout)
                login_code = LoginCode.objects.get(user=user, code=code, timestamp__gt=timestamp)
                user = login_code.user
                user.code = login_code
                login_code.delete()
                return user
        except (TypeError, get_user_model().DoesNotExist, LoginCode.DoesNotExist, FieldError):
            return None

    def send_login_code(self, code, secure=False, host=None, **kwargs):
        raise NotImplementedError

    def verify_user(self, user):
        return user.is_active

class TwilioBackend(NoPasswordBackend):
    def __init__(self):
        self.twilio_client = TwilioRestClient(
            settings.NOPASSWORD_TWILIO_SID,
            settings.NOPASSWORD_TWILIO_AUTH_TOKEN
        )
        super(TwilioBackend, self).__init__()

    def send_login_code(self, code, secure=False, host=None, **kwargs):
        """
        Send a login code via SMS
        """
        from_number = getattr(settings, 'DEFAULT_FROM_NUMBER')

        context = {'url': code.login_url(secure=secure, host=host), 'code': code}
        sms_content = render_to_string('registration/login_sms.txt', context)

        self.twilio_client.messages.create(
            to=code.user.phone_number,
            from_=from_number,
            body=sms_content
        )

class CustomUserAuth(AbstractBaseUser):
    def authenticate(self, code=None, **credentials):
        try:
            user = get_user_model().objects.get(**credentials)
            if not self.verify_user(user):
                return None
            if code is None:
                return LoginCode.create_code_for_user(user)
            else:
                timeout = getattr(settings, 'NOPASSWORD_LOGIN_CODE_TIMEOUT', 900)
                timestamp = datetime.now() - timedelta(seconds=timeout)
                login_code = LoginCode.objects.get(user=user, code=code, timestamp__gt=timestamp)
                user = login_code.user
                user.code = login_code
                login_code.delete()
                return user
        except (TypeError, get_user_model().DoesNotExist, LoginCode.DoesNotExist, FieldError):
            return None

    def send_login_code(self, code, secure=False, host=None, **kwargs):
        raise NotImplementedError

    def verify_user(self, user):
        return user.is_active
