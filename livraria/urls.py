from django.urls import path
from django.http import HttpResponse
from livraria.views import home, logout_user

urlpatterns = [
    path('', home, name = 'home'),
    path('logout/', logout_user, name='logout')
]