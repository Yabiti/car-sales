from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'cars/home.html')

def about(request):
    return render(request, 'cars/about.html')

def contact(request):
    return render(request, 'cars/contact.html')