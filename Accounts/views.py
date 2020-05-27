from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


def registration_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    elif request.method == "POST":
        first_name = request.POST['name']
        last_name = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                text = 'Podany email użytkownika już istnieje'
                return render(request, 'registration/register.html', {'text': text})
            else:
                User.objects.create_user(email, email, password2, first_name=first_name, last_name=last_name)
                return redirect('/')
        else:
            text = 'Wprowadzone hasła nie są jednakowe'
            return render(request, 'registration/register2.html', {'text': text})

    return redirect('/')


