from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from django.views import View

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


def add_donation(request):
    if request.method == "GET":
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, "institutions": institutions})

    elif request.method == "POST":
        category = request.POST['categories']
        bags = request.POST['bags']
        organization = request.POST['organization']
        address = request.POST['address']
        city = request.POST['city']
        postcode = request.POST['postcode']
        phone = request.POST['phone']
        data = request.POST['data']
        time = request.POST['time']
        more_info = request.POST['more_info']
        user= request.user
        Donation.objects.create(quantity=bags, category=category, institution=organization, address=address,
                                phone=phone,
                                city=city, zip_code=postcode, pick_up_date=data, pick_up_time=time,
                                pick_up_comment=more_info, user=user)
        return redirect('/hjbjhb/')




class Login(View):
    def get(self, request):
        return render(request, 'registration/login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
# Create your views here.
