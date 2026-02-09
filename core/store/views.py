# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to my local commerce app 🚀")

# def home(request):
#     return render(request,'home.html')
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProductForm 
from .models import Product

def home(request):

    # products = [
    #     {"name": "Rice", "price": 50},
    #     {"name": "Milk", "price": 30},
    #     {"name": "Bread", "price": 25},
    # ]
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request, "home.html", context)


def add_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProductForm()

    return render(request, "add_product.html", {"form": form})


from django.shortcuts import get_object_or_404

def edit_product(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProductForm(instance=product)

    return render(request, "add_product.html", {"form": form})