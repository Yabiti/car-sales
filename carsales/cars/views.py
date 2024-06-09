from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import carsale

# Create your views here.

def home(request):
    return render(request, 'cars/home.html')

def about(request):
    return render(request, 'cars/about.html')

def contact(request):
    return render(request, 'cars/contact.html')

def insertuser(request):
    Brand = request.POST['first name']
    Model = request.POST['last name']
    x = carsale(Brand=Brand, Model=Model)
    x.save()
    return render(request, 'flight/home.html')