from django import forms
from django.contrib.auth.forms import UserCreationForm
from Accounts.models import MyUser


class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = MyUser
        fields = ["first_name", "last_name", "email", "password1", "password2"]
