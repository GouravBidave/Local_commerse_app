from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to my local commerce app 🚀")

# def home(request):
#     return render(request,'home.html')
from django.shortcuts import render

def home(request):

    products = [
        {"name": "Rice", "price": 50},
        {"name": "Milk", "price": 30},
        {"name": "Bread", "price": 25},
    ]

    context = {
        "products": products
    }

    return render(request, "home.html", context)


