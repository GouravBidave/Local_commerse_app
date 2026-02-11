from django import forms
from .models import Product,Book,Employee,MenuItem,Feedback

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','pages']        

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','email_id','salary']  

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields =['name','price','category','is_vegeterian']

class FeedbackForm(forms.ModelForm):
    class Meta:
     model = Feedback
     fields = ['name','rating', 'message']