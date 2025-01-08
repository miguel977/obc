from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout

def home(request):
    return render(request, 'home.html')

def logout_user(request):
    pass


