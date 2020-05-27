from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from Base_app.models import Donation


class RegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = [
            'quantity',
            'category',
            'institution',
            'address',
            'phone',
            'city',
            'zip_code',
            'pick_up_date',
            'pick_up_time',
            'pick_up_comment']
