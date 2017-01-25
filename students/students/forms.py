from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from mobileReg.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

  def __init__(self, *args, **kargs):
      super(CustomUserCreationForm, self).__init__(*args, **kargs)
      del self.fields['username', 'password',]
  class Meta:
    model = CustomUser
    fields = ['phone_number',]

class CustomUserChangeForm(UserChangeForm):
  def __init__(self, *args, **kargs):
    super(CustomUserChangeForm, self).__init__(self, *args, **kargs)
    del self.fields['username', 'password',]

    class Meta:
      model = CustomUser