from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    

    def __str__(self):
        return self.title
    

class Employee(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    salary = models.IntegerField()    


    def __str__(self):
        return self.first_name

class MenuItem(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)  
    is_vegeterian = models.BooleanField(default = False)

    def __str__(self):
        return self.name
        
class Feedback(models.Model):

    name = models.CharField(max_length=100)
    rating = models.IntegerField() 
    message = models.TextField()

    
    def __str__(self):
        return self.name
    