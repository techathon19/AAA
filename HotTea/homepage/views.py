from django.shortcuts import render
from homepage.models import Homemenu

# Create your views here.


def home(request):
    products = Homemenu.objects.all(); 
    return render(request,"index.html",{"products":products})

def login(request):
    return render(request,"login.html")
