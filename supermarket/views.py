from django.shortcuts import render
from .models import Employee,Category,Supply,Product
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm,CategoryForm,employeeForm,supplyForm
# Create your views here.

def home(request):
    return render(request, 'supermarkert/index.htm')

def loginPage(request):
    return render(request, 'supermarkert/login.htm')

def dashboardHomePage(request):
    product = Product.objects.all()
    data_length = len(product)

    Categories = Category.objects.all()
    Categories_len= len(Categories)

    Supplies = Supply.objects.all()
    supply_len= len(Supplies)

    Employees = Employee.objects.all()
    Employee_len= len(Employees)

    return render(request, 'dashboard/home.htm',
                  {'data_length': data_length,
                   'Categories_len':Categories_len,
                   'supply_len':supply_len,
                   'Employee_len':Employee_len})

def Categories(request):
    Categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        new_category = Category(name=name)
        new_category.save()
        
    return render(request, 'categories/category.htm', {'Categories': Categories})

def delete_category(request, category_id):
    product = Category.objects.get(id=category_id)
    if product:
        product.delete()
        return redirect('category')

def update_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')

    else:
        form = CategoryForm(instance=category)

    return render(request, 'categories/update_category.htm', {'form': form})





def supply(request):
    Supplies = Supply.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        new_category = Supply(name=name, email=email,phone_number=phone_number)
        new_category.save()
    return render(request, 'supplies/supply.htm', {'Supplies': Supplies})

def delete_supply(request, supply_id):
    supplies = Supply.objects.get(id=supply_id)
    if supplies :
        supplies .delete()
        return redirect('supply')

def update_supply(request, supply_id):
    supply = get_object_or_404(Supply, pk=supply_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=supply)
        if form.is_valid():
            form.save()
            return redirect('supply')

    else:
        form = supplyForm(instance=supply)

    return render(request, 'supplies/update_supply.htm', {'form': form})



def addEmployee(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        password = request.POST['password']
        new_employee = Employee(name=name, email=email,phone_number=phone_number,password=password)
        new_employee.save()
    return render(request, 'employees/employee_list.htm', {'employees': employees})

def delete_employee(request, employee_id):
    Employees = Employee.objects.get(id=employee_id)
    if Employees :
        Employees.delete()
        return redirect('employees')  

def update_employee(request, employee_id):
    employees = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=employees)
        if form.is_valid():
            form.save()
            return redirect('employees')

    else:
        form = employeeForm(instance=employees)

    return render(request, 'employees/update_employee.htm', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product.htm', {'products': products})


def add_product(request):
        products = Product.objects.all()
        
        if request.method == 'POST':
            product_name = request.POST['product_name']
            price = request.POST['price']
            quantity=price = request.POST['quantity']
            category_id = request.POST['category']
            employee_id = request.POST['employee']
            supply_id = request.POST['supply']

            # Get the selected category, employee, and supply objects
            category = Category.objects.get(pk=category_id)
            employee = Employee.objects.get(pk=employee_id)
            supply = Supply.objects.get(pk=supply_id)

            # Create the product with the associated category, employee, and supply
            Product.objects.create(product_name=product_name, price=price,quantity=quantity, category=category, employee=employee, supply=supply)
            

    # Retrieve the lists of categories, employees, and supplies to populate the dropdown menus
        category = Category.objects.all()
        employees = Employee.objects.all()
        supplies = Supply.objects.all()
        return render(request, 'product/products.htm', {'categories': category, 'employees': employees, 'supplies': supplies,'products': products})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if product:
        product.delete()
        return redirect('products')

        # return redirect('products')
    # return render(request, 'product/delete_product.htm', {'product': product})

def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')

    else:
        form = ProductForm(instance=product)

    return render(request, 'product/update_product.htm', {'form': form})



