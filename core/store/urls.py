from django.urls import path
from .views import home,add_product,edit_product

urlpatterns = [
    path('', home , name = 'home'),
    path('add_product/', add_product,name = "add_product"),
    path('edit/<int:id>/', edit_product),
]