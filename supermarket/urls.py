from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.loginPage, name='login'),
    path('dashboard/', views.dashboardHomePage, name='home'),

    path('category/', views.Categories, name='category'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    path('category/<int:category_id>/update/', views.update_category, name='update_category'),
   
    path('employees/', views.addEmployee, name='employees'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
    path('employees/<int:employee_id>/update/', views.update_employee, name='update_employee'),
   
    path('supply/', views.supply, name='supply'),
    path('supply/<int:supply_id>/delete/', views.delete_supply, name='delete_supply'),
    path('supply/<int:supply_id>/update/', views.update_supply, name='update_supply'),

    path('products/', views.add_product, name='products'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),  
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
]