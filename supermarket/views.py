from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'supermarkert/index.htm')

def loginPage(request):
    return render(request, 'supermarkert/login.htm')

def dashboardHomePage(request):
    return render(request, 'dashboard/home.htm')

def Categories(request):
    return render(request, 'categories/category.htm')

def addCategory(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        password = request.POST['password']
        new_employee = Employee(name=name, email=email,phone_number=phone_number,password=password)
        new_employee.save()
    return render(request, 'categories/addCategory.htm')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.htm', {'employees': employees})   

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    
    return render(request, 'employees/delete_employee.htm', {'employee': employee})
    
