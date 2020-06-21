from profile import Profile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from django.views import View

from Base_app.forms import DonationForm
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


def form_confirmation(request):
    return render(request, 'form-confirmation.html')


@login_required
def add_donation(request):
    if request.method == "GET":
        form = DonationForm()
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, "institutions": institutions, "form": form})

    elif request.method == "POST" and request.is_ajax():
        form = DonationForm(request.POST)
        if form.is_valid():
            categories = form.cleaned_data.get('category')
            quantity = form.cleaned_data['quantity']
            institution = form.cleaned_data['institution']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            phone = form.cleaned_data['phone']
            pick_up_date = form.cleaned_data['pick_up_date']
            pick_up_time = form.cleaned_data['pick_up_time']
            pick_up_comment = form.cleaned_data['pick_up_comment']
            user = request.user
            donation = Donation.objects.create(quantity=quantity,
                                               institution=institution,
                                               address=address,
                                               city=city,
                                               zip_code=zip_code,
                                               phone=phone,
                                               pick_up_date=pick_up_date,
                                               pick_up_time=pick_up_time,
                                               pick_up_comment=pick_up_comment,
                                               user=user)
            donation.category.set(categories)
            return HttpResponseRedirect('conf')
        else:
            pass
        return render(request, 'form.html', {"form": form})
