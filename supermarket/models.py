from django.db import models

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
      
class Customer(models.Model):
    Customer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone_number = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderItem')
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

