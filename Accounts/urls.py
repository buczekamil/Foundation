from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.registration_view, name='signup'),
]