from django import forms
from .models import Product,Category,Employee,Supply


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'quantity']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class employeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','phone_number']


class supplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['name','email','phone_number']