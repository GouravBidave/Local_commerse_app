from django.urls import path
from .views import (home,add_product,edit_product,delete_product,add_book,add_employee,add_menu_item,
add_feedback)
from . import views

urlpatterns = [
    path('', home , name = 'home'),
    path('add_product/', add_product,name = "add_product"),
    path('edit/<int:id>/', edit_product),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('add_book/', views.add_book, name = 'add_book'),
    path('add_employee/',views.add_employee,name = 'add_employee'),
    path('add_menu_item/',views.add_menu_item, name = 'add_menu_item'),
    path('add_feedback/',views.add_feedback, name = 'add_feedback'),

]