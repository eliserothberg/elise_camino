from models import CustomUser

class CustomUserAuth(object):

  def authenticate(self, username=None, password=None):
    try:
      user = CustomUser.objects.get(phone_number=username, pin=password)
      if user.check_pin(pin):
              return user
    except CustomUser.DoesNotExist:
      return None
  
  def get_user(self, user_id):
    try:
      user = CustomUser.objects.get(pk=user_id)
      if user.is_active:
          return user
    except CustomUser.DoesNotExist:
      return None