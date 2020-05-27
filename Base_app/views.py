from profile import Profile
from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from django.views import View

from Base_app.forms import RegistrationForm, DonationForm
from Base_app.models import Donation, Category, Institution


class LandingPage(View):
    def get(self, request):
        bags_dics = Donation.objects.all().aggregate(Sum('quantity'))
        institutions_dics = Donation.objects.all().aggregate(Count('institution'))
        try:
            bags = int(bags_dics['total__sum'])
            institutions = int(institutions_dics['total__sum'])
        except KeyError:
            bags = 0
            institutions = 0
        return render(request, 'index.html', {'bags': bags, 'institutions': institutions})


# def add_donation(request):
#     if request.method == "GET":
#         categories = Category.objects.all()
#         institutions = Institution.objects.all()
#         return render(request, 'form.html', {'categories': categories, "institutions": institutions})
#
#     elif request.method == "POST":
#         category = request.POST['categories']
#         bags = request.POST['bags']
#         organization = request.POST['organization']
#         address = request.POST['address']
#         city = request.POST['city']
#         postcode = request.POST['postcode']
#         phone = request.POST['phone']
#         data = request.POST['data']
#         time = request.POST['time']
#         more_info = request.POST['more_info']
#         user = request.user
#         Donation.objects.create(quantity=bags, category=category, institution=organization, address=address,
#                                 phone=phone, city=city, zip_code=postcode, pick_up_date=data, pick_up_time=time,
#                                 pick_up_comment=more_info, user=user)
#         return redirect('/hjbjhb/')

def add_donation(request):
    if request.method == "GET":
        form = DonationForm()

        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, "institutions": institutions, "form": form})

    elif request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['categories']
            quantity = form.cleaned_data['bags']
            institution = form.cleaned_data['organization']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['postcode']
            phone = form.cleaned_data['phone']
            pick_up_date = form.cleaned_data['data']
            pick_up_time = form.cleaned_data['time']
            pick_up_comment = form.cleaned_data['more_info']
            user = request.user
            Donation.objects.create(category=category, quantity=quantity, institution=institution, address=address,
                                    city=city, zip_code=zip_code, phone=phone, pick_up_date=pick_up_date, pick_up_time=pick_up_time,
                                    pick_up_comment=pick_up_comment, user=1)
            # Donation.objects.create(**form.cleaned_data, user=1)
            return

        return render(request, 'form.html', {"form": form})


