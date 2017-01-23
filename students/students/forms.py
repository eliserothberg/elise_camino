from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.forms import ModelForm
from mobileReg.models import SMSVerification, Student

class SMSVerification(forms.ModelForm):
    class Meta:
        model = SMSVerification
        fields = ['phone']
        phone = forms.IntegerField(label="Mobile", 
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'phone'}))
 
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Name", 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'Name'}))
    password = forms.CharField(label="PIN", 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'PIN'}))

class addClassForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['classes']
        classes = forms.CharField(label="Class",  
                               widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'Class Name'}))


# class SMSVerification(forms.Form):
#     user = forms.ForeignKey(User, on_delete=models.CASCADE)
#     verified = forms.BooleanField(default=False)
#     pin = forms.IntegerField()
#     sent = forms.BooleanField(default=False)
#     phone = PhoneNumberField(null=False, blank=False)

# class Student(forms.Form):
#     user = forms.ForeignKey(User, on_delete=models.CASCADE)
#     name = forms.CharField(max_length=200)
#     classes = forms.CharField(widget=forms.Textarea)
#     def __str__(self):
#         return self.name
#         return self.classes