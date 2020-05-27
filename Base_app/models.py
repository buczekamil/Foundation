from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name

typy = (
    (1,'fundacja'),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna"),

)
class Institution(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    type = models.IntegerField(choices=typy, default='1')
    categories = models.ManyToManyField(Category)


class PhoneField(object):
    pass


class Donation(models.Model):
    quantity = models.IntegerField(validators=[MinValueValidator(0, message='Minimum value = 0')])
    category = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    # phone = PhoneField()
    phone = models.IntegerField()
    city = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=250)
    user = models.ForeignKey(User, default='Null', on_delete=models.CASCADE)

    def __str__(self):
        return self.institution


# Create your models here.
