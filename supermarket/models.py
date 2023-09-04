from django.db import models
from django.utils import timezone
# Create your models here.


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

 
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone_number = models.DecimalField(max_digits=10, decimal_places=2)
    password = models.PositiveIntegerField()

class Supply(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.DecimalField(max_digits=10, decimal_places=2)
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    supply=models.ForeignKey(Supply, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='media/', default='images.jpeg')
    # date = models.DateTimeField(default='2023-01-01')
      
class Customer(models.Model):
    Customer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone_number = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)





