from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Accounts.models import MyUser


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length =100)
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = MyUser
        fields = ["first_name", "last_name","email", "password1", "password2"]
