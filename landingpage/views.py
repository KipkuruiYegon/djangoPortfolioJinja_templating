from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

# all functions shall be defined here
def welcome(request):
    return render(request, 'welcome.html', {'navbar':'welcome'})

def about(request):
    return render(request, 'about.html', {'navbar':'about'})

def services(request):
    return render(request, 'services.html', {'navbar':'services'})

def contact(request):
    return render(request, 'contact.html', {'navbar':'contact'})