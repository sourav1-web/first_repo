from django import forms
from django.contrib.auth.models import User
from testapp.models import Student
class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'        