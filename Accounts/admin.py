from django.contrib import admin

# Register your models here.
from Accounts.models import MyUser
from Base_app.models import Category, Institution

admin.site.register(MyUser)
admin.site.register(Category)
admin.site.register(Institution)