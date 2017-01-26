from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# frofrom mobileReg.models import CustomUser
from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from mobileReg.models import LoginCode
from mobileReg.utils import get_username_field


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username logins.
    """
    username = forms.CharField(label=_("Username"), max_length=30)

    error_messages = {
        'invalid_login': _("Please enter a correct username. "
                           "Note that it is case-sensitive."),
        'no_cookies': _("Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = _(get_username_field().capitalize())

    def clean(self):
        username = self.cleaned_data.get('username')

        if username:
            self.user_cache = authenticate(**{get_username_field(): username})
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'])
            elif not isinstance(self.user_cache, LoginCode) and \
                    not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages['no_cookies'])

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

# class CustomUserCreationForm(UserCreationForm):

#   def __init__(self, *args, **kwargs):
#       super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#       self.fields.pop('password1')
#       self.fields.pop('password2')

#       del self.fields['password1']
#       del self.fields['password2']
#   class Meta:
#     model = CustomUser
#     # fields = ("phone",)
#     fields = ['phone', 'name', 'pin', 'class_name']

# class CustomUserChangeForm(UserChangeForm):
#   def __init__(self, *args, **kwargs):
#     super(CustomUserChangeForm, self).__init__(self, *args, **kwargs)
#     del self.fields['password1']
#     del self.fields['password2']

#     class Meta:
#       model = CustomUser

# from django.contrib.auth.forms import AuthenticationForm 
# from django import forms
# from django.forms import ModelForm
# from mobileReg.models import EnrolledIn

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label="Name", 
#                                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
#     password = forms.CharField(label="PIN", 
#                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
