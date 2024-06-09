from django.shortcuts import render
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
    Brand = request.POST['Brand']
    Model = request.POST['Model']
    x = carsale(Brand=Brand, Model=Model)
    x.save()
    return HttpResponse("Thanks")