from django.urls import path
from .views import (show_book_info,feedback_list,add_feedback,home,add_product,edit_product,
add_menu_item,delete_product,add_employee,)
# from .views import *
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
    path('feedback_list/',views.feedback_list, name = 'feedback_list'),
    path('show_book_info/',views.show_book_info, name = 'show_book_info'),

]