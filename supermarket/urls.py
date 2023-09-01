from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.loginPage, name='login'),
    path('dashboard/home/', views.dashboardHomePage, name='home'),
    path('category/', views.Categories, name='category'),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
]