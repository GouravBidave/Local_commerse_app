from django.contrib import admin
from .models import Product
from .models import Book
from .models import Employee
from .models import MenuItem
from .models import Feedback

#register your models
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Employee)
admin.site.register(MenuItem)
admin.site.register(Feedback)