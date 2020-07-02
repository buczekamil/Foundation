from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Prefetch
from django.shortcuts import render, redirect
from django.views import View
from Accounts.models import MyUser
from Base_app.forms import DonationForm
from Base_app.models import Donation, Category, Institution


class LandingPage(View):
    def get(self, request):
        bags = Donation.objects.all().aggregate(Sum('quantity'))
        institutions = Institution.objects.all().aggregate((Count('pk')))
        foundations = Institution.objects.filter(type=1)
        organizations = Institution.objects.filter(type=2)
        locals = Institution.objects.filter(type=3)

        try:
            bag = int(bags['quantity__sum'])
            institution = int(institutions['pk__count'])
        except KeyError:
            bag = 0
            institution = 0
        return render(request, 'index.html', {'bags': bag, 'institutions': institution, 'foundations': foundations,
                                              "organizations": organizations, "locals":locals})


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
            donation.category.set(categories)  ### << --- MultipleChoiceField

            return redirect('/adddonation/conf/')
        else:
            pass
        return render(request, 'form.html', {"form": form})


def get_user_profile(request, pk):
    user = MyUser.objects.get(pk=pk)
    return render(request, 'accounts/user_profile.html', {"user": user})
