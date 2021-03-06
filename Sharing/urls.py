
from django.contrib import admin
from django.urls import path, include

from Base_app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.LandingPage.as_view(), name='landing'),
    path('adddonation/conf/', v.form_confirmation, name='conf'),
    path('adddonation/', v.add_donation, name='donation'),
    path('accounts/', include('Accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/<int:pk>/', v.get_user_profile),

]
