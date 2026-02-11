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
from .forms import BookForm
from .forms import EmployeeForm
from .forms import MenuItemForm
from .forms import FeedbackForm


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

from django.shortcuts import redirect, get_object_or_404

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()

    return redirect('home')



def add_book(request):


    if request.method == "POST":
        form = BookForm(request.POST)


        if form.is_valid():
            form.save()
            return redirect('/') 

    else:
        form = BookForm

    return render(request, "booklist.html", {"form": form})


def add_employee(request):

    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')


    else:
        form = EmployeeForm
    return render(request,'employee.html',{"form":form})            



def add_menu_item(request):

    if request.method == "POST":
        form = MenuItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = MenuItemForm
    return render(request,'menu.html',{'form':form} )        



def add_feedback(request):

    if request.method == 'POST':
       form = FeedbackForm(request.POST)


       if form.is_valid():
          form.save()
          return redirect('/')
    
    else:
        form = FeedbackForm

    return render(request,'feedback.html',{'form':form})   