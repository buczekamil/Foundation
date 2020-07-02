from django.urls import reverse_lazy
from django.views import generic
from Accounts.forms import RegisterForm


class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('signup')
    template_name = 'registration/register.html'


